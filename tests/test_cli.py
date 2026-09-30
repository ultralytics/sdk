# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license
"""Exercise CLI mutation boundaries through the installed module and real loopback HTTP."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import pytest


def test_cli_wire_and_auth(tmp_path):
    requests = []

    class Receiver(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
            requests.append((self.command, self.path, dict(self.headers), body))
            if self.headers.get("Authorization") == "Bearer invalid":
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b"sensitive upstream response")
                return
            invalid_training = self.path == "/api/training/start" and json.loads(body)["trainArgs"] == {"epochs": 100}
            payload = {"username": "jane"} if self.path == "/api/account/summary" else {"ok": True}
            if invalid_training:
                payload = {"error": "model and data are required"}
            self.send_response(422 if invalid_training else 200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode())

        do_POST = do_PATCH = do_GET

    server = ThreadingHTTPServer(("127.0.0.1", 0), Receiver)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    env = {
        **os.environ,
        "YOLO_CONFIG_DIR": str(tmp_path),
        "ULTRALYTICS_API_KEY": "",
        "ULTRALYTICS_PLATFORM_URL": f"http://127.0.0.1:{server.server_port}",
    }

    def run(*args, input=None):
        return subprocess.run(
            [sys.executable, "-m", "ultralytics_platform.cli", *args],
            env=env,
            input=input,
            text=True,
            capture_output=True,
            timeout=20,
            check=False,
        )

    try:
        settings = tmp_path / "Ultralytics" / "settings.json"
        settings.parent.mkdir()
        saved = {"api_key": "ul_" + "a" * 40, "runs_dir": "custom runs"}
        settings.write_text(json.dumps(saved))
        assert run("cloud", "datasets", "limit=0").returncode == 0
        assert [item[1] for item in requests[-2:]] == ["/api/account/summary", "/api/datasets/jane?limit=0"]
        assert requests[-1][2]["Authorization"] == f"Bearer {saved['api_key']}"
        env["ULTRALYTICS_API_KEY"] = "environment-key"
        count = len(requests)
        assert run("cloud", "exports", "owner=team", "project=p", "model=m", "export_id=e").returncode == 0
        assert len(requests) == count + 1 and requests[-1][:2] == ("GET", "/api/models/team/p/m/exports/e")
        assert requests[-1][2]["Authorization"] == "Bearer environment-key"
        env["ULTRALYTICS_API_KEY"] = ""
        count = len(requests)
        for name in (["name=token="], ["name="], ["name", "="]):
            for flag in ("help", "--help", "-h"):
                help_result = run("cloud", "projects", "create", "project=p", *name, flag)
                assert help_result.returncode == 0 and "name (" in help_result.stdout
                assert "timeout (" not in help_result.stdout and "extra_headers (" not in help_result.stdout
        for arguments in (["model=m"], ["project=p", "model=m", "epochs=True"], ["project=p", "model=m", "starred=0"]):
            assert run("cloud", "models", "update", *arguments).returncode == 2
        assert run("cloud", "datasets", "dataset=coco8", "limit=1").returncode == 2
        failed = run("cloud", "datasets", "images", "dataset=d", "limit=private-value")
        assert failed.returncode == 2 and "private-value" not in failed.stderr
        for number in ("NaN", "Infinity", "-Infinity", "1e999"):
            failed = run("cloud", "models", "predict", "project=p", "model=m", f'body={{"nested":[{number}]}}')
            assert failed.returncode == 2
        assert len(requests) == count
        assert run("cloud", "projects", "create", "project=p", "name=--help").returncode == 0
        assert json.loads(requests[-1][3])["name"] == "--help"
        result = run(
            "cloud",
            "models",
            "update",
            "owner=jane",
            "project=p",
            "model=m",
            "starred=False",
            "epochs=0",
            "color=null",
            "license=None",
        )
        assert result.returncode == 0 and json.loads(result.stdout) == {"ok": True}
        assert json.loads(requests[-1][3]) == {"starred": False, "epochs": 0, "color": None, "license": "None"}
        for name in (["name="], ["name", "="]):
            result = run("cloud", "models", "update", "owner=jane", "project=p", "model=m", *name, "starred")
            assert result.returncode == 0 and json.loads(requests[-1][3]) == {"name": "", "starred": True}
        image = tmp_path / "image with spaces.jpg"
        image.write_bytes(b"binary image contents")
        request = tmp_path / "request.json"
        request.write_text(json.dumps({"file": "@" + str(image), "normalize": False}))
        result = run("cloud", "deployments", "predict", "deployment=production", f"body=@{request}")
        assert result.returncode == 0 and requests[-1][1] == "/api/deployments/jane/production/predict"
        assert b"binary image contents" in requests[-1][3] and b"false" in requests[-1][3]
        result = run("cloud", "models", "predict", "project=p", "model=m", "body=@-", input='{"source":"image.jpg"}')
        assert result.returncode == 0 and b"image.jpg" in requests[-1][3]
        count = len(requests)
        result = run("cloud", "models", "update", "project=p", "model=m", "metadata=@-", "train_args=@-", input="{}")
        assert result.returncode == 2 and len(requests) == count
        failed = run("cloud", "training", "start", "model_id=m", 'train_args={"epochs":100}')
        assert failed.returncode == 1 and "HTTP 422): model and data are required" in failed.stderr
        env["ULTRALYTICS_API_KEY"] = "invalid"
        failed = run("cloud", "account", "summary")
        assert failed.returncode == 1 and "sensitive" not in failed.stderr
        assert json.loads(settings.read_text()) == saved
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def test_cloud_predict_saves_outputs(tmp_path):
    if importlib.util.find_spec("ultralytics") is None:  # never import it here: that could reset the real settings
        pytest.skip("ul cloud predict requires ultralytics")
    import cv2
    import numpy as np

    frame = np.full((48, 64, 3), 128, np.uint8)
    video, image = tmp_path / "clip.mp4", tmp_path / "image.jpg"
    writer = cv2.VideoWriter(str(video), cv2.VideoWriter_fourcc(*"mp4v"), 10, (64, 48))
    for _ in range(6):
        writer.write(frame)
    writer.release()
    cv2.imwrite(str(image), frame)
    posts = []

    class Receiver(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_POST(self):
            self.rfile.read(int(self.headers["Content-Length"]))
            posts.append(self.path)
            box = {"x1": 8, "y1": 8, "x2": 40, "y2": 32}
            speed = {"preprocess": 1.0, "inference": 1.0, "postprocess": 1.0}
            images = [  # each Platform frame's class is its index, so saved labels show which frames were kept
                {"results": [{"class": i, "name": str(i), "confidence": 0.9, "box": box}], "speed": speed}
                for i in range(6 if self.path == "/api/models/jane/p/video/predict" else 1)
            ]
            payload = {"metadata": {"task": "detect", "classNames": [str(i) for i in range(6)]}, "images": images}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode())

    server = ThreadingHTTPServer(("127.0.0.1", 0), Receiver)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    env = {
        **os.environ,
        "YOLO_CONFIG_DIR": str(tmp_path),
        "ULTRALYTICS_API_KEY": "key",
        "ULTRALYTICS_PLATFORM_URL": f"http://127.0.0.1:{server.server_port}",
    }

    def run(model, source, *args):
        command = [sys.executable, "-m", "ultralytics_platform.cli", "cloud", "predict", f"model=ul://jane/p/{model}"]
        command += [f"source={source}", f"project={tmp_path / 'runs'}", f"name={model}", *args]
        return subprocess.run(command, env=env, cwd=tmp_path, text=True, capture_output=True, timeout=120, check=False)

    try:
        result = run("video", video, "vid_stride=0")
        assert result.returncode == 2 and not posts, result.stderr
        result = run("video", video, "vid_stride=2", "save_txt=True", "save_crop=True")
        assert result.returncode == 0, result.stderr
        output = tmp_path / "runs" / "video"
        labels = [(output / "labels" / f"clip_{k}.txt").read_text().split()[0] for k in (1, 2, 3)]
        assert labels == ["1", "3", "5"] and len(list((output / "labels").iterdir())) == 3
        assert (output / "crops" / "3" / "clip_2.jpg").is_file()
        capture = cv2.VideoCapture(str(next(output.glob("clip.*"))))  # .mp4 on macOS, .avi elsewhere
        assert (capture.get(cv2.CAP_PROP_FRAME_COUNT), capture.get(cv2.CAP_PROP_FPS)) == (3, 5)
        capture.release()
        result = run("image", image)
        assert result.returncode == 0, result.stderr
        assert (tmp_path / "runs" / "image" / "image.jpg").is_file()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
