// Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

(globalThis.TURBOPACK || (globalThis.TURBOPACK = [])).push([
  "object" == typeof document ? document.currentScript : void 0,
  26568,
  (e, t, n) => {
    "use strict";
    var r = /\/\*[^*]*\*+([^/*][^*]*\*+)*\//g,
      i = /\n/g,
      o = /^\s*/,
      l = /^(\*?[-#/*\\\w]+(\[[0-9a-z_-]+\])?)\s*/,
      a = /^:\s*/,
      s = /^((?:'(?:\\'|.)*?'|"(?:\\"|.)*?"|\([^)]*?\)|[^};])+)/,
      u = /^[;\s]*/,
      c = /^\s+|\s+$/g;
    function d(e) {
      return e ? e.replace(c, "") : "";
    }
    t.exports = function (e, t) {
      if ("string" != typeof e) throw TypeError("First argument must be a string");
      if (!e) return [];
      t = t || {};
      var n = 1,
        c = 1;
      function f(e) {
        var t = e.match(i);
        t && (n += t.length);
        var r = e.lastIndexOf("\n");
        c = ~r ? e.length - r : c + e.length;
      }
      function p() {
        var e = { line: n, column: c };
        return function (t) {
          return ((t.position = new h(e)), g(o), t);
        };
      }
      function h(e) {
        ((this.start = e), (this.end = { line: n, column: c }), (this.source = t.source));
      }
      function m(r) {
        var i = Error(t.source + ":" + n + ":" + c + ": " + r);
        if (((i.reason = r), (i.filename = t.source), (i.line = n), (i.column = c), (i.source = e), t.silent));
        else throw i;
      }
      function g(t) {
        var n = t.exec(e);
        if (n) {
          var r = n[0];
          return (f(r), (e = e.slice(r.length)), n);
        }
      }
      function v(e) {
        var t;
        for (e = e || []; (t = y()); ) !1 !== t && e.push(t);
        return e;
      }
      function y() {
        var t = p();
        if ("/" == e.charAt(0) && "*" == e.charAt(1)) {
          for (var n = 2; "" != e.charAt(n) && ("*" != e.charAt(n) || "/" != e.charAt(n + 1)); ) ++n;
          if (((n += 2), "" === e.charAt(n - 1))) return m("End of comment missing");
          var r = e.slice(2, n - 2);
          return ((c += 2), f(r), (e = e.slice(n)), (c += 2), t({ type: "comment", comment: r }));
        }
      }
      ((h.prototype.content = e), g(o));
      var b,
        x = [];
      for (
        v(x);
        (b = (function () {
          var e = p(),
            t = g(l);
          if (t) {
            if ((y(), !g(a))) return m("property missing ':'");
            var n = g(s),
              i = e({ type: "declaration", property: d(t[0].replace(r, "")), value: n ? d(n[0].replace(r, "")) : "" });
            return (g(u), i);
          }
        })());
      )
        !1 !== b && (x.push(b), v(x));
      return x;
    };
  },
  70454,
  (e, t, n) => {
    "use strict";
    var r =
      (e.e && e.e.__importDefault) ||
      function (e) {
        return e && e.__esModule ? e : { default: e };
      };
    (Object.defineProperty(n, "__esModule", { value: !0 }),
      (n.default = function (e, t) {
        let n = null;
        if (!e || "string" != typeof e) return n;
        let r = (0, i.default)(e),
          o = "function" == typeof t;
        return (
          r.forEach((e) => {
            if ("declaration" !== e.type) return;
            let { property: r, value: i } = e;
            o ? t(r, i, e) : i && ((n = n || {})[r] = i);
          }),
          n
        );
      }));
    let i = r(e.r(26568));
  },
  65185,
  (e, t, n) => {
    "use strict";
    (Object.defineProperty(n, "__esModule", { value: !0 }), (n.camelCase = void 0));
    var r = /^--[a-zA-Z0-9_-]+$/,
      i = /-([a-z])/g,
      o = /^[^-]+$/,
      l = /^-(webkit|moz|ms|o|khtml)-/,
      a = /^-(ms)-/,
      s = function (e, t) {
        return t.toUpperCase();
      },
      u = function (e, t) {
        return "".concat(t, "-");
      };
    n.camelCase = function (e, t) {
      var n;
      return (void 0 === t && (t = {}), !(n = e) || o.test(n) || r.test(n))
        ? e
        : ((e = e.toLowerCase()), (e = t.reactCompat ? e.replace(a, u) : e.replace(l, u)).replace(i, s));
    };
  },
  15511,
  (e, t, n) => {
    "use strict";
    var r = (
        (e.e && e.e.__importDefault) ||
        function (e) {
          return e && e.__esModule ? e : { default: e };
        }
      )(e.r(70454)),
      i = e.r(65185);
    function o(e, t) {
      var n = {};
      return (
        e &&
          "string" == typeof e &&
          (0, r.default)(e, function (e, r) {
            e && r && (n[(0, i.camelCase)(e, t)] = r);
          }),
        n
      );
    }
    ((o.default = o), (t.exports = o));
  },
  4100,
  (e, t, n) => {
    "use strict";
    var r = Object.prototype.hasOwnProperty,
      i = Object.prototype.toString,
      o = Object.defineProperty,
      l = Object.getOwnPropertyDescriptor,
      a = function (e) {
        return "function" == typeof Array.isArray ? Array.isArray(e) : "[object Array]" === i.call(e);
      },
      s = function (e) {
        if (!e || "[object Object]" !== i.call(e)) return !1;
        var t,
          n = r.call(e, "constructor"),
          o = e.constructor && e.constructor.prototype && r.call(e.constructor.prototype, "isPrototypeOf");
        if (e.constructor && !n && !o) return !1;
        for (t in e);
        return void 0 === t || r.call(e, t);
      },
      u = function (e, t) {
        o && "__proto__" === t.name
          ? o(e, t.name, { enumerable: !0, configurable: !0, value: t.newValue, writable: !0 })
          : (e[t.name] = t.newValue);
      },
      c = function (e, t) {
        if ("__proto__" === t) {
          if (!r.call(e, t)) return;
          else if (l) return l(e, t).value;
        }
        return e[t];
      };
    t.exports = function e() {
      var t,
        n,
        r,
        i,
        o,
        l,
        d = arguments[0],
        f = 1,
        p = arguments.length,
        h = !1;
      for (
        "boolean" == typeof d && ((h = d), (d = arguments[1] || {}), (f = 2)),
          (null == d || ("object" != typeof d && "function" != typeof d)) && (d = {});
        f < p;
        ++f
      )
        if (((t = arguments[f]), null != t))
          for (n in t)
            ((r = c(d, n)),
              d !== (i = c(t, n)) &&
                (h && i && (s(i) || (o = a(i)))
                  ? (o ? ((o = !1), (l = r && a(r) ? r : [])) : (l = r && s(r) ? r : {}),
                    u(d, { name: n, newValue: e(h, l, i) }))
                  : void 0 !== i && u(d, { name: n, newValue: i })));
      return d;
    };
  },
  55838,
  (e, t, n) => {
    "use strict";
    var r = e.r(71645),
      i =
        "function" == typeof Object.is
          ? Object.is
          : function (e, t) {
              return (e === t && (0 !== e || 1 / e == 1 / t)) || (e != e && t != t);
            },
      o = r.useState,
      l = r.useEffect,
      a = r.useLayoutEffect,
      s = r.useDebugValue;
    function u(e) {
      var t = e.getSnapshot;
      e = e.value;
      try {
        var n = t();
        return !i(e, n);
      } catch (e) {
        return !0;
      }
    }
    var c =
      "u" < typeof window || void 0 === window.document || void 0 === window.document.createElement
        ? function (e, t) {
            return t();
          }
        : function (e, t) {
            var n = t(),
              r = o({ inst: { value: n, getSnapshot: t } }),
              i = r[0].inst,
              c = r[1];
            return (
              a(
                function () {
                  ((i.value = n), (i.getSnapshot = t), u(i) && c({ inst: i }));
                },
                [e, n, t],
              ),
              l(
                function () {
                  return (
                    u(i) && c({ inst: i }),
                    e(function () {
                      u(i) && c({ inst: i });
                    })
                  );
                },
                [e],
              ),
              s(n),
              n
            );
          };
    n.useSyncExternalStore = void 0 !== r.useSyncExternalStore ? r.useSyncExternalStore : c;
  },
  2239,
  (e, t, n) => {
    "use strict";
    (e.i(47167), (t.exports = e.r(55838)));
  },
  52822,
  (e, t, n) => {
    "use strict";
    var r = e.r(71645),
      i = e.r(2239),
      o =
        "function" == typeof Object.is
          ? Object.is
          : function (e, t) {
              return (e === t && (0 !== e || 1 / e == 1 / t)) || (e != e && t != t);
            },
      l = i.useSyncExternalStore,
      a = r.useRef,
      s = r.useEffect,
      u = r.useMemo,
      c = r.useDebugValue;
    n.useSyncExternalStoreWithSelector = function (e, t, n, r, i) {
      var d = a(null);
      if (null === d.current) {
        var f = { hasValue: !1, value: null };
        d.current = f;
      } else f = d.current;
      var p = l(
        e,
        (d = u(
          function () {
            function e(e) {
              if (!s) {
                if (((s = !0), (l = e), (e = r(e)), void 0 !== i && f.hasValue)) {
                  var t = f.value;
                  if (i(t, e)) return (a = t);
                }
                return (a = e);
              }
              if (((t = a), o(l, e))) return t;
              var n = r(e);
              return void 0 !== i && i(t, n) ? ((l = e), t) : ((l = e), (a = n));
            }
            var l,
              a,
              s = !1,
              u = void 0 === n ? null : n;
            return [
              function () {
                return e(t());
              },
              null === u
                ? void 0
                : function () {
                    return e(u());
                  },
            ];
          },
          [t, n, r, i],
        ))[0],
        d[1],
      );
      return (
        s(
          function () {
            ((f.hasValue = !0), (f.value = p));
          },
          [p],
        ),
        c(p),
        p
      );
    };
  },
  30224,
  (e, t, n) => {
    "use strict";
    (e.i(47167), (t.exports = e.r(52822)));
  },
  50341,
  (e) => {
    "use strict";
    let t, n, r, i, o, l;
    var a,
      s,
      u,
      c,
      d = e.i(43476),
      f = e.i(71645);
    let p = (...e) =>
        e
          .filter((e, t, n) => !!e && "" !== e.trim() && n.indexOf(e) === t)
          .join(" ")
          .trim(),
      h = (e) => {
        let t = e.replace(/^([A-Z])|[\s-_]+(\w)/g, (e, t, n) => (n ? n.toUpperCase() : t.toLowerCase()));
        return t.charAt(0).toUpperCase() + t.slice(1);
      };
    var m = {
      xmlns: "http://www.w3.org/2000/svg",
      width: 24,
      height: 24,
      viewBox: "0 0 24 24",
      fill: "none",
      stroke: "currentColor",
      strokeWidth: 2,
      strokeLinecap: "round",
      strokeLinejoin: "round",
    };
    let g = (0, f.createContext)({}),
      v = (0, f.forwardRef)(
        (
          {
            color: e,
            size: t,
            strokeWidth: n,
            absoluteStrokeWidth: r,
            className: i = "",
            children: o,
            iconNode: l,
            ...a
          },
          s,
        ) => {
          let {
              size: u = 24,
              strokeWidth: c = 2,
              absoluteStrokeWidth: d = !1,
              color: h = "currentColor",
              className: v = "",
            } = (0, f.useContext)(g) ?? {},
            y = (r ?? d) ? (24 * Number(n ?? c)) / Number(t ?? u) : (n ?? c);
          return (0, f.createElement)(
            "svg",
            {
              ref: s,
              ...m,
              width: t ?? u ?? m.width,
              height: t ?? u ?? m.height,
              stroke: e ?? h,
              strokeWidth: y,
              className: p("lucide", v, i),
              ...(!o &&
                !((e) => {
                  for (let t in e) if (t.startsWith("aria-") || "role" === t || "title" === t) return !0;
                  return !1;
                })(a) && { "aria-hidden": "true" }),
              ...a,
            },
            [...l.map(([e, t]) => (0, f.createElement)(e, t)), ...(Array.isArray(o) ? o : [o])],
          );
        },
      ),
      y = (e, t) => {
        let n = (0, f.forwardRef)(({ className: n, ...r }, i) =>
          (0, f.createElement)(v, {
            ref: i,
            iconNode: t,
            className: p(
              `lucide-${h(e)
                .replace(/([a-z0-9])([A-Z])/g, "$1-$2")
                .toLowerCase()}`,
              `lucide-${e}`,
              n,
            ),
            ...r,
          }),
        );
        return ((n.displayName = h(e)), n);
      },
      b = y("check", [["path", { d: "M20 6 9 17l-5-5", key: "1gmf2c" }]]),
      x = y("copy", [
        ["rect", { width: "14", height: "14", x: "8", y: "8", rx: "2", ry: "2", key: "17jyea" }],
        ["path", { d: "M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2", key: "zix9uf" }],
      ]),
      k = y("key-round", [
        [
          "path",
          {
            d: "M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z",
            key: "1s6t7t",
          },
        ],
        ["circle", { cx: "16.5", cy: "7.5", r: ".5", fill: "currentColor", key: "w0ekpg" }],
      ]),
      w = y("loader-circle", [["path", { d: "M21 12a9 9 0 1 1-6.219-8.56", key: "13zald" }]]),
      S = y("menu", [
        ["path", { d: "M4 5h16", key: "1tepv9" }],
        ["path", { d: "M4 12h16", key: "1lakjw" }],
        ["path", { d: "M4 19h16", key: "1djgab" }],
      ]),
      C = y("play", [
        [
          "path",
          { d: "M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z", key: "10ikf1" },
        ],
      ]),
      E = y("search", [
        ["path", { d: "m21 21-4.34-4.34", key: "14j7rj" }],
        ["circle", { cx: "11", cy: "11", r: "8", key: "4ej97u" }],
      ]);
    function j() {}
    function R() {}
    let P = /^[$_\p{ID_Start}][$_\u{200C}\u{200D}\p{ID_Continue}]*$/u,
      T = /^[$_\p{ID_Start}][-$_\u{200C}\u{200D}\p{ID_Continue}]*$/u,
      A = {};
    function O(e, t) {
      return ((t || A).jsx ? T : P).test(e);
    }
    let I = /[ \t\n\f\r]/g;
    function M(e) {
      return "" === e.replace(I, "");
    }
    class N {
      constructor(e, t) {
        ((this.attribute = t), (this.property = e));
      }
    }
    ((N.prototype.attribute = ""),
      (N.prototype.booleanish = !1),
      (N.prototype.boolean = !1),
      (N.prototype.commaOrSpaceSeparated = !1),
      (N.prototype.commaSeparated = !1),
      (N.prototype.defined = !1),
      (N.prototype.mustUseProperty = !1),
      (N.prototype.number = !1),
      (N.prototype.overloadedBoolean = !1),
      (N.prototype.property = ""),
      (N.prototype.spaceSeparated = !1),
      (N.prototype.space = void 0));
    let z = 0,
      D = q(),
      L = q(),
      $ = q(),
      F = q(),
      _ = q(),
      B = q(),
      H = q();
    function q() {
      return 2 ** ++z;
    }
    e.s(
      [
        "boolean",
        0,
        D,
        "booleanish",
        0,
        L,
        "commaOrSpaceSeparated",
        0,
        H,
        "commaSeparated",
        0,
        B,
        "number",
        0,
        F,
        "overloadedBoolean",
        0,
        $,
        "spaceSeparated",
        0,
        _,
      ],
      744,
    );
    var U = e.i(744);
    let W = Object.keys(U);
    class V extends N {
      constructor(e, t, n, r) {
        let i = -1;
        if (
          (super(e, t),
          (function (e, t, n) {
            n && (e[t] = n);
          })(this, "space", r),
          "number" == typeof n)
        )
          for (; ++i < W.length; ) {
            const e = W[i];
            !(function (e, t, n) {
              n && (e[t] = n);
            })(this, W[i], (n & U[e]) === U[e]);
          }
      }
    }
    function K(e) {
      return e.toLowerCase();
    }
    V.prototype.defined = !0;
    let X = /[A-Z]/g,
      Y = /-[a-z]/g,
      G = /^data[-\w.:]+$/i;
    function J(e) {
      return "-" + e.toLowerCase();
    }
    function Q(e) {
      return e.charAt(1).toUpperCase();
    }
    let Z = {
      classId: "classID",
      dataType: "datatype",
      itemId: "itemID",
      strokeDashArray: "strokeDasharray",
      strokeDashOffset: "strokeDashoffset",
      strokeLineCap: "strokeLinecap",
      strokeLineJoin: "strokeLinejoin",
      strokeMiterLimit: "strokeMiterlimit",
      typeOf: "typeof",
      xLinkActuate: "xlinkActuate",
      xLinkArcRole: "xlinkArcrole",
      xLinkHref: "xlinkHref",
      xLinkRole: "xlinkRole",
      xLinkShow: "xlinkShow",
      xLinkTitle: "xlinkTitle",
      xLinkType: "xlinkType",
      xmlnsXLink: "xmlnsXlink",
    };
    class ee {
      constructor(e, t, n) {
        ((this.normal = t), (this.property = e), n && (this.space = n));
      }
    }
    function et(e, t) {
      let n = {},
        r = {};
      for (let t of e) (Object.assign(n, t.property), Object.assign(r, t.normal));
      return new ee(n, r, t);
    }
    function en(e) {
      let t = {},
        n = {};
      for (let [r, i] of Object.entries(e.properties)) {
        let o = new V(r, e.transform(e.attributes || {}, r), i, e.space);
        (e.mustUseProperty && e.mustUseProperty.includes(r) && (o.mustUseProperty = !0),
          (t[r] = o),
          (n[K(r)] = r),
          (n[K(o.attribute)] = r));
      }
      return new ee(t, n, e.space);
    }
    ((ee.prototype.normal = {}), (ee.prototype.property = {}), (ee.prototype.space = void 0));
    let er = en({
      properties: {
        ariaActiveDescendant: null,
        ariaAtomic: L,
        ariaAutoComplete: null,
        ariaBusy: L,
        ariaChecked: L,
        ariaColCount: F,
        ariaColIndex: F,
        ariaColSpan: F,
        ariaControls: _,
        ariaCurrent: null,
        ariaDescribedBy: _,
        ariaDetails: null,
        ariaDisabled: L,
        ariaDropEffect: _,
        ariaErrorMessage: null,
        ariaExpanded: L,
        ariaFlowTo: _,
        ariaGrabbed: L,
        ariaHasPopup: null,
        ariaHidden: L,
        ariaInvalid: null,
        ariaKeyShortcuts: null,
        ariaLabel: null,
        ariaLabelledBy: _,
        ariaLevel: F,
        ariaLive: null,
        ariaModal: L,
        ariaMultiLine: L,
        ariaMultiSelectable: L,
        ariaOrientation: null,
        ariaOwns: _,
        ariaPlaceholder: null,
        ariaPosInSet: F,
        ariaPressed: L,
        ariaReadOnly: L,
        ariaRelevant: null,
        ariaRequired: L,
        ariaRoleDescription: _,
        ariaRowCount: F,
        ariaRowIndex: F,
        ariaRowSpan: F,
        ariaSelected: L,
        ariaSetSize: F,
        ariaSort: null,
        ariaValueMax: F,
        ariaValueMin: F,
        ariaValueNow: F,
        ariaValueText: null,
        role: null,
      },
      transform: (e, t) => ("role" === t ? t : "aria-" + t.slice(4).toLowerCase()),
    });
    function ei(e, t) {
      return t in e ? e[t] : t;
    }
    function eo(e, t) {
      return ei(e, t.toLowerCase());
    }
    let el = en({
        attributes: { acceptcharset: "accept-charset", classname: "class", htmlfor: "for", httpequiv: "http-equiv" },
        mustUseProperty: ["checked", "multiple", "muted", "selected"],
        properties: {
          abbr: null,
          accept: B,
          acceptCharset: _,
          accessKey: _,
          action: null,
          allow: null,
          allowFullScreen: D,
          allowPaymentRequest: D,
          allowUserMedia: D,
          alpha: D,
          alt: null,
          as: null,
          async: D,
          autoCapitalize: null,
          autoComplete: _,
          autoFocus: D,
          autoPlay: D,
          blocking: _,
          capture: null,
          charSet: null,
          checked: D,
          cite: null,
          className: _,
          closedBy: null,
          colorSpace: null,
          cols: F,
          colSpan: F,
          command: null,
          commandFor: null,
          content: null,
          contentEditable: L,
          controls: D,
          controlsList: _,
          coords: F | B,
          crossOrigin: null,
          data: null,
          dateTime: null,
          decoding: null,
          default: D,
          defer: D,
          dir: null,
          dirName: null,
          disabled: D,
          download: $,
          draggable: L,
          encType: null,
          enterKeyHint: null,
          fetchPriority: null,
          form: null,
          formAction: null,
          formEncType: null,
          formMethod: null,
          formNoValidate: D,
          formTarget: null,
          headers: _,
          height: F,
          hidden: $,
          high: F,
          href: null,
          hrefLang: null,
          htmlFor: _,
          httpEquiv: _,
          id: null,
          imageSizes: null,
          imageSrcSet: null,
          inert: D,
          inputMode: null,
          integrity: null,
          is: null,
          isMap: D,
          itemId: null,
          itemProp: _,
          itemRef: _,
          itemScope: D,
          itemType: _,
          kind: null,
          label: null,
          lang: null,
          language: null,
          list: null,
          loading: null,
          loop: D,
          low: F,
          manifest: null,
          max: null,
          maxLength: F,
          media: null,
          method: null,
          min: null,
          minLength: F,
          multiple: D,
          muted: D,
          name: null,
          nonce: null,
          noModule: D,
          noValidate: D,
          onAbort: null,
          onAfterPrint: null,
          onAuxClick: null,
          onBeforeMatch: null,
          onBeforePrint: null,
          onBeforeToggle: null,
          onBeforeUnload: null,
          onBlur: null,
          onCancel: null,
          onCanPlay: null,
          onCanPlayThrough: null,
          onChange: null,
          onClick: null,
          onClose: null,
          onContextLost: null,
          onContextMenu: null,
          onContextRestored: null,
          onCopy: null,
          onCueChange: null,
          onCut: null,
          onDblClick: null,
          onDrag: null,
          onDragEnd: null,
          onDragEnter: null,
          onDragExit: null,
          onDragLeave: null,
          onDragOver: null,
          onDragStart: null,
          onDrop: null,
          onDurationChange: null,
          onEmptied: null,
          onEnded: null,
          onError: null,
          onFocus: null,
          onFormData: null,
          onHashChange: null,
          onInput: null,
          onInvalid: null,
          onKeyDown: null,
          onKeyPress: null,
          onKeyUp: null,
          onLanguageChange: null,
          onLoad: null,
          onLoadedData: null,
          onLoadedMetadata: null,
          onLoadEnd: null,
          onLoadStart: null,
          onMessage: null,
          onMessageError: null,
          onMouseDown: null,
          onMouseEnter: null,
          onMouseLeave: null,
          onMouseMove: null,
          onMouseOut: null,
          onMouseOver: null,
          onMouseUp: null,
          onOffline: null,
          onOnline: null,
          onPageHide: null,
          onPageShow: null,
          onPaste: null,
          onPause: null,
          onPlay: null,
          onPlaying: null,
          onPopState: null,
          onProgress: null,
          onRateChange: null,
          onRejectionHandled: null,
          onReset: null,
          onResize: null,
          onScroll: null,
          onScrollEnd: null,
          onSecurityPolicyViolation: null,
          onSeeked: null,
          onSeeking: null,
          onSelect: null,
          onSlotChange: null,
          onStalled: null,
          onStorage: null,
          onSubmit: null,
          onSuspend: null,
          onTimeUpdate: null,
          onToggle: null,
          onUnhandledRejection: null,
          onUnload: null,
          onVolumeChange: null,
          onWaiting: null,
          onWheel: null,
          open: D,
          optimum: F,
          pattern: null,
          ping: _,
          placeholder: null,
          playsInline: D,
          popover: null,
          popoverTarget: null,
          popoverTargetAction: null,
          poster: null,
          preload: null,
          readOnly: D,
          referrerPolicy: null,
          rel: _,
          required: D,
          reversed: D,
          rows: F,
          rowSpan: F,
          sandbox: _,
          scope: null,
          scoped: D,
          seamless: D,
          selected: D,
          shadowRootClonable: D,
          shadowRootCustomElementRegistry: D,
          shadowRootDelegatesFocus: D,
          shadowRootMode: null,
          shadowRootSerializable: D,
          shape: null,
          size: F,
          sizes: null,
          slot: null,
          span: F,
          spellCheck: L,
          src: null,
          srcDoc: null,
          srcLang: null,
          srcSet: null,
          start: F,
          step: null,
          style: null,
          tabIndex: F,
          target: null,
          title: null,
          translate: null,
          type: null,
          typeMustMatch: D,
          useMap: null,
          value: L,
          width: F,
          wrap: null,
          writingSuggestions: null,
          align: null,
          aLink: null,
          archive: _,
          axis: null,
          background: null,
          bgColor: null,
          border: F,
          borderColor: null,
          bottomMargin: F,
          cellPadding: null,
          cellSpacing: null,
          char: null,
          charOff: null,
          classId: null,
          clear: null,
          code: null,
          codeBase: null,
          codeType: null,
          color: null,
          compact: D,
          declare: D,
          event: null,
          face: null,
          frame: null,
          frameBorder: null,
          hSpace: F,
          leftMargin: F,
          link: null,
          longDesc: null,
          lowSrc: null,
          marginHeight: F,
          marginWidth: F,
          noResize: D,
          noHref: D,
          noShade: D,
          noWrap: D,
          object: null,
          profile: null,
          prompt: null,
          rev: null,
          rightMargin: F,
          rules: null,
          scheme: null,
          scrolling: L,
          standby: null,
          summary: null,
          text: null,
          topMargin: F,
          valueType: null,
          version: null,
          vAlign: null,
          vLink: null,
          vSpace: F,
          allowTransparency: null,
          autoCorrect: null,
          autoSave: null,
          credentialless: D,
          disablePictureInPicture: D,
          disableRemotePlayback: D,
          exportParts: B,
          part: _,
          prefix: null,
          property: null,
          results: F,
          security: null,
          unselectable: null,
        },
        space: "html",
        transform: eo,
      }),
      ea = en({
        attributes: {
          accentHeight: "accent-height",
          alignmentBaseline: "alignment-baseline",
          arabicForm: "arabic-form",
          baselineShift: "baseline-shift",
          capHeight: "cap-height",
          className: "class",
          clipPath: "clip-path",
          clipRule: "clip-rule",
          colorInterpolation: "color-interpolation",
          colorInterpolationFilters: "color-interpolation-filters",
          colorProfile: "color-profile",
          colorRendering: "color-rendering",
          crossOrigin: "crossorigin",
          dataType: "datatype",
          dominantBaseline: "dominant-baseline",
          enableBackground: "enable-background",
          fillOpacity: "fill-opacity",
          fillRule: "fill-rule",
          floodColor: "flood-color",
          floodOpacity: "flood-opacity",
          fontFamily: "font-family",
          fontSize: "font-size",
          fontSizeAdjust: "font-size-adjust",
          fontStretch: "font-stretch",
          fontStyle: "font-style",
          fontVariant: "font-variant",
          fontWeight: "font-weight",
          glyphName: "glyph-name",
          glyphOrientationHorizontal: "glyph-orientation-horizontal",
          glyphOrientationVertical: "glyph-orientation-vertical",
          hrefLang: "hreflang",
          horizAdvX: "horiz-adv-x",
          horizOriginX: "horiz-origin-x",
          horizOriginY: "horiz-origin-y",
          imageRendering: "image-rendering",
          letterSpacing: "letter-spacing",
          lightingColor: "lighting-color",
          markerEnd: "marker-end",
          markerMid: "marker-mid",
          markerStart: "marker-start",
          maskType: "mask-type",
          navDown: "nav-down",
          navDownLeft: "nav-down-left",
          navDownRight: "nav-down-right",
          navLeft: "nav-left",
          navNext: "nav-next",
          navPrev: "nav-prev",
          navRight: "nav-right",
          navUp: "nav-up",
          navUpLeft: "nav-up-left",
          navUpRight: "nav-up-right",
          onAbort: "onabort",
          onActivate: "onactivate",
          onAfterPrint: "onafterprint",
          onBeforePrint: "onbeforeprint",
          onBegin: "onbegin",
          onCancel: "oncancel",
          onCanPlay: "oncanplay",
          onCanPlayThrough: "oncanplaythrough",
          onChange: "onchange",
          onClick: "onclick",
          onClose: "onclose",
          onCopy: "oncopy",
          onCueChange: "oncuechange",
          onCut: "oncut",
          onDblClick: "ondblclick",
          onDrag: "ondrag",
          onDragEnd: "ondragend",
          onDragEnter: "ondragenter",
          onDragExit: "ondragexit",
          onDragLeave: "ondragleave",
          onDragOver: "ondragover",
          onDragStart: "ondragstart",
          onDrop: "ondrop",
          onDurationChange: "ondurationchange",
          onEmptied: "onemptied",
          onEnd: "onend",
          onEnded: "onended",
          onError: "onerror",
          onFocus: "onfocus",
          onFocusIn: "onfocusin",
          onFocusOut: "onfocusout",
          onHashChange: "onhashchange",
          onInput: "oninput",
          onInvalid: "oninvalid",
          onKeyDown: "onkeydown",
          onKeyPress: "onkeypress",
          onKeyUp: "onkeyup",
          onLoad: "onload",
          onLoadedData: "onloadeddata",
          onLoadedMetadata: "onloadedmetadata",
          onLoadStart: "onloadstart",
          onMessage: "onmessage",
          onMouseDown: "onmousedown",
          onMouseEnter: "onmouseenter",
          onMouseLeave: "onmouseleave",
          onMouseMove: "onmousemove",
          onMouseOut: "onmouseout",
          onMouseOver: "onmouseover",
          onMouseUp: "onmouseup",
          onMouseWheel: "onmousewheel",
          onOffline: "onoffline",
          onOnline: "ononline",
          onPageHide: "onpagehide",
          onPageShow: "onpageshow",
          onPaste: "onpaste",
          onPause: "onpause",
          onPlay: "onplay",
          onPlaying: "onplaying",
          onPopState: "onpopstate",
          onProgress: "onprogress",
          onRateChange: "onratechange",
          onRepeat: "onrepeat",
          onReset: "onreset",
          onResize: "onresize",
          onScroll: "onscroll",
          onSeeked: "onseeked",
          onSeeking: "onseeking",
          onSelect: "onselect",
          onShow: "onshow",
          onStalled: "onstalled",
          onStorage: "onstorage",
          onSubmit: "onsubmit",
          onSuspend: "onsuspend",
          onTimeUpdate: "ontimeupdate",
          onToggle: "ontoggle",
          onUnload: "onunload",
          onVolumeChange: "onvolumechange",
          onWaiting: "onwaiting",
          onZoom: "onzoom",
          overlinePosition: "overline-position",
          overlineThickness: "overline-thickness",
          paintOrder: "paint-order",
          panose1: "panose-1",
          pointerEvents: "pointer-events",
          referrerPolicy: "referrerpolicy",
          renderingIntent: "rendering-intent",
          shapeRendering: "shape-rendering",
          stopColor: "stop-color",
          stopOpacity: "stop-opacity",
          strikethroughPosition: "strikethrough-position",
          strikethroughThickness: "strikethrough-thickness",
          strokeDashArray: "stroke-dasharray",
          strokeDashOffset: "stroke-dashoffset",
          strokeLineCap: "stroke-linecap",
          strokeLineJoin: "stroke-linejoin",
          strokeMiterLimit: "stroke-miterlimit",
          strokeOpacity: "stroke-opacity",
          strokeWidth: "stroke-width",
          tabIndex: "tabindex",
          textAnchor: "text-anchor",
          textDecoration: "text-decoration",
          textRendering: "text-rendering",
          transformOrigin: "transform-origin",
          typeOf: "typeof",
          underlinePosition: "underline-position",
          underlineThickness: "underline-thickness",
          unicodeBidi: "unicode-bidi",
          unicodeRange: "unicode-range",
          unitsPerEm: "units-per-em",
          vAlphabetic: "v-alphabetic",
          vHanging: "v-hanging",
          vIdeographic: "v-ideographic",
          vMathematical: "v-mathematical",
          vectorEffect: "vector-effect",
          vertAdvY: "vert-adv-y",
          vertOriginX: "vert-origin-x",
          vertOriginY: "vert-origin-y",
          wordSpacing: "word-spacing",
          writingMode: "writing-mode",
          xHeight: "x-height",
          playbackOrder: "playbackorder",
          timelineBegin: "timelinebegin",
        },
        properties: {
          about: H,
          accentHeight: F,
          accumulate: null,
          additive: null,
          alignmentBaseline: null,
          alphabetic: F,
          amplitude: F,
          arabicForm: null,
          ascent: F,
          attributeName: null,
          attributeType: null,
          azimuth: F,
          bandwidth: null,
          baselineShift: null,
          baseFrequency: null,
          baseProfile: null,
          bbox: null,
          begin: null,
          bias: F,
          by: null,
          calcMode: null,
          capHeight: F,
          className: _,
          clip: null,
          clipPath: null,
          clipPathUnits: null,
          clipRule: null,
          color: null,
          colorInterpolation: null,
          colorInterpolationFilters: null,
          colorProfile: null,
          colorRendering: null,
          content: null,
          contentScriptType: null,
          contentStyleType: null,
          crossOrigin: null,
          cursor: null,
          cx: null,
          cy: null,
          d: null,
          dataType: null,
          defaultAction: null,
          descent: F,
          diffuseConstant: F,
          direction: null,
          display: null,
          dur: null,
          divisor: F,
          dominantBaseline: null,
          download: D,
          dx: null,
          dy: null,
          edgeMode: null,
          editable: null,
          elevation: F,
          enableBackground: null,
          end: null,
          event: null,
          exponent: F,
          externalResourcesRequired: null,
          fill: null,
          fillOpacity: F,
          fillRule: null,
          filter: null,
          filterRes: null,
          filterUnits: null,
          floodColor: null,
          floodOpacity: null,
          focusable: null,
          focusHighlight: null,
          fontFamily: null,
          fontSize: null,
          fontSizeAdjust: null,
          fontStretch: null,
          fontStyle: null,
          fontVariant: null,
          fontWeight: null,
          format: null,
          fr: null,
          from: null,
          fx: null,
          fy: null,
          g1: B,
          g2: B,
          glyphName: B,
          glyphOrientationHorizontal: null,
          glyphOrientationVertical: null,
          glyphRef: null,
          gradientTransform: null,
          gradientUnits: null,
          handler: null,
          hanging: F,
          hatchContentUnits: null,
          hatchUnits: null,
          height: null,
          href: null,
          hrefLang: null,
          horizAdvX: F,
          horizOriginX: F,
          horizOriginY: F,
          id: null,
          ideographic: F,
          imageRendering: null,
          initialVisibility: null,
          in: null,
          in2: null,
          intercept: F,
          k: F,
          k1: F,
          k2: F,
          k3: F,
          k4: F,
          kernelMatrix: H,
          kernelUnitLength: null,
          keyPoints: null,
          keySplines: null,
          keyTimes: null,
          kerning: null,
          lang: null,
          lengthAdjust: null,
          letterSpacing: null,
          lightingColor: null,
          limitingConeAngle: F,
          local: null,
          markerEnd: null,
          markerMid: null,
          markerStart: null,
          markerHeight: null,
          markerUnits: null,
          markerWidth: null,
          mask: null,
          maskContentUnits: null,
          maskType: null,
          maskUnits: null,
          mathematical: null,
          max: null,
          media: null,
          mediaCharacterEncoding: null,
          mediaContentEncodings: null,
          mediaSize: F,
          mediaTime: null,
          method: null,
          min: null,
          mode: null,
          name: null,
          navDown: null,
          navDownLeft: null,
          navDownRight: null,
          navLeft: null,
          navNext: null,
          navPrev: null,
          navRight: null,
          navUp: null,
          navUpLeft: null,
          navUpRight: null,
          numOctaves: null,
          observer: null,
          offset: null,
          onAbort: null,
          onActivate: null,
          onAfterPrint: null,
          onBeforePrint: null,
          onBegin: null,
          onCancel: null,
          onCanPlay: null,
          onCanPlayThrough: null,
          onChange: null,
          onClick: null,
          onClose: null,
          onCopy: null,
          onCueChange: null,
          onCut: null,
          onDblClick: null,
          onDrag: null,
          onDragEnd: null,
          onDragEnter: null,
          onDragExit: null,
          onDragLeave: null,
          onDragOver: null,
          onDragStart: null,
          onDrop: null,
          onDurationChange: null,
          onEmptied: null,
          onEnd: null,
          onEnded: null,
          onError: null,
          onFocus: null,
          onFocusIn: null,
          onFocusOut: null,
          onHashChange: null,
          onInput: null,
          onInvalid: null,
          onKeyDown: null,
          onKeyPress: null,
          onKeyUp: null,
          onLoad: null,
          onLoadedData: null,
          onLoadedMetadata: null,
          onLoadStart: null,
          onMessage: null,
          onMouseDown: null,
          onMouseEnter: null,
          onMouseLeave: null,
          onMouseMove: null,
          onMouseOut: null,
          onMouseOver: null,
          onMouseUp: null,
          onMouseWheel: null,
          onOffline: null,
          onOnline: null,
          onPageHide: null,
          onPageShow: null,
          onPaste: null,
          onPause: null,
          onPlay: null,
          onPlaying: null,
          onPopState: null,
          onProgress: null,
          onRateChange: null,
          onRepeat: null,
          onReset: null,
          onResize: null,
          onScroll: null,
          onSeeked: null,
          onSeeking: null,
          onSelect: null,
          onShow: null,
          onStalled: null,
          onStorage: null,
          onSubmit: null,
          onSuspend: null,
          onTimeUpdate: null,
          onToggle: null,
          onUnload: null,
          onVolumeChange: null,
          onWaiting: null,
          onZoom: null,
          opacity: null,
          operator: null,
          order: null,
          orient: null,
          orientation: null,
          origin: null,
          overflow: null,
          overlay: null,
          overlinePosition: F,
          overlineThickness: F,
          paintOrder: null,
          panose1: null,
          path: null,
          pathLength: F,
          patternContentUnits: null,
          patternTransform: null,
          patternUnits: null,
          phase: null,
          ping: _,
          pitch: null,
          playbackOrder: null,
          pointerEvents: null,
          points: null,
          pointsAtX: F,
          pointsAtY: F,
          pointsAtZ: F,
          preserveAlpha: null,
          preserveAspectRatio: null,
          primitiveUnits: null,
          propagate: null,
          property: H,
          r: null,
          radius: null,
          referrerPolicy: null,
          refX: null,
          refY: null,
          rel: H,
          rev: H,
          renderingIntent: null,
          repeatCount: null,
          repeatDur: null,
          requiredExtensions: H,
          requiredFeatures: H,
          requiredFonts: H,
          requiredFormats: H,
          resource: null,
          restart: null,
          result: null,
          rotate: null,
          rx: null,
          ry: null,
          scale: null,
          seed: null,
          shapeRendering: null,
          side: null,
          slope: null,
          snapshotTime: null,
          specularConstant: F,
          specularExponent: F,
          spreadMethod: null,
          spacing: null,
          startOffset: null,
          stdDeviation: null,
          stemh: null,
          stemv: null,
          stitchTiles: null,
          stopColor: null,
          stopOpacity: null,
          strikethroughPosition: F,
          strikethroughThickness: F,
          string: null,
          stroke: null,
          strokeDashArray: H,
          strokeDashOffset: null,
          strokeLineCap: null,
          strokeLineJoin: null,
          strokeMiterLimit: F,
          strokeOpacity: F,
          strokeWidth: null,
          style: null,
          surfaceScale: F,
          syncBehavior: null,
          syncBehaviorDefault: null,
          syncMaster: null,
          syncTolerance: null,
          syncToleranceDefault: null,
          systemLanguage: H,
          tabIndex: F,
          tableValues: null,
          target: null,
          targetX: F,
          targetY: F,
          textAnchor: null,
          textDecoration: null,
          textRendering: null,
          textLength: null,
          timelineBegin: null,
          title: null,
          transformBehavior: null,
          type: null,
          typeOf: H,
          to: null,
          transform: null,
          transformOrigin: null,
          u1: null,
          u2: null,
          underlinePosition: F,
          underlineThickness: F,
          unicode: null,
          unicodeBidi: null,
          unicodeRange: null,
          unitsPerEm: F,
          values: null,
          vAlphabetic: F,
          vMathematical: F,
          vectorEffect: null,
          vHanging: F,
          vIdeographic: F,
          version: null,
          vertAdvY: F,
          vertOriginX: F,
          vertOriginY: F,
          viewBox: null,
          viewTarget: null,
          visibility: null,
          width: null,
          widths: null,
          wordSpacing: null,
          writingMode: null,
          x: null,
          x1: null,
          x2: null,
          xChannelSelector: null,
          xHeight: F,
          y: null,
          y1: null,
          y2: null,
          yChannelSelector: null,
          z: null,
          zoomAndPan: null,
        },
        space: "svg",
        transform: ei,
      }),
      es = en({
        properties: {
          xLinkActuate: null,
          xLinkArcRole: null,
          xLinkHref: null,
          xLinkRole: null,
          xLinkShow: null,
          xLinkTitle: null,
          xLinkType: null,
        },
        space: "xlink",
        transform: (e, t) => "xlink:" + t.slice(5).toLowerCase(),
      }),
      eu = en({
        attributes: { xmlnsxlink: "xmlns:xlink" },
        properties: { xmlnsXLink: null, xmlns: null },
        space: "xmlns",
        transform: eo,
      }),
      ec = en({
        properties: { xmlBase: null, xmlLang: null, xmlSpace: null },
        space: "xml",
        transform: (e, t) => "xml:" + t.slice(3).toLowerCase(),
      }),
      ed = et([er, el, es, eu, ec], "html"),
      ef = et([er, ea, es, eu, ec], "svg");
    var ep = e.i(15511);
    let eh = eg("end"),
      em = eg("start");
    function eg(e) {
      return function (t) {
        let n = (t && t.position && t.position[e]) || {};
        if ("number" == typeof n.line && n.line > 0 && "number" == typeof n.column && n.column > 0)
          return {
            line: n.line,
            column: n.column,
            offset: "number" == typeof n.offset && n.offset > -1 ? n.offset : void 0,
          };
      };
    }
    function ev(e) {
      return e && "object" == typeof e
        ? "position" in e || "type" in e
          ? eb(e.position)
          : "start" in e || "end" in e
            ? eb(e)
            : "line" in e || "column" in e
              ? ey(e)
              : ""
        : "";
    }
    function ey(e) {
      return ex(e && e.line) + ":" + ex(e && e.column);
    }
    function eb(e) {
      return ey(e && e.start) + "-" + ey(e && e.end);
    }
    function ex(e) {
      return e && "number" == typeof e ? e : 1;
    }
    class ek extends Error {
      constructor(e, t, n) {
        (super(), "string" == typeof t && ((n = t), (t = void 0)));
        let r = "",
          i = {},
          o = !1;
        if (
          (t &&
            (i =
              ("line" in t && "column" in t) || ("start" in t && "end" in t)
                ? { place: t }
                : "type" in t
                  ? { ancestors: [t], place: t.position }
                  : { ...t }),
          "string" == typeof e ? (r = e) : !i.cause && e && ((o = !0), (r = e.message), (i.cause = e)),
          !i.ruleId && !i.source && "string" == typeof n)
        ) {
          const e = n.indexOf(":");
          -1 === e ? (i.ruleId = n) : ((i.source = n.slice(0, e)), (i.ruleId = n.slice(e + 1)));
        }
        if (!i.place && i.ancestors && i.ancestors) {
          const e = i.ancestors[i.ancestors.length - 1];
          e && (i.place = e.position);
        }
        const l = i.place && "start" in i.place ? i.place.start : i.place;
        ((this.ancestors = i.ancestors || void 0),
          (this.cause = i.cause || void 0),
          (this.column = l ? l.column : void 0),
          (this.fatal = void 0),
          (this.file = ""),
          (this.message = r),
          (this.line = l ? l.line : void 0),
          (this.name = ev(i.place) || "1:1"),
          (this.place = i.place || void 0),
          (this.reason = this.message),
          (this.ruleId = i.ruleId || void 0),
          (this.source = i.source || void 0),
          (this.stack = o && i.cause && "string" == typeof i.cause.stack ? i.cause.stack : ""),
          (this.actual = void 0),
          (this.expected = void 0),
          (this.note = void 0),
          (this.url = void 0));
      }
    }
    ((ek.prototype.file = ""),
      (ek.prototype.name = ""),
      (ek.prototype.reason = ""),
      (ek.prototype.message = ""),
      (ek.prototype.stack = ""),
      (ek.prototype.column = void 0),
      (ek.prototype.line = void 0),
      (ek.prototype.ancestors = void 0),
      (ek.prototype.cause = void 0),
      (ek.prototype.fatal = void 0),
      (ek.prototype.place = void 0),
      (ek.prototype.ruleId = void 0),
      (ek.prototype.source = void 0));
    let ew = {}.hasOwnProperty,
      eS = new Map(),
      eC = /[A-Z]/g,
      eE = new Set(["table", "tbody", "thead", "tfoot", "tr"]),
      ej = new Set(["td", "th"]),
      eR = "https://github.com/syntax-tree/hast-util-to-jsx-runtime";
    function eP(e, t, n) {
      var r, i, o, l, a, s, u, c, d;
      let f, p, h, m, g, v, y, b, x, k, w;
      return "element" === t.type
        ? ((r = e),
          (i = t),
          (o = n),
          (p = f = r.schema),
          "svg" === i.tagName.toLowerCase() && "html" === f.space && (r.schema = ef),
          r.ancestors.push(i),
          (h = eI(r, i.tagName, !1)),
          (m = (function (e, t) {
            let n,
              r,
              i = {};
            for (r in t.properties)
              if ("children" !== r && ew.call(t.properties, r)) {
                let o = (function (e, t, n) {
                  let r = (function (e, t) {
                    let n = K(t),
                      r = t,
                      i = N;
                    if (n in e.normal) return e.property[e.normal[n]];
                    if (n.length > 4 && "data" === n.slice(0, 4) && G.test(t)) {
                      if ("-" === t.charAt(4)) {
                        let e = t.slice(5).replace(Y, Q);
                        r = "data" + e.charAt(0).toUpperCase() + e.slice(1);
                      } else {
                        let e = t.slice(4);
                        if (!Y.test(e)) {
                          let n = e.replace(X, J);
                          ("-" !== n.charAt(0) && (n = "-" + n), (t = "data" + n));
                        }
                      }
                      i = V;
                    }
                    return new i(r, t);
                  })(e.schema, t);
                  if (!(null == n || ("number" == typeof n && Number.isNaN(n)))) {
                    var i;
                    let t;
                    if (
                      (Array.isArray(n) &&
                        (n = r.commaSeparated
                          ? ((t = {}),
                            ("" === (i = n)[i.length - 1] ? [...i, ""] : i)
                              .join((t.padRight ? " " : "") + "," + (!1 === t.padLeft ? "" : " "))
                              .trim())
                          : n.join(" ").trim()),
                      "style" === r.property)
                    ) {
                      let t =
                        "object" == typeof n
                          ? n
                          : (function (e, t) {
                              try {
                                return (0, ep.default)(t, { reactCompat: !0 });
                              } catch (n) {
                                if (e.ignoreInvalidStyle) return {};
                                let t = new ek("Cannot parse `style` attribute", {
                                  ancestors: e.ancestors,
                                  cause: n,
                                  ruleId: "style",
                                  source: "hast-util-to-jsx-runtime",
                                });
                                throw (
                                  (t.file = e.filePath || void 0),
                                  (t.url = eR + "#cannot-parse-style-attribute"),
                                  t
                                );
                              }
                            })(e, String(n));
                      return (
                        "css" === e.stylePropertyNameCase &&
                          (t = (function (e) {
                            let t,
                              n = {};
                            for (t in e)
                              ew.call(e, t) &&
                                (n[
                                  (function (e) {
                                    let t = e.replace(eC, eN);
                                    return ("ms-" === t.slice(0, 3) && (t = "-" + t), t);
                                  })(t)
                                ] = e[t]);
                            return n;
                          })(t)),
                        ["style", t]
                      );
                    }
                    return [
                      "react" === e.elementAttributeNameCase && r.space ? Z[r.property] || r.property : r.attribute,
                      n,
                    ];
                  }
                })(e, r, t.properties[r]);
                if (o) {
                  let [r, l] = o;
                  e.tableCellAlignToStyle && "align" === r && "string" == typeof l && ej.has(t.tagName)
                    ? (n = l)
                    : (i[r] = l);
                }
              }
            return (
              n && ((i.style || (i.style = {}))["css" === e.stylePropertyNameCase ? "text-align" : "textAlign"] = n),
              i
            );
          })(r, i)),
          (g = eO(r, i)),
          eE.has(i.tagName) &&
            (g = g.filter(function (e) {
              return "string" != typeof e || !("object" == typeof e ? "text" === e.type && M(e.value) : M(e));
            })),
          eT(r, m, h, i),
          eA(m, g),
          r.ancestors.pop(),
          (r.schema = f),
          r.create(i, h, m, o))
        : "mdxFlowExpression" === t.type || "mdxTextExpression" === t.type
          ? (function (e, t) {
              if (t.data && t.data.estree && e.evaluater) {
                let n = t.data.estree.body[0];
                return (j(n.type), e.evaluater.evaluateExpression(n.expression));
              }
              eM(e, t.position);
            })(e, t)
          : "mdxJsxFlowElement" === t.type || "mdxJsxTextElement" === t.type
            ? ((l = e),
              (a = t),
              (s = n),
              (y = v = l.schema),
              "svg" === a.name && "html" === v.space && (l.schema = ef),
              l.ancestors.push(a),
              (b = null === a.name ? l.Fragment : eI(l, a.name, !0)),
              (x = (function (e, t) {
                let n = {};
                for (let r of t.attributes)
                  if ("mdxJsxExpressionAttribute" === r.type)
                    if (r.data && r.data.estree && e.evaluater) {
                      let t = r.data.estree.body[0];
                      j(t.type);
                      let i = t.expression;
                      j(i.type);
                      let o = i.properties[0];
                      (j(o.type), Object.assign(n, e.evaluater.evaluateExpression(o.argument)));
                    } else eM(e, t.position);
                  else {
                    let i,
                      o = r.name;
                    if (r.value && "object" == typeof r.value)
                      if (r.value.data && r.value.data.estree && e.evaluater) {
                        let t = r.value.data.estree.body[0];
                        (j(t.type), (i = e.evaluater.evaluateExpression(t.expression)));
                      } else eM(e, t.position);
                    else i = null === r.value || r.value;
                    n[o] = i;
                  }
                return n;
              })(l, a)),
              (k = eO(l, a)),
              eT(l, x, b, a),
              eA(x, k),
              l.ancestors.pop(),
              (l.schema = v),
              l.create(a, b, x, s))
            : "mdxjsEsm" === t.type
              ? (function (e, t) {
                  if (t.data && t.data.estree && e.evaluater) return e.evaluater.evaluateProgram(t.data.estree);
                  eM(e, t.position);
                })(e, t)
              : "root" === t.type
                ? ((u = e), (c = t), (d = n), eA((w = {}), eO(u, c)), u.create(c, u.Fragment, w, d))
                : "text" === t.type
                  ? t.value
                  : void 0;
    }
    function eT(e, t, n, r) {
      "string" != typeof n && n !== e.Fragment && e.passNode && (t.node = r);
    }
    function eA(e, t) {
      if (t.length > 0) {
        let n = t.length > 1 ? t : t[0];
        n && (e.children = n);
      }
    }
    function eO(e, t) {
      let n = [],
        r = -1,
        i = e.passKeys ? new Map() : eS;
      for (; ++r < t.children.length; ) {
        let o,
          l = t.children[r];
        if (e.passKeys) {
          let e =
            "element" === l.type
              ? l.tagName
              : "mdxJsxFlowElement" === l.type || "mdxJsxTextElement" === l.type
                ? l.name
                : void 0;
          if (e) {
            let t = i.get(e) || 0;
            ((o = e + "-" + t), i.set(e, t + 1));
          }
        }
        let a = eP(e, l, o);
        void 0 !== a && n.push(a);
      }
      return n;
    }
    function eI(e, t, n) {
      let r;
      if (n)
        if (t.includes(".")) {
          let e,
            n = t.split("."),
            i = -1;
          for (; ++i < n.length; ) {
            let t = O(n[i]) ? { type: "Identifier", name: n[i] } : { type: "Literal", value: n[i] };
            e = e
              ? {
                  type: "MemberExpression",
                  object: e,
                  property: t,
                  computed: !!(i && "Literal" === t.type),
                  optional: !1,
                }
              : t;
          }
          (j(), (r = e));
        } else r = O(t) && !/^[a-z]/.test(t) ? { type: "Identifier", name: t } : { type: "Literal", value: t };
      else r = { type: "Literal", value: t };
      if ("Literal" === r.type) {
        let t = r.value;
        return ew.call(e.components, t) ? e.components[t] : t;
      }
      if (e.evaluater) return e.evaluater.evaluateExpression(r);
      eM(e);
    }
    function eM(e, t) {
      let n = new ek("Cannot handle MDX estrees without `createEvaluater`", {
        ancestors: e.ancestors,
        place: t,
        ruleId: "mdx-estree",
        source: "hast-util-to-jsx-runtime",
      });
      throw ((n.file = e.filePath || void 0), (n.url = eR + "#cannot-handle-mdx-estrees-without-createevaluater"), n);
    }
    function eN(e) {
      return "-" + e.toLowerCase();
    }
    let ez = {
        action: ["form"],
        cite: ["blockquote", "del", "ins", "q"],
        data: ["object"],
        formAction: ["button", "input"],
        href: ["a", "area", "base", "link"],
        icon: ["menuitem"],
        itemId: null,
        manifest: ["html"],
        ping: ["a", "area"],
        poster: ["video"],
        src: ["audio", "embed", "iframe", "img", "input", "script", "source", "track", "video"],
      },
      eD = {};
    function eL(e, t, n) {
      var r;
      if ((r = e) && "object" == typeof r) {
        if ("value" in e) return "html" !== e.type || n ? e.value : "";
        if (t && "alt" in e && e.alt) return e.alt;
        if ("children" in e) return e$(e.children, t, n);
      }
      return Array.isArray(e) ? e$(e, t, n) : "";
    }
    function e$(e, t, n) {
      let r = [],
        i = -1;
      for (; ++i < e.length; ) r[i] = eL(e[i], t, n);
      return r.join("");
    }
    function eF(e, t, n, r) {
      let i,
        o = e.length,
        l = 0;
      if (((t = t < 0 ? (-t > o ? 0 : o + t) : t > o ? o : t), (n = n > 0 ? n : 0), r.length < 1e4))
        ((i = Array.from(r)).unshift(t, n), e.splice(...i));
      else
        for (n && e.splice(t, n); l < r.length; )
          ((i = r.slice(l, l + 1e4)).unshift(t, 0), e.splice(...i), (l += 1e4), (t += 1e4));
    }
    function e_(e, t) {
      return e.length > 0 ? (eF(e, e.length, 0, t), e) : t;
    }
    let eB = {}.hasOwnProperty,
      eH = e0(/[A-Za-z]/),
      eq = e0(/[\dA-Za-z]/),
      eU = e0(/[#-'*+\--9=?A-Z^-~]/);
    function eW(e) {
      return null !== e && (e < 32 || 127 === e);
    }
    let eV = e0(/\d/),
      eK = e0(/[\dA-Fa-f]/),
      eX = e0(/[!-/:-@[-`{-~]/);
    function eY(e) {
      return null !== e && e < -2;
    }
    function eG(e) {
      return null !== e && (e < 0 || 32 === e);
    }
    function eJ(e) {
      return -2 === e || -1 === e || 32 === e;
    }
    let eQ = e0(/\p{P}|\p{S}/u),
      eZ = e0(/\s/);
    function e0(e) {
      return function (t) {
        return null !== t && t > -1 && e.test(String.fromCharCode(t));
      };
    }
    function e1(e, t, n, r) {
      let i = r ? r - 1 : 1 / 0,
        o = 0;
      return function (r) {
        return eJ(r)
          ? (e.enter(n),
            (function r(l) {
              return eJ(l) && o++ < i ? (e.consume(l), r) : (e.exit(n), t(l));
            })(r))
          : t(r);
      };
    }
    let e2 = {
        tokenize: function (e) {
          let t,
            n = e.attempt(
              this.parser.constructs.contentInitial,
              function (t) {
                return null === t
                  ? void e.consume(t)
                  : (e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), e1(e, n, "linePrefix"));
              },
              function (n) {
                return (
                  e.enter("paragraph"),
                  (function n(r) {
                    let i = e.enter("chunkText", { contentType: "text", previous: t });
                    return (
                      t && (t.next = i),
                      (t = i),
                      (function t(r) {
                        if (null === r) {
                          (e.exit("chunkText"), e.exit("paragraph"), e.consume(r));
                          return;
                        }
                        return eY(r) ? (e.consume(r), e.exit("chunkText"), n) : (e.consume(r), t);
                      })(r)
                    );
                  })(n)
                );
              },
            );
          return n;
        },
      },
      e4 = {
        tokenize: function (e) {
          let t,
            n,
            r,
            i = this,
            o = [],
            l = 0;
          return a;
          function a(t) {
            if (l < o.length) {
              let n = o[l];
              return ((i.containerState = n[1]), e.attempt(n[0].continuation, s, u)(t));
            }
            return u(t);
          }
          function s(e) {
            if ((l++, i.containerState._closeFlow)) {
              let n;
              ((i.containerState._closeFlow = void 0), t && v());
              let r = i.events.length,
                o = r;
              for (; o--; )
                if ("exit" === i.events[o][0] && "chunkFlow" === i.events[o][1].type) {
                  n = i.events[o][1].end;
                  break;
                }
              g(l);
              let a = r;
              for (; a < i.events.length; ) ((i.events[a][1].end = { ...n }), a++);
              return (eF(i.events, o + 1, 0, i.events.slice(r)), (i.events.length = a), u(e));
            }
            return a(e);
          }
          function u(n) {
            if (l === o.length) {
              if (!t) return f(n);
              if (t.currentConstruct && t.currentConstruct.concrete) return h(n);
              i.interrupt = !!(t.currentConstruct && !t._gfmTableDynamicInterruptHack);
            }
            return ((i.containerState = {}), e.check(e5, c, d)(n));
          }
          function c(e) {
            return (t && v(), g(l), f(e));
          }
          function d(e) {
            return ((i.parser.lazy[i.now().line] = l !== o.length), (r = i.now().offset), h(e));
          }
          function f(t) {
            return ((i.containerState = {}), e.attempt(e5, p, h)(t));
          }
          function p(e) {
            return (l++, o.push([i.currentConstruct, i.containerState]), f(e));
          }
          function h(r) {
            if (null === r) {
              (t && v(), g(0), e.consume(r));
              return;
            }
            return (
              (t = t || i.parser.flow(i.now())),
              e.enter("chunkFlow", { _tokenizer: t, contentType: "flow", previous: n }),
              (function t(n) {
                if (null === n) {
                  (m(e.exit("chunkFlow"), !0), g(0), e.consume(n));
                  return;
                }
                return eY(n)
                  ? (e.consume(n), m(e.exit("chunkFlow")), (l = 0), (i.interrupt = void 0), a)
                  : (e.consume(n), t);
              })(r)
            );
          }
          function m(e, o) {
            let a = i.sliceStream(e);
            if (
              (o && a.push(null),
              (e.previous = n),
              n && (n.next = e),
              (n = e),
              t.defineSkip(e.start),
              t.write(a),
              i.parser.lazy[e.start.line])
            ) {
              let e,
                n,
                o = t.events.length;
              for (; o--; )
                if (t.events[o][1].start.offset < r && (!t.events[o][1].end || t.events[o][1].end.offset > r)) return;
              let a = i.events.length,
                s = a;
              for (; s--; )
                if ("exit" === i.events[s][0] && "chunkFlow" === i.events[s][1].type) {
                  if (e) {
                    n = i.events[s][1].end;
                    break;
                  }
                  e = !0;
                }
              for (g(l), o = a; o < i.events.length; ) ((i.events[o][1].end = { ...n }), o++);
              (eF(i.events, s + 1, 0, i.events.slice(a)), (i.events.length = o));
            }
          }
          function g(t) {
            let n = o.length;
            for (; n-- > t; ) {
              let t = o[n];
              ((i.containerState = t[1]), t[0].exit.call(i, e));
            }
            o.length = t;
          }
          function v() {
            (t.write([null]), (n = void 0), (t = void 0), (i.containerState._closeFlow = void 0));
          }
        },
      },
      e5 = {
        tokenize: function (e, t, n) {
          return e1(
            e,
            e.attempt(this.parser.constructs.document, t, n),
            "linePrefix",
            this.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4,
          );
        },
      },
      e3 = {
        partial: !0,
        tokenize: function (e, t, n) {
          return function (t) {
            return eJ(t) ? e1(e, r, "linePrefix")(t) : r(t);
          };
          function r(e) {
            return null === e || eY(e) ? t(e) : n(e);
          }
        },
      };
    class e6 {
      constructor(e) {
        ((this.left = e ? [...e] : []), (this.right = []));
      }
      get(e) {
        if (e < 0 || e >= this.left.length + this.right.length)
          throw RangeError(
            "Cannot access index `" +
              e +
              "` in a splice buffer of size `" +
              (this.left.length + this.right.length) +
              "`",
          );
        return e < this.left.length ? this.left[e] : this.right[this.right.length - e + this.left.length - 1];
      }
      get length() {
        return this.left.length + this.right.length;
      }
      shift() {
        return (this.setCursor(0), this.right.pop());
      }
      slice(e, t) {
        let n = null == t ? 1 / 0 : t;
        return n < this.left.length
          ? this.left.slice(e, n)
          : e > this.left.length
            ? this.right
                .slice(this.right.length - n + this.left.length, this.right.length - e + this.left.length)
                .reverse()
            : this.left.slice(e).concat(this.right.slice(this.right.length - n + this.left.length).reverse());
      }
      splice(e, t, n) {
        this.setCursor(Math.trunc(e));
        let r = this.right.splice(this.right.length - (t || 0), 1 / 0);
        return (n && e9(this.left, n), r.reverse());
      }
      pop() {
        return (this.setCursor(1 / 0), this.left.pop());
      }
      push(e) {
        (this.setCursor(1 / 0), this.left.push(e));
      }
      pushMany(e) {
        (this.setCursor(1 / 0), e9(this.left, e));
      }
      unshift(e) {
        (this.setCursor(0), this.right.push(e));
      }
      unshiftMany(e) {
        (this.setCursor(0), e9(this.right, e.reverse()));
      }
      setCursor(e) {
        if (
          e !== this.left.length &&
          (!(e > this.left.length) || 0 !== this.right.length) &&
          (!(e < 0) || 0 !== this.left.length)
        )
          if (e < this.left.length) {
            let t = this.left.splice(e, 1 / 0);
            e9(this.right, t.reverse());
          } else {
            let t = this.right.splice(this.left.length + this.right.length - e, 1 / 0);
            e9(this.left, t.reverse());
          }
      }
    }
    function e9(e, t) {
      let n = 0;
      if (t.length < 1e4) e.push(...t);
      else for (; n < t.length; ) (e.push(...t.slice(n, n + 1e4)), (n += 1e4));
    }
    function e7(e) {
      let t,
        n,
        r,
        i,
        o,
        l,
        a,
        s = {},
        u = -1,
        c = new e6(e);
      for (; ++u < c.length; ) {
        for (; u in s; ) u = s[u];
        if (
          ((t = c.get(u)),
          u &&
            "chunkFlow" === t[1].type &&
            "listItemPrefix" === c.get(u - 1)[1].type &&
            ((r = 0) < (l = t[1]._tokenizer.events).length && "lineEndingBlank" === l[r][1].type && (r += 2),
            r < l.length && "content" === l[r][1].type))
        )
          for (; ++r < l.length && "content" !== l[r][1].type; )
            "chunkText" === l[r][1].type && ((l[r][1]._isInFirstContentOfListItem = !0), r++);
        if ("enter" === t[0])
          t[1].contentType &&
            (Object.assign(
              s,
              (function (e, t) {
                let n,
                  r,
                  i = e.get(t)[1],
                  o = e.get(t)[2],
                  l = t - 1,
                  a = [],
                  s = i._tokenizer;
                !s &&
                  ((s = o.parser[i.contentType](i.start)),
                  i._contentTypeTextTrailing && (s._contentTypeTextTrailing = !0));
                let u = s.events,
                  c = [],
                  d = {},
                  f = -1,
                  p = i,
                  h = 0,
                  m = 0,
                  g = [0];
                for (; p; ) {
                  for (; e.get(++l)[1] !== p; );
                  (a.push(l),
                    !p._tokenizer &&
                      ((n = o.sliceStream(p)),
                      p.next || n.push(null),
                      r && s.defineSkip(p.start),
                      p._isInFirstContentOfListItem && (s._gfmTasklistFirstContentOfListItem = !0),
                      s.write(n),
                      p._isInFirstContentOfListItem && (s._gfmTasklistFirstContentOfListItem = void 0)),
                    (r = p),
                    (p = p.next));
                }
                for (p = i; ++f < u.length; )
                  "exit" === u[f][0] &&
                    "enter" === u[f - 1][0] &&
                    u[f][1].type === u[f - 1][1].type &&
                    u[f][1].start.line !== u[f][1].end.line &&
                    ((m = f + 1), g.push(m), (p._tokenizer = void 0), (p.previous = void 0), (p = p.next));
                for (
                  s.events = [], p ? ((p._tokenizer = void 0), (p.previous = void 0)) : g.pop(), f = g.length;
                  f--;
                ) {
                  let t = u.slice(g[f], g[f + 1]),
                    n = a.pop();
                  (c.push([n, n + t.length - 1]), e.splice(n, 2, t));
                }
                for (c.reverse(), f = -1; ++f < c.length; )
                  ((d[h + c[f][0]] = h + c[f][1]), (h += c[f][1] - c[f][0] - 1));
                return d;
              })(c, u),
            ),
            (u = s[u]),
            (a = !0));
        else if (t[1]._container) {
          for (r = u, n = void 0; r--; )
            if ("lineEnding" === (i = c.get(r))[1].type || "lineEndingBlank" === i[1].type)
              "enter" === i[0] && (n && (c.get(n)[1].type = "lineEndingBlank"), (i[1].type = "lineEnding"), (n = r));
            else if ("linePrefix" === i[1].type || "listItemIndent" === i[1].type);
            else break;
          n && ((t[1].end = { ...c.get(n)[1].start }), (o = c.slice(n, u)).unshift(t), c.splice(n, u - n + 1, o));
        }
      }
      return (eF(e, 0, 1 / 0, c.slice(0)), !a);
    }
    let e8 = {
        resolve: function (e) {
          return (e7(e), e);
        },
        tokenize: function (e, t) {
          let n;
          return function (t) {
            return (e.enter("content"), (n = e.enter("chunkContent", { contentType: "content" })), r(t));
          };
          function r(t) {
            return null === t ? i(t) : eY(t) ? e.check(te, o, i)(t) : (e.consume(t), r);
          }
          function i(n) {
            return (e.exit("chunkContent"), e.exit("content"), t(n));
          }
          function o(t) {
            return (
              e.consume(t),
              e.exit("chunkContent"),
              (n.next = e.enter("chunkContent", { contentType: "content", previous: n })),
              (n = n.next),
              r
            );
          }
        },
      },
      te = {
        partial: !0,
        tokenize: function (e, t, n) {
          let r = this;
          return function (t) {
            return (
              e.exit("chunkContent"),
              e.enter("lineEnding"),
              e.consume(t),
              e.exit("lineEnding"),
              e1(e, i, "linePrefix")
            );
          };
          function i(i) {
            if (null === i || eY(i)) return n(i);
            let o = r.events[r.events.length - 1];
            return !r.parser.constructs.disable.null.includes("codeIndented") &&
              o &&
              "linePrefix" === o[1].type &&
              o[2].sliceSerialize(o[1], !0).length >= 4
              ? t(i)
              : e.interrupt(r.parser.constructs.flow, n, t)(i);
          }
        },
      },
      tt = {
        tokenize: function (e) {
          let t = this,
            n = e.attempt(
              e3,
              function (r) {
                return null === r
                  ? void e.consume(r)
                  : (e.enter("lineEndingBlank"),
                    e.consume(r),
                    e.exit("lineEndingBlank"),
                    (t.currentConstruct = void 0),
                    n);
              },
              e.attempt(
                this.parser.constructs.flowInitial,
                r,
                e1(e, e.attempt(this.parser.constructs.flow, r, e.attempt(e8, r)), "linePrefix"),
              ),
            );
          return n;
          function r(r) {
            return null === r
              ? void e.consume(r)
              : (e.enter("lineEnding"), e.consume(r), e.exit("lineEnding"), (t.currentConstruct = void 0), n);
          }
        },
      },
      tn = { resolveAll: tl() },
      tr = to("string"),
      ti = to("text");
    function to(e) {
      return {
        resolveAll: tl("text" === e ? ta : void 0),
        tokenize: function (t) {
          let n = this,
            r = this.parser.constructs[e],
            i = t.attempt(r, o, l);
          return o;
          function o(e) {
            return s(e) ? i(e) : l(e);
          }
          function l(e) {
            return null === e ? void t.consume(e) : (t.enter("data"), t.consume(e), a);
          }
          function a(e) {
            return s(e) ? (t.exit("data"), i(e)) : (t.consume(e), a);
          }
          function s(e) {
            if (null === e) return !0;
            let t = r[e],
              i = -1;
            if (t)
              for (; ++i < t.length; ) {
                let e = t[i];
                if (!e.previous || e.previous.call(n, n.previous)) return !0;
              }
            return !1;
          }
        },
      };
    }
    function tl(e) {
      return function (t, n) {
        let r,
          i = -1;
        for (; ++i <= t.length; )
          void 0 === r
            ? t[i] && "data" === t[i][1].type && ((r = i), i++)
            : (t[i] && "data" === t[i][1].type) ||
              (i !== r + 2 && ((t[r][1].end = t[i - 1][1].end), t.splice(r + 2, i - r - 2), (i = r + 2)), (r = void 0));
        return e ? e(t, n) : t;
      };
    }
    function ta(e, t) {
      let n = 0;
      for (; ++n <= e.length; )
        if ((n === e.length || "lineEnding" === e[n][1].type) && "data" === e[n - 1][1].type) {
          let r,
            i = e[n - 1][1],
            o = t.sliceStream(i),
            l = o.length,
            a = -1,
            s = 0;
          for (; l--; ) {
            let e = o[l];
            if ("string" == typeof e) {
              for (a = e.length; 32 === e.charCodeAt(a - 1); ) (s++, a--);
              if (a) break;
              a = -1;
            } else if (-2 === e) ((r = !0), s++);
            else if (-1 === e);
            else {
              l++;
              break;
            }
          }
          if ((t._contentTypeTextTrailing && n === e.length && (s = 0), s)) {
            let o = {
              type: n === e.length || r || s < 2 ? "lineSuffix" : "hardBreakTrailing",
              start: {
                _bufferIndex: l ? a : i.start._bufferIndex + a,
                _index: i.start._index + l,
                line: i.end.line,
                column: i.end.column - s,
                offset: i.end.offset - s,
              },
              end: { ...i.end },
            };
            ((i.end = { ...o.start }),
              i.start.offset === i.end.offset
                ? Object.assign(i, o)
                : (e.splice(n, 0, ["enter", o, t], ["exit", o, t]), (n += 2)));
          }
          n++;
        }
      return e;
    }
    function ts(e) {
      return null === e || eG(e) || eZ(e) ? 1 : eQ(e) ? 2 : void 0;
    }
    function tu(e, t, n) {
      let r = [],
        i = -1;
      for (; ++i < e.length; ) {
        let o = e[i].resolveAll;
        o && !r.includes(o) && ((t = o(t, n)), r.push(o));
      }
      return t;
    }
    let tc = {
      name: "attention",
      resolveAll: function (e, t) {
        let n,
          r,
          i,
          o,
          l,
          a,
          s,
          u,
          c = -1;
        for (; ++c < e.length; )
          if ("enter" === e[c][0] && "attentionSequence" === e[c][1].type && e[c][1]._close) {
            for (n = c; n--; )
              if (
                "exit" === e[n][0] &&
                "attentionSequence" === e[n][1].type &&
                e[n][1]._open &&
                t.sliceSerialize(e[n][1]).charCodeAt(0) === t.sliceSerialize(e[c][1]).charCodeAt(0)
              ) {
                if (
                  (e[n][1]._close || e[c][1]._open) &&
                  (e[c][1].end.offset - e[c][1].start.offset) % 3 &&
                  !((e[n][1].end.offset - e[n][1].start.offset + e[c][1].end.offset - e[c][1].start.offset) % 3)
                )
                  continue;
                a =
                  e[n][1].end.offset - e[n][1].start.offset > 1 && e[c][1].end.offset - e[c][1].start.offset > 1
                    ? 2
                    : 1;
                let d = { ...e[n][1].end },
                  f = { ...e[c][1].start };
                (td(d, -a),
                  td(f, a),
                  (o = { type: a > 1 ? "strongSequence" : "emphasisSequence", start: d, end: { ...e[n][1].end } }),
                  (l = { type: a > 1 ? "strongSequence" : "emphasisSequence", start: { ...e[c][1].start }, end: f }),
                  (i = {
                    type: a > 1 ? "strongText" : "emphasisText",
                    start: { ...e[n][1].end },
                    end: { ...e[c][1].start },
                  }),
                  (r = { type: a > 1 ? "strong" : "emphasis", start: { ...o.start }, end: { ...l.end } }),
                  (e[n][1].end = { ...o.start }),
                  (e[c][1].start = { ...l.end }),
                  (s = []),
                  e[n][1].end.offset - e[n][1].start.offset &&
                    (s = e_(s, [
                      ["enter", e[n][1], t],
                      ["exit", e[n][1], t],
                    ])),
                  (s = e_(s, [
                    ["enter", r, t],
                    ["enter", o, t],
                    ["exit", o, t],
                    ["enter", i, t],
                  ])),
                  (s = e_(s, tu(t.parser.constructs.insideSpan.null, e.slice(n + 1, c), t))),
                  (s = e_(s, [
                    ["exit", i, t],
                    ["enter", l, t],
                    ["exit", l, t],
                    ["exit", r, t],
                  ])),
                  e[c][1].end.offset - e[c][1].start.offset
                    ? ((u = 2),
                      (s = e_(s, [
                        ["enter", e[c][1], t],
                        ["exit", e[c][1], t],
                      ])))
                    : (u = 0),
                  eF(e, n - 1, c - n + 3, s),
                  (c = n + s.length - u - 2));
                break;
              }
          }
        for (c = -1; ++c < e.length; ) "attentionSequence" === e[c][1].type && (e[c][1].type = "data");
        return e;
      },
      tokenize: function (e, t) {
        let n,
          r = this.parser.constructs.attentionMarkers.null,
          i = this.previous,
          o = ts(i);
        return function (l) {
          return (
            (n = l),
            e.enter("attentionSequence"),
            (function l(a) {
              if (a === n) return (e.consume(a), l);
              let s = e.exit("attentionSequence"),
                u = ts(a),
                c = !u || (2 === u && o) || r.includes(a),
                d = !o || (2 === o && u) || r.includes(i);
              return (
                (s._open = !!(42 === n ? c : c && (o || !d))),
                (s._close = !!(42 === n ? d : d && (u || !c))),
                t(a)
              );
            })(l)
          );
        };
      },
    };
    function td(e, t) {
      ((e.column += t), (e.offset += t), (e._bufferIndex += t));
    }
    let tf = {
        continuation: {
          tokenize: function (e, t, n) {
            let r = this;
            return function (t) {
              return eJ(t)
                ? e1(e, i, "linePrefix", r.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4)(t)
                : i(t);
            };
            function i(r) {
              return e.attempt(tf, t, n)(r);
            }
          },
        },
        exit: function (e) {
          e.exit("blockQuote");
        },
        name: "blockQuote",
        tokenize: function (e, t, n) {
          let r = this;
          return function (t) {
            if (62 === t) {
              let n = r.containerState;
              return (
                n.open || (e.enter("blockQuote", { _container: !0 }), (n.open = !0)),
                e.enter("blockQuotePrefix"),
                e.enter("blockQuoteMarker"),
                e.consume(t),
                e.exit("blockQuoteMarker"),
                i
              );
            }
            return n(t);
          };
          function i(n) {
            return eJ(n)
              ? (e.enter("blockQuotePrefixWhitespace"),
                e.consume(n),
                e.exit("blockQuotePrefixWhitespace"),
                e.exit("blockQuotePrefix"),
                t)
              : (e.exit("blockQuotePrefix"), t(n));
          }
        },
      },
      tp = {
        name: "characterEscape",
        tokenize: function (e, t, n) {
          return function (t) {
            return (e.enter("characterEscape"), e.enter("escapeMarker"), e.consume(t), e.exit("escapeMarker"), r);
          };
          function r(r) {
            return eX(r)
              ? (e.enter("characterEscapeValue"),
                e.consume(r),
                e.exit("characterEscapeValue"),
                e.exit("characterEscape"),
                t)
              : n(r);
          }
        },
      },
      th = document.createElement("i");
    function tm(e) {
      let t = "&" + e + ";";
      th.innerHTML = t;
      let n = th.textContent;
      return (59 !== n.charCodeAt(n.length - 1) || "semi" === e) && n !== t && n;
    }
    let tg = {
        name: "characterReference",
        tokenize: function (e, t, n) {
          let r,
            i,
            o = this,
            l = 0;
          return function (t) {
            return (
              e.enter("characterReference"),
              e.enter("characterReferenceMarker"),
              e.consume(t),
              e.exit("characterReferenceMarker"),
              a
            );
          };
          function a(t) {
            return 35 === t
              ? (e.enter("characterReferenceMarkerNumeric"), e.consume(t), e.exit("characterReferenceMarkerNumeric"), s)
              : (e.enter("characterReferenceValue"), (r = 31), (i = eq), u(t));
          }
          function s(t) {
            return 88 === t || 120 === t
              ? (e.enter("characterReferenceMarkerHexadecimal"),
                e.consume(t),
                e.exit("characterReferenceMarkerHexadecimal"),
                e.enter("characterReferenceValue"),
                (r = 6),
                (i = eK),
                u)
              : (e.enter("characterReferenceValue"), (r = 7), (i = eV), u(t));
          }
          function u(a) {
            if (59 === a && l) {
              let r = e.exit("characterReferenceValue");
              return i !== eq || tm(o.sliceSerialize(r))
                ? (e.enter("characterReferenceMarker"),
                  e.consume(a),
                  e.exit("characterReferenceMarker"),
                  e.exit("characterReference"),
                  t)
                : n(a);
            }
            return i(a) && l++ < r ? (e.consume(a), u) : n(a);
          }
        },
      },
      tv = {
        partial: !0,
        tokenize: function (e, t, n) {
          let r = this;
          return function (t) {
            return null === t ? n(t) : (e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), i);
          };
          function i(e) {
            return r.parser.lazy[r.now().line] ? n(e) : t(e);
          }
        },
      },
      ty = {
        concrete: !0,
        name: "codeFenced",
        tokenize: function (e, t, n) {
          let r,
            i = this,
            o = {
              partial: !0,
              tokenize: function (e, t, n) {
                let o = 0;
                return function (t) {
                  return (e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), l);
                };
                function l(t) {
                  return (
                    e.enter("codeFencedFence"),
                    eJ(t)
                      ? e1(
                          e,
                          s,
                          "linePrefix",
                          i.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4,
                        )(t)
                      : s(t)
                  );
                }
                function s(t) {
                  return t === r
                    ? (e.enter("codeFencedFenceSequence"),
                      (function t(i) {
                        return i === r
                          ? (o++, e.consume(i), t)
                          : o >= a
                            ? (e.exit("codeFencedFenceSequence"), eJ(i) ? e1(e, u, "whitespace")(i) : u(i))
                            : n(i);
                      })(t))
                    : n(t);
                }
                function u(r) {
                  return null === r || eY(r) ? (e.exit("codeFencedFence"), t(r)) : n(r);
                }
              },
            },
            l = 0,
            a = 0;
          return function (t) {
            var o;
            let u;
            return (
              (o = t),
              (l =
                (u = i.events[i.events.length - 1]) && "linePrefix" === u[1].type
                  ? u[2].sliceSerialize(u[1], !0).length
                  : 0),
              (r = o),
              e.enter("codeFenced"),
              e.enter("codeFencedFence"),
              e.enter("codeFencedFenceSequence"),
              (function t(i) {
                return i === r
                  ? (a++, e.consume(i), t)
                  : a < 3
                    ? n(i)
                    : (e.exit("codeFencedFenceSequence"), eJ(i) ? e1(e, s, "whitespace")(i) : s(i));
              })(o)
            );
          };
          function s(o) {
            return null === o || eY(o)
              ? (e.exit("codeFencedFence"), i.interrupt ? t(o) : e.check(tv, c, h)(o))
              : (e.enter("codeFencedFenceInfo"),
                e.enter("chunkString", { contentType: "string" }),
                (function t(i) {
                  return null === i || eY(i)
                    ? (e.exit("chunkString"), e.exit("codeFencedFenceInfo"), s(i))
                    : eJ(i)
                      ? (e.exit("chunkString"), e.exit("codeFencedFenceInfo"), e1(e, u, "whitespace")(i))
                      : 96 === i && i === r
                        ? n(i)
                        : (e.consume(i), t);
                })(o));
          }
          function u(t) {
            return null === t || eY(t)
              ? s(t)
              : (e.enter("codeFencedFenceMeta"),
                e.enter("chunkString", { contentType: "string" }),
                (function t(i) {
                  return null === i || eY(i)
                    ? (e.exit("chunkString"), e.exit("codeFencedFenceMeta"), s(i))
                    : 96 === i && i === r
                      ? n(i)
                      : (e.consume(i), t);
                })(t));
          }
          function c(t) {
            return e.attempt(o, h, d)(t);
          }
          function d(t) {
            return (e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), f);
          }
          function f(t) {
            return l > 0 && eJ(t) ? e1(e, p, "linePrefix", l + 1)(t) : p(t);
          }
          function p(t) {
            return null === t || eY(t)
              ? e.check(tv, c, h)(t)
              : (e.enter("codeFlowValue"),
                (function t(n) {
                  return null === n || eY(n) ? (e.exit("codeFlowValue"), p(n)) : (e.consume(n), t);
                })(t));
          }
          function h(n) {
            return (e.exit("codeFenced"), t(n));
          }
        },
      },
      tb = {
        name: "codeIndented",
        tokenize: function (e, t, n) {
          let r = this;
          return function (t) {
            return (e.enter("codeIndented"), e1(e, i, "linePrefix", 5)(t));
          };
          function i(t) {
            let i = r.events[r.events.length - 1];
            return i && "linePrefix" === i[1].type && i[2].sliceSerialize(i[1], !0).length >= 4
              ? (function t(n) {
                  return null === n
                    ? o(n)
                    : eY(n)
                      ? e.attempt(tx, t, o)(n)
                      : (e.enter("codeFlowValue"),
                        (function n(r) {
                          return null === r || eY(r) ? (e.exit("codeFlowValue"), t(r)) : (e.consume(r), n);
                        })(n));
                })(t)
              : n(t);
          }
          function o(n) {
            return (e.exit("codeIndented"), t(n));
          }
        },
      },
      tx = {
        partial: !0,
        tokenize: function (e, t, n) {
          let r = this;
          return i;
          function i(t) {
            return r.parser.lazy[r.now().line]
              ? n(t)
              : eY(t)
                ? (e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), i)
                : e1(e, o, "linePrefix", 5)(t);
          }
          function o(e) {
            let o = r.events[r.events.length - 1];
            return o && "linePrefix" === o[1].type && o[2].sliceSerialize(o[1], !0).length >= 4
              ? t(e)
              : eY(e)
                ? i(e)
                : n(e);
          }
        },
      };
    function tk(e, t, n, r, i, o, l, a, s) {
      let u = s || 1 / 0,
        c = 0;
      return function (t) {
        return 60 === t
          ? (e.enter(r), e.enter(i), e.enter(o), e.consume(t), e.exit(o), d)
          : null === t || 32 === t || 41 === t || eW(t)
            ? n(t)
            : (e.enter(r), e.enter(l), e.enter(a), e.enter("chunkString", { contentType: "string" }), h(t));
      };
      function d(n) {
        return 62 === n
          ? (e.enter(o), e.consume(n), e.exit(o), e.exit(i), e.exit(r), t)
          : (e.enter(a), e.enter("chunkString", { contentType: "string" }), f(n));
      }
      function f(t) {
        return 62 === t
          ? (e.exit("chunkString"), e.exit(a), d(t))
          : null === t || 60 === t || eY(t)
            ? n(t)
            : (e.consume(t), 92 === t ? p : f);
      }
      function p(t) {
        return 60 === t || 62 === t || 92 === t ? (e.consume(t), f) : f(t);
      }
      function h(i) {
        return !c && (null === i || 41 === i || eG(i))
          ? (e.exit("chunkString"), e.exit(a), e.exit(l), e.exit(r), t(i))
          : c < u && 40 === i
            ? (e.consume(i), c++, h)
            : 41 === i
              ? (e.consume(i), c--, h)
              : null === i || 32 === i || 40 === i || eW(i)
                ? n(i)
                : (e.consume(i), 92 === i ? m : h);
      }
      function m(t) {
        return 40 === t || 41 === t || 92 === t ? (e.consume(t), h) : h(t);
      }
    }
    function tw(e, t, n, r, i, o) {
      let l,
        a = this,
        s = 0;
      return function (t) {
        return (e.enter(r), e.enter(i), e.consume(t), e.exit(i), e.enter(o), u);
      };
      function u(d) {
        return s > 999 ||
          null === d ||
          91 === d ||
          (93 === d && !l) ||
          (94 === d && !s && "_hiddenFootnoteSupport" in a.parser.constructs)
          ? n(d)
          : 93 === d
            ? (e.exit(o), e.enter(i), e.consume(d), e.exit(i), e.exit(r), t)
            : eY(d)
              ? (e.enter("lineEnding"), e.consume(d), e.exit("lineEnding"), u)
              : (e.enter("chunkString", { contentType: "string" }), c(d));
      }
      function c(t) {
        return null === t || 91 === t || 93 === t || eY(t) || s++ > 999
          ? (e.exit("chunkString"), u(t))
          : (e.consume(t), l || (l = !eJ(t)), 92 === t ? d : c);
      }
      function d(t) {
        return 91 === t || 92 === t || 93 === t ? (e.consume(t), s++, c) : c(t);
      }
    }
    function tS(e, t, n, r, i, o) {
      let l;
      return function (t) {
        return 34 === t || 39 === t || 40 === t
          ? (e.enter(r), e.enter(i), e.consume(t), e.exit(i), (l = 40 === t ? 41 : t), a)
          : n(t);
      };
      function a(n) {
        return n === l ? (e.enter(i), e.consume(n), e.exit(i), e.exit(r), t) : (e.enter(o), s(n));
      }
      function s(t) {
        return t === l
          ? (e.exit(o), a(l))
          : null === t
            ? n(t)
            : eY(t)
              ? (e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), e1(e, s, "linePrefix"))
              : (e.enter("chunkString", { contentType: "string" }), u(t));
      }
      function u(t) {
        return t === l || null === t || eY(t) ? (e.exit("chunkString"), s(t)) : (e.consume(t), 92 === t ? c : u);
      }
      function c(t) {
        return t === l || 92 === t ? (e.consume(t), u) : u(t);
      }
    }
    function tC(e, t) {
      let n;
      return function r(i) {
        return eY(i)
          ? (e.enter("lineEnding"), e.consume(i), e.exit("lineEnding"), (n = !0), r)
          : eJ(i)
            ? e1(e, r, n ? "linePrefix" : "lineSuffix")(i)
            : t(i);
      };
    }
    function tE(e) {
      return e
        .replace(/[\t\n\r ]+/g, " ")
        .replace(/^ | $/g, "")
        .toLowerCase()
        .toUpperCase();
    }
    let tj = {
        partial: !0,
        tokenize: function (e, t, n) {
          return function (t) {
            return eG(t) ? tC(e, r)(t) : n(t);
          };
          function r(t) {
            return tS(e, i, n, "definitionTitle", "definitionTitleMarker", "definitionTitleString")(t);
          }
          function i(t) {
            return eJ(t) ? e1(e, o, "whitespace")(t) : o(t);
          }
          function o(e) {
            return null === e || eY(e) ? t(e) : n(e);
          }
        },
      },
      tR = [
        "address",
        "article",
        "aside",
        "base",
        "basefont",
        "blockquote",
        "body",
        "caption",
        "center",
        "col",
        "colgroup",
        "dd",
        "details",
        "dialog",
        "dir",
        "div",
        "dl",
        "dt",
        "fieldset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "frame",
        "frameset",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "head",
        "header",
        "hr",
        "html",
        "iframe",
        "legend",
        "li",
        "link",
        "main",
        "menu",
        "menuitem",
        "nav",
        "noframes",
        "ol",
        "optgroup",
        "option",
        "p",
        "param",
        "search",
        "section",
        "summary",
        "table",
        "tbody",
        "td",
        "tfoot",
        "th",
        "thead",
        "title",
        "tr",
        "track",
        "ul",
      ],
      tP = ["pre", "script", "style", "textarea"],
      tT = {
        partial: !0,
        tokenize: function (e, t, n) {
          return function (r) {
            return (e.enter("lineEnding"), e.consume(r), e.exit("lineEnding"), e.attempt(e3, t, n));
          };
        },
      },
      tA = {
        partial: !0,
        tokenize: function (e, t, n) {
          let r = this;
          return function (t) {
            return eY(t) ? (e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), i) : n(t);
          };
          function i(e) {
            return r.parser.lazy[r.now().line] ? n(e) : t(e);
          }
        },
      },
      tO = {
        name: "labelEnd",
        resolveAll: function (e) {
          let t = -1,
            n = [];
          for (; ++t < e.length; ) {
            let r = e[t][1];
            if ((n.push(e[t]), "labelImage" === r.type || "labelLink" === r.type || "labelEnd" === r.type)) {
              let e = "labelImage" === r.type ? 4 : 2;
              ((r.type = "data"), (t += e));
            }
          }
          return (e.length !== n.length && eF(e, 0, e.length, n), e);
        },
        resolveTo: function (e, t) {
          let n,
            r,
            i,
            o,
            l = e.length,
            a = 0;
          for (; l--; )
            if (((n = e[l][1]), r)) {
              if ("link" === n.type || ("labelLink" === n.type && n._inactive)) break;
              "enter" === e[l][0] && "labelLink" === n.type && (n._inactive = !0);
            } else if (i) {
              if (
                "enter" === e[l][0] &&
                ("labelImage" === n.type || "labelLink" === n.type) &&
                !n._balanced &&
                ((r = l), "labelLink" !== n.type)
              ) {
                a = 2;
                break;
              }
            } else "labelEnd" === n.type && (i = l);
          let s = {
              type: "labelLink" === e[r][1].type ? "link" : "image",
              start: { ...e[r][1].start },
              end: { ...e[e.length - 1][1].end },
            },
            u = { type: "label", start: { ...e[r][1].start }, end: { ...e[i][1].end } },
            c = { type: "labelText", start: { ...e[r + a + 2][1].end }, end: { ...e[i - 2][1].start } };
          return (
            (o = e_(
              (o = [
                ["enter", s, t],
                ["enter", u, t],
              ]),
              e.slice(r + 1, r + a + 3),
            )),
            (o = e_(o, [["enter", c, t]])),
            (o = e_(o, tu(t.parser.constructs.insideSpan.null, e.slice(r + a + 4, i - 3), t))),
            (o = e_(o, [["exit", c, t], e[i - 2], e[i - 1], ["exit", u, t]])),
            (o = e_(o, e.slice(i + 1))),
            (o = e_(o, [["exit", s, t]])),
            eF(e, r, e.length, o),
            e
          );
        },
        tokenize: function (e, t, n) {
          let r,
            i,
            o = this,
            l = o.events.length;
          for (; l--; )
            if (
              ("labelImage" === o.events[l][1].type || "labelLink" === o.events[l][1].type) &&
              !o.events[l][1]._balanced
            ) {
              r = o.events[l][1];
              break;
            }
          return function (t) {
            return r
              ? r._inactive
                ? c(t)
                : ((i = o.parser.defined.includes(tE(o.sliceSerialize({ start: r.end, end: o.now() })))),
                  e.enter("labelEnd"),
                  e.enter("labelMarker"),
                  e.consume(t),
                  e.exit("labelMarker"),
                  e.exit("labelEnd"),
                  a)
              : n(t);
          };
          function a(t) {
            return 40 === t
              ? e.attempt(tI, u, i ? u : c)(t)
              : 91 === t
                ? e.attempt(tM, u, i ? s : c)(t)
                : i
                  ? u(t)
                  : c(t);
          }
          function s(t) {
            return e.attempt(tN, u, c)(t);
          }
          function u(e) {
            return t(e);
          }
          function c(e) {
            return ((r._balanced = !0), n(e));
          }
        },
      },
      tI = {
        tokenize: function (e, t, n) {
          return function (t) {
            return (e.enter("resource"), e.enter("resourceMarker"), e.consume(t), e.exit("resourceMarker"), r);
          };
          function r(t) {
            return eG(t) ? tC(e, i)(t) : i(t);
          }
          function i(t) {
            return 41 === t
              ? u(t)
              : tk(
                  e,
                  o,
                  l,
                  "resourceDestination",
                  "resourceDestinationLiteral",
                  "resourceDestinationLiteralMarker",
                  "resourceDestinationRaw",
                  "resourceDestinationString",
                  32,
                )(t);
          }
          function o(t) {
            return eG(t) ? tC(e, a)(t) : u(t);
          }
          function l(e) {
            return n(e);
          }
          function a(t) {
            return 34 === t || 39 === t || 40 === t
              ? tS(e, s, n, "resourceTitle", "resourceTitleMarker", "resourceTitleString")(t)
              : u(t);
          }
          function s(t) {
            return eG(t) ? tC(e, u)(t) : u(t);
          }
          function u(r) {
            return 41 === r
              ? (e.enter("resourceMarker"), e.consume(r), e.exit("resourceMarker"), e.exit("resource"), t)
              : n(r);
          }
        },
      },
      tM = {
        tokenize: function (e, t, n) {
          let r = this;
          return function (t) {
            return tw.call(r, e, i, o, "reference", "referenceMarker", "referenceString")(t);
          };
          function i(e) {
            return r.parser.defined.includes(tE(r.sliceSerialize(r.events[r.events.length - 1][1]).slice(1, -1)))
              ? t(e)
              : n(e);
          }
          function o(e) {
            return n(e);
          }
        },
      },
      tN = {
        tokenize: function (e, t, n) {
          return function (t) {
            return (e.enter("reference"), e.enter("referenceMarker"), e.consume(t), e.exit("referenceMarker"), r);
          };
          function r(r) {
            return 93 === r
              ? (e.enter("referenceMarker"), e.consume(r), e.exit("referenceMarker"), e.exit("reference"), t)
              : n(r);
          }
        },
      },
      tz = {
        name: "labelStartImage",
        resolveAll: tO.resolveAll,
        tokenize: function (e, t, n) {
          let r = this;
          return function (t) {
            return (e.enter("labelImage"), e.enter("labelImageMarker"), e.consume(t), e.exit("labelImageMarker"), i);
          };
          function i(t) {
            return 91 === t
              ? (e.enter("labelMarker"), e.consume(t), e.exit("labelMarker"), e.exit("labelImage"), o)
              : n(t);
          }
          function o(e) {
            return 94 === e && "_hiddenFootnoteSupport" in r.parser.constructs ? n(e) : t(e);
          }
        },
      },
      tD = {
        name: "labelStartLink",
        resolveAll: tO.resolveAll,
        tokenize: function (e, t, n) {
          let r = this;
          return function (t) {
            return (
              e.enter("labelLink"),
              e.enter("labelMarker"),
              e.consume(t),
              e.exit("labelMarker"),
              e.exit("labelLink"),
              i
            );
          };
          function i(e) {
            return 94 === e && "_hiddenFootnoteSupport" in r.parser.constructs ? n(e) : t(e);
          }
        },
      },
      tL = {
        name: "lineEnding",
        tokenize: function (e, t) {
          return function (n) {
            return (e.enter("lineEnding"), e.consume(n), e.exit("lineEnding"), e1(e, t, "linePrefix"));
          };
        },
      },
      t$ = {
        name: "thematicBreak",
        tokenize: function (e, t, n) {
          let r,
            i = 0;
          return function (o) {
            var l;
            return (
              e.enter("thematicBreak"),
              (r = l = o),
              (function o(l) {
                return l === r
                  ? (e.enter("thematicBreakSequence"),
                    (function t(n) {
                      return n === r
                        ? (e.consume(n), i++, t)
                        : (e.exit("thematicBreakSequence"), eJ(n) ? e1(e, o, "whitespace")(n) : o(n));
                    })(l))
                  : i >= 3 && (null === l || eY(l))
                    ? (e.exit("thematicBreak"), t(l))
                    : n(l);
              })(l)
            );
          };
        },
      },
      tF = {
        continuation: {
          tokenize: function (e, t, n) {
            let r = this;
            return (
              (r.containerState._closeFlow = void 0),
              e.check(
                e3,
                function (n) {
                  return (
                    (r.containerState.furtherBlankLines =
                      r.containerState.furtherBlankLines || r.containerState.initialBlankLine),
                    e1(e, t, "listItemIndent", r.containerState.size + 1)(n)
                  );
                },
                function (n) {
                  return r.containerState.furtherBlankLines || !eJ(n)
                    ? ((r.containerState.furtherBlankLines = void 0),
                      (r.containerState.initialBlankLine = void 0),
                      i(n))
                    : ((r.containerState.furtherBlankLines = void 0),
                      (r.containerState.initialBlankLine = void 0),
                      e.attempt(tB, t, i)(n));
                },
              )
            );
            function i(i) {
              return (
                (r.containerState._closeFlow = !0),
                (r.interrupt = void 0),
                e1(
                  e,
                  e.attempt(tF, t, n),
                  "linePrefix",
                  r.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4,
                )(i)
              );
            }
          },
        },
        exit: function (e) {
          e.exit(this.containerState.type);
        },
        name: "list",
        tokenize: function (e, t, n) {
          let r = this,
            i = r.events[r.events.length - 1],
            o = i && "linePrefix" === i[1].type ? i[2].sliceSerialize(i[1], !0).length : 0,
            l = 0;
          return function (t) {
            let i = r.containerState.type || (42 === t || 43 === t || 45 === t ? "listUnordered" : "listOrdered");
            if ("listUnordered" === i ? !r.containerState.marker || t === r.containerState.marker : eV(t)) {
              if (
                (r.containerState.type || ((r.containerState.type = i), e.enter(i, { _container: !0 })),
                "listUnordered" === i)
              )
                return (e.enter("listItemPrefix"), 42 === t || 45 === t ? e.check(t$, n, a)(t) : a(t));
              if (!r.interrupt || 49 === t)
                return (
                  e.enter("listItemPrefix"),
                  e.enter("listItemValue"),
                  (function t(i) {
                    return eV(i) && ++l < 10
                      ? (e.consume(i), t)
                      : (!r.interrupt || l < 2) &&
                          (r.containerState.marker ? i === r.containerState.marker : 41 === i || 46 === i)
                        ? (e.exit("listItemValue"), a(i))
                        : n(i);
                  })(t)
                );
            }
            return n(t);
          };
          function a(t) {
            return (
              e.enter("listItemMarker"),
              e.consume(t),
              e.exit("listItemMarker"),
              (r.containerState.marker = r.containerState.marker || t),
              e.check(e3, r.interrupt ? n : s, e.attempt(t_, c, u))
            );
          }
          function s(e) {
            return ((r.containerState.initialBlankLine = !0), o++, c(e));
          }
          function u(t) {
            return eJ(t)
              ? (e.enter("listItemPrefixWhitespace"), e.consume(t), e.exit("listItemPrefixWhitespace"), c)
              : n(t);
          }
          function c(n) {
            return ((r.containerState.size = o + r.sliceSerialize(e.exit("listItemPrefix"), !0).length), t(n));
          }
        },
      },
      t_ = {
        partial: !0,
        tokenize: function (e, t, n) {
          let r = this;
          return e1(
            e,
            function (e) {
              let i = r.events[r.events.length - 1];
              return !eJ(e) && i && "listItemPrefixWhitespace" === i[1].type ? t(e) : n(e);
            },
            "listItemPrefixWhitespace",
            r.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 5,
          );
        },
      },
      tB = {
        partial: !0,
        tokenize: function (e, t, n) {
          let r = this;
          return e1(
            e,
            function (e) {
              let i = r.events[r.events.length - 1];
              return i &&
                "listItemIndent" === i[1].type &&
                i[2].sliceSerialize(i[1], !0).length === r.containerState.size
                ? t(e)
                : n(e);
            },
            "listItemIndent",
            r.containerState.size + 1,
          );
        },
      },
      tH = {
        name: "setextUnderline",
        resolveTo: function (e, t) {
          let n,
            r,
            i,
            o = e.length;
          for (; o--; )
            if ("enter" === e[o][0]) {
              if ("content" === e[o][1].type) {
                n = o;
                break;
              }
              "paragraph" === e[o][1].type && (r = o);
            } else ("content" === e[o][1].type && e.splice(o, 1), i || "definition" !== e[o][1].type || (i = o));
          let l = { type: "setextHeading", start: { ...e[n][1].start }, end: { ...e[e.length - 1][1].end } };
          return (
            (e[r][1].type = "setextHeadingText"),
            i
              ? (e.splice(r, 0, ["enter", l, t]),
                e.splice(i + 1, 0, ["exit", e[n][1], t]),
                (e[n][1].end = { ...e[i][1].end }))
              : (e[n][1] = l),
            e.push(["exit", l, t]),
            e
          );
        },
        tokenize: function (e, t, n) {
          let r,
            i = this;
          return function (t) {
            var l;
            let a,
              s = i.events.length;
            for (; s--; )
              if (
                "lineEnding" !== i.events[s][1].type &&
                "linePrefix" !== i.events[s][1].type &&
                "content" !== i.events[s][1].type
              ) {
                a = "paragraph" === i.events[s][1].type;
                break;
              }
            return !i.parser.lazy[i.now().line] && (i.interrupt || a)
              ? (e.enter("setextHeadingLine"),
                (r = t),
                (l = t),
                e.enter("setextHeadingLineSequence"),
                (function t(n) {
                  return n === r
                    ? (e.consume(n), t)
                    : (e.exit("setextHeadingLineSequence"), eJ(n) ? e1(e, o, "lineSuffix")(n) : o(n));
                })(l))
              : n(t);
          };
          function o(r) {
            return null === r || eY(r) ? (e.exit("setextHeadingLine"), t(r)) : n(r);
          }
        },
      };
    e.s(
      [
        "attentionMarkers",
        0,
        { null: [42, 95] },
        "contentInitial",
        0,
        {
          91: {
            name: "definition",
            tokenize: function (e, t, n) {
              let r,
                i = this;
              return function (t) {
                var r;
                return (
                  e.enter("definition"),
                  (r = t),
                  tw.call(i, e, o, n, "definitionLabel", "definitionLabelMarker", "definitionLabelString")(r)
                );
              };
              function o(t) {
                return ((r = tE(i.sliceSerialize(i.events[i.events.length - 1][1]).slice(1, -1))), 58 === t)
                  ? (e.enter("definitionMarker"), e.consume(t), e.exit("definitionMarker"), l)
                  : n(t);
              }
              function l(t) {
                return eG(t) ? tC(e, a)(t) : a(t);
              }
              function a(t) {
                return tk(
                  e,
                  s,
                  n,
                  "definitionDestination",
                  "definitionDestinationLiteral",
                  "definitionDestinationLiteralMarker",
                  "definitionDestinationRaw",
                  "definitionDestinationString",
                )(t);
              }
              function s(t) {
                return e.attempt(tj, u, u)(t);
              }
              function u(t) {
                return eJ(t) ? e1(e, c, "whitespace")(t) : c(t);
              }
              function c(o) {
                return null === o || eY(o) ? (e.exit("definition"), i.parser.defined.push(r), t(o)) : n(o);
              }
            },
          },
        },
        "disable",
        0,
        { null: [] },
        "document",
        0,
        {
          42: tF,
          43: tF,
          45: tF,
          48: tF,
          49: tF,
          50: tF,
          51: tF,
          52: tF,
          53: tF,
          54: tF,
          55: tF,
          56: tF,
          57: tF,
          62: tf,
        },
        "flow",
        0,
        {
          35: {
            name: "headingAtx",
            resolve: function (e, t) {
              let n,
                r,
                i = e.length - 2,
                o = 3;
              return (
                "whitespace" === e[3][1].type && (o += 2),
                i - 2 > o && "whitespace" === e[i][1].type && (i -= 2),
                "atxHeadingSequence" === e[i][1].type &&
                  (o === i - 1 || (i - 4 > o && "whitespace" === e[i - 2][1].type)) &&
                  (i -= o + 1 === i ? 2 : 4),
                i > o &&
                  ((n = { type: "atxHeadingText", start: e[o][1].start, end: e[i][1].end }),
                  (r = { type: "chunkText", start: e[o][1].start, end: e[i][1].end, contentType: "text" }),
                  eF(e, o, i - o + 1, [
                    ["enter", n, t],
                    ["enter", r, t],
                    ["exit", r, t],
                    ["exit", n, t],
                  ])),
                e
              );
            },
            tokenize: function (e, t, n) {
              let r = 0;
              return function (i) {
                var o;
                return (
                  e.enter("atxHeading"),
                  (o = i),
                  e.enter("atxHeadingSequence"),
                  (function i(o) {
                    return 35 === o && r++ < 6
                      ? (e.consume(o), i)
                      : null === o || eG(o)
                        ? (e.exit("atxHeadingSequence"),
                          (function n(r) {
                            return 35 === r
                              ? (e.enter("atxHeadingSequence"),
                                (function t(r) {
                                  return 35 === r ? (e.consume(r), t) : (e.exit("atxHeadingSequence"), n(r));
                                })(r))
                              : null === r || eY(r)
                                ? (e.exit("atxHeading"), t(r))
                                : eJ(r)
                                  ? e1(e, n, "whitespace")(r)
                                  : (e.enter("atxHeadingText"),
                                    (function t(r) {
                                      return null === r || 35 === r || eG(r)
                                        ? (e.exit("atxHeadingText"), n(r))
                                        : (e.consume(r), t);
                                    })(r));
                          })(o))
                        : n(o);
                  })(o)
                );
              };
            },
          },
          42: t$,
          45: [tH, t$],
          60: {
            concrete: !0,
            name: "htmlFlow",
            resolveTo: function (e) {
              let t = e.length;
              for (; t-- && ("enter" !== e[t][0] || "htmlFlow" !== e[t][1].type); );
              return (
                t > 1 &&
                  "linePrefix" === e[t - 2][1].type &&
                  ((e[t][1].start = e[t - 2][1].start), (e[t + 1][1].start = e[t - 2][1].start), e.splice(t - 2, 2)),
                e
              );
            },
            tokenize: function (e, t, n) {
              let r,
                i,
                o,
                l,
                a,
                s = this;
              return function (t) {
                var n;
                return ((n = t), e.enter("htmlFlow"), e.enter("htmlFlowData"), e.consume(n), u);
              };
              function u(l) {
                return 33 === l
                  ? (e.consume(l), c)
                  : 47 === l
                    ? (e.consume(l), (i = !0), p)
                    : 63 === l
                      ? (e.consume(l), (r = 3), s.interrupt ? t : I)
                      : eH(l)
                        ? (e.consume(l), (o = String.fromCharCode(l)), h)
                        : n(l);
              }
              function c(i) {
                return 45 === i
                  ? (e.consume(i), (r = 2), d)
                  : 91 === i
                    ? (e.consume(i), (r = 5), (l = 0), f)
                    : eH(i)
                      ? (e.consume(i), (r = 4), s.interrupt ? t : I)
                      : n(i);
              }
              function d(r) {
                return 45 === r ? (e.consume(r), s.interrupt ? t : I) : n(r);
              }
              function f(r) {
                let i = "CDATA[";
                return r === i.charCodeAt(l++) ? ((e.consume(r), l === i.length) ? (s.interrupt ? t : C) : f) : n(r);
              }
              function p(t) {
                return eH(t) ? (e.consume(t), (o = String.fromCharCode(t)), h) : n(t);
              }
              function h(l) {
                if (null === l || 47 === l || 62 === l || eG(l)) {
                  let a = 47 === l,
                    u = o.toLowerCase();
                  return !a && !i && tP.includes(u)
                    ? ((r = 1), s.interrupt ? t(l) : C(l))
                    : tR.includes(o.toLowerCase())
                      ? ((r = 6), a)
                        ? (e.consume(l), m)
                        : s.interrupt
                          ? t(l)
                          : C(l)
                      : ((r = 7),
                        s.interrupt && !s.parser.lazy[s.now().line]
                          ? n(l)
                          : i
                            ? (function t(n) {
                                return eJ(n) ? (e.consume(n), t) : w(n);
                              })(l)
                            : g(l));
                }
                return 45 === l || eq(l) ? (e.consume(l), (o += String.fromCharCode(l)), h) : n(l);
              }
              function m(r) {
                return 62 === r ? (e.consume(r), s.interrupt ? t : C) : n(r);
              }
              function g(t) {
                return 47 === t
                  ? (e.consume(t), w)
                  : 58 === t || 95 === t || eH(t)
                    ? (e.consume(t), v)
                    : eJ(t)
                      ? (e.consume(t), g)
                      : w(t);
              }
              function v(t) {
                return 45 === t || 46 === t || 58 === t || 95 === t || eq(t) ? (e.consume(t), v) : y(t);
              }
              function y(t) {
                return 61 === t ? (e.consume(t), b) : eJ(t) ? (e.consume(t), y) : g(t);
              }
              function b(t) {
                return null === t || 60 === t || 61 === t || 62 === t || 96 === t
                  ? n(t)
                  : 34 === t || 39 === t
                    ? (e.consume(t), (a = t), x)
                    : eJ(t)
                      ? (e.consume(t), b)
                      : (function t(n) {
                          return null === n ||
                            34 === n ||
                            39 === n ||
                            47 === n ||
                            60 === n ||
                            61 === n ||
                            62 === n ||
                            96 === n ||
                            eG(n)
                            ? y(n)
                            : (e.consume(n), t);
                        })(t);
              }
              function x(t) {
                return t === a ? (e.consume(t), (a = null), k) : null === t || eY(t) ? n(t) : (e.consume(t), x);
              }
              function k(e) {
                return 47 === e || 62 === e || eJ(e) ? g(e) : n(e);
              }
              function w(t) {
                return 62 === t ? (e.consume(t), S) : n(t);
              }
              function S(t) {
                return null === t || eY(t) ? C(t) : eJ(t) ? (e.consume(t), S) : n(t);
              }
              function C(t) {
                return 45 === t && 2 === r
                  ? (e.consume(t), P)
                  : 60 === t && 1 === r
                    ? (e.consume(t), T)
                    : 62 === t && 4 === r
                      ? (e.consume(t), M)
                      : 63 === t && 3 === r
                        ? (e.consume(t), I)
                        : 93 === t && 5 === r
                          ? (e.consume(t), O)
                          : eY(t) && (6 === r || 7 === r)
                            ? (e.exit("htmlFlowData"), e.check(tT, N, E)(t))
                            : null === t || eY(t)
                              ? (e.exit("htmlFlowData"), E(t))
                              : (e.consume(t), C);
              }
              function E(t) {
                return e.check(tA, j, N)(t);
              }
              function j(t) {
                return (e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), R);
              }
              function R(t) {
                return null === t || eY(t) ? E(t) : (e.enter("htmlFlowData"), C(t));
              }
              function P(t) {
                return 45 === t ? (e.consume(t), I) : C(t);
              }
              function T(t) {
                return 47 === t ? (e.consume(t), (o = ""), A) : C(t);
              }
              function A(t) {
                if (62 === t) {
                  let n = o.toLowerCase();
                  return tP.includes(n) ? (e.consume(t), M) : C(t);
                }
                return eH(t) && o.length < 8 ? (e.consume(t), (o += String.fromCharCode(t)), A) : C(t);
              }
              function O(t) {
                return 93 === t ? (e.consume(t), I) : C(t);
              }
              function I(t) {
                return 62 === t ? (e.consume(t), M) : 45 === t && 2 === r ? (e.consume(t), I) : C(t);
              }
              function M(t) {
                return null === t || eY(t) ? (e.exit("htmlFlowData"), N(t)) : (e.consume(t), M);
              }
              function N(n) {
                return (e.exit("htmlFlow"), t(n));
              }
            },
          },
          61: tH,
          95: t$,
          96: ty,
          126: ty,
        },
        "flowInitial",
        0,
        { [-2]: tb, [-1]: tb, 32: tb },
        "insideSpan",
        0,
        { null: [tc, tn] },
        "string",
        0,
        { 38: tg, 92: tp },
        "text",
        0,
        {
          [-5]: tL,
          [-4]: tL,
          [-3]: tL,
          33: tz,
          38: tg,
          42: tc,
          60: [
            {
              name: "autolink",
              tokenize: function (e, t, n) {
                let r = 0;
                return function (t) {
                  return (
                    e.enter("autolink"),
                    e.enter("autolinkMarker"),
                    e.consume(t),
                    e.exit("autolinkMarker"),
                    e.enter("autolinkProtocol"),
                    i
                  );
                };
                function i(t) {
                  return eH(t) ? (e.consume(t), o) : 64 === t ? n(t) : a(t);
                }
                function o(t) {
                  return 43 === t || 45 === t || 46 === t || eq(t)
                    ? ((r = 1),
                      (function t(n) {
                        return 58 === n
                          ? (e.consume(n), (r = 0), l)
                          : (43 === n || 45 === n || 46 === n || eq(n)) && r++ < 32
                            ? (e.consume(n), t)
                            : ((r = 0), a(n));
                      })(t))
                    : a(t);
                }
                function l(r) {
                  return 62 === r
                    ? (e.exit("autolinkProtocol"),
                      e.enter("autolinkMarker"),
                      e.consume(r),
                      e.exit("autolinkMarker"),
                      e.exit("autolink"),
                      t)
                    : null === r || 32 === r || 60 === r || eW(r)
                      ? n(r)
                      : (e.consume(r), l);
                }
                function a(t) {
                  return 64 === t ? (e.consume(t), s) : eU(t) ? (e.consume(t), a) : n(t);
                }
                function s(i) {
                  return eq(i)
                    ? (function i(o) {
                        return 46 === o
                          ? (e.consume(o), (r = 0), s)
                          : 62 === o
                            ? ((e.exit("autolinkProtocol").type = "autolinkEmail"),
                              e.enter("autolinkMarker"),
                              e.consume(o),
                              e.exit("autolinkMarker"),
                              e.exit("autolink"),
                              t)
                            : (function t(o) {
                                if ((45 === o || eq(o)) && r++ < 63) {
                                  let n = 45 === o ? t : i;
                                  return (e.consume(o), n);
                                }
                                return n(o);
                              })(o);
                      })(i)
                    : n(i);
                }
              },
            },
            {
              name: "htmlText",
              tokenize: function (e, t, n) {
                let r,
                  i,
                  o,
                  l = this;
                return function (t) {
                  return (e.enter("htmlText"), e.enter("htmlTextData"), e.consume(t), a);
                };
                function a(t) {
                  return 33 === t
                    ? (e.consume(t), s)
                    : 47 === t
                      ? (e.consume(t), x)
                      : 63 === t
                        ? (e.consume(t), y)
                        : eH(t)
                          ? (e.consume(t), w)
                          : n(t);
                }
                function s(t) {
                  return 45 === t
                    ? (e.consume(t), u)
                    : 91 === t
                      ? (e.consume(t), (i = 0), p)
                      : eH(t)
                        ? (e.consume(t), v)
                        : n(t);
                }
                function u(t) {
                  return 45 === t ? (e.consume(t), f) : n(t);
                }
                function c(t) {
                  return null === t ? n(t) : 45 === t ? (e.consume(t), d) : eY(t) ? ((o = c), A(t)) : (e.consume(t), c);
                }
                function d(t) {
                  return 45 === t ? (e.consume(t), f) : c(t);
                }
                function f(e) {
                  return 62 === e ? T(e) : 45 === e ? d(e) : c(e);
                }
                function p(t) {
                  let r = "CDATA[";
                  return t === r.charCodeAt(i++) ? (e.consume(t), i === r.length ? h : p) : n(t);
                }
                function h(t) {
                  return null === t ? n(t) : 93 === t ? (e.consume(t), m) : eY(t) ? ((o = h), A(t)) : (e.consume(t), h);
                }
                function m(t) {
                  return 93 === t ? (e.consume(t), g) : h(t);
                }
                function g(t) {
                  return 62 === t ? T(t) : 93 === t ? (e.consume(t), g) : h(t);
                }
                function v(t) {
                  return null === t || 62 === t ? T(t) : eY(t) ? ((o = v), A(t)) : (e.consume(t), v);
                }
                function y(t) {
                  return null === t ? n(t) : 63 === t ? (e.consume(t), b) : eY(t) ? ((o = y), A(t)) : (e.consume(t), y);
                }
                function b(e) {
                  return 62 === e ? T(e) : y(e);
                }
                function x(t) {
                  return eH(t) ? (e.consume(t), k) : n(t);
                }
                function k(t) {
                  return 45 === t || eq(t)
                    ? (e.consume(t), k)
                    : (function t(n) {
                        return eY(n) ? ((o = t), A(n)) : eJ(n) ? (e.consume(n), t) : T(n);
                      })(t);
                }
                function w(t) {
                  return 45 === t || eq(t) ? (e.consume(t), w) : 47 === t || 62 === t || eG(t) ? S(t) : n(t);
                }
                function S(t) {
                  return 47 === t
                    ? (e.consume(t), T)
                    : 58 === t || 95 === t || eH(t)
                      ? (e.consume(t), C)
                      : eY(t)
                        ? ((o = S), A(t))
                        : eJ(t)
                          ? (e.consume(t), S)
                          : T(t);
                }
                function C(t) {
                  return 45 === t || 46 === t || 58 === t || 95 === t || eq(t)
                    ? (e.consume(t), C)
                    : (function t(n) {
                        return 61 === n
                          ? (e.consume(n), E)
                          : eY(n)
                            ? ((o = t), A(n))
                            : eJ(n)
                              ? (e.consume(n), t)
                              : S(n);
                      })(t);
                }
                function E(t) {
                  return null === t || 60 === t || 61 === t || 62 === t || 96 === t
                    ? n(t)
                    : 34 === t || 39 === t
                      ? (e.consume(t), (r = t), j)
                      : eY(t)
                        ? ((o = E), A(t))
                        : eJ(t)
                          ? (e.consume(t), E)
                          : (e.consume(t), R);
                }
                function j(t) {
                  return t === r
                    ? (e.consume(t), (r = void 0), P)
                    : null === t
                      ? n(t)
                      : eY(t)
                        ? ((o = j), A(t))
                        : (e.consume(t), j);
                }
                function R(t) {
                  return null === t || 34 === t || 39 === t || 60 === t || 61 === t || 96 === t
                    ? n(t)
                    : 47 === t || 62 === t || eG(t)
                      ? S(t)
                      : (e.consume(t), R);
                }
                function P(e) {
                  return 47 === e || 62 === e || eG(e) ? S(e) : n(e);
                }
                function T(r) {
                  return 62 === r ? (e.consume(r), e.exit("htmlTextData"), e.exit("htmlText"), t) : n(r);
                }
                function A(t) {
                  return (e.exit("htmlTextData"), e.enter("lineEnding"), e.consume(t), e.exit("lineEnding"), O);
                }
                function O(t) {
                  return eJ(t)
                    ? e1(e, I, "linePrefix", l.parser.constructs.disable.null.includes("codeIndented") ? void 0 : 4)(t)
                    : I(t);
                }
                function I(t) {
                  return (e.enter("htmlTextData"), o(t));
                }
              },
            },
          ],
          91: tD,
          92: [
            {
              name: "hardBreakEscape",
              tokenize: function (e, t, n) {
                return function (t) {
                  return (e.enter("hardBreakEscape"), e.consume(t), r);
                };
                function r(r) {
                  return eY(r) ? (e.exit("hardBreakEscape"), t(r)) : n(r);
                }
              },
            },
            tp,
          ],
          93: tO,
          95: tc,
          96: {
            name: "codeText",
            previous: function (e) {
              return 96 !== e || "characterEscape" === this.events[this.events.length - 1][1].type;
            },
            resolve: function (e) {
              let t,
                n,
                r = e.length - 4,
                i = 3;
              if (
                ("lineEnding" === e[3][1].type || "space" === e[i][1].type) &&
                ("lineEnding" === e[r][1].type || "space" === e[r][1].type)
              ) {
                for (t = i; ++t < r; )
                  if ("codeTextData" === e[t][1].type) {
                    ((e[i][1].type = "codeTextPadding"), (e[r][1].type = "codeTextPadding"), (i += 2), (r -= 2));
                    break;
                  }
              }
              for (t = i - 1, r++; ++t <= r; )
                void 0 === n
                  ? t !== r && "lineEnding" !== e[t][1].type && (n = t)
                  : (t === r || "lineEnding" === e[t][1].type) &&
                    ((e[n][1].type = "codeTextData"),
                    t !== n + 2 &&
                      ((e[n][1].end = e[t - 1][1].end), e.splice(n + 2, t - n - 2), (r -= t - n - 2), (t = n + 2)),
                    (n = void 0));
              return e;
            },
            tokenize: function (e, t, n) {
              let r,
                i,
                o = 0;
              return function (t) {
                return (
                  e.enter("codeText"),
                  e.enter("codeTextSequence"),
                  (function t(n) {
                    return 96 === n ? (e.consume(n), o++, t) : (e.exit("codeTextSequence"), l(n));
                  })(t)
                );
              };
              function l(s) {
                return null === s
                  ? n(s)
                  : 32 === s
                    ? (e.enter("space"), e.consume(s), e.exit("space"), l)
                    : 96 === s
                      ? ((i = e.enter("codeTextSequence")),
                        (r = 0),
                        (function n(l) {
                          return 96 === l
                            ? (e.consume(l), r++, n)
                            : r === o
                              ? (e.exit("codeTextSequence"), e.exit("codeText"), t(l))
                              : ((i.type = "codeTextData"), a(l));
                        })(s))
                      : eY(s)
                        ? (e.enter("lineEnding"), e.consume(s), e.exit("lineEnding"), l)
                        : (e.enter("codeTextData"), a(s));
              }
              function a(t) {
                return null === t || 32 === t || 96 === t || eY(t) ? (e.exit("codeTextData"), l(t)) : (e.consume(t), a);
              }
            },
          },
        },
      ],
      4127,
    );
    var tq = e.i(4127);
    let tU = /[\0\t\n\r]/g;
    function tW(e, t) {
      let n = Number.parseInt(e, t);
      return n < 9 ||
        11 === n ||
        (n > 13 && n < 32) ||
        (n > 126 && n < 160) ||
        (n > 55295 && n < 57344) ||
        (n > 64975 && n < 65008) ||
        (65535 & n) == 65535 ||
        (65535 & n) == 65534 ||
        n > 1114111
        ? "�"
        : String.fromCodePoint(n);
    }
    let tV = /\\([!-/:-@[-`{-~])|&(#(?:\d{1,7}|x[\da-f]{1,6})|[\da-z]{1,31});/gi;
    function tK(e, t, n) {
      if (t) return t;
      if (35 === n.charCodeAt(0)) {
        let e = n.charCodeAt(1),
          t = 120 === e || 88 === e;
        return tW(n.slice(t ? 2 : 1), t ? 16 : 10);
      }
      return tm(n) || e;
    }
    let tX = {}.hasOwnProperty;
    function tY(e) {
      return { line: e.line, column: e.column, offset: e.offset };
    }
    function tG(e, t) {
      if (e)
        throw Error(
          "Cannot close `" +
            e.type +
            "` (" +
            ev({ start: e.start, end: e.end }) +
            "): a different token (`" +
            t.type +
            "`, " +
            ev({ start: t.start, end: t.end }) +
            ") is open",
        );
      throw Error(
        "Cannot close document, a token (`" + t.type + "`, " + ev({ start: t.start, end: t.end }) + ") is still open",
      );
    }
    function tJ(e) {
      let t = this;
      t.parser = function (n) {
        var r, i;
        let o, l, a, s;
        return (
          "object" ==
            typeof (r = {
              ...t.data("settings"),
              ...e,
              extensions: t.data("micromarkExtensions") || [],
              mdastExtensions: t.data("fromMarkdownExtensions") || [],
            }) && ((i = r), (r = void 0)),
          (function (e) {
            let t = {
              transforms: [],
              canContainEols: ["emphasis", "fragment", "heading", "paragraph", "strong"],
              enter: {
                autolink: r(v),
                autolinkProtocol: u,
                autolinkEmail: u,
                atxHeading: r(h),
                blockQuote: r(function () {
                  return { type: "blockquote", children: [] };
                }),
                characterEscape: u,
                characterReference: u,
                codeFenced: r(p),
                codeFencedFenceInfo: i,
                codeFencedFenceMeta: i,
                codeIndented: r(p, i),
                codeText: r(function () {
                  return { type: "inlineCode", value: "" };
                }, i),
                codeTextData: u,
                data: u,
                codeFlowValue: u,
                definition: r(function () {
                  return { type: "definition", identifier: "", label: null, title: null, url: "" };
                }),
                definitionDestinationString: i,
                definitionLabelString: i,
                definitionTitleString: i,
                emphasis: r(function () {
                  return { type: "emphasis", children: [] };
                }),
                hardBreakEscape: r(m),
                hardBreakTrailing: r(m),
                htmlFlow: r(g, i),
                htmlFlowData: u,
                htmlText: r(g, i),
                htmlTextData: u,
                image: r(function () {
                  return { type: "image", title: null, url: "", alt: null };
                }),
                label: i,
                link: r(v),
                listItem: r(function (e) {
                  return { type: "listItem", spread: e._spread, checked: null, children: [] };
                }),
                listItemValue: function (e) {
                  this.data.expectingFirstListItemValue &&
                    ((this.stack[this.stack.length - 2].start = Number.parseInt(this.sliceSerialize(e), 10)),
                    (this.data.expectingFirstListItemValue = void 0));
                },
                listOrdered: r(y, function () {
                  this.data.expectingFirstListItemValue = !0;
                }),
                listUnordered: r(y),
                paragraph: r(function () {
                  return { type: "paragraph", children: [] };
                }),
                reference: function () {
                  this.data.referenceType = "collapsed";
                },
                referenceString: i,
                resourceDestinationString: i,
                resourceTitleString: i,
                setextHeading: r(h),
                strong: r(function () {
                  return { type: "strong", children: [] };
                }),
                thematicBreak: r(function () {
                  return { type: "thematicBreak" };
                }),
              },
              exit: {
                atxHeading: l(),
                atxHeadingSequence: function (e) {
                  let t = this.stack[this.stack.length - 1];
                  t.depth || (t.depth = this.sliceSerialize(e).length);
                },
                autolink: l(),
                autolinkEmail: function (e) {
                  (c.call(this, e), (this.stack[this.stack.length - 1].url = "mailto:" + this.sliceSerialize(e)));
                },
                autolinkProtocol: function (e) {
                  (c.call(this, e), (this.stack[this.stack.length - 1].url = this.sliceSerialize(e)));
                },
                blockQuote: l(),
                characterEscapeValue: c,
                characterReferenceMarkerHexadecimal: f,
                characterReferenceMarkerNumeric: f,
                characterReferenceValue: function (e) {
                  let t,
                    n = this.sliceSerialize(e),
                    r = this.data.characterReferenceType;
                  r
                    ? ((t = tW(n, "characterReferenceMarkerNumeric" === r ? 10 : 16)),
                      (this.data.characterReferenceType = void 0))
                    : (t = tm(n));
                  let i = this.stack[this.stack.length - 1];
                  i.value += t;
                },
                characterReference: function (e) {
                  this.stack.pop().position.end = tY(e.end);
                },
                codeFenced: l(function () {
                  let e = this.resume();
                  ((this.stack[this.stack.length - 1].value = e.replace(/^(\r?\n|\r)|(\r?\n|\r)$/g, "")),
                    (this.data.flowCodeInside = void 0));
                }),
                codeFencedFence: function () {
                  this.data.flowCodeInside || (this.buffer(), (this.data.flowCodeInside = !0));
                },
                codeFencedFenceInfo: function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].lang = e;
                },
                codeFencedFenceMeta: function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].meta = e;
                },
                codeFlowValue: c,
                codeIndented: l(function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].value = e.replace(/(\r?\n|\r)$/g, "");
                }),
                codeText: l(function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].value = e;
                }),
                codeTextData: c,
                data: c,
                definition: l(),
                definitionDestinationString: function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].url = e;
                },
                definitionLabelString: function (e) {
                  let t = this.resume(),
                    n = this.stack[this.stack.length - 1];
                  ((n.label = t), (n.identifier = tE(this.sliceSerialize(e)).toLowerCase()));
                },
                definitionTitleString: function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].title = e;
                },
                emphasis: l(),
                hardBreakEscape: l(d),
                hardBreakTrailing: l(d),
                htmlFlow: l(function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].value = e;
                }),
                htmlFlowData: c,
                htmlText: l(function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].value = e;
                }),
                htmlTextData: c,
                image: l(function () {
                  let e = this.stack[this.stack.length - 1];
                  if (this.data.inReference) {
                    let t = this.data.referenceType || "shortcut";
                    ((e.type += "Reference"), (e.referenceType = t), delete e.url, delete e.title);
                  } else (delete e.identifier, delete e.label);
                  this.data.referenceType = void 0;
                }),
                label: function () {
                  let e = this.stack[this.stack.length - 1],
                    t = this.resume(),
                    n = this.stack[this.stack.length - 1];
                  ((this.data.inReference = !0), "link" === n.type ? (n.children = e.children) : (n.alt = t));
                },
                labelText: function (e) {
                  let t = this.sliceSerialize(e),
                    n = this.stack[this.stack.length - 2];
                  ((n.label = t.replace(tV, tK)), (n.identifier = tE(t).toLowerCase()));
                },
                lineEnding: function (e) {
                  let n = this.stack[this.stack.length - 1];
                  if (this.data.atHardBreak) {
                    ((n.children[n.children.length - 1].position.end = tY(e.end)), (this.data.atHardBreak = void 0));
                    return;
                  }
                  !this.data.setextHeadingSlurpLineEnding &&
                    t.canContainEols.includes(n.type) &&
                    (u.call(this, e), c.call(this, e));
                },
                link: l(function () {
                  let e = this.stack[this.stack.length - 1];
                  if (this.data.inReference) {
                    let t = this.data.referenceType || "shortcut";
                    ((e.type += "Reference"), (e.referenceType = t), delete e.url, delete e.title);
                  } else (delete e.identifier, delete e.label);
                  this.data.referenceType = void 0;
                }),
                listItem: l(),
                listOrdered: l(),
                listUnordered: l(),
                paragraph: l(),
                referenceString: function (e) {
                  let t = this.resume(),
                    n = this.stack[this.stack.length - 1];
                  ((n.label = t),
                    (n.identifier = tE(this.sliceSerialize(e)).toLowerCase()),
                    (this.data.referenceType = "full"));
                },
                resourceDestinationString: function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].url = e;
                },
                resourceTitleString: function () {
                  let e = this.resume();
                  this.stack[this.stack.length - 1].title = e;
                },
                resource: function () {
                  this.data.inReference = void 0;
                },
                setextHeading: l(function () {
                  this.data.setextHeadingSlurpLineEnding = void 0;
                }),
                setextHeadingLineSequence: function (e) {
                  this.stack[this.stack.length - 1].depth = 61 === this.sliceSerialize(e).codePointAt(0) ? 1 : 2;
                },
                setextHeadingText: function () {
                  this.data.setextHeadingSlurpLineEnding = !0;
                },
                strong: l(),
                thematicBreak: l(),
              },
            };
            !(function e(t, n) {
              let r = -1;
              for (; ++r < n.length; ) {
                let i = n[r];
                Array.isArray(i)
                  ? e(t, i)
                  : (function (e, t) {
                      let n;
                      for (n in t)
                        if (tX.call(t, n))
                          switch (n) {
                            case "canContainEols": {
                              let r = t[n];
                              r && e[n].push(...r);
                              break;
                            }
                            case "transforms": {
                              let r = t[n];
                              r && e[n].push(...r);
                              break;
                            }
                            case "enter":
                            case "exit": {
                              let r = t[n];
                              r && Object.assign(e[n], r);
                            }
                          }
                    })(t, i);
              }
            })(t, (e || {}).mdastExtensions || []);
            let n = {};
            return function (e) {
              let r = { type: "root", children: [] },
                l = { stack: [r], tokenStack: [], config: t, enter: o, exit: a, buffer: i, resume: s, data: n },
                u = [],
                c = -1;
              for (; ++c < e.length; )
                ("listOrdered" === e[c][1].type || "listUnordered" === e[c][1].type) &&
                  ("enter" === e[c][0]
                    ? u.push(c)
                    : (c = (function (e, t, n) {
                        let r,
                          i,
                          o,
                          l,
                          a = t - 1,
                          s = -1,
                          u = !1;
                        for (; ++a <= n; ) {
                          let t = e[a];
                          switch (t[1].type) {
                            case "listUnordered":
                            case "listOrdered":
                            case "blockQuote":
                              ("enter" === t[0] ? s++ : s--, (l = void 0));
                              break;
                            case "lineEndingBlank":
                              "enter" === t[0] && (!r || l || s || o || (o = a), (l = void 0));
                              break;
                            case "linePrefix":
                            case "listItemValue":
                            case "listItemMarker":
                            case "listItemPrefix":
                            case "listItemPrefixWhitespace":
                              break;
                            default:
                              l = void 0;
                          }
                          if (
                            (!s && "enter" === t[0] && "listItemPrefix" === t[1].type) ||
                            (-1 === s &&
                              "exit" === t[0] &&
                              ("listUnordered" === t[1].type || "listOrdered" === t[1].type))
                          ) {
                            if (r) {
                              let l = a;
                              for (i = void 0; l--; ) {
                                let t = e[l];
                                if ("lineEnding" === t[1].type || "lineEndingBlank" === t[1].type) {
                                  if ("exit" === t[0]) continue;
                                  (i && ((e[i][1].type = "lineEndingBlank"), (u = !0)),
                                    (t[1].type = "lineEnding"),
                                    (i = l));
                                } else if (
                                  "linePrefix" === t[1].type ||
                                  "blockQuotePrefix" === t[1].type ||
                                  "blockQuotePrefixWhitespace" === t[1].type ||
                                  "blockQuoteMarker" === t[1].type ||
                                  "listItemIndent" === t[1].type
                                );
                                else break;
                              }
                              (o && (!i || o < i) && (r._spread = !0),
                                (r.end = Object.assign({}, i ? e[i][1].start : t[1].end)),
                                e.splice(i || a, 0, ["exit", r, t[2]]),
                                a++,
                                n++);
                            }
                            if ("listItemPrefix" === t[1].type) {
                              let i = {
                                type: "listItem",
                                _spread: !1,
                                start: Object.assign({}, t[1].start),
                                end: void 0,
                              };
                              ((r = i), e.splice(a, 0, ["enter", i, t[2]]), a++, n++, (o = void 0), (l = !0));
                            }
                          }
                        }
                        return ((e[t][1]._spread = u), n);
                      })(e, u.pop(), c)));
              for (c = -1; ++c < e.length; ) {
                let n = t[e[c][0]];
                tX.call(n, e[c][1].type) &&
                  n[e[c][1].type].call(Object.assign({ sliceSerialize: e[c][2].sliceSerialize }, l), e[c][1]);
              }
              if (l.tokenStack.length > 0) {
                let e = l.tokenStack[l.tokenStack.length - 1];
                (e[1] || tG).call(l, void 0, e[0]);
              }
              for (
                r.position = {
                  start: tY(e.length > 0 ? e[0][1].start : { line: 1, column: 1, offset: 0 }),
                  end: tY(e.length > 0 ? e[e.length - 2][1].end : { line: 1, column: 1, offset: 0 }),
                },
                  c = -1;
                ++c < t.transforms.length;
              )
                r = t.transforms[c](r) || r;
              return r;
            };
            function r(e, t) {
              return function (n) {
                (o.call(this, e(n), n), t && t.call(this, n));
              };
            }
            function i() {
              this.stack.push({ type: "fragment", children: [] });
            }
            function o(e, t, n) {
              (this.stack[this.stack.length - 1].children.push(e),
                this.stack.push(e),
                this.tokenStack.push([t, n || void 0]),
                (e.position = { start: tY(t.start), end: void 0 }));
            }
            function l(e) {
              return function (t) {
                (e && e.call(this, t), a.call(this, t));
              };
            }
            function a(e, t) {
              let n = this.stack.pop(),
                r = this.tokenStack.pop();
              if (r) r[0].type !== e.type && (t ? t.call(this, e, r[0]) : (r[1] || tG).call(this, e, r[0]));
              else
                throw Error(
                  "Cannot close `" + e.type + "` (" + ev({ start: e.start, end: e.end }) + "): it’s not open",
                );
              n.position.end = tY(e.end);
            }
            function s() {
              var e;
              return (
                (e = this.stack.pop()),
                eL(
                  e,
                  "boolean" != typeof eD.includeImageAlt || eD.includeImageAlt,
                  "boolean" != typeof eD.includeHtml || eD.includeHtml,
                )
              );
            }
            function u(e) {
              let t = this.stack[this.stack.length - 1].children,
                n = t[t.length - 1];
              ((n && "text" === n.type) ||
                (((n = { type: "text", value: "" }).position = { start: tY(e.start), end: void 0 }), t.push(n)),
                this.stack.push(n));
            }
            function c(e) {
              let t = this.stack.pop();
              ((t.value += this.sliceSerialize(e)), (t.position.end = tY(e.end)));
            }
            function d() {
              this.data.atHardBreak = !0;
            }
            function f(e) {
              this.data.characterReferenceType = e.type;
            }
            function p() {
              return { type: "code", lang: null, meta: null, value: "" };
            }
            function h() {
              return { type: "heading", depth: 0, children: [] };
            }
            function m() {
              return { type: "break" };
            }
            function g() {
              return { type: "html", value: "" };
            }
            function v() {
              return { type: "link", title: null, url: "", children: [] };
            }
            function y(e) {
              return { type: "list", ordered: "listOrdered" === e.type, start: null, spread: e._spread, children: [] };
            }
          })(i)(
            (function (e) {
              for (; !e7(e); );
              return e;
            })(
              (function (e) {
                let t = {
                  constructs: (function (e) {
                    let t = {},
                      n = -1;
                    for (; ++n < e.length; )
                      !(function (e, t) {
                        let n;
                        for (n in t) {
                          let r,
                            i = (eB.call(e, n) ? e[n] : void 0) || (e[n] = {}),
                            o = t[n];
                          if (o)
                            for (r in o) {
                              eB.call(i, r) || (i[r] = []);
                              let e = o[r];
                              !(function (e, t) {
                                let n = -1,
                                  r = [];
                                for (; ++n < t.length; ) ("after" === t[n].add ? e : r).push(t[n]);
                                eF(e, 0, 0, r);
                              })(i[r], Array.isArray(e) ? e : e ? [e] : []);
                            }
                        }
                      })(t, e[n]);
                    return t;
                  })([tq, ...((e || {}).extensions || [])]),
                  content: n(e2),
                  defined: [],
                  document: n(e4),
                  flow: n(tt),
                  lazy: {},
                  string: n(tr),
                  text: n(ti),
                };
                return t;
                function n(e) {
                  return function (n) {
                    return (function (e, t, n) {
                      let r = {
                          _bufferIndex: -1,
                          _index: 0,
                          line: (n && n.line) || 1,
                          column: (n && n.column) || 1,
                          offset: (n && n.offset) || 0,
                        },
                        i = {},
                        o = [],
                        l = [],
                        a = [],
                        s = {
                          attempt: h(function (e, t) {
                            m(e, t.from);
                          }),
                          check: h(p),
                          consume: function (e) {
                            (eY(e)
                              ? (r.line++, (r.column = 1), (r.offset += -3 === e ? 2 : 1), g())
                              : -1 !== e && (r.column++, r.offset++),
                              r._bufferIndex < 0
                                ? r._index++
                                : (r._bufferIndex++,
                                  r._bufferIndex === l[r._index].length && ((r._bufferIndex = -1), r._index++)),
                              (u.previous = e));
                          },
                          enter: function (e, t) {
                            let n = t || {};
                            return ((n.type = e), (n.start = f()), u.events.push(["enter", n, u]), a.push(n), n);
                          },
                          exit: function (e) {
                            let t = a.pop();
                            return ((t.end = f()), u.events.push(["exit", t, u]), t);
                          },
                          interrupt: h(p, { interrupt: !0 }),
                        },
                        u = {
                          code: null,
                          containerState: {},
                          defineSkip: function (e) {
                            ((i[e.line] = e.column), g());
                          },
                          events: [],
                          now: f,
                          parser: e,
                          previous: null,
                          sliceSerialize: function (e, t) {
                            return (function (e, t) {
                              let n,
                                r = -1,
                                i = [];
                              for (; ++r < e.length; ) {
                                let o,
                                  l = e[r];
                                if ("string" == typeof l) o = l;
                                else
                                  switch (l) {
                                    case -5:
                                      o = "\r";
                                      break;
                                    case -4:
                                      o = "\n";
                                      break;
                                    case -3:
                                      o = "\r\n";
                                      break;
                                    case -2:
                                      o = t ? " " : "	";
                                      break;
                                    case -1:
                                      if (!t && n) continue;
                                      o = " ";
                                      break;
                                    default:
                                      o = String.fromCharCode(l);
                                  }
                                ((n = -2 === l), i.push(o));
                              }
                              return i.join("");
                            })(d(e), t);
                          },
                          sliceStream: d,
                          write: function (e) {
                            return ((l = e_(l, e)),
                            (function () {
                              let e;
                              for (; r._index < l.length; ) {
                                let n = l[r._index];
                                if ("string" == typeof n)
                                  for (
                                    e = r._index, r._bufferIndex < 0 && (r._bufferIndex = 0);
                                    r._index === e && r._bufferIndex < n.length;
                                  ) {
                                    var t;
                                    ((t = n.charCodeAt(r._bufferIndex)), (c = c(t)));
                                  }
                                else c = c(n);
                              }
                            })(),
                            null !== l[l.length - 1])
                              ? []
                              : (m(t, 0), (u.events = tu(o, u.events, u)), u.events);
                          },
                        },
                        c = t.tokenize.call(u, s);
                      return (t.resolveAll && o.push(t), u);
                      function d(e) {
                        return (function (e, t) {
                          let n,
                            r = t.start._index,
                            i = t.start._bufferIndex,
                            o = t.end._index,
                            l = t.end._bufferIndex;
                          if (r === o) n = [e[r].slice(i, l)];
                          else {
                            if (((n = e.slice(r, o)), i > -1)) {
                              let e = n[0];
                              "string" == typeof e ? (n[0] = e.slice(i)) : n.shift();
                            }
                            l > 0 && n.push(e[o].slice(0, l));
                          }
                          return n;
                        })(l, e);
                      }
                      function f() {
                        let { _bufferIndex: e, _index: t, line: n, column: i, offset: o } = r;
                        return { _bufferIndex: e, _index: t, line: n, column: i, offset: o };
                      }
                      function p(e, t) {
                        t.restore();
                      }
                      function h(e, t) {
                        return function (n, i, o) {
                          var l;
                          let c, d, p, h;
                          return Array.isArray(n)
                            ? m(n)
                            : "tokenize" in n
                              ? m([n])
                              : ((l = n),
                                function (e) {
                                  let t = null !== e && l[e],
                                    n = null !== e && l.null;
                                  return m([
                                    ...(Array.isArray(t) ? t : t ? [t] : []),
                                    ...(Array.isArray(n) ? n : n ? [n] : []),
                                  ])(e);
                                });
                          function m(e) {
                            return ((c = e), (d = 0), 0 === e.length) ? o : v(e[d]);
                          }
                          function v(e) {
                            return function (n) {
                              let i, o, l, c, d;
                              return ((i = f()),
                              (o = u.previous),
                              (l = u.currentConstruct),
                              (c = u.events.length),
                              (d = Array.from(a)),
                              (h = {
                                from: c,
                                restore: function () {
                                  ((r = i),
                                    (u.previous = o),
                                    (u.currentConstruct = l),
                                    (u.events.length = c),
                                    (a = d),
                                    g());
                                },
                              }),
                              (p = e),
                              e.partial || (u.currentConstruct = e),
                              e.name && u.parser.constructs.disable.null.includes(e.name))
                                ? b(n)
                                : e.tokenize.call(t ? Object.assign(Object.create(u), t) : u, s, y, b)(n);
                            };
                          }
                          function y(t) {
                            return (e(p, h), i);
                          }
                          function b(e) {
                            return (h.restore(), ++d < c.length) ? v(c[d]) : o;
                          }
                        };
                      }
                      function m(e, t) {
                        (e.resolveAll && !o.includes(e) && o.push(e),
                          e.resolve && eF(u.events, t, u.events.length - t, e.resolve(u.events.slice(t), u)),
                          e.resolveTo && (u.events = e.resolveTo(u.events, u)));
                      }
                      function g() {
                        r.line in i && r.column < 2 && ((r.column = i[r.line]), (r.offset += i[r.line] - 1));
                      }
                    })(t, e, n);
                  };
                }
              })(i)
                .document()
                .write(
                  ((l = 1),
                  (a = ""),
                  (s = !0),
                  function (e, t, n) {
                    let r,
                      i,
                      u,
                      c,
                      d,
                      f = [];
                    for (
                      e = a + ("string" == typeof e ? e.toString() : new TextDecoder(t || void 0).decode(e)),
                        u = 0,
                        a = "",
                        s && (65279 === e.charCodeAt(0) && u++, (s = void 0));
                      u < e.length;
                    ) {
                      if (
                        ((tU.lastIndex = u),
                        (c = (r = tU.exec(e)) && void 0 !== r.index ? r.index : e.length),
                        (d = e.charCodeAt(c)),
                        !r)
                      ) {
                        a = e.slice(u);
                        break;
                      }
                      if (10 === d && u === c && o) (f.push(-3), (o = void 0));
                      else
                        switch ((o && (f.push(-5), (o = void 0)), u < c && (f.push(e.slice(u, c)), (l += c - u)), d)) {
                          case 0:
                            (f.push(65533), l++);
                            break;
                          case 9:
                            for (i = 4 * Math.ceil(l / 4), f.push(-2); l++ < i; ) f.push(-1);
                            break;
                          case 10:
                            (f.push(-4), (l = 1));
                            break;
                          default:
                            ((o = !0), (l = 1));
                        }
                      u = c + 1;
                    }
                    return (n && (o && f.push(-5), a && f.push(a), f.push(null)), f);
                  })(n, r, !0),
                ),
            ),
          )
        );
      };
    }
    let tQ = "object" == typeof self ? self : globalThis,
      tZ = (e, t) => {
        switch (e) {
          case "Function":
          case "SharedWorker":
          case "Worker":
          case "eval":
          case "setInterval":
          case "setTimeout":
            throw TypeError("unable to deserialize " + e);
        }
        return new tQ[e](t);
      },
      t0 = (e) => {
        var t;
        let n, r;
        return ((t = new Map()),
        (n = (e, n) => (t.set(n, e), e)),
        (r = (i) => {
          if (t.has(i)) return t.get(i);
          let [o, l] = e[i];
          switch (o) {
            case 0:
            case -1:
              return n(l, i);
            case 1: {
              let e = n([], i);
              for (let t of l) e.push(r(t));
              return e;
            }
            case 2: {
              let e = n({}, i);
              for (let [t, n] of l) e[r(t)] = r(n);
              return e;
            }
            case 3:
              return n(new Date(l), i);
            case 4: {
              let { source: e, flags: t } = l;
              return n(new RegExp(e, t), i);
            }
            case 5: {
              let e = n(new Map(), i);
              for (let [t, n] of l) e.set(r(t), r(n));
              return e;
            }
            case 6: {
              let e = n(new Set(), i);
              for (let t of l) e.add(r(t));
              return e;
            }
            case 7: {
              let { name: e, message: t } = l;
              return n("function" == typeof tQ[e] ? tZ(e, t) : Error(t), i);
            }
            case 8:
              return n(BigInt(l), i);
            case "BigInt":
              return n(Object(BigInt(l)), i);
            case "ArrayBuffer":
              return n(new Uint8Array(l).buffer, l);
            case "DataView": {
              let { buffer: e } = new Uint8Array(l);
              return n(new DataView(e), l);
            }
          }
          return n(tZ(o, l), i);
        }))(0);
      },
      { toString: t1 } = {},
      { keys: t2 } = Object,
      t4 = (e) => {
        let t = typeof e;
        if ("object" !== t || !e) return [0, t];
        let n = t1.call(e).slice(8, -1);
        switch (n) {
          case "Array":
            return [1, ""];
          case "Object":
            return [2, ""];
          case "Date":
            return [3, ""];
          case "RegExp":
            return [4, ""];
          case "Map":
            return [5, ""];
          case "Set":
            return [6, ""];
          case "DataView":
            return [1, n];
        }
        return n.includes("Array") ? [1, n] : e instanceof Error ? [7, e.name || "Error"] : [2, n];
      },
      t5 = ([e, t]) => 0 === e && ("function" === t || "symbol" === t),
      t3 = (e, { json: t, lossy: n } = {}) => {
        var r, i, o;
        let l,
          a,
          s = [];
        return (
          ((r = !(t || n)),
          (i = !!t),
          (o = new Map()),
          (l = (e, t) => {
            let n = s.push(e) - 1;
            return (o.set(t, n), n);
          }),
          (a = (e) => {
            if (o.has(e)) return o.get(e);
            let [t, n] = t4(e);
            switch (t) {
              case 0: {
                let i = e;
                switch (n) {
                  case "bigint":
                    ((t = 8), (i = e.toString()));
                    break;
                  case "function":
                  case "symbol":
                    if (r) throw TypeError("unable to serialize " + n);
                    i = null;
                    break;
                  case "undefined":
                    return l([-1], e);
                }
                return l([t, i], e);
              }
              case 1: {
                if (n) {
                  let t = e;
                  return (
                    "DataView" === n ? (t = new Uint8Array(e.buffer)) : "ArrayBuffer" === n && (t = new Uint8Array(e)),
                    l([n, [...t]], e)
                  );
                }
                let r = [],
                  i = l([t, r], e);
                for (let t of e) r.push(a(t));
                return i;
              }
              case 2: {
                if (n)
                  switch (n) {
                    case "BigInt":
                      return l([n, e.toString()], e);
                    case "Boolean":
                    case "Number":
                    case "String":
                      return l([n, e.valueOf()], e);
                  }
                if (i && "toJSON" in e) return a(e.toJSON());
                let o = [],
                  s = l([t, o], e);
                for (let t of t2(e)) (r || !t5(t4(e[t]))) && o.push([a(t), a(e[t])]);
                return s;
              }
              case 3:
                return l([t, isNaN(e.getTime()) ? "" : e.toISOString()], e);
              case 4: {
                let { source: n, flags: r } = e;
                return l([t, { source: n, flags: r }], e);
              }
              case 5: {
                let n = [],
                  i = l([t, n], e);
                for (let [t, i] of e) (r || !(t5(t4(t)) || t5(t4(i)))) && n.push([a(t), a(i)]);
                return i;
              }
              case 6: {
                let n = [],
                  i = l([t, n], e);
                for (let t of e) (r || !t5(t4(t))) && n.push(a(t));
                return i;
              }
            }
            let { message: s } = e;
            return l([t, { name: n, message: s }], e);
          }))(e),
          s
        );
      },
      t6 =
        "function" == typeof structuredClone
          ? (e, t) => (t && ("json" in t || "lossy" in t) ? t0(t3(e, t)) : structuredClone(e))
          : (e, t) => t0(t3(e, t));
    function t9(e) {
      let t = [],
        n = -1,
        r = 0,
        i = 0;
      for (; ++n < e.length; ) {
        let o = e.charCodeAt(n),
          l = "";
        if (37 === o && eq(e.charCodeAt(n + 1)) && eq(e.charCodeAt(n + 2))) i = 2;
        else if (o < 128) /[!#$&-;=?-Z_a-z~]/.test(String.fromCharCode(o)) || (l = String.fromCharCode(o));
        else if (o > 55295 && o < 57344) {
          let t = e.charCodeAt(n + 1);
          o < 56320 && t > 56319 && t < 57344 ? ((l = String.fromCharCode(o, t)), (i = 1)) : (l = "�");
        } else l = String.fromCharCode(o);
        (l && (t.push(e.slice(r, n), encodeURIComponent(l)), (r = n + i + 1), (l = "")), i && ((n += i), (i = 0)));
      }
      return t.join("") + e.slice(r);
    }
    function t7(e, t) {
      let n = [{ type: "text", value: "↩" }];
      return (
        t > 1 &&
          n.push({ type: "element", tagName: "sup", properties: {}, children: [{ type: "text", value: String(t) }] }),
        n
      );
    }
    function t8(e, t) {
      return "Back to reference " + (e + 1) + (t > 1 ? "-" + t : "");
    }
    let ne = function (e) {
      var t, n;
      if (null == e) return nn;
      if ("function" == typeof e) return nt(e);
      if ("object" == typeof e) {
        return Array.isArray(e)
          ? (function (e) {
              let t = [],
                n = -1;
              for (; ++n < e.length; ) t[n] = ne(e[n]);
              return nt(function (...e) {
                let n = -1;
                for (; ++n < t.length; ) if (t[n].apply(this, e)) return !0;
                return !1;
              });
            })(e)
          : ((t = e),
            nt(function (e) {
              let n;
              for (n in t) if (e[n] !== t[n]) return !1;
              return !0;
            }));
      }
      if ("string" == typeof e) {
        return (
          (n = e),
          nt(function (e) {
            return e && e.type === n;
          })
        );
      }
      throw Error("Expected function, string, or object as test");
    };
    function nt(e) {
      return function (t, n, r) {
        return !!(
          (function (e) {
            return null !== e && "object" == typeof e && "type" in e;
          })(t) && e.call(this, t, "number" == typeof n ? n : void 0, r || void 0)
        );
      };
    }
    function nn() {
      return !0;
    }
    let nr = [];
    function ni(e, t, n, r) {
      var i, o, l;
      let a, s, u, c, d, f;
      ("function" == typeof t && "function" != typeof n
        ? ((s = void 0), (u = t), (a = n))
        : ((s = t), (u = n), (a = r)),
        (i = s),
        (o = function (e, t) {
          let n = t[t.length - 1],
            r = n ? n.children.indexOf(e) : void 0;
          return u(e, r, n);
        }),
        (l = a),
        "function" == typeof i && "function" != typeof o ? ((l = o), (o = i)) : (c = i),
        (d = ne(c)),
        (f = l ? -1 : 1),
        (function e(t, n, r) {
          let a = t && "object" == typeof t ? t : {};
          if ("string" == typeof a.type) {
            let e = "string" == typeof a.tagName ? a.tagName : "string" == typeof a.name ? a.name : void 0;
            Object.defineProperty(s, "name", { value: "node (" + t.type + (e ? "<" + e + ">" : "") + ")" });
          }
          return s;
          function s() {
            var a;
            let s,
              u,
              c,
              p = nr;
            if (
              (!i || d(t, n, r[r.length - 1] || void 0)) &&
              !1 === (p = Array.isArray((a = o(t, r))) ? a : "number" == typeof a ? [!0, a] : null == a ? nr : [a])[0]
            )
              return p;
            if ("children" in t && t.children && t.children && "skip" !== p[0])
              for (u = (l ? t.children.length : -1) + f, c = r.concat(t); u > -1 && u < t.children.length; ) {
                if (!1 === (s = e(t.children[u], u, c)())[0]) return s;
                u = "number" == typeof s[1] ? s[1] : u + f;
              }
            return p;
          }
        })(e, void 0, [])());
    }
    function no(e, t) {
      let n = t.referenceType,
        r = "]";
      if (
        ("collapsed" === n ? (r += "[]") : "full" === n && (r += "[" + (t.label || t.identifier) + "]"),
        "imageReference" === t.type)
      )
        return [{ type: "text", value: "![" + t.alt + r }];
      let i = e.all(t),
        o = i[0];
      o && "text" === o.type ? (o.value = "[" + o.value) : i.unshift({ type: "text", value: "[" });
      let l = i[i.length - 1];
      return (l && "text" === l.type ? (l.value += r) : i.push({ type: "text", value: r }), i);
    }
    function nl(e) {
      let t = e.spread;
      return null == t ? e.children.length > 1 : t;
    }
    function na(e, t, n) {
      let r = 0,
        i = e.length;
      if (t) {
        let t = e.codePointAt(r);
        for (; 9 === t || 32 === t; ) (r++, (t = e.codePointAt(r)));
      }
      if (n) {
        let t = e.codePointAt(i - 1);
        for (; 9 === t || 32 === t; ) (i--, (t = e.codePointAt(i - 1)));
      }
      return i > r ? e.slice(r, i) : "";
    }
    let ns = {
      blockquote: function (e, t) {
        let n = { type: "element", tagName: "blockquote", properties: {}, children: e.wrap(e.all(t), !0) };
        return (e.patch(t, n), e.applyData(t, n));
      },
      break: function (e, t) {
        let n = { type: "element", tagName: "br", properties: {}, children: [] };
        return (e.patch(t, n), [e.applyData(t, n), { type: "text", value: "\n" }]);
      },
      code: function (e, t) {
        let n = t.value ? t.value + "\n" : "",
          r = {},
          i = t.lang ? t.lang.split(/\s+/) : [];
        i.length > 0 && (r.className = ["language-" + i[0]]);
        let o = { type: "element", tagName: "code", properties: r, children: [{ type: "text", value: n }] };
        return (
          t.meta && (o.data = { meta: t.meta }),
          e.patch(t, o),
          (o = { type: "element", tagName: "pre", properties: {}, children: [(o = e.applyData(t, o))] }),
          e.patch(t, o),
          o
        );
      },
      delete: function (e, t) {
        let n = { type: "element", tagName: "del", properties: {}, children: e.all(t) };
        return (e.patch(t, n), e.applyData(t, n));
      },
      emphasis: function (e, t) {
        let n = { type: "element", tagName: "em", properties: {}, children: e.all(t) };
        return (e.patch(t, n), e.applyData(t, n));
      },
      footnoteReference: function (e, t) {
        let n,
          r = "string" == typeof e.options.clobberPrefix ? e.options.clobberPrefix : "user-content-",
          i = String(t.identifier).toUpperCase(),
          o = t9(i.toLowerCase()),
          l = e.footnoteOrder.indexOf(i),
          a = e.footnoteCounts.get(i);
        (void 0 === a ? ((a = 0), e.footnoteOrder.push(i), (n = e.footnoteOrder.length)) : (n = l + 1),
          (a += 1),
          e.footnoteCounts.set(i, a));
        let s = {
          type: "element",
          tagName: "a",
          properties: {
            href: "#" + r + "fn-" + o,
            id: r + "fnref-" + o + (a > 1 ? "-" + a : ""),
            dataFootnoteRef: !0,
            ariaDescribedBy: ["footnote-label"],
          },
          children: [{ type: "text", value: String(n) }],
        };
        e.patch(t, s);
        let u = { type: "element", tagName: "sup", properties: {}, children: [s] };
        return (e.patch(t, u), e.applyData(t, u));
      },
      heading: function (e, t) {
        let n = { type: "element", tagName: "h" + t.depth, properties: {}, children: e.all(t) };
        return (e.patch(t, n), e.applyData(t, n));
      },
      html: function (e, t) {
        if (e.options.allowDangerousHtml) {
          let n = { type: "raw", value: t.value };
          return (e.patch(t, n), e.applyData(t, n));
        }
      },
      imageReference: function (e, t) {
        let n = String(t.identifier).toUpperCase(),
          r = e.definitionById.get(n);
        if (!r) return no(e, t);
        let i = { src: t9(r.url || ""), alt: t.alt };
        null !== r.title && void 0 !== r.title && (i.title = r.title);
        let o = { type: "element", tagName: "img", properties: i, children: [] };
        return (e.patch(t, o), e.applyData(t, o));
      },
      image: function (e, t) {
        let n = { src: t9(t.url) };
        (null !== t.alt && void 0 !== t.alt && (n.alt = t.alt),
          null !== t.title && void 0 !== t.title && (n.title = t.title));
        let r = { type: "element", tagName: "img", properties: n, children: [] };
        return (e.patch(t, r), e.applyData(t, r));
      },
      inlineCode: function (e, t) {
        let n = { type: "text", value: t.value.replace(/\r?\n|\r/g, " ") };
        e.patch(t, n);
        let r = { type: "element", tagName: "code", properties: {}, children: [n] };
        return (e.patch(t, r), e.applyData(t, r));
      },
      linkReference: function (e, t) {
        let n = String(t.identifier).toUpperCase(),
          r = e.definitionById.get(n);
        if (!r) return no(e, t);
        let i = { href: t9(r.url || "") };
        null !== r.title && void 0 !== r.title && (i.title = r.title);
        let o = { type: "element", tagName: "a", properties: i, children: e.all(t) };
        return (e.patch(t, o), e.applyData(t, o));
      },
      link: function (e, t) {
        let n = { href: t9(t.url) };
        null !== t.title && void 0 !== t.title && (n.title = t.title);
        let r = { type: "element", tagName: "a", properties: n, children: e.all(t) };
        return (e.patch(t, r), e.applyData(t, r));
      },
      listItem: function (e, t, n) {
        let r = e.all(t),
          i = n
            ? (function (e) {
                let t = !1;
                if ("list" === e.type) {
                  t = e.spread || !1;
                  let n = e.children,
                    r = -1;
                  for (; !t && ++r < n.length; ) t = nl(n[r]);
                }
                return t;
              })(n)
            : nl(t),
          o = {},
          l = [];
        if ("boolean" == typeof t.checked) {
          let e,
            n = r[0];
          (n && "element" === n.type && "p" === n.tagName
            ? (e = n)
            : ((e = { type: "element", tagName: "p", properties: {}, children: [] }), r.unshift(e)),
            e.children.length > 0 && e.children.unshift({ type: "text", value: " " }),
            e.children.unshift({
              type: "element",
              tagName: "input",
              properties: { type: "checkbox", checked: t.checked, disabled: !0 },
              children: [],
            }),
            (o.className = ["task-list-item"]));
        }
        let a = -1;
        for (; ++a < r.length; ) {
          let e = r[a];
          ((i || 0 !== a || "element" !== e.type || "p" !== e.tagName) && l.push({ type: "text", value: "\n" }),
            "element" !== e.type || "p" !== e.tagName || i ? l.push(e) : l.push(...e.children));
        }
        let s = r[r.length - 1];
        s && (i || "element" !== s.type || "p" !== s.tagName) && l.push({ type: "text", value: "\n" });
        let u = { type: "element", tagName: "li", properties: o, children: l };
        return (e.patch(t, u), e.applyData(t, u));
      },
      list: function (e, t) {
        let n = {},
          r = e.all(t),
          i = -1;
        for ("number" == typeof t.start && 1 !== t.start && (n.start = t.start); ++i < r.length; ) {
          let e = r[i];
          if (
            "element" === e.type &&
            "li" === e.tagName &&
            e.properties &&
            Array.isArray(e.properties.className) &&
            e.properties.className.includes("task-list-item")
          ) {
            n.className = ["contains-task-list"];
            break;
          }
        }
        let o = { type: "element", tagName: t.ordered ? "ol" : "ul", properties: n, children: e.wrap(r, !0) };
        return (e.patch(t, o), e.applyData(t, o));
      },
      paragraph: function (e, t) {
        let n = { type: "element", tagName: "p", properties: {}, children: e.all(t) };
        return (e.patch(t, n), e.applyData(t, n));
      },
      root: function (e, t) {
        let n = { type: "root", children: e.wrap(e.all(t)) };
        return (e.patch(t, n), e.applyData(t, n));
      },
      strong: function (e, t) {
        let n = { type: "element", tagName: "strong", properties: {}, children: e.all(t) };
        return (e.patch(t, n), e.applyData(t, n));
      },
      table: function (e, t) {
        let n = e.all(t),
          r = n.shift(),
          i = [];
        if (r) {
          let n = { type: "element", tagName: "thead", properties: {}, children: e.wrap([r], !0) };
          (e.patch(t.children[0], n), i.push(n));
        }
        if (n.length > 0) {
          let r = { type: "element", tagName: "tbody", properties: {}, children: e.wrap(n, !0) },
            o = em(t.children[1]),
            l = eh(t.children[t.children.length - 1]);
          (o && l && (r.position = { start: o, end: l }), i.push(r));
        }
        let o = { type: "element", tagName: "table", properties: {}, children: e.wrap(i, !0) };
        return (e.patch(t, o), e.applyData(t, o));
      },
      tableCell: function (e, t) {
        let n = { type: "element", tagName: "td", properties: {}, children: e.all(t) };
        return (e.patch(t, n), e.applyData(t, n));
      },
      tableRow: function (e, t, n) {
        let r = n ? n.children : void 0,
          i = 0 === (r ? r.indexOf(t) : 1) ? "th" : "td",
          o = n && "table" === n.type ? n.align : void 0,
          l = o ? o.length : t.children.length,
          a = -1,
          s = [];
        for (; ++a < l; ) {
          let n = t.children[a],
            r = {},
            l = o ? o[a] : void 0;
          l && (r.align = l);
          let u = { type: "element", tagName: i, properties: r, children: [] };
          (n && ((u.children = e.all(n)), e.patch(n, u), (u = e.applyData(n, u))), s.push(u));
        }
        let u = { type: "element", tagName: "tr", properties: {}, children: e.wrap(s, !0) };
        return (e.patch(t, u), e.applyData(t, u));
      },
      text: function (e, t) {
        let n = {
          type: "text",
          value: (function (e) {
            let t = String(e),
              n = /\r?\n|\r/g,
              r = n.exec(t),
              i = 0,
              o = [];
            for (; r; )
              (o.push(na(t.slice(i, r.index), i > 0, !0), r[0]), (i = r.index + r[0].length), (r = n.exec(t)));
            return (o.push(na(t.slice(i), i > 0, !1)), o.join(""));
          })(String(t.value)),
        };
        return (e.patch(t, n), e.applyData(t, n));
      },
      thematicBreak: function (e, t) {
        let n = { type: "element", tagName: "hr", properties: {}, children: [] };
        return (e.patch(t, n), e.applyData(t, n));
      },
      toml: nu,
      yaml: nu,
      definition: nu,
      footnoteDefinition: nu,
    };
    function nu() {}
    let nc = {}.hasOwnProperty,
      nd = {};
    function nf(e, t) {
      e.position &&
        (t.position = (function (e) {
          let t = em(e),
            n = eh(e);
          if (t && n) return { start: t, end: n };
        })(e));
    }
    function np(e, t) {
      let n = t;
      if (e && e.data) {
        let t = e.data.hName,
          r = e.data.hChildren,
          i = e.data.hProperties;
        ("string" == typeof t &&
          ("element" === n.type
            ? (n.tagName = t)
            : (n = { type: "element", tagName: t, properties: {}, children: "children" in n ? n.children : [n] })),
          "element" === n.type && i && Object.assign(n.properties, t6(i)),
          "children" in n && n.children && null != r && (n.children = r));
      }
      return n;
    }
    function nh(e, t) {
      let n = [],
        r = -1;
      for (t && n.push({ type: "text", value: "\n" }); ++r < e.length; )
        (r && n.push({ type: "text", value: "\n" }), n.push(e[r]));
      return (t && e.length > 0 && n.push({ type: "text", value: "\n" }), n);
    }
    function nm(e) {
      let t = 0,
        n = e.charCodeAt(t);
      for (; 9 === n || 32 === n; ) (t++, (n = e.charCodeAt(t)));
      return e.slice(t);
    }
    function ng(e, t) {
      let n,
        r,
        i,
        o,
        l =
          ((n = t || nd),
          (r = new Map()),
          (i = new Map()),
          (o = {
            all: function (e) {
              let t = [];
              if ("children" in e) {
                let n = e.children,
                  r = -1;
                for (; ++r < n.length; ) {
                  let i = o.one(n[r], e);
                  if (i) {
                    if (
                      r &&
                      "break" === n[r - 1].type &&
                      (Array.isArray(i) || "text" !== i.type || (i.value = nm(i.value)),
                      !Array.isArray(i) && "element" === i.type)
                    ) {
                      let e = i.children[0];
                      e && "text" === e.type && (e.value = nm(e.value));
                    }
                    Array.isArray(i) ? t.push(...i) : t.push(i);
                  }
                }
              }
              return t;
            },
            applyData: np,
            definitionById: r,
            footnoteById: i,
            footnoteCounts: new Map(),
            footnoteOrder: [],
            handlers: { ...ns, ...n.handlers },
            one: function (e, t) {
              let n = e.type,
                r = o.handlers[n];
              if (nc.call(o.handlers, n) && r) return r(o, e, t);
              if (o.options.passThrough && o.options.passThrough.includes(n)) {
                if ("children" in e) {
                  let { children: t, ...n } = e,
                    r = t6(n);
                  return ((r.children = o.all(e)), r);
                }
                return t6(e);
              }
              return (
                o.options.unknownHandler ||
                function (e, t) {
                  let n = t.data || {},
                    r =
                      "value" in t && !(nc.call(n, "hProperties") || nc.call(n, "hChildren"))
                        ? { type: "text", value: t.value }
                        : { type: "element", tagName: "div", properties: {}, children: e.all(t) };
                  return (e.patch(t, r), e.applyData(t, r));
                }
              )(o, e, t);
            },
            options: n,
            patch: nf,
            wrap: nh,
          }),
          ni(e, function (e) {
            if ("definition" === e.type || "footnoteDefinition" === e.type) {
              let t = "definition" === e.type ? r : i,
                n = String(e.identifier).toUpperCase();
              t.has(n) || t.set(n, e);
            }
          }),
          o),
        a = l.one(e, void 0),
        s = (function (e) {
          let t = "string" == typeof e.options.clobberPrefix ? e.options.clobberPrefix : "user-content-",
            n = e.options.footnoteBackContent || t7,
            r = e.options.footnoteBackLabel || t8,
            i = e.options.footnoteLabel || "Footnotes",
            o = e.options.footnoteLabelTagName || "h2",
            l = e.options.footnoteLabelProperties || { className: ["sr-only"] },
            a = [],
            s = -1;
          for (; ++s < e.footnoteOrder.length; ) {
            let i = e.footnoteById.get(e.footnoteOrder[s]);
            if (!i) continue;
            let o = e.all(i),
              l = String(i.identifier).toUpperCase(),
              u = t9(l.toLowerCase()),
              c = 0,
              d = [],
              f = e.footnoteCounts.get(l);
            for (; void 0 !== f && ++c <= f; ) {
              d.length > 0 && d.push({ type: "text", value: " " });
              let e = "string" == typeof n ? n : n(s, c);
              ("string" == typeof e && (e = { type: "text", value: e }),
                d.push({
                  type: "element",
                  tagName: "a",
                  properties: {
                    href: "#" + t + "fnref-" + u + (c > 1 ? "-" + c : ""),
                    dataFootnoteBackref: "",
                    ariaLabel: "string" == typeof r ? r : r(s, c),
                    className: ["data-footnote-backref"],
                  },
                  children: Array.isArray(e) ? e : [e],
                }));
            }
            let p = o[o.length - 1];
            if (p && "element" === p.type && "p" === p.tagName) {
              let e = p.children[p.children.length - 1];
              (e && "text" === e.type ? (e.value += " ") : p.children.push({ type: "text", value: " " }),
                p.children.push(...d));
            } else o.push(...d);
            let h = { type: "element", tagName: "li", properties: { id: t + "fn-" + u }, children: e.wrap(o, !0) };
            (e.patch(i, h), a.push(h));
          }
          if (0 !== a.length)
            return {
              type: "element",
              tagName: "section",
              properties: { dataFootnotes: !0, className: ["footnotes"] },
              children: [
                {
                  type: "element",
                  tagName: o,
                  properties: { ...t6(l), id: "footnote-label" },
                  children: [{ type: "text", value: i }],
                },
                { type: "text", value: "\n" },
                { type: "element", tagName: "ol", properties: {}, children: e.wrap(a, !0) },
                { type: "text", value: "\n" },
              ],
            };
        })(l),
        u = Array.isArray(a) ? { type: "root", children: a } : a || { type: "root", children: [] };
      return (s && (j(), u.children.push({ type: "text", value: "\n" }, s)), u);
    }
    function nv(e, t) {
      return e && "run" in e
        ? async function (n, r) {
            let i = ng(n, { file: r, ...t });
            await e.run(i, r);
          }
        : function (n, r) {
            return ng(n, { file: r, ...(e || t) });
          };
    }
    function ny(e) {
      if (e) throw e;
    }
    var nb = e.i(4100);
    function nx(e) {
      if ("object" != typeof e || null === e) return !1;
      let t = Object.getPrototypeOf(e);
      return (
        (null === t || t === Object.prototype || null === Object.getPrototypeOf(t)) &&
        !(Symbol.toStringTag in e) &&
        !(Symbol.iterator in e)
      );
    }
    let nk = function (e, t) {
        let n;
        if (void 0 !== t && "string" != typeof t) throw TypeError('"ext" argument must be a string');
        nE(e);
        let r = 0,
          i = -1,
          o = e.length;
        if (void 0 === t || 0 === t.length || t.length > e.length) {
          for (; o--; )
            if (47 === e.codePointAt(o)) {
              if (n) {
                r = o + 1;
                break;
              }
            } else i < 0 && ((n = !0), (i = o + 1));
          return i < 0 ? "" : e.slice(r, i);
        }
        if (t === e) return "";
        let l = -1,
          a = t.length - 1;
        for (; o--; )
          if (47 === e.codePointAt(o)) {
            if (n) {
              r = o + 1;
              break;
            }
          } else
            (l < 0 && ((n = !0), (l = o + 1)),
              a > -1 && (e.codePointAt(o) === t.codePointAt(a--) ? a < 0 && (i = o) : ((a = -1), (i = l))));
        return (r === i ? (i = l) : i < 0 && (i = e.length), e.slice(r, i));
      },
      nw = function (e) {
        let t;
        if ((nE(e), 0 === e.length)) return ".";
        let n = -1,
          r = e.length;
        for (; --r; )
          if (47 === e.codePointAt(r)) {
            if (t) {
              n = r;
              break;
            }
          } else t || (t = !0);
        return n < 0
          ? 47 === e.codePointAt(0)
            ? "/"
            : "."
          : 1 === n && 47 === e.codePointAt(0)
            ? "//"
            : e.slice(0, n);
      },
      nS = function (e) {
        let t;
        nE(e);
        let n = e.length,
          r = -1,
          i = 0,
          o = -1,
          l = 0;
        for (; n--; ) {
          let a = e.codePointAt(n);
          if (47 === a) {
            if (t) {
              i = n + 1;
              break;
            }
            continue;
          }
          (r < 0 && ((t = !0), (r = n + 1)), 46 === a ? (o < 0 ? (o = n) : 1 !== l && (l = 1)) : o > -1 && (l = -1));
        }
        return o < 0 || r < 0 || 0 === l || (1 === l && o === r - 1 && o === i + 1) ? "" : e.slice(o, r);
      },
      nC = function (...e) {
        var t;
        let n,
          r,
          i,
          o = -1;
        for (; ++o < e.length; ) (nE(e[o]), e[o] && (i = void 0 === i ? e[o] : i + "/" + e[o]));
        return void 0 === i
          ? "."
          : (nE((t = i)),
            (n = 47 === t.codePointAt(0)),
            0 !==
              (r = (function (e, t) {
                let n,
                  r,
                  i = "",
                  o = 0,
                  l = -1,
                  a = 0,
                  s = -1;
                for (; ++s <= e.length; ) {
                  if (s < e.length) n = e.codePointAt(s);
                  else if (47 === n) break;
                  else n = 47;
                  if (47 === n) {
                    if (l === s - 1 || 1 === a);
                    else if (l !== s - 1 && 2 === a) {
                      if (
                        i.length < 2 ||
                        2 !== o ||
                        46 !== i.codePointAt(i.length - 1) ||
                        46 !== i.codePointAt(i.length - 2)
                      ) {
                        if (i.length > 2) {
                          if ((r = i.lastIndexOf("/")) !== i.length - 1) {
                            (r < 0 ? ((i = ""), (o = 0)) : (o = (i = i.slice(0, r)).length - 1 - i.lastIndexOf("/")),
                              (l = s),
                              (a = 0));
                            continue;
                          }
                        } else if (i.length > 0) {
                          ((i = ""), (o = 0), (l = s), (a = 0));
                          continue;
                        }
                      }
                      t && ((i = i.length > 0 ? i + "/.." : ".."), (o = 2));
                    } else (i.length > 0 ? (i += "/" + e.slice(l + 1, s)) : (i = e.slice(l + 1, s)), (o = s - l - 1));
                    ((l = s), (a = 0));
                  } else 46 === n && a > -1 ? a++ : (a = -1);
                }
                return i;
              })(t, !n)).length ||
              n ||
              (r = "."),
            r.length > 0 && 47 === t.codePointAt(t.length - 1) && (r += "/"),
            n ? "/" + r : r);
      };
    function nE(e) {
      if ("string" != typeof e) throw TypeError("Path must be a string. Received " + JSON.stringify(e));
    }
    function nj(e) {
      return !!(
        null !== e &&
        "object" == typeof e &&
        "href" in e &&
        e.href &&
        "protocol" in e &&
        e.protocol &&
        void 0 === e.auth
      );
    }
    let nR = ["history", "path", "basename", "stem", "extname", "dirname"];
    class nP {
      constructor(e) {
        let t, n;
        ((t = e
          ? nj(e)
            ? { path: e }
            : "string" == typeof e ||
                (function (e) {
                  return !!(e && "object" == typeof e && "byteLength" in e && "byteOffset" in e);
                })(e)
              ? { value: e }
              : e
          : {}),
          (this.cwd = "cwd" in t ? "" : "/"),
          (this.data = {}),
          (this.history = []),
          (this.messages = []),
          this.value,
          this.map,
          this.result,
          this.stored);
        let r = -1;
        for (; ++r < nR.length; ) {
          const e = nR[r];
          e in t && void 0 !== t[e] && null !== t[e] && (this[e] = "history" === e ? [...t[e]] : t[e]);
        }
        for (n in t) nR.includes(n) || (this[n] = t[n]);
      }
      get basename() {
        return "string" == typeof this.path ? nk(this.path) : void 0;
      }
      set basename(e) {
        (nA(e, "basename"), nT(e, "basename"), (this.path = nC(this.dirname || "", e)));
      }
      get dirname() {
        return "string" == typeof this.path ? nw(this.path) : void 0;
      }
      set dirname(e) {
        (nO(this.basename, "dirname"), (this.path = nC(e || "", this.basename)));
      }
      get extname() {
        return "string" == typeof this.path ? nS(this.path) : void 0;
      }
      set extname(e) {
        if ((nT(e, "extname"), nO(this.dirname, "extname"), e)) {
          if (46 !== e.codePointAt(0)) throw Error("`extname` must start with `.`");
          if (e.includes(".", 1)) throw Error("`extname` cannot contain multiple dots");
        }
        this.path = nC(this.dirname, this.stem + (e || ""));
      }
      get path() {
        return this.history[this.history.length - 1];
      }
      set path(e) {
        (nj(e) &&
          (e = (function (e) {
            if ("string" == typeof e) e = new URL(e);
            else if (!nj(e)) {
              let t = TypeError(
                'The "path" argument must be of type string or an instance of URL. Received `' + e + "`",
              );
              throw ((t.code = "ERR_INVALID_ARG_TYPE"), t);
            }
            if ("file:" !== e.protocol) {
              let e = TypeError("The URL must be of scheme file");
              throw ((e.code = "ERR_INVALID_URL_SCHEME"), e);
            }
            return (function (e) {
              if ("" !== e.hostname) {
                let e = TypeError('File URL host must be "localhost" or empty on darwin');
                throw ((e.code = "ERR_INVALID_FILE_URL_HOST"), e);
              }
              let t = e.pathname,
                n = -1;
              for (; ++n < t.length; )
                if (37 === t.codePointAt(n) && 50 === t.codePointAt(n + 1)) {
                  let e = t.codePointAt(n + 2);
                  if (70 === e || 102 === e) {
                    let e = TypeError("File URL path must not include encoded / characters");
                    throw ((e.code = "ERR_INVALID_FILE_URL_PATH"), e);
                  }
                }
              return decodeURIComponent(t);
            })(e);
          })(e)),
          nA(e, "path"),
          this.path !== e && this.history.push(e));
      }
      get stem() {
        return "string" == typeof this.path ? nk(this.path, this.extname) : void 0;
      }
      set stem(e) {
        (nA(e, "stem"), nT(e, "stem"), (this.path = nC(this.dirname || "", e + (this.extname || ""))));
      }
      fail(e, t, n) {
        let r = this.message(e, t, n);
        throw ((r.fatal = !0), r);
      }
      info(e, t, n) {
        let r = this.message(e, t, n);
        return ((r.fatal = void 0), r);
      }
      message(e, t, n) {
        let r = new ek(e, t, n);
        return (
          this.path && ((r.name = this.path + ":" + r.name), (r.file = this.path)),
          (r.fatal = !1),
          this.messages.push(r),
          r
        );
      }
      toString(e) {
        return void 0 === this.value
          ? ""
          : "string" == typeof this.value
            ? this.value
            : new TextDecoder(e || void 0).decode(this.value);
      }
    }
    function nT(e, t) {
      if (e && e.includes("/")) throw Error("`" + t + "` cannot be a path: did not expect `/`");
    }
    function nA(e, t) {
      if (!e) throw Error("`" + t + "` cannot be empty");
    }
    function nO(e, t) {
      if (!e) throw Error("Setting `" + t + "` requires `path` to be set too");
    }
    let nI = function (e) {
        let t = this.constructor.prototype,
          n = t[e],
          r = function () {
            return n.apply(r, arguments);
          };
        return (Object.setPrototypeOf(r, t), r);
      },
      nM = {}.hasOwnProperty,
      nN = new (class e extends nI {
        constructor() {
          (super("copy"),
            (this.Compiler = void 0),
            (this.Parser = void 0),
            (this.attachers = []),
            (this.compiler = void 0),
            (this.freezeIndex = -1),
            (this.frozen = void 0),
            (this.namespace = {}),
            (this.parser = void 0),
            (this.transformers = (function () {
              let e = [],
                t = {
                  run: function (...t) {
                    let n = -1,
                      r = t.pop();
                    if ("function" != typeof r) throw TypeError("Expected function as last argument, not " + r);
                    !(function i(o, ...l) {
                      let a = e[++n],
                        s = -1;
                      if (o) return void r(o);
                      for (; ++s < t.length; ) (null === l[s] || void 0 === l[s]) && (l[s] = t[s]);
                      ((t = l),
                        a
                          ? (function (e, t) {
                              let n;
                              return function (...t) {
                                let o,
                                  l = e.length > t.length;
                                l && t.push(r);
                                try {
                                  o = e.apply(this, t);
                                } catch (e) {
                                  if (l && n) throw e;
                                  return r(e);
                                }
                                l ||
                                  (o && o.then && "function" == typeof o.then
                                    ? o.then(i, r)
                                    : o instanceof Error
                                      ? r(o)
                                      : i(o));
                              };
                              function r(e, ...i) {
                                n || ((n = !0), t(e, ...i));
                              }
                              function i(e) {
                                r(null, e);
                              }
                            })(
                              a,
                              i,
                            )(...l)
                          : r(null, ...l));
                    })(null, ...t);
                  },
                  use: function (n) {
                    if ("function" != typeof n) throw TypeError("Expected `middelware` to be a function, not " + n);
                    return (e.push(n), t);
                  },
                };
              return t;
            })()));
        }
        copy() {
          let t = new e(),
            n = -1;
          for (; ++n < this.attachers.length; ) {
            let e = this.attachers[n];
            t.use(...e);
          }
          return (t.data((0, nb.default)(!0, {}, this.namespace)), t);
        }
        data(e, t) {
          return "string" == typeof e
            ? 2 == arguments.length
              ? (nL("data", this.frozen), (this.namespace[e] = t), this)
              : (nM.call(this.namespace, e) && this.namespace[e]) || void 0
            : e
              ? (nL("data", this.frozen), (this.namespace = e), this)
              : this.namespace;
        }
        freeze() {
          if (this.frozen) return this;
          for (; ++this.freezeIndex < this.attachers.length; ) {
            let [e, ...t] = this.attachers[this.freezeIndex];
            if (!1 === t[0]) continue;
            !0 === t[0] && (t[0] = void 0);
            let n = e.call(this, ...t);
            "function" == typeof n && this.transformers.use(n);
          }
          return ((this.frozen = !0), (this.freezeIndex = 1 / 0), this);
        }
        parse(e) {
          this.freeze();
          let t = n_(e),
            n = this.parser || this.Parser;
          return (nz("parse", n), n(String(t), t));
        }
        process(e, t) {
          let n = this;
          return (
            this.freeze(),
            nz("process", this.parser || this.Parser),
            nD("process", this.compiler || this.Compiler),
            t ? r(void 0, t) : new Promise(r)
          );
          function r(r, i) {
            let o = n_(e),
              l = n.parse(o);
            function a(e, n) {
              e || !n ? i(e) : r ? r(n) : (j(), t(void 0, n));
            }
            n.run(l, o, function (e, t, r) {
              var i, o;
              if (e || !t || !r) return a(e);
              let l = n.stringify(t, r);
              ("string" == typeof (i = l) || ((o = i) && "object" == typeof o && "byteLength" in o && "byteOffset" in o)
                ? (r.value = l)
                : (r.result = l),
                a(e, r));
            });
          }
        }
        processSync(e) {
          let t,
            n = !1;
          return (
            this.freeze(),
            nz("processSync", this.parser || this.Parser),
            nD("processSync", this.compiler || this.Compiler),
            this.process(e, function (e, r) {
              ((n = !0), ny(e), (t = r));
            }),
            nF("processSync", "process", n),
            j(),
            t
          );
        }
        run(e, t, n) {
          (n$(e), this.freeze());
          let r = this.transformers;
          return (n || "function" != typeof t || ((n = t), (t = void 0)), n ? i(void 0, n) : new Promise(i));
          function i(i, o) {
            j();
            let l = n_(t);
            r.run(e, l, function (t, r, l) {
              let a = r || e;
              t ? o(t) : i ? i(a) : (j(), n(void 0, a, l));
            });
          }
        }
        runSync(e, t) {
          let n,
            r = !1;
          return (
            this.run(e, t, function (e, t) {
              (ny(e), (n = t), (r = !0));
            }),
            nF("runSync", "run", r),
            j(),
            n
          );
        }
        stringify(e, t) {
          this.freeze();
          let n = n_(t),
            r = this.compiler || this.Compiler;
          return (nD("stringify", r), n$(e), r(e, n));
        }
        use(e, ...t) {
          let n = this.attachers,
            r = this.namespace;
          if ((nL("use", this.frozen), null == e));
          else if ("function" == typeof e) l(e, t);
          else if ("object" == typeof e) Array.isArray(e) ? o(e) : i(e);
          else throw TypeError("Expected usable value, not `" + e + "`");
          return this;
          function i(e) {
            if (!("plugins" in e) && !("settings" in e))
              throw Error(
                "Expected usable value but received an empty preset, which is probably a mistake: presets typically come with `plugins` and sometimes with `settings`, but this has neither",
              );
            (o(e.plugins), e.settings && (r.settings = (0, nb.default)(!0, r.settings, e.settings)));
          }
          function o(e) {
            let t = -1;
            if (null == e);
            else if (Array.isArray(e))
              for (; ++t < e.length; )
                !(function (e) {
                  if ("function" == typeof e) l(e, []);
                  else if ("object" == typeof e)
                    if (Array.isArray(e)) {
                      let [t, ...n] = e;
                      l(t, n);
                    } else i(e);
                  else throw TypeError("Expected usable value, not `" + e + "`");
                })(e[t]);
            else throw TypeError("Expected a list of plugins, not `" + e + "`");
          }
          function l(e, t) {
            let r = -1,
              i = -1;
            for (; ++r < n.length; )
              if (n[r][0] === e) {
                i = r;
                break;
              }
            if (-1 === i) n.push([e, ...t]);
            else if (t.length > 0) {
              let [r, ...o] = t,
                l = n[i][1];
              (nx(l) && nx(r) && (r = (0, nb.default)(!0, l, r)), (n[i] = [e, r, ...o]));
            }
          }
        }
      })().freeze();
    function nz(e, t) {
      if ("function" != typeof t) throw TypeError("Cannot `" + e + "` without `parser`");
    }
    function nD(e, t) {
      if ("function" != typeof t) throw TypeError("Cannot `" + e + "` without `compiler`");
    }
    function nL(e, t) {
      if (t)
        throw Error(
          "Cannot call `" +
            e +
            "` on a frozen processor.\nCreate a new processor first, by calling it: use `processor()` instead of `processor`.",
        );
    }
    function n$(e) {
      if (!nx(e) || "string" != typeof e.type) throw TypeError("Expected node, got `" + e + "`");
    }
    function nF(e, t, n) {
      if (!n) throw Error("`" + e + "` finished async. Use `" + t + "` instead");
    }
    function n_(e) {
      var t;
      return (t = e) && "object" == typeof t && "message" in t && "messages" in t ? e : new nP(e);
    }
    let nB = [],
      nH = { allowDangerousHtml: !0 },
      nq = /^(https?|ircs?|mailto|xmpp)$/i,
      nU = [
        { from: "astPlugins", id: "remove-buggy-html-in-markdown-parser" },
        { from: "allowDangerousHtml", id: "remove-buggy-html-in-markdown-parser" },
        { from: "allowNode", id: "replace-allownode-allowedtypes-and-disallowedtypes", to: "allowElement" },
        { from: "allowedTypes", id: "replace-allownode-allowedtypes-and-disallowedtypes", to: "allowedElements" },
        { from: "className", id: "remove-classname" },
        { from: "disallowedTypes", id: "replace-allownode-allowedtypes-and-disallowedtypes", to: "disallowedElements" },
        { from: "escapeHtml", id: "remove-buggy-html-in-markdown-parser" },
        { from: "includeElementIndex", id: "#remove-includeelementindex" },
        { from: "includeNodeIndex", id: "change-includenodeindex-to-includeelementindex" },
        { from: "linkTarget", id: "remove-linktarget" },
        { from: "plugins", id: "change-plugins-to-remarkplugins", to: "remarkPlugins" },
        { from: "rawSourcePos", id: "#remove-rawsourcepos" },
        { from: "renderers", id: "change-renderers-to-components", to: "components" },
        { from: "source", id: "change-source-to-children", to: "children" },
        { from: "sourcePos", id: "#remove-sourcepos" },
        { from: "transformImageUri", id: "#add-urltransform", to: "urlTransform" },
        { from: "transformLinkUri", id: "#add-urltransform", to: "urlTransform" },
      ];
    function nW(e) {
      var t;
      let n,
        r,
        i,
        o,
        l,
        a =
          ((n = (t = e).rehypePlugins || nB),
          (r = t.remarkPlugins || nB),
          (i = t.remarkRehypeOptions ? { ...t.remarkRehypeOptions, ...nH } : nH),
          nN().use(tJ).use(r).use(nv, i).use(n)),
        s = ((o = e.children || ""), (l = new nP()), "string" == typeof o ? (l.value = o) : R(), l);
      return (function (e, t) {
        let n = t.allowedElements,
          r = t.allowElement,
          i = t.components,
          o = t.disallowedElements,
          l = t.skipHtml,
          a = t.unwrapDisallowed,
          s = t.urlTransform || nV;
        for (let e of nU) Object.hasOwn(t, e.from) && R((e.from, e.to && e.to, e.id));
        return (
          n && o && R(),
          ni(e, function (e, t, i) {
            if ("raw" === e.type && i && "number" == typeof t)
              return (l ? i.children.splice(t, 1) : (i.children[t] = { type: "text", value: e.value }), t);
            if ("element" === e.type) {
              let t;
              for (t in ez)
                if (Object.hasOwn(ez, t) && Object.hasOwn(e.properties, t)) {
                  let n = e.properties[t],
                    r = ez[t];
                  (null === r || r.includes(e.tagName)) && (e.properties[t] = s(String(n || ""), t, e));
                }
            }
            if ("element" === e.type) {
              let l = n ? !n.includes(e.tagName) : !!o && o.includes(e.tagName);
              if ((!l && r && "number" == typeof t && (l = !r(e, t, i)), l && i && "number" == typeof t))
                return (a && e.children ? i.children.splice(t, 1, ...e.children) : i.children.splice(t, 1), t);
            }
          }),
          (function (e, t) {
            var n, r, i, o;
            let l;
            if (!t || void 0 === t.Fragment) throw TypeError("Expected `Fragment` in options");
            let a = t.filePath || void 0;
            if (t.development) {
              if ("function" != typeof t.jsxDEV)
                throw TypeError("Expected `jsxDEV` in options when `development: true`");
              ((n = a),
                (r = t.jsxDEV),
                (l = function (e, t, i, o) {
                  let l = Array.isArray(i.children),
                    a = em(e);
                  return r(
                    t,
                    i,
                    o,
                    l,
                    { columnNumber: a ? a.column - 1 : void 0, fileName: n, lineNumber: a ? a.line : void 0 },
                    void 0,
                  );
                }));
            } else {
              if ("function" != typeof t.jsx) throw TypeError("Expected `jsx` in production options");
              if ("function" != typeof t.jsxs) throw TypeError("Expected `jsxs` in production options");
              ((i = t.jsx),
                (o = t.jsxs),
                (l = function (e, t, n, r) {
                  let l = Array.isArray(n.children) ? o : i;
                  return r ? l(t, n, r) : l(t, n);
                }));
            }
            let s = {
                Fragment: t.Fragment,
                ancestors: [],
                components: t.components || {},
                create: l,
                elementAttributeNameCase: t.elementAttributeNameCase || "react",
                evaluater: t.createEvaluater ? t.createEvaluater() : void 0,
                filePath: a,
                ignoreInvalidStyle: t.ignoreInvalidStyle || !1,
                passKeys: !1 !== t.passKeys,
                passNode: t.passNode || !1,
                schema: "svg" === t.space ? ef : ed,
                stylePropertyNameCase: t.stylePropertyNameCase || "dom",
                tableCellAlignToStyle: !1 !== t.tableCellAlignToStyle,
              },
              u = eP(s, e, void 0);
            return u && "string" != typeof u ? u : s.create(e, s.Fragment, { children: u || void 0 }, void 0);
          })(e, {
            Fragment: d.Fragment,
            components: i,
            ignoreInvalidStyle: !0,
            jsx: d.jsx,
            jsxs: d.jsxs,
            passKeys: !0,
            passNode: !0,
          })
        );
      })(a.runSync(a.parse(s), s), e);
    }
    function nV(e) {
      let t = e.indexOf(":"),
        n = e.indexOf("?"),
        r = e.indexOf("#"),
        i = e.indexOf("/");
      return -1 === t || (-1 !== i && t > i) || (-1 !== n && t > n) || (-1 !== r && t > r) || nq.test(e.slice(0, t))
        ? e
        : "";
    }
    function nK(e, t) {
      return e && !t ? e : !e && t ? t : e || t ? { ...e, ...t } : void 0;
    }
    let nX = {};
    function nY(e, t, n, r, i) {
      if (!n && !r && !i && !e) return nG(t);
      let o = nG(e);
      return (t && (o = nJ(o, t)), n && (o = nJ(o, n)), r && (o = nJ(o, r)), i && (o = nJ(o, i)), o);
    }
    function nG(e) {
      return nZ(e)
        ? { ...n0(e, nX) }
        : (function (e) {
            let t = { ...e };
            for (let e in t) {
              let n = t[e];
              nQ(e, n) && (t[e] = n1(n));
            }
            return t;
          })(e);
    }
    function nJ(e, t) {
      return nZ(t)
        ? n0(t, e)
        : (function (e, t) {
            if (!t) return e;
            for (let n in t) {
              let r = t[n];
              switch (n) {
                case "style":
                  e[n] = nK(e.style, r);
                  break;
                case "className":
                  e[n] = n4(e.className, r);
                  break;
                default:
                  nQ(n, r)
                    ? (e[n] = (function (e, t) {
                        return t
                          ? e
                            ? (...n) => {
                                let r = n[0];
                                if (n5(r)) {
                                  n2(r);
                                  let i = t(...n);
                                  return (r.baseUIHandlerPrevented || e?.(...n), i);
                                }
                                let i = t(...n);
                                return (e?.(...n), i);
                              }
                            : n1(t)
                          : e;
                      })(e[n], r))
                    : (e[n] = r);
              }
            }
            return e;
          })(e, t);
    }
    function nQ(e, t) {
      let n = e.charCodeAt(0),
        r = e.charCodeAt(1),
        i = e.charCodeAt(2);
      return 111 === n && 110 === r && i >= 65 && i <= 90 && ("function" == typeof t || void 0 === t);
    }
    function nZ(e) {
      return "function" == typeof e;
    }
    function n0(e, t) {
      return nZ(e) ? e(t) : (e ?? nX);
    }
    function n1(e) {
      return e
        ? (...t) => {
            let n = t[0];
            return (n5(n) && n2(n), e(...t));
          }
        : e;
    }
    function n2(e) {
      return (
        (e.preventBaseUIHandler = () => {
          e.baseUIHandlerPrevented = !0;
        }),
        e
      );
    }
    function n4(e, t) {
      return t ? (e ? t + " " + e : t) : e;
    }
    function n5(e) {
      return null != e && "object" == typeof e && "nativeEvent" in e;
    }
    let n3 = function (e, ...t) {
        let n = new URL("https://base-ui.com/production-error");
        return (
          n.searchParams.set("code", e.toString()),
          t.forEach((e) => n.searchParams.append("args[]", e)),
          `Base UI error #${e}; visit ${n} for the full message.`
        );
      },
      n6 = {};
    function n9(e, t) {
      let n = f.useRef(n6);
      return (n.current === n6 && (n.current = e(t)), n);
    }
    function n7(e, t, n, r) {
      var i, o, l, a, s;
      let u = n9(n8).current;
      return (
        (i = u),
        (o = e),
        (l = t),
        (a = n),
        (s = r),
        (i.refs[0] !== o || i.refs[1] !== l || i.refs[2] !== a || i.refs[3] !== s) && re(u, [e, t, n, r]),
        u.callback
      );
    }
    function n8() {
      return { callback: null, cleanup: null, refs: [] };
    }
    function re(e, t) {
      if (((e.refs = t), t.every((e) => null == e))) {
        e.callback = null;
        return;
      }
      e.callback = (n) => {
        if ((e.cleanup && (e.cleanup(), (e.cleanup = null)), null != n)) {
          let r = Array(t.length).fill(null);
          for (let e = 0; e < t.length; e += 1) {
            let i = t[e];
            if (null != i)
              switch (typeof i) {
                case "function": {
                  let t = i(n);
                  "function" == typeof t && (r[e] = t);
                  break;
                }
                case "object":
                  i.current = n;
              }
          }
          e.cleanup = () => {
            for (let e = 0; e < t.length; e += 1) {
              let n = t[e];
              if (null != n)
                switch (typeof n) {
                  case "function": {
                    let t = r[e];
                    "function" == typeof t ? t() : n(null);
                    break;
                  }
                  case "object":
                    n.current = null;
                }
            }
          };
        }
      };
    }
    let rt = parseInt(f.version, 10);
    function rn(e) {
      if (!f.isValidElement(e)) return null;
      let t = e.props;
      return (rt >= 19 ? t?.ref : e.ref) ?? null;
    }
    function rr() {}
    let ri = Object.freeze([]),
      ro = Object.freeze({});
    function rl(e, t, n = {}) {
      let r = t.render,
        i = (function (e, t = {}) {
          var n, r, i;
          let { className: o, style: l, render: a } = e,
            { state: s = ro, ref: u, props: c, stateAttributesMapping: d, enabled: f = !0 } = t,
            p = f ? ("function" == typeof o ? o(s) : o) : void 0,
            h = f ? ("function" == typeof l ? l(s) : l) : void 0,
            m = f
              ? (function (e, t) {
                  let n = {};
                  for (let r in e) {
                    let i = e[r];
                    if (t?.hasOwnProperty(r)) {
                      let e = t[r](i);
                      null != e && Object.assign(n, e);
                      continue;
                    }
                    !0 === i ? (n[`data-${r.toLowerCase()}`] = "") : i && (n[`data-${r.toLowerCase()}`] = i.toString());
                  }
                  return n;
                })(s, d)
              : ro,
            g =
              f && c
                ? (function (e) {
                    if (Array.isArray(e)) {
                      if (0 === e.length) return nX;
                      if (1 === e.length) return nG(e[0]);
                      let t = nG(e[0]);
                      for (let n = 1; n < e.length; n += 1) t = nJ(t, e[n]);
                      return t;
                    }
                    return nY(void 0, e);
                  })(c)
                : void 0,
            v = f ? (nK(m, g) ?? {}) : ro;
          if ("u" > typeof document)
            if (f)
              if (Array.isArray(u)) {
                let e;
                ((n = [v.ref, rn(a), ...u]),
                  (r = e = n9(n8).current),
                  (i = n),
                  (r.refs.length !== i.length || r.refs.some((e, t) => e !== i[t])) && re(e, n),
                  (v.ref = e.callback));
              } else v.ref = n7(v.ref, rn(a), u);
            else n7(null, null);
          return f
            ? (void 0 !== p && (v.className = n4(v.className, p)), void 0 !== h && (v.style = nK(v.style, h)), v)
            : ro;
        })(t, n);
      return !1 === n.enabled
        ? null
        : (function (e, t, n, r) {
            if (t) {
              if ("function" == typeof t) return t(n, r);
              let e = nY(n, t.props);
              e.ref = n.ref;
              let i = t;
              return (i?.$$typeof === ra && (i = f.Children.toArray(t)[0]), f.cloneElement(i, e));
            }
            if (e && "string" == typeof e) {
              var i, o;
              return (
                (i = e),
                (o = n),
                "button" === i
                  ? (0, f.createElement)("button", { type: "button", ...o, key: o.key })
                  : "img" === i
                    ? (0, f.createElement)("img", { alt: "", ...o, key: o.key })
                    : f.createElement(i, o)
              );
            }
            throw Error(n3(8));
          })(e, r, i, n.state ?? ro);
    }
    let ra = Symbol.for("react.lazy");
    function rs() {
      for (var e, t, n = 0, r = "", i = arguments.length; n < i; n++)
        (e = arguments[n]) &&
          (t = (function e(t) {
            var n,
              r,
              i = "";
            if ("string" == typeof t || "number" == typeof t) i += t;
            else if ("object" == typeof t)
              if (Array.isArray(t)) {
                var o = t.length;
                for (n = 0; n < o; n++) t[n] && (r = e(t[n])) && (i && (i += " "), (i += r));
              } else for (r in t) t[r] && (i && (i += " "), (i += r));
            return i;
          })(e)) &&
          (r && (r += " "), (r += t));
      return r;
    }
    let ru = (e) => ("boolean" == typeof e ? `${e}` : 0 === e ? "0" : e),
      rc = (e, t) => (n) => {
        var r;
        if ((null == t ? void 0 : t.variants) == null)
          return rs(e, null == n ? void 0 : n.class, null == n ? void 0 : n.className);
        let { variants: i, defaultVariants: o } = t,
          l = Object.keys(i).map((e) => {
            let t = null == n ? void 0 : n[e],
              r = null == o ? void 0 : o[e];
            if (null === t) return null;
            let l = ru(t) || ru(r);
            return i[e][l];
          }),
          a =
            n &&
            Object.entries(n).reduce((e, t) => {
              let [n, r] = t;
              return (void 0 === r || (e[n] = r), e);
            }, {});
        return rs(
          e,
          l,
          null == t || null == (r = t.compoundVariants)
            ? void 0
            : r.reduce((e, t) => {
                let { class: n, className: r, ...i } = t;
                return Object.entries(i).every((e) => {
                  let [t, n] = e;
                  return Array.isArray(n) ? n.includes({ ...o, ...a }[t]) : { ...o, ...a }[t] === n;
                })
                  ? [...e, n, r]
                  : e;
              }, []),
          null == n ? void 0 : n.class,
          null == n ? void 0 : n.className,
        );
      },
      rd = (e = new Map(), t = null, n) => ({ nextPart: e, validators: t, classGroupId: n }),
      rf = [],
      rp = (e, t, n) => {
        if (0 == e.length - t) return n.classGroupId;
        let r = e[t],
          i = n.nextPart.get(r);
        if (i) {
          let n = rp(e, t + 1, i);
          if (n) return n;
        }
        let o = n.validators;
        if (null === o) return;
        let l = 0 === t ? e.join("-") : e.slice(t).join("-"),
          a = o.length;
        for (let e = 0; e < a; e++) {
          let t = o[e];
          if (t.validator(l)) return t.classGroupId;
        }
      },
      rh = (e, t) => {
        let n = rd();
        for (let r in e) rm(e[r], n, r, t);
        return n;
      },
      rm = (e, t, n, r) => {
        let i = e.length;
        for (let o = 0; o < i; o++) rg(e[o], t, n, r);
      },
      rg = (e, t, n, r) => {
        "string" == typeof e ? rv(e, t, n) : "function" == typeof e ? ry(e, t, n, r) : rb(e, t, n, r);
      },
      rv = (e, t, n) => {
        ("" === e ? t : rx(t, e)).classGroupId = n;
      },
      ry = (e, t, n, r) => {
        rk(e)
          ? rm(e(r), t, n, r)
          : (null === t.validators && (t.validators = []), t.validators.push({ classGroupId: n, validator: e }));
      },
      rb = (e, t, n, r) => {
        let i = Object.entries(e),
          o = i.length;
        for (let e = 0; e < o; e++) {
          let [o, l] = i[e];
          rm(l, rx(t, o), n, r);
        }
      },
      rx = (e, t) => {
        let n = e,
          r = t.split("-"),
          i = r.length;
        for (let e = 0; e < i; e++) {
          let t = r[e],
            i = n.nextPart.get(t);
          (i || ((i = rd()), n.nextPart.set(t, i)), (n = i));
        }
        return n;
      },
      rk = (e) => "isThemeGetter" in e && !0 === e.isThemeGetter,
      rw = [],
      rS = (e, t, n, r, i) => ({
        modifiers: e,
        hasImportantModifier: t,
        baseClassName: n,
        maybePostfixModifierPosition: r,
        isExternal: i,
      }),
      rC = /\s+/,
      rE = (e) => {
        let t;
        if ("string" == typeof e) return e;
        let n = "";
        for (let r = 0; r < e.length; r++) e[r] && (t = rE(e[r])) && (n && (n += " "), (n += t));
        return n;
      },
      rj = [],
      rR = (e) => {
        let t = (t) => t[e] || rj;
        return ((t.isThemeGetter = !0), t);
      },
      rP = /^\[(?:(\w[\w-]*):)?(.+)\]$/i,
      rT = /^\((?:(\w[\w-]*):)?(.+)\)$/i,
      rA = /^\d+(?:\.\d+)?\/\d+(?:\.\d+)?$/,
      rO = /^(\d+(\.\d+)?)?(xs|sm|md|lg|xl)$/,
      rI =
        /\d+(%|px|r?em|[sdl]?v([hwib]|min|max)|pt|pc|in|cm|mm|cap|ch|ex|r?lh|cq(w|h|i|b|min|max))|\b(calc|min|max|clamp)\(.+\)|^0$/,
      rM = /^(rgba?|hsla?|hwb|(ok)?(lab|lch)|color-mix)\(.+\)$/,
      rN = /^(inset_)?-?((\d+)?\.?(\d+)[a-z]+|0)_-?((\d+)?\.?(\d+)[a-z]+|0)/,
      rz = /^(url|image|image-set|cross-fade|element|(repeating-)?(linear|radial|conic)-gradient)\(.+\)$/,
      rD = (e) => rA.test(e),
      rL = (e) => !!e && !Number.isNaN(Number(e)),
      r$ = (e) => !!e && Number.isInteger(Number(e)),
      rF = (e) => e.endsWith("%") && rL(e.slice(0, -1)),
      r_ = (e) => rO.test(e),
      rB = () => !0,
      rH = (e) => rI.test(e) && !rM.test(e),
      rq = () => !1,
      rU = (e) => rN.test(e),
      rW = (e) => rz.test(e),
      rV = (e) => !rY(e) && !r4(e),
      rK = (e) =>
        e.startsWith("@container") &&
        (("/" === e[10] && void 0 !== e[11]) ||
          ("s" === e[11] && void 0 !== e[16] && e.startsWith("-size/", 10)) ||
          ("n" === e[11] && void 0 !== e[18] && e.startsWith("-normal/", 10))),
      rX = (e) => it(e, il, rq),
      rY = (e) => rP.test(e),
      rG = (e) => it(e, ia, rH),
      rJ = (e) => it(e, is, rL),
      rQ = (e) => it(e, ic, rB),
      rZ = (e) => it(e, iu, rq),
      r0 = (e) => it(e, ii, rq),
      r1 = (e) => it(e, io, rW),
      r2 = (e) => it(e, id, rU),
      r4 = (e) => rT.test(e),
      r5 = (e) => ir(e, ia),
      r3 = (e) => ir(e, iu),
      r6 = (e) => ir(e, ii),
      r9 = (e) => ir(e, il),
      r7 = (e) => ir(e, io),
      r8 = (e) => ir(e, id, !0),
      ie = (e) => ir(e, ic, !0),
      it = (e, t, n) => {
        let r = rP.exec(e);
        return !!r && (r[1] ? t(r[1]) : n(r[2]));
      },
      ir = (e, t, n = !1) => {
        let r = rT.exec(e);
        return !!r && (r[1] ? t(r[1]) : n);
      },
      ii = (e) => "position" === e || "percentage" === e,
      io = (e) => "image" === e || "url" === e,
      il = (e) => "length" === e || "size" === e || "bg-size" === e,
      ia = (e) => "length" === e,
      is = (e) => "number" === e,
      iu = (e) => "family-name" === e,
      ic = (e) => "number" === e || "weight" === e,
      id = (e) => "shadow" === e,
      ip =
        ((a = () => {
          let e = rR("color"),
            t = rR("font"),
            n = rR("text"),
            r = rR("font-weight"),
            i = rR("tracking"),
            o = rR("leading"),
            l = rR("breakpoint"),
            a = rR("container"),
            s = rR("spacing"),
            u = rR("radius"),
            c = rR("shadow"),
            d = rR("inset-shadow"),
            f = rR("text-shadow"),
            p = rR("drop-shadow"),
            h = rR("blur"),
            m = rR("perspective"),
            g = rR("aspect"),
            v = rR("ease"),
            y = rR("animate"),
            b = () => ["auto", "avoid", "all", "avoid-page", "page", "left", "right", "column"],
            x = () => [
              "center",
              "top",
              "bottom",
              "left",
              "right",
              "top-left",
              "left-top",
              "top-right",
              "right-top",
              "bottom-right",
              "right-bottom",
              "bottom-left",
              "left-bottom",
            ],
            k = () => [...x(), r4, rY],
            w = () => ["auto", "hidden", "clip", "visible", "scroll"],
            S = () => ["auto", "contain", "none"],
            C = () => [r4, rY, s],
            E = () => [rD, "full", "auto", ...C()],
            j = () => [r$, "none", "subgrid", r4, rY],
            R = () => ["auto", { span: ["full", r$, r4, rY] }, r$, r4, rY],
            P = () => [r$, "auto", r4, rY],
            T = () => ["auto", "min", "max", "fr", r4, rY],
            A = () => [
              "start",
              "end",
              "center",
              "between",
              "around",
              "evenly",
              "stretch",
              "baseline",
              "center-safe",
              "end-safe",
            ],
            O = () => ["start", "end", "center", "stretch", "center-safe", "end-safe"],
            I = () => ["auto", ...C()],
            M = () => [rD, "auto", "full", "dvw", "dvh", "lvw", "lvh", "svw", "svh", "min", "max", "fit", ...C()],
            N = () => [rD, "screen", "full", "dvw", "lvw", "svw", "min", "max", "fit", ...C()],
            z = () => [rD, "screen", "full", "lh", "dvh", "lvh", "svh", "min", "max", "fit", ...C()],
            D = () => [e, r4, rY],
            L = () => [...x(), r6, r0, { position: [r4, rY] }],
            $ = () => ["no-repeat", { repeat: ["", "x", "y", "space", "round"] }],
            F = () => ["auto", "cover", "contain", r9, rX, { size: [r4, rY] }],
            _ = () => [rF, r5, rG],
            B = () => ["", "none", "full", u, r4, rY],
            H = () => ["", rL, r5, rG],
            q = () => ["solid", "dashed", "dotted", "double"],
            U = () => [
              "normal",
              "multiply",
              "screen",
              "overlay",
              "darken",
              "lighten",
              "color-dodge",
              "color-burn",
              "hard-light",
              "soft-light",
              "difference",
              "exclusion",
              "hue",
              "saturation",
              "color",
              "luminosity",
            ],
            W = () => [rL, rF, r6, r0],
            V = () => ["", "none", h, r4, rY],
            K = () => ["none", rL, r4, rY],
            X = () => ["none", rL, r4, rY],
            Y = () => [rL, r4, rY],
            G = () => [rD, "full", ...C()];
          return {
            cacheSize: 500,
            theme: {
              animate: ["spin", "ping", "pulse", "bounce"],
              aspect: ["video"],
              blur: [r_],
              breakpoint: [r_],
              color: [rB],
              container: [r_],
              "drop-shadow": [r_],
              ease: ["in", "out", "in-out"],
              font: [rV],
              "font-weight": [
                "thin",
                "extralight",
                "light",
                "normal",
                "medium",
                "semibold",
                "bold",
                "extrabold",
                "black",
              ],
              "inset-shadow": [r_],
              leading: ["none", "tight", "snug", "normal", "relaxed", "loose"],
              perspective: ["dramatic", "near", "normal", "midrange", "distant", "none"],
              radius: [r_],
              shadow: [r_],
              spacing: ["px", rL],
              text: [r_],
              "text-shadow": [r_],
              tracking: ["tighter", "tight", "normal", "wide", "wider", "widest"],
            },
            classGroups: {
              aspect: [{ aspect: ["auto", "square", rD, rY, r4, g] }],
              container: ["container"],
              "container-type": [{ "@container": ["", "normal", "size", r4, rY] }],
              "container-named": [rK],
              columns: [{ columns: [rL, rY, r4, a] }],
              "break-after": [{ "break-after": b() }],
              "break-before": [{ "break-before": b() }],
              "break-inside": [{ "break-inside": ["auto", "avoid", "avoid-page", "avoid-column"] }],
              "box-decoration": [{ "box-decoration": ["slice", "clone"] }],
              box: [{ box: ["border", "content"] }],
              display: [
                "block",
                "inline-block",
                "inline",
                "flex",
                "inline-flex",
                "table",
                "inline-table",
                "table-caption",
                "table-cell",
                "table-column",
                "table-column-group",
                "table-footer-group",
                "table-header-group",
                "table-row-group",
                "table-row",
                "flow-root",
                "grid",
                "inline-grid",
                "contents",
                "list-item",
                "hidden",
              ],
              sr: ["sr-only", "not-sr-only"],
              float: [{ float: ["right", "left", "none", "start", "end"] }],
              clear: [{ clear: ["left", "right", "both", "none", "start", "end"] }],
              isolation: ["isolate", "isolation-auto"],
              "object-fit": [{ object: ["contain", "cover", "fill", "none", "scale-down"] }],
              "object-position": [{ object: k() }],
              overflow: [{ overflow: w() }],
              "overflow-x": [{ "overflow-x": w() }],
              "overflow-y": [{ "overflow-y": w() }],
              overscroll: [{ overscroll: S() }],
              "overscroll-x": [{ "overscroll-x": S() }],
              "overscroll-y": [{ "overscroll-y": S() }],
              position: ["static", "fixed", "absolute", "relative", "sticky"],
              inset: [{ inset: E() }],
              "inset-x": [{ "inset-x": E() }],
              "inset-y": [{ "inset-y": E() }],
              start: [{ "inset-s": E(), start: E() }],
              end: [{ "inset-e": E(), end: E() }],
              "inset-bs": [{ "inset-bs": E() }],
              "inset-be": [{ "inset-be": E() }],
              top: [{ top: E() }],
              right: [{ right: E() }],
              bottom: [{ bottom: E() }],
              left: [{ left: E() }],
              visibility: ["visible", "invisible", "collapse"],
              z: [{ z: [r$, "auto", r4, rY] }],
              basis: [{ basis: [rD, "full", "auto", a, ...C()] }],
              "flex-direction": [{ flex: ["row", "row-reverse", "col", "col-reverse"] }],
              "flex-wrap": [{ flex: ["nowrap", "wrap", "wrap-reverse"] }],
              flex: [{ flex: [rL, rD, "auto", "initial", "none", rY] }],
              grow: [{ grow: ["", rL, r4, rY] }],
              shrink: [{ shrink: ["", rL, r4, rY] }],
              order: [{ order: [r$, "first", "last", "none", r4, rY] }],
              "grid-cols": [{ "grid-cols": j() }],
              "col-start-end": [{ col: R() }],
              "col-start": [{ "col-start": P() }],
              "col-end": [{ "col-end": P() }],
              "grid-rows": [{ "grid-rows": j() }],
              "row-start-end": [{ row: R() }],
              "row-start": [{ "row-start": P() }],
              "row-end": [{ "row-end": P() }],
              "grid-flow": [{ "grid-flow": ["row", "col", "dense", "row-dense", "col-dense"] }],
              "auto-cols": [{ "auto-cols": T() }],
              "auto-rows": [{ "auto-rows": T() }],
              gap: [{ gap: C() }],
              "gap-x": [{ "gap-x": C() }],
              "gap-y": [{ "gap-y": C() }],
              "justify-content": [{ justify: [...A(), "normal"] }],
              "justify-items": [{ "justify-items": [...O(), "normal"] }],
              "justify-self": [{ "justify-self": ["auto", ...O()] }],
              "align-content": [{ content: ["normal", ...A()] }],
              "align-items": [{ items: [...O(), { baseline: ["", "last"] }] }],
              "align-self": [{ self: ["auto", ...O(), { baseline: ["", "last"] }] }],
              "place-content": [{ "place-content": A() }],
              "place-items": [{ "place-items": [...O(), "baseline"] }],
              "place-self": [{ "place-self": ["auto", ...O()] }],
              p: [{ p: C() }],
              px: [{ px: C() }],
              py: [{ py: C() }],
              ps: [{ ps: C() }],
              pe: [{ pe: C() }],
              pbs: [{ pbs: C() }],
              pbe: [{ pbe: C() }],
              pt: [{ pt: C() }],
              pr: [{ pr: C() }],
              pb: [{ pb: C() }],
              pl: [{ pl: C() }],
              m: [{ m: I() }],
              mx: [{ mx: I() }],
              my: [{ my: I() }],
              ms: [{ ms: I() }],
              me: [{ me: I() }],
              mbs: [{ mbs: I() }],
              mbe: [{ mbe: I() }],
              mt: [{ mt: I() }],
              mr: [{ mr: I() }],
              mb: [{ mb: I() }],
              ml: [{ ml: I() }],
              "space-x": [{ "space-x": C() }],
              "space-x-reverse": ["space-x-reverse"],
              "space-y": [{ "space-y": C() }],
              "space-y-reverse": ["space-y-reverse"],
              size: [{ size: M() }],
              "inline-size": [{ inline: ["auto", ...N()] }],
              "min-inline-size": [{ "min-inline": ["auto", ...N()] }],
              "max-inline-size": [{ "max-inline": ["none", ...N()] }],
              "block-size": [{ block: ["auto", ...z()] }],
              "min-block-size": [{ "min-block": ["auto", ...z()] }],
              "max-block-size": [{ "max-block": ["none", ...z()] }],
              w: [{ w: [a, "screen", ...M()] }],
              "min-w": [{ "min-w": [a, "screen", "none", ...M()] }],
              "max-w": [{ "max-w": [a, "screen", "none", "prose", { screen: [l] }, ...M()] }],
              h: [{ h: ["screen", "lh", ...M()] }],
              "min-h": [{ "min-h": ["screen", "lh", "none", ...M()] }],
              "max-h": [{ "max-h": ["screen", "lh", ...M()] }],
              "font-size": [{ text: ["base", n, r5, rG] }],
              "font-smoothing": ["antialiased", "subpixel-antialiased"],
              "font-style": ["italic", "not-italic"],
              "font-weight": [{ font: [r, ie, rQ] }],
              "font-stretch": [
                {
                  "font-stretch": [
                    "ultra-condensed",
                    "extra-condensed",
                    "condensed",
                    "semi-condensed",
                    "normal",
                    "semi-expanded",
                    "expanded",
                    "extra-expanded",
                    "ultra-expanded",
                    rF,
                    rY,
                  ],
                },
              ],
              "font-family": [{ font: [r3, rZ, t] }],
              "font-features": [{ "font-features": [rY] }],
              "fvn-normal": ["normal-nums"],
              "fvn-ordinal": ["ordinal"],
              "fvn-slashed-zero": ["slashed-zero"],
              "fvn-figure": ["lining-nums", "oldstyle-nums"],
              "fvn-spacing": ["proportional-nums", "tabular-nums"],
              "fvn-fraction": ["diagonal-fractions", "stacked-fractions"],
              tracking: [{ tracking: [i, r4, rY] }],
              "line-clamp": [{ "line-clamp": [rL, "none", r4, rJ] }],
              leading: [{ leading: [o, ...C()] }],
              "list-image": [{ "list-image": ["none", r4, rY] }],
              "list-style-position": [{ list: ["inside", "outside"] }],
              "list-style-type": [{ list: ["disc", "decimal", "none", r4, rY] }],
              "text-alignment": [{ text: ["left", "center", "right", "justify", "start", "end"] }],
              "placeholder-color": [{ placeholder: D() }],
              "text-color": [{ text: D() }],
              "text-decoration": ["underline", "overline", "line-through", "no-underline"],
              "text-decoration-style": [{ decoration: [...q(), "wavy"] }],
              "text-decoration-thickness": [{ decoration: [rL, "from-font", "auto", r4, rG] }],
              "text-decoration-color": [{ decoration: D() }],
              "underline-offset": [{ "underline-offset": [rL, "auto", r4, rY] }],
              "text-transform": ["uppercase", "lowercase", "capitalize", "normal-case"],
              "text-overflow": ["truncate", "text-ellipsis", "text-clip"],
              "text-wrap": [{ text: ["wrap", "nowrap", "balance", "pretty"] }],
              indent: [{ indent: C() }],
              "tab-size": [{ tab: [r$, r4, rY] }],
              "vertical-align": [
                { align: ["baseline", "top", "middle", "bottom", "text-top", "text-bottom", "sub", "super", r4, rY] },
              ],
              whitespace: [{ whitespace: ["normal", "nowrap", "pre", "pre-line", "pre-wrap", "break-spaces"] }],
              break: [{ break: ["normal", "words", "all", "keep"] }],
              wrap: [{ wrap: ["break-word", "anywhere", "normal"] }],
              hyphens: [{ hyphens: ["none", "manual", "auto"] }],
              content: [{ content: ["none", r4, rY] }],
              "bg-attachment": [{ bg: ["fixed", "local", "scroll"] }],
              "bg-clip": [{ "bg-clip": ["border", "padding", "content", "text"] }],
              "bg-origin": [{ "bg-origin": ["border", "padding", "content"] }],
              "bg-position": [{ bg: L() }],
              "bg-repeat": [{ bg: $() }],
              "bg-size": [{ bg: F() }],
              "bg-image": [
                {
                  bg: [
                    "none",
                    {
                      linear: [{ to: ["t", "tr", "r", "br", "b", "bl", "l", "tl"] }, r$, r4, rY],
                      radial: ["", r4, rY],
                      conic: [r$, r4, rY],
                    },
                    r7,
                    r1,
                  ],
                },
              ],
              "bg-color": [{ bg: D() }],
              "gradient-from-pos": [{ from: _() }],
              "gradient-via-pos": [{ via: _() }],
              "gradient-to-pos": [{ to: _() }],
              "gradient-from": [{ from: D() }],
              "gradient-via": [{ via: D() }],
              "gradient-to": [{ to: D() }],
              rounded: [{ rounded: B() }],
              "rounded-s": [{ "rounded-s": B() }],
              "rounded-e": [{ "rounded-e": B() }],
              "rounded-t": [{ "rounded-t": B() }],
              "rounded-r": [{ "rounded-r": B() }],
              "rounded-b": [{ "rounded-b": B() }],
              "rounded-l": [{ "rounded-l": B() }],
              "rounded-ss": [{ "rounded-ss": B() }],
              "rounded-se": [{ "rounded-se": B() }],
              "rounded-ee": [{ "rounded-ee": B() }],
              "rounded-es": [{ "rounded-es": B() }],
              "rounded-tl": [{ "rounded-tl": B() }],
              "rounded-tr": [{ "rounded-tr": B() }],
              "rounded-br": [{ "rounded-br": B() }],
              "rounded-bl": [{ "rounded-bl": B() }],
              "border-w": [{ border: H() }],
              "border-w-x": [{ "border-x": H() }],
              "border-w-y": [{ "border-y": H() }],
              "border-w-s": [{ "border-s": H() }],
              "border-w-e": [{ "border-e": H() }],
              "border-w-bs": [{ "border-bs": H() }],
              "border-w-be": [{ "border-be": H() }],
              "border-w-t": [{ "border-t": H() }],
              "border-w-r": [{ "border-r": H() }],
              "border-w-b": [{ "border-b": H() }],
              "border-w-l": [{ "border-l": H() }],
              "divide-x": [{ "divide-x": H() }],
              "divide-x-reverse": ["divide-x-reverse"],
              "divide-y": [{ "divide-y": H() }],
              "divide-y-reverse": ["divide-y-reverse"],
              "border-style": [{ border: [...q(), "hidden", "none"] }],
              "divide-style": [{ divide: [...q(), "hidden", "none"] }],
              "border-color": [{ border: D() }],
              "border-color-x": [{ "border-x": D() }],
              "border-color-y": [{ "border-y": D() }],
              "border-color-s": [{ "border-s": D() }],
              "border-color-e": [{ "border-e": D() }],
              "border-color-bs": [{ "border-bs": D() }],
              "border-color-be": [{ "border-be": D() }],
              "border-color-t": [{ "border-t": D() }],
              "border-color-r": [{ "border-r": D() }],
              "border-color-b": [{ "border-b": D() }],
              "border-color-l": [{ "border-l": D() }],
              "divide-color": [{ divide: D() }],
              "outline-style": [{ outline: [...q(), "none", "hidden"] }],
              "outline-offset": [{ "outline-offset": [rL, r4, rY] }],
              "outline-w": [{ outline: ["", rL, r5, rG] }],
              "outline-color": [{ outline: D() }],
              shadow: [{ shadow: ["", "none", c, r8, r2] }],
              "shadow-color": [{ shadow: D() }],
              "inset-shadow": [{ "inset-shadow": ["none", d, r8, r2] }],
              "inset-shadow-color": [{ "inset-shadow": D() }],
              "ring-w": [{ ring: H() }],
              "ring-w-inset": ["ring-inset"],
              "ring-color": [{ ring: D() }],
              "ring-offset-w": [{ "ring-offset": [rL, rG] }],
              "ring-offset-color": [{ "ring-offset": D() }],
              "inset-ring-w": [{ "inset-ring": H() }],
              "inset-ring-color": [{ "inset-ring": D() }],
              "text-shadow": [{ "text-shadow": ["none", f, r8, r2] }],
              "text-shadow-color": [{ "text-shadow": D() }],
              opacity: [{ opacity: [rL, r4, rY] }],
              "mix-blend": [{ "mix-blend": [...U(), "plus-darker", "plus-lighter"] }],
              "bg-blend": [{ "bg-blend": U() }],
              "mask-clip": [
                { "mask-clip": ["border", "padding", "content", "fill", "stroke", "view"] },
                "mask-no-clip",
              ],
              "mask-composite": [{ mask: ["add", "subtract", "intersect", "exclude"] }],
              "mask-image-linear-pos": [{ "mask-linear": [rL] }],
              "mask-image-linear-from-pos": [{ "mask-linear-from": W() }],
              "mask-image-linear-to-pos": [{ "mask-linear-to": W() }],
              "mask-image-linear-from-color": [{ "mask-linear-from": D() }],
              "mask-image-linear-to-color": [{ "mask-linear-to": D() }],
              "mask-image-t-from-pos": [{ "mask-t-from": W() }],
              "mask-image-t-to-pos": [{ "mask-t-to": W() }],
              "mask-image-t-from-color": [{ "mask-t-from": D() }],
              "mask-image-t-to-color": [{ "mask-t-to": D() }],
              "mask-image-r-from-pos": [{ "mask-r-from": W() }],
              "mask-image-r-to-pos": [{ "mask-r-to": W() }],
              "mask-image-r-from-color": [{ "mask-r-from": D() }],
              "mask-image-r-to-color": [{ "mask-r-to": D() }],
              "mask-image-b-from-pos": [{ "mask-b-from": W() }],
              "mask-image-b-to-pos": [{ "mask-b-to": W() }],
              "mask-image-b-from-color": [{ "mask-b-from": D() }],
              "mask-image-b-to-color": [{ "mask-b-to": D() }],
              "mask-image-l-from-pos": [{ "mask-l-from": W() }],
              "mask-image-l-to-pos": [{ "mask-l-to": W() }],
              "mask-image-l-from-color": [{ "mask-l-from": D() }],
              "mask-image-l-to-color": [{ "mask-l-to": D() }],
              "mask-image-x-from-pos": [{ "mask-x-from": W() }],
              "mask-image-x-to-pos": [{ "mask-x-to": W() }],
              "mask-image-x-from-color": [{ "mask-x-from": D() }],
              "mask-image-x-to-color": [{ "mask-x-to": D() }],
              "mask-image-y-from-pos": [{ "mask-y-from": W() }],
              "mask-image-y-to-pos": [{ "mask-y-to": W() }],
              "mask-image-y-from-color": [{ "mask-y-from": D() }],
              "mask-image-y-to-color": [{ "mask-y-to": D() }],
              "mask-image-radial": [{ "mask-radial": [r4, rY] }],
              "mask-image-radial-from-pos": [{ "mask-radial-from": W() }],
              "mask-image-radial-to-pos": [{ "mask-radial-to": W() }],
              "mask-image-radial-from-color": [{ "mask-radial-from": D() }],
              "mask-image-radial-to-color": [{ "mask-radial-to": D() }],
              "mask-image-radial-shape": [{ "mask-radial": ["circle", "ellipse"] }],
              "mask-image-radial-size": [
                { "mask-radial": [{ closest: ["side", "corner"], farthest: ["side", "corner"] }] },
              ],
              "mask-image-radial-pos": [{ "mask-radial-at": x() }],
              "mask-image-conic-pos": [{ "mask-conic": [rL] }],
              "mask-image-conic-from-pos": [{ "mask-conic-from": W() }],
              "mask-image-conic-to-pos": [{ "mask-conic-to": W() }],
              "mask-image-conic-from-color": [{ "mask-conic-from": D() }],
              "mask-image-conic-to-color": [{ "mask-conic-to": D() }],
              "mask-mode": [{ mask: ["alpha", "luminance", "match"] }],
              "mask-origin": [{ "mask-origin": ["border", "padding", "content", "fill", "stroke", "view"] }],
              "mask-position": [{ mask: L() }],
              "mask-repeat": [{ mask: $() }],
              "mask-size": [{ mask: F() }],
              "mask-type": [{ "mask-type": ["alpha", "luminance"] }],
              "mask-image": [{ mask: ["none", r4, rY] }],
              filter: [{ filter: ["", "none", r4, rY] }],
              blur: [{ blur: V() }],
              brightness: [{ brightness: [rL, r4, rY] }],
              contrast: [{ contrast: [rL, r4, rY] }],
              "drop-shadow": [{ "drop-shadow": ["", "none", p, r8, r2] }],
              "drop-shadow-color": [{ "drop-shadow": D() }],
              grayscale: [{ grayscale: ["", rL, r4, rY] }],
              "hue-rotate": [{ "hue-rotate": [rL, r4, rY] }],
              invert: [{ invert: ["", rL, r4, rY] }],
              saturate: [{ saturate: [rL, r4, rY] }],
              sepia: [{ sepia: ["", rL, r4, rY] }],
              "backdrop-filter": [{ "backdrop-filter": ["", "none", r4, rY] }],
              "backdrop-blur": [{ "backdrop-blur": V() }],
              "backdrop-brightness": [{ "backdrop-brightness": [rL, r4, rY] }],
              "backdrop-contrast": [{ "backdrop-contrast": [rL, r4, rY] }],
              "backdrop-grayscale": [{ "backdrop-grayscale": ["", rL, r4, rY] }],
              "backdrop-hue-rotate": [{ "backdrop-hue-rotate": [rL, r4, rY] }],
              "backdrop-invert": [{ "backdrop-invert": ["", rL, r4, rY] }],
              "backdrop-opacity": [{ "backdrop-opacity": [rL, r4, rY] }],
              "backdrop-saturate": [{ "backdrop-saturate": [rL, r4, rY] }],
              "backdrop-sepia": [{ "backdrop-sepia": ["", rL, r4, rY] }],
              "border-collapse": [{ border: ["collapse", "separate"] }],
              "border-spacing": [{ "border-spacing": C() }],
              "border-spacing-x": [{ "border-spacing-x": C() }],
              "border-spacing-y": [{ "border-spacing-y": C() }],
              "table-layout": [{ table: ["auto", "fixed"] }],
              caption: [{ caption: ["top", "bottom"] }],
              transition: [{ transition: ["", "all", "colors", "opacity", "shadow", "transform", "none", r4, rY] }],
              "transition-behavior": [{ transition: ["normal", "discrete"] }],
              duration: [{ duration: [rL, "initial", r4, rY] }],
              ease: [{ ease: ["linear", "initial", v, r4, rY] }],
              delay: [{ delay: [rL, r4, rY] }],
              animate: [{ animate: ["none", y, r4, rY] }],
              backface: [{ backface: ["hidden", "visible"] }],
              perspective: [{ perspective: [m, r4, rY] }],
              "perspective-origin": [{ "perspective-origin": k() }],
              rotate: [{ rotate: K() }],
              "rotate-x": [{ "rotate-x": K() }],
              "rotate-y": [{ "rotate-y": K() }],
              "rotate-z": [{ "rotate-z": K() }],
              scale: [{ scale: X() }],
              "scale-x": [{ "scale-x": X() }],
              "scale-y": [{ "scale-y": X() }],
              "scale-z": [{ "scale-z": X() }],
              "scale-3d": ["scale-3d"],
              skew: [{ skew: Y() }],
              "skew-x": [{ "skew-x": Y() }],
              "skew-y": [{ "skew-y": Y() }],
              transform: [{ transform: [r4, rY, "", "none", "gpu", "cpu"] }],
              "transform-origin": [{ origin: k() }],
              "transform-style": [{ transform: ["3d", "flat"] }],
              translate: [{ translate: G() }],
              "translate-x": [{ "translate-x": G() }],
              "translate-y": [{ "translate-y": G() }],
              "translate-z": [{ "translate-z": G() }],
              "translate-none": ["translate-none"],
              zoom: [{ zoom: [r$, r4, rY] }],
              accent: [{ accent: D() }],
              appearance: [{ appearance: ["none", "auto"] }],
              "caret-color": [{ caret: D() }],
              "color-scheme": [{ scheme: ["normal", "dark", "light", "light-dark", "only-dark", "only-light"] }],
              cursor: [
                {
                  cursor: [
                    "auto",
                    "default",
                    "pointer",
                    "wait",
                    "text",
                    "move",
                    "help",
                    "not-allowed",
                    "none",
                    "context-menu",
                    "progress",
                    "cell",
                    "crosshair",
                    "vertical-text",
                    "alias",
                    "copy",
                    "no-drop",
                    "grab",
                    "grabbing",
                    "all-scroll",
                    "col-resize",
                    "row-resize",
                    "n-resize",
                    "e-resize",
                    "s-resize",
                    "w-resize",
                    "ne-resize",
                    "nw-resize",
                    "se-resize",
                    "sw-resize",
                    "ew-resize",
                    "ns-resize",
                    "nesw-resize",
                    "nwse-resize",
                    "zoom-in",
                    "zoom-out",
                    r4,
                    rY,
                  ],
                },
              ],
              "field-sizing": [{ "field-sizing": ["fixed", "content"] }],
              "pointer-events": [{ "pointer-events": ["auto", "none"] }],
              resize: [{ resize: ["none", "", "y", "x"] }],
              "scroll-behavior": [{ scroll: ["auto", "smooth"] }],
              "scrollbar-thumb-color": [{ "scrollbar-thumb": D() }],
              "scrollbar-track-color": [{ "scrollbar-track": D() }],
              "scrollbar-gutter": [{ "scrollbar-gutter": ["auto", "stable", "both"] }],
              "scrollbar-w": [{ scrollbar: ["auto", "thin", "none"] }],
              "scroll-m": [{ "scroll-m": C() }],
              "scroll-mx": [{ "scroll-mx": C() }],
              "scroll-my": [{ "scroll-my": C() }],
              "scroll-ms": [{ "scroll-ms": C() }],
              "scroll-me": [{ "scroll-me": C() }],
              "scroll-mbs": [{ "scroll-mbs": C() }],
              "scroll-mbe": [{ "scroll-mbe": C() }],
              "scroll-mt": [{ "scroll-mt": C() }],
              "scroll-mr": [{ "scroll-mr": C() }],
              "scroll-mb": [{ "scroll-mb": C() }],
              "scroll-ml": [{ "scroll-ml": C() }],
              "scroll-p": [{ "scroll-p": C() }],
              "scroll-px": [{ "scroll-px": C() }],
              "scroll-py": [{ "scroll-py": C() }],
              "scroll-ps": [{ "scroll-ps": C() }],
              "scroll-pe": [{ "scroll-pe": C() }],
              "scroll-pbs": [{ "scroll-pbs": C() }],
              "scroll-pbe": [{ "scroll-pbe": C() }],
              "scroll-pt": [{ "scroll-pt": C() }],
              "scroll-pr": [{ "scroll-pr": C() }],
              "scroll-pb": [{ "scroll-pb": C() }],
              "scroll-pl": [{ "scroll-pl": C() }],
              "snap-align": [{ snap: ["start", "end", "center", "align-none"] }],
              "snap-stop": [{ snap: ["normal", "always"] }],
              "snap-type": [{ snap: ["none", "x", "y", "both"] }],
              "snap-strictness": [{ snap: ["mandatory", "proximity"] }],
              touch: [{ touch: ["auto", "none", "manipulation"] }],
              "touch-x": [{ "touch-pan": ["x", "left", "right"] }],
              "touch-y": [{ "touch-pan": ["y", "up", "down"] }],
              "touch-pz": ["touch-pinch-zoom"],
              select: [{ select: ["none", "text", "all", "auto"] }],
              "will-change": [{ "will-change": ["auto", "scroll", "contents", "transform", r4, rY] }],
              fill: [{ fill: ["none", ...D()] }],
              "stroke-w": [{ stroke: [rL, r5, rG, rJ] }],
              stroke: [{ stroke: ["none", ...D()] }],
              "forced-color-adjust": [{ "forced-color-adjust": ["auto", "none"] }],
            },
            conflictingClassGroups: {
              "container-named": ["container-type"],
              overflow: ["overflow-x", "overflow-y"],
              overscroll: ["overscroll-x", "overscroll-y"],
              inset: ["inset-x", "inset-y", "inset-bs", "inset-be", "start", "end", "top", "right", "bottom", "left"],
              "inset-x": ["right", "left"],
              "inset-y": ["top", "bottom"],
              flex: ["basis", "grow", "shrink"],
              gap: ["gap-x", "gap-y"],
              p: ["px", "py", "ps", "pe", "pbs", "pbe", "pt", "pr", "pb", "pl"],
              px: ["pr", "pl"],
              py: ["pt", "pb"],
              m: ["mx", "my", "ms", "me", "mbs", "mbe", "mt", "mr", "mb", "ml"],
              mx: ["mr", "ml"],
              my: ["mt", "mb"],
              size: ["w", "h"],
              "font-size": ["leading"],
              "fvn-normal": ["fvn-ordinal", "fvn-slashed-zero", "fvn-figure", "fvn-spacing", "fvn-fraction"],
              "fvn-ordinal": ["fvn-normal"],
              "fvn-slashed-zero": ["fvn-normal"],
              "fvn-figure": ["fvn-normal"],
              "fvn-spacing": ["fvn-normal"],
              "fvn-fraction": ["fvn-normal"],
              "line-clamp": ["display", "overflow"],
              rounded: [
                "rounded-s",
                "rounded-e",
                "rounded-t",
                "rounded-r",
                "rounded-b",
                "rounded-l",
                "rounded-ss",
                "rounded-se",
                "rounded-ee",
                "rounded-es",
                "rounded-tl",
                "rounded-tr",
                "rounded-br",
                "rounded-bl",
              ],
              "rounded-s": ["rounded-ss", "rounded-es"],
              "rounded-e": ["rounded-se", "rounded-ee"],
              "rounded-t": ["rounded-tl", "rounded-tr"],
              "rounded-r": ["rounded-tr", "rounded-br"],
              "rounded-b": ["rounded-br", "rounded-bl"],
              "rounded-l": ["rounded-tl", "rounded-bl"],
              "border-spacing": ["border-spacing-x", "border-spacing-y"],
              "border-w": [
                "border-w-x",
                "border-w-y",
                "border-w-s",
                "border-w-e",
                "border-w-bs",
                "border-w-be",
                "border-w-t",
                "border-w-r",
                "border-w-b",
                "border-w-l",
              ],
              "border-w-x": ["border-w-r", "border-w-l"],
              "border-w-y": ["border-w-t", "border-w-b"],
              "border-color": [
                "border-color-x",
                "border-color-y",
                "border-color-s",
                "border-color-e",
                "border-color-bs",
                "border-color-be",
                "border-color-t",
                "border-color-r",
                "border-color-b",
                "border-color-l",
              ],
              "border-color-x": ["border-color-r", "border-color-l"],
              "border-color-y": ["border-color-t", "border-color-b"],
              translate: ["translate-x", "translate-y", "translate-none"],
              "translate-none": ["translate", "translate-x", "translate-y", "translate-z"],
              "scroll-m": [
                "scroll-mx",
                "scroll-my",
                "scroll-ms",
                "scroll-me",
                "scroll-mbs",
                "scroll-mbe",
                "scroll-mt",
                "scroll-mr",
                "scroll-mb",
                "scroll-ml",
              ],
              "scroll-mx": ["scroll-mr", "scroll-ml"],
              "scroll-my": ["scroll-mt", "scroll-mb"],
              "scroll-p": [
                "scroll-px",
                "scroll-py",
                "scroll-ps",
                "scroll-pe",
                "scroll-pbs",
                "scroll-pbe",
                "scroll-pt",
                "scroll-pr",
                "scroll-pb",
                "scroll-pl",
              ],
              "scroll-px": ["scroll-pr", "scroll-pl"],
              "scroll-py": ["scroll-pt", "scroll-pb"],
              touch: ["touch-x", "touch-y", "touch-pz"],
              "touch-x": ["touch"],
              "touch-y": ["touch"],
              "touch-pz": ["touch"],
            },
            conflictingClassGroupModifiers: { "font-size": ["leading"] },
            postfixLookupClassGroups: ["container-type"],
            orderSensitiveModifiers: [
              "*",
              "**",
              "after",
              "backdrop",
              "before",
              "details-content",
              "file",
              "first-letter",
              "first-line",
              "marker",
              "placeholder",
              "selection",
            ],
          };
        }),
        (o = (e) => {
          let i = n(e);
          if (i) return i;
          let o = ((e, t) => {
            let {
                parseClassName: n,
                getClassGroupId: r,
                getConflictingClassGroupIds: i,
                sortModifiers: o,
                postfixLookupClassGroupIds: l,
              } = t,
              a = [],
              s = e.trim().split(rC),
              u = "";
            for (let e = s.length - 1; e >= 0; e -= 1) {
              let t,
                c = s[e],
                {
                  isExternal: d,
                  modifiers: f,
                  hasImportantModifier: p,
                  baseClassName: h,
                  maybePostfixModifierPosition: m,
                } = n(c);
              if (d) {
                u = c + (u.length > 0 ? " " + u : u);
                continue;
              }
              let g = !!m;
              if (g) {
                let e = (t = r(h.substring(0, m))) && l[t] ? r(h) : void 0;
                e && e !== t && ((t = e), (g = !1));
              } else t = r(h);
              if (!t) {
                if (!g || !(t = r(h))) {
                  u = c + (u.length > 0 ? " " + u : u);
                  continue;
                }
                g = !1;
              }
              let v = 0 === f.length ? "" : 1 === f.length ? f[0] : o(f).join(":"),
                y = p ? v + "!" : v,
                b = y + t;
              if (a.indexOf(b) > -1) continue;
              a.push(b);
              let x = i(t, g);
              for (let e = 0; e < x.length; ++e) {
                let t = x[e];
                a.push(y + t);
              }
              u = c + (u.length > 0 ? " " + u : u);
            }
            return u;
          })(e, t);
          return (r(e, o), o);
        }),
        (i = (e) => {
          var l;
          let s;
          return (
            (n = (t = {
              cache: ((e) => {
                if (e < 1) return { get: () => void 0, set: () => {} };
                let t = 0,
                  n = Object.create(null),
                  r = Object.create(null),
                  i = (i, o) => {
                    ((n[i] = o), ++t > e && ((t = 0), (r = n), (n = Object.create(null))));
                  };
                return {
                  get(e) {
                    let t = n[e];
                    return void 0 !== t ? t : void 0 !== (t = r[e]) ? (i(e, t), t) : void 0;
                  },
                  set(e, t) {
                    e in n ? (n[e] = t) : i(e, t);
                  },
                };
              })((l = [].reduce((e, t) => t(e), a())).cacheSize),
              parseClassName: ((e) => {
                let { prefix: t, experimentalParseClassName: n } = e,
                  r = (e) => {
                    let t,
                      n = [],
                      r = 0,
                      i = 0,
                      o = 0,
                      l = e.length;
                    for (let a = 0; a < l; a++) {
                      let l = e[a];
                      if (0 === r && 0 === i) {
                        if (":" === l) {
                          (n.push(e.slice(o, a)), (o = a + 1));
                          continue;
                        }
                        if ("/" === l) {
                          t = a;
                          continue;
                        }
                      }
                      "[" === l ? r++ : "]" === l ? r-- : "(" === l ? i++ : ")" === l && i--;
                    }
                    let a = 0 === n.length ? e : e.slice(o),
                      s = a,
                      u = !1;
                    return (
                      a.endsWith("!")
                        ? ((s = a.slice(0, -1)), (u = !0))
                        : a.startsWith("!") && ((s = a.slice(1)), (u = !0)),
                      rS(n, u, s, t && t > o ? t - o : void 0)
                    );
                  };
                if (t) {
                  let e = t + ":",
                    n = r;
                  r = (t) => (t.startsWith(e) ? n(t.slice(e.length)) : rS(rw, !1, t, void 0, !0));
                }
                if (n) {
                  let e = r;
                  r = (t) => n({ className: t, parseClassName: e });
                }
                return r;
              })(l),
              sortModifiers:
                ((s = new Map()),
                l.orderSensitiveModifiers.forEach((e, t) => {
                  s.set(e, 1e6 + t);
                }),
                (e) => {
                  let t = [],
                    n = [];
                  for (let r = 0; r < e.length; r++) {
                    let i = e[r],
                      o = "[" === i[0],
                      l = s.has(i);
                    o || l ? (n.length > 0 && (n.sort(), t.push(...n), (n = [])), t.push(i)) : n.push(i);
                  }
                  return (n.length > 0 && (n.sort(), t.push(...n)), t);
                }),
              postfixLookupClassGroupIds: ((e) => {
                let t = Object.create(null),
                  n = e.postfixLookupClassGroups;
                if (n) for (let e = 0; e < n.length; e++) t[n[e]] = !0;
                return t;
              })(l),
              ...((e) => {
                let t = ((e) => {
                    let { theme: t, classGroups: n } = e;
                    return rh(n, t);
                  })(e),
                  { conflictingClassGroups: n, conflictingClassGroupModifiers: r } = e;
                return {
                  getClassGroupId: (e) => {
                    if (e.startsWith("[") && e.endsWith("]")) {
                      var n;
                      let t, r, i;
                      return -1 === (n = e).slice(1, -1).indexOf(":")
                        ? void 0
                        : ((r = (t = n.slice(1, -1)).indexOf(":")), (i = t.slice(0, r)) ? "arbitrary.." + i : void 0);
                    }
                    let r = e.split("-"),
                      i = +("" === r[0] && r.length > 1);
                    return rp(r, i, t);
                  },
                  getConflictingClassGroupIds: (e, t) => {
                    if (t) {
                      let t = r[e],
                        i = n[e];
                      if (t) {
                        if (i) {
                          let e = Array(i.length + t.length);
                          for (let t = 0; t < i.length; t++) e[t] = i[t];
                          for (let n = 0; n < t.length; n++) e[i.length + n] = t[n];
                          return e;
                        }
                        return t;
                      }
                      return i || rf;
                    }
                    return n[e] || rf;
                  },
                };
              })(l),
            }).cache.get),
            (r = t.cache.set),
            (i = o),
            o(e)
          );
        }),
        (...e) =>
          i(
            ((...e) => {
              let t,
                n,
                r = 0,
                i = "";
              for (; r < e.length; ) (t = e[r++]) && (n = rE(t)) && (i && (i += " "), (i += n));
              return i;
            })(...e),
          ));
    function ih(...e) {
      return ip(rs(e));
    }
    let im = rc(
      "group/badge inline-flex h-5 w-fit shrink-0 items-center justify-center gap-1 overflow-hidden rounded-4xl border border-transparent px-2 py-0.5 text-xs font-medium whitespace-nowrap transition-all focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 has-data-[icon=inline-end]:pr-1.5 has-data-[icon=inline-start]:pl-1.5 aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 [&>svg]:pointer-events-none [&>svg]:size-3!",
      {
        variants: {
          variant: {
            default: "bg-primary text-primary-foreground [a]:hover:bg-primary/80",
            secondary: "bg-secondary text-secondary-foreground [a]:hover:bg-secondary/80",
            destructive:
              "bg-destructive/10 text-destructive focus-visible:ring-destructive/20 dark:bg-destructive/20 dark:focus-visible:ring-destructive/40 [a]:hover:bg-destructive/20",
            outline: "border-border text-foreground [a]:hover:bg-muted [a]:hover:text-muted-foreground",
            ghost: "hover:bg-muted hover:text-muted-foreground dark:hover:bg-muted/50",
            link: "text-primary underline-offset-4 hover:underline",
          },
        },
        defaultVariants: { variant: "default" },
      },
    );
    function ig({ className: e, variant: t = "default", render: n, ...r }) {
      var i;
      return rl(
        (i = {
          defaultTagName: "span",
          props: nY({ className: ih(im({ variant: t }), e) }, r),
          render: n,
          state: { slot: "badge", variant: t },
        }).defaultTagName ?? "div",
        i,
        i,
      );
    }
    function iv() {
      return "u" > typeof window;
    }
    function iy(e) {
      return ix(e) ? (e.nodeName || "").toLowerCase() : "#document";
    }
    function ib(e) {
      var t;
      return (null == e || null == (t = e.ownerDocument) ? void 0 : t.defaultView) || window;
    }
    function ix(e) {
      return !!iv() && (e instanceof Node || e instanceof ib(e).Node);
    }
    function ik(e) {
      return !!iv() && (e instanceof Element || e instanceof ib(e).Element);
    }
    function iw(e) {
      return !!iv() && (e instanceof HTMLElement || e instanceof ib(e).HTMLElement);
    }
    function iS(e) {
      return !(!iv() || "u" < typeof ShadowRoot) && (e instanceof ShadowRoot || e instanceof ib(e).ShadowRoot);
    }
    function iC(e) {
      return /^(html|body|#document)$/.test(iy(e));
    }
    function iE(e) {
      return ib(e).getComputedStyle(e);
    }
    let ij = { ...f },
      iR = ij.useInsertionEffect,
      iP = iR && iR !== ij.useLayoutEffect ? iR : (e) => e();
    function iT(e) {
      let t = n9(iA).current;
      return ((t.next = e), iP(t.effect), t.trampoline);
    }
    function iA() {
      let e = {
        next: void 0,
        callback: iO,
        trampoline: (...t) => e.callback?.(...t),
        effect: () => {
          e.callback = e.next;
        },
      };
      return e;
    }
    function iO() {}
    let iI = "u" > typeof document ? f.useLayoutEffect : () => {},
      iM = f.createContext(void 0);
    function iN(e = !1) {
      let t = f.useContext(iM);
      if (void 0 === t && !e) throw Error(n3(16));
      return t;
    }
    function iz(e, t, { detail: n = 0 } = {}) {
      e.dispatchEvent(
        new (ib(e).PointerEvent)("click", {
          bubbles: !0,
          cancelable: !0,
          composed: !0,
          detail: n,
          shiftKey: t.shiftKey,
          ctrlKey: t.ctrlKey,
          altKey: t.altKey,
          metaKey: t.metaKey,
        }),
      );
    }
    function iD(e = {}) {
      let { disabled: t = !1, focusableWhenDisabled: n, tabIndex: r = 0, native: i = !0, composite: o } = e,
        l = f.useRef(null),
        a = iN(!0),
        s = o ?? void 0 !== a,
        { props: u } = (function (e) {
          let { focusableWhenDisabled: t, disabled: n, composite: r = !1, tabIndex: i = 0, isNativeButton: o } = e,
            l = r && !1 !== t,
            a = r && !1 === t;
          return {
            props: f.useMemo(() => {
              let e = {
                onKeyDown(e) {
                  n && t && "Tab" !== e.key && e.preventDefault();
                },
              };
              return (
                r || ((e.tabIndex = i), !o && n && (e.tabIndex = t ? i : -1)),
                ((o && (t || l)) || (!o && n)) && (e["aria-disabled"] = n),
                o && (!t || a) && (e.disabled = n),
                e
              );
            }, [r, n, t, l, a, o, i]),
          };
        })({ focusableWhenDisabled: n, disabled: t, composite: s, tabIndex: r, isNativeButton: i }),
        c = f.useCallback(() => {
          let e = l.current;
          iL(e) && s && t && void 0 === u.disabled && e.disabled && (e.disabled = !1);
        }, [t, u.disabled, s]);
      return (
        iI(c, [c]),
        {
          getButtonProps: f.useCallback(
            (e = {}) => {
              let { onClick: n, onMouseDown: r, onKeyUp: o, onKeyDown: l, onPointerDown: a, ...c } = e;
              return nY(
                {
                  onClick(e) {
                    t ? e.preventDefault() : n?.(e);
                  },
                  onMouseDown(e) {
                    t || r?.(e);
                  },
                  onKeyDown(e) {
                    var n;
                    if (t || (n2(e), l?.(e), e.baseUIHandlerPrevented)) return;
                    let r = e.target === e.currentTarget,
                      o = e.currentTarget,
                      a = iL(o),
                      u = !i && iw((n = o)) && "A" === n.tagName && !!n.href,
                      c = r && (i ? a : !u),
                      d = "Enter" === e.key,
                      f = " " === e.key,
                      p = o.getAttribute("role"),
                      h = p?.startsWith("menuitem") || "option" === p || "gridcell" === p;
                    if (r && s && f) {
                      if (e.defaultPrevented && h) return;
                      (e.preventDefault(), (!i || a) && (e.preventBaseUIHandler(), iz(o, e)));
                      return;
                    }
                    if (!c || i || (!f && !d)) {
                      r && u && f && e.preventDefault();
                      return;
                    }
                    !e.defaultPrevented && (e.preventDefault(), d && (e.preventBaseUIHandler(), iz(o, e)));
                  },
                  onKeyUp(e) {
                    t ||
                      ((n2(e), o?.(e), e.target === e.currentTarget && i && s && iL(e.currentTarget) && " " === e.key)
                        ? e.preventDefault()
                        : !e.baseUIHandlerPrevented &&
                          (e.target !== e.currentTarget ||
                            i ||
                            s ||
                            e.defaultPrevented ||
                            " " !== e.key ||
                            (e.preventBaseUIHandler(), iz(e.currentTarget, e))));
                  },
                  onPointerDown(e) {
                    t ? e.preventDefault() : a?.(e);
                  },
                },
                i ? { type: "button" } : { role: "button" },
                u,
                c,
              );
            },
            [t, u, s, i],
          ),
          buttonRef: iT((e) => {
            ((l.current = e), c());
          }),
        }
      );
    }
    function iL(e) {
      return iw(e) && "BUTTON" === e.tagName;
    }
    let i$ = f.forwardRef(function (e, t) {
        let {
            render: n,
            className: r,
            disabled: i = !1,
            focusableWhenDisabled: o = !1,
            nativeButton: l = !0,
            style: a,
            ...s
          } = e,
          { getButtonProps: u, buttonRef: c } = iD({ disabled: i, focusableWhenDisabled: o, native: l });
        return rl("button", e, { state: { disabled: i }, ref: [t, c], props: [s, u] });
      }),
      iF = rc(
        "group/button inline-flex shrink-0 items-center justify-center rounded-lg border border-transparent bg-clip-padding text-sm font-medium whitespace-nowrap transition-all outline-none select-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 active:not-aria-[haspopup]:translate-y-px disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        {
          variants: {
            variant: {
              default: "bg-primary text-primary-foreground hover:bg-primary/80",
              outline:
                "border-border bg-background hover:bg-muted hover:text-foreground aria-expanded:bg-muted aria-expanded:text-foreground dark:border-input dark:bg-input/30 dark:hover:bg-input/50",
              secondary:
                "bg-secondary text-secondary-foreground hover:bg-[color-mix(in_oklch,var(--secondary),var(--foreground)_5%)] aria-expanded:bg-secondary aria-expanded:text-secondary-foreground",
              ghost:
                "hover:bg-muted hover:text-foreground aria-expanded:bg-muted aria-expanded:text-foreground dark:hover:bg-muted/50",
              destructive:
                "bg-destructive/10 text-destructive hover:bg-destructive/20 focus-visible:border-destructive/40 focus-visible:ring-destructive/20 dark:bg-destructive/20 dark:hover:bg-destructive/30 dark:focus-visible:ring-destructive/40",
              link: "text-primary underline-offset-4 hover:underline",
            },
            size: {
              default: "h-8 gap-1.5 px-2.5 has-data-[icon=inline-end]:pr-2 has-data-[icon=inline-start]:pl-2",
              xs: "h-6 gap-1 rounded-[min(var(--radius-md),10px)] px-2 text-xs in-data-[slot=button-group]:rounded-lg has-data-[icon=inline-end]:pr-1.5 has-data-[icon=inline-start]:pl-1.5 [&_svg:not([class*='size-'])]:size-3",
              sm: "h-7 gap-1 rounded-[min(var(--radius-md),12px)] px-2.5 text-[0.8rem] in-data-[slot=button-group]:rounded-lg has-data-[icon=inline-end]:pr-1.5 has-data-[icon=inline-start]:pl-1.5 [&_svg:not([class*='size-'])]:size-3.5",
              lg: "h-9 gap-1.5 px-2.5 has-data-[icon=inline-end]:pr-2 has-data-[icon=inline-start]:pl-2",
              icon: "size-8",
              "icon-xs":
                "size-6 rounded-[min(var(--radius-md),10px)] in-data-[slot=button-group]:rounded-lg [&_svg:not([class*='size-'])]:size-3",
              "icon-sm": "size-7 rounded-[min(var(--radius-md),12px)] in-data-[slot=button-group]:rounded-lg",
              "icon-lg": "size-9",
            },
          },
          defaultVariants: { variant: "default", size: "default" },
        },
      );
    function i_({ className: e, variant: t = "default", size: n = "default", ...r }) {
      return (0, d.jsx)(i$, { "data-slot": "button", className: ih(iF({ variant: t, size: n, className: e })), ...r });
    }
    function iB({ className: e, size: t = "default", ...n }) {
      return (0, d.jsx)("div", {
        "data-slot": "card",
        "data-size": t,
        className: ih(
          "group/card flex flex-col gap-(--card-spacing) overflow-hidden rounded-xl bg-card py-(--card-spacing) text-sm text-card-foreground ring-1 ring-foreground/10 [--card-spacing:--spacing(4)] has-data-[slot=card-footer]:pb-0 has-[>img:first-child]:pt-0 data-[size=sm]:[--card-spacing:--spacing(3)] data-[size=sm]:has-data-[slot=card-footer]:pb-0 *:[img:first-child]:rounded-t-xl *:[img:last-child]:rounded-b-xl",
          e,
        ),
        ...n,
      });
    }
    function iH({ className: e, ...t }) {
      return (0, d.jsx)("div", {
        "data-slot": "card-header",
        className: ih(
          "group/card-header @container/card-header grid auto-rows-min items-start gap-1 rounded-t-xl px-(--card-spacing) has-data-[slot=card-action]:grid-cols-[1fr_auto] has-data-[slot=card-description]:grid-rows-[auto_auto] [.border-b]:pb-(--card-spacing)",
          e,
        ),
        ...t,
      });
    }
    function iq({ className: e, ...t }) {
      return (0, d.jsx)("div", {
        "data-slot": "card-title",
        className: ih("font-heading text-base leading-snug font-medium group-data-[size=sm]/card:text-sm", e),
        ...t,
      });
    }
    function iU({ className: e, ...t }) {
      return (0, d.jsx)("div", {
        "data-slot": "card-description",
        className: ih("text-sm text-muted-foreground", e),
        ...t,
      });
    }
    function iW({ className: e, ...t }) {
      return (0, d.jsx)("div", { "data-slot": "card-content", className: ih("px-(--card-spacing)", e), ...t });
    }
    (e.s([], 66432), e.i(66432));
    let iV = {
        badInput: !1,
        customError: !1,
        patternMismatch: !1,
        rangeOverflow: !1,
        rangeUnderflow: !1,
        stepMismatch: !1,
        tooLong: !1,
        tooShort: !1,
        typeMismatch: !1,
        valid: null,
        valueMissing: !1,
      },
      iK = { valid: (e) => (null === e ? null : e ? { "data-valid": "" } : { "data-invalid": "" }) },
      iX = {
        invalid: void 0,
        name: void 0,
        validityData: { state: iV, errors: [], error: "", value: "", initialValue: null },
        setValidityData: rr,
        disabled: void 0,
        setTouched: rr,
        setDirty: rr,
        setFilled: rr,
        setFocused: rr,
        validationMode: "onSubmit",
        shouldValidateOnChange: () => !1,
        state: { disabled: !1, valid: null, touched: !1, dirty: !1, filled: !1, focused: !1 },
        registerFieldControl: rr,
        validation: {
          getValidationProps: (e, t = ro) => t,
          inputRef: { current: null },
          registeredInputs: new Map(),
          registerInput: rr,
          getInputControl: () => null,
          commit: async () => {},
          change: rr,
        },
      },
      iY = f.createContext(iX);
    function iG(e = !0) {
      let t = f.useContext(iY);
      if (t.setValidityData === rr && !e) throw Error(n3(28));
      return t;
    }
    let iJ = f.createContext(void 0),
      iQ = f.createContext({
        elementRef: { current: null },
        formRef: { current: { fields: new Map() } },
        errors: {},
        clearErrors: rr,
        validationMode: "onSubmit",
        submitAttemptedRef: { current: !1 },
      });
    function iZ() {
      return f.useContext(iQ);
    }
    let i0 = 0,
      i1 = ij.useId;
    function i2(e, t) {
      if (void 0 !== i1) {
        let n = i1();
        return e ?? (t ? `${t}-${n}` : n);
      }
      return (function (e, t = "mui") {
        let [n, r] = f.useState(e),
          i = e || n;
        return (
          f.useEffect(() => {
            null == n && ((i0 += 1), r(`${t}-${i0}`));
          }, [n, t]),
          i
        );
      })(e, t);
    }
    function i4(e) {
      return i2(e, "base-ui");
    }
    let i5 = f.createContext({
      controlId: void 0,
      registerControlId: rr,
      labelId: void 0,
      setLabelId: rr,
      messageIds: [],
      setMessageIds: rr,
      getDescriptionProps: (e) => e,
    });
    function i3() {
      return f.useContext(i5);
    }
    let i6 = function (e) {
      let t = i4(),
        n = void 0 === e.controlId ? t : e.controlId,
        [r, i] = f.useState(n),
        [o, l] = f.useState(e.labelId),
        [a, s] = f.useState([]),
        u = n9(() => new Map()),
        { messageIds: c } = i3(),
        p = iT((e, t) => {
          let n = u.current;
          void 0 === t
            ? n.delete(e)
            : (n.set(e, t),
              i((e) => {
                let t;
                if (0 !== n.size) {
                  for (let r of n.values()) {
                    if (void 0 !== e && r === e) return e;
                    void 0 === t && (t = r);
                  }
                  return t;
                }
              }));
        }),
        h = f.useCallback(
          (e) => {
            let t = e["aria-describedby"] ? e["aria-describedby"].split(" ") : [];
            return (t.push(...c, ...a), { ...e, "aria-describedby": Array.from(new Set(t)).join(" ") || void 0 });
          },
          [c, a],
        ),
        m = f.useMemo(
          () => ({
            controlId: r,
            registerControlId: p,
            labelId: o,
            setLabelId: l,
            messageIds: a,
            setMessageIds: s,
            getDescriptionProps: h,
          }),
          [r, p, o, l, a, s, h],
        );
      return (0, d.jsx)(i5.Provider, { value: m, children: e.children });
    };
    function i9(e) {
      f.useEffect(e, ri);
    }
    class i7 {
      static create() {
        return new i7();
      }
      currentId = 0;
      start(e, t) {
        (this.clear(),
          (this.currentId = setTimeout(() => {
            ((this.currentId = 0), t());
          }, e)));
      }
      isStarted() {
        return 0 !== this.currentId;
      }
      clear = () => {
        0 !== this.currentId && (clearTimeout(this.currentId), (this.currentId = 0));
      };
      disposeEffect = () => this.clear;
    }
    function i8() {
      let e = n9(i7.create).current;
      return (i9(e.disposeEffect), e);
    }
    function oe(e, t) {
      return { ...e, state: { ...e.state, valid: !t && e.state.valid } };
    }
    let ot = Object.keys(iV);
    function on(e, t) {
      let n = null;
      for (let r of e.keys())
        if (!r.matches(":disabled") && (!t || r.form === t || (null === r.form && !r.hasAttribute("form")))) {
          if (!r.validity.valid) return r;
          n ??= r;
        }
      return n;
    }
    function or(e, t) {
      for (let e of t.keys()) e.setCustomValidity("");
      e?.setCustomValidity("");
    }
    let oi = f.forwardRef(function (e, t) {
        let { errors: n, validationMode: r, submitAttemptedRef: i } = iZ(),
          {
            render: o,
            className: l,
            validate: a,
            validationDebounceTime: s = 0,
            validationMode: u = r,
            name: c,
            disabled: p = !1,
            invalid: h,
            dirty: m,
            touched: g,
            actionsRef: v,
            style: y,
            ...b
          } = e,
          x = (function (e = !1) {
            let t = f.useContext(iJ);
            if (!t && !e) throw Error(n3(86));
            return t;
          })(!0)?.disabled,
          k = iT(a || (() => null)),
          w = x || p,
          [S, C] = f.useState(!1),
          [E, j] = f.useState(!1),
          [R, P] = f.useState(!1),
          [T, A] = f.useState(!1),
          O = m ?? E,
          I = g ?? S,
          M = f.useRef(O),
          N = f.useRef(void 0),
          [z, D] = f.useState(),
          L = c ?? z;
        iI(() => {
          void 0 !== m && (M.current = m);
        }, [m]);
        let $ = iT((e) => {
            void 0 === m && (e && (M.current = !0), j(e));
          }),
          F = iT((e) => {
            void 0 === g && C(e);
          }),
          _ = iT(() => "onChange" === u || ("onSubmit" === u && i.current)),
          B = L && Object.hasOwn(n, L) ? n[L] : null,
          H = !!(Array.isArray(B) ? B.length : B),
          q = !0 === h || H,
          [U, W] = f.useState({ state: iV, error: "", errors: [], value: null, initialValue: null }),
          V = !q && (w ? null : U.state.valid),
          K = f.useMemo(
            () => ({ disabled: w, touched: I, dirty: O, valid: V, filled: R, focused: T }),
            [w, I, O, V, R, T],
          ),
          X = (function (e) {
            let { elementRef: t, formRef: n } = iZ(),
              {
                setValidityData: r,
                validate: i,
                validityData: o,
                validationDebounceTime: l,
                invalid: a,
                markedDirtyRef: s,
                state: u,
                shouldValidateOnChange: c,
                registeredFieldIdRef: d,
              } = e,
              { controlId: p, getDescriptionProps: h } = i3(),
              m = i8(),
              g = f.useRef(null),
              v = n9(() => new Map()).current,
              y = f.useRef(0),
              b = f.useCallback(
                (e, t) => (
                  v.set(e, t),
                  () => {
                    v.delete(e);
                  }
                ),
                [v],
              ),
              x = iT(() => {
                let e = on(v, t.current);
                return (e && v.get(e)?.controlRef.current) || null;
              }),
              k = iT(async (e, l = !1) => {
                let f;
                y.current += 1;
                let h = y.current;
                function b(e, t = a) {
                  let r = d.current ?? p;
                  if (null == r) return;
                  let i = n.current.fields.get(r);
                  if (!i) return;
                  let o = oe(e, t);
                  n.current.fields.set(r, { ...i, validityData: o });
                }
                let x = v.size > 0 ? on(v, t.current) : g.current;
                if (l) {
                  if (!1 !== u.valid || !x) return;
                  let t = x.validity;
                  if (!t.valueMissing) {
                    let t;
                    return void ((t = {
                      value: e,
                      state: { ...iV, valid: !0 },
                      error: "",
                      errors: [],
                      initialValue: o.initialValue,
                    }),
                    or(x, v),
                    b(t, !1),
                    r(t));
                  }
                  for (let e of ot) if ("valid" !== e && "valueMissing" !== e && "customError" !== e && t[e]) return;
                }
                m.clear();
                let k = null,
                  w = [],
                  S = x
                    ? (function (e) {
                        let t = ot.reduce((t, n) => ((t[n] = e.validity[n]), t), {}),
                          n = !1;
                        for (let e of ot)
                          if ("valid" !== e) {
                            if ("valueMissing" === e && t[e]) n = !0;
                            else if (t[e]) return t;
                          }
                        return (n && !s.current && ((t.valid = !0), (t.valueMissing = !1)), t);
                      })(x)
                    : { ...iV, valid: !0 },
                  C = c();
                if (x && x.validationMessage && !C) ((f = x.validationMessage), (w = [x.validationMessage]));
                else {
                  let t = i(
                    e,
                    Array.from(n.current.fields.values()).reduce(
                      (e, t) => (t.name && (e[t.name] = t.getValue()), e),
                      {},
                    ),
                  );
                  if ("object" == typeof t && null !== t && "then" in t) {
                    if (((k = await t), h !== y.current)) return;
                  } else k = t;
                  null !== k
                    ? ((S.valid = !1),
                      (S.customError = !0),
                      Array.isArray(k)
                        ? ((w = k), x?.setCustomValidity(k.join("\n")))
                        : k && ((w = [k]), x?.setCustomValidity(k)))
                    : C &&
                      (or(x, v),
                      (S.customError = !1),
                      x && x.validationMessage
                        ? ((f = x.validationMessage), (w = [x.validationMessage]))
                        : (x && !x.validity.valid) || S.valid || (S.valid = !0));
                }
                let E = {
                  value: e,
                  state: S,
                  error: f ?? (Array.isArray(k) ? k[0] : (k ?? "")),
                  errors: w,
                  initialValue: o.initialValue,
                };
                (b(E), r(E));
              }),
              w = iT((e) => {
                m.clear();
                let t = c();
                t && "" !== e && l
                  ? ((y.current += 1),
                    m.start(l, () => {
                      k(e);
                    }))
                  : k(e, !t);
              }),
              S = f.useCallback(
                (e, t = {}) => nY(h(t), !1 !== u.valid || u.disabled || e ? ro : { "aria-invalid": !0 }),
                [h, u.disabled, u.valid],
              );
            return f.useMemo(
              () => ({
                getValidationProps: S,
                inputRef: g,
                registeredInputs: v,
                registerInput: b,
                getInputControl: x,
                commit: k,
                change: w,
              }),
              [S, v, b, x, k, w],
            );
          })({
            setValidityData: W,
            validate: k,
            validityData: U,
            validationDebounceTime: s,
            invalid: q,
            markedDirtyRef: M,
            state: K,
            shouldValidateOnChange: _,
            registeredFieldIdRef: N,
          }),
          [Y, G] = (function (e) {
            let {
                commit: t,
                invalid: n,
                markedDirtyRef: r,
                name: i,
                setRegisteredFieldName: o,
                registeredFieldIdRef: l,
                setValidityData: a,
                validityData: s,
              } = e,
              { formRef: u } = iZ(),
              c = f.useRef(null),
              d = f.useRef(null),
              p = f.useRef(!1),
              h = iT(() => {
                let e = d.current;
                if (e) return e.getValue ? e.getValue() : e.value;
              });
            function m(e) {
              return void 0 === e.value ? h() : e.value;
            }
            let g = iT(() => {
              let e = d.current;
              ((r.current = !0), e) ? t(m(e)) : t(s.value);
            });
            function v(e = d.current?.id) {
              e && u.current.fields.delete(e);
            }
            (iI(() => {
              let e = d.current;
              e &&
                e.id &&
                (o(i ? void 0 : e.name),
                u.current.fields.set(e.id, {
                  getValue: h,
                  name: i ?? e.name,
                  controlRef: e.controlRef,
                  validityData: oe(s, n),
                  validate: g,
                }));
            }, [u, h, n, i, o, g, s]),
              iI(() => {
                let e = u.current.fields;
                return () => {
                  let t = d.current?.id;
                  t && e.delete(t);
                };
              }, [u]));
            let y = iT((e, t) => {
              let r;
              if (!t) {
                c.current === e && ((c.current = null), v(), (d.current = null), o(void 0), (l.current = void 0));
                return;
              }
              let f = d.current?.id;
              ((c.current = e),
                (d.current = t),
                i || o(t.name),
                (l.current = t.id),
                f && f !== t.id && v(f),
                (function (e) {
                  if (p.current) return;
                  p.current = !0;
                  let t = m(e);
                  a((e) => (e.initialValue === t ? e : { ...e, initialValue: t }));
                })(t),
                (r = d.current) &&
                  r.id &&
                  u.current.fields.set(r.id, {
                    getValue: h,
                    name: i ?? r.name,
                    controlRef: r.controlRef,
                    validityData: oe(s, n),
                    validate: g,
                  }));
            });
            return [g, y];
          })({
            commit: X.commit,
            invalid: q,
            markedDirtyRef: M,
            name: c,
            setRegisteredFieldName: D,
            registeredFieldIdRef: N,
            setValidityData: W,
            validityData: U,
          });
        f.useImperativeHandle(v, () => ({ validate: Y }), [Y]);
        let J = f.useMemo(
            () => ({
              invalid: q,
              name: L,
              validityData: U,
              setValidityData: W,
              disabled: w,
              setTouched: F,
              setDirty: $,
              setFilled: P,
              setFocused: A,
              validationMode: u,
              shouldValidateOnChange: _,
              state: K,
              registerFieldControl: G,
              validation: X,
            }),
            [q, L, U, w, F, $, P, A, u, _, K, G, X],
          ),
          Q = rl("div", e, { ref: t, state: K, props: b, stateAttributesMapping: iK });
        return (0, d.jsx)(iY.Provider, { value: J, children: Q });
      }),
      oo = f.forwardRef(function (e, t) {
        return (0, d.jsx)(i6, { children: (0, d.jsx)(oi, { ...e, ref: t }) });
      });
    function ol(e) {
      return e?.ownerDocument || document;
    }
    function oa(e) {
      let t = e.activeElement;
      for (; t?.shadowRoot?.activeElement != null; ) t = t.shadowRoot.activeElement;
      return t;
    }
    function os(e, t) {
      if (!e || !t) return !1;
      let n = t.getRootNode?.();
      if (e.contains(t)) return !0;
      if (n && iS(n)) {
        let n = t;
        for (; n; ) {
          if (e === n) return !0;
          n = n.parentNode || n.host;
        }
      }
      return !1;
    }
    function ou(e) {
      return "composedPath" in e ? e.composedPath()[0] : e.target;
    }
    let oc = f.createContext({ disabled: !1 });
    function od() {
      return f.useContext(oc);
    }
    let of = f.forwardRef(function (e, t) {
      let { render: n, className: r, style: i, id: o, nativeLabel: l = !0, ...a } = e,
        s = iG(!1),
        u = od(),
        { labelId: c } = i3(),
        d = { ...s.state, disabled: s.disabled || u.disabled };
      return rl("label", e, {
        ref: [t, f.useRef(null)],
        state: d,
        props: [
          (function (e = {}) {
            let t,
              { id: n, fallbackControlId: r, native: i = !1, setLabelId: o, focusControl: l } = e,
              { controlId: a, setLabelId: s } = i3(),
              u = iT((e) => {
                (s(e), o?.(e));
              }),
              c =
                (iI(
                  () => (
                    u(t),
                    () => {
                      u((e) => (e === t ? void 0 : e));
                    }
                  ),
                  [(t = i4(n)), u],
                ),
                t),
              d = a ?? r;
            function f(e) {
              let t = ou(e.nativeEvent);
              t?.closest("button,input,select,textarea") ||
                (!e.defaultPrevented && e.detail > 1 && e.preventDefault(),
                i ||
                  (function (e) {
                    if (l) return l(e, d);
                    if (!d) return;
                    let t = ol(e.currentTarget).getElementById(d);
                    iw(t) && t.focus({ focusVisible: !0 });
                  })(e));
            }
            return i
              ? { id: c, htmlFor: d ?? void 0, onMouseDown: f }
              : {
                  id: c,
                  onClick: f,
                  onPointerDown(e) {
                    e.preventDefault();
                  },
                };
          })({ id: c ?? o, native: l }),
          a,
        ],
        stateAttributesMapping: iK,
      });
    });
    var op = e.i(74080);
    let oh = new (class {
      callbacks = [];
      callbacksCount = 0;
      nextId = 1;
      startId = 1;
      isScheduled = !1;
      tick = (e) => {
        this.isScheduled = !1;
        let t = this.callbacks,
          n = this.callbacksCount;
        if (((this.callbacks = []), (this.callbacksCount = 0), (this.startId = this.nextId), n > 0))
          for (let n = 0; n < t.length; n += 1) t[n]?.(e);
      };
      request(e) {
        let t = this.nextId;
        return (
          (this.nextId += 1),
          this.callbacks.push(e),
          (this.callbacksCount += 1),
          this.isScheduled || (requestAnimationFrame(this.tick), (this.isScheduled = !0)),
          t
        );
      }
      cancel(e) {
        let t = e - this.startId;
        t < 0 || t >= this.callbacks.length || ((this.callbacks[t] = null), (this.callbacksCount -= 1));
      }
    })();
    class om {
      static create() {
        return new om();
      }
      static request(e) {
        return oh.request(e);
      }
      static cancel(e) {
        return oh.cancel(e);
      }
      currentId = null;
      request(e) {
        (this.cancel(),
          (this.currentId = oh.request(() => {
            ((this.currentId = null), e());
          })));
      }
      cancel = () => {
        null !== this.currentId && (oh.cancel(this.currentId), (this.currentId = null));
      };
      disposeEffect = () => this.cancel;
    }
    function og() {
      let e = n9(om.create).current;
      return (i9(e.disposeEffect), e);
    }
    function ov(e) {
      return null == e ? e : "current" in e ? e.current : e;
    }
    function oy(e) {
      let { enabled: t = !0, open: n, ref: r, onComplete: i } = e,
        o = iT(i),
        l = (function (e, t = !1) {
          let n = og();
          return iT((r, i = null) => {
            n.cancel();
            let o = ov(e);
            if (null == o) return;
            let l = () => {
              op.flushSync(r);
            };
            if ("function" != typeof o.getAnimations || globalThis.BASE_UI_ANIMATIONS_DISABLED) return void r();
            function a() {
              Promise.all(o.getAnimations().map((e) => e.finished)).then(
                () => {
                  i?.aborted || l();
                },
                () => {
                  i?.aborted || (o.getAnimations().some((e) => e.pending || "finished" !== e.playState) ? a() : l());
                },
              );
            }
            if (t) {
              let e = "data-starting-style";
              if (!o.hasAttribute(e)) return void n.request(a);
              let t = new MutationObserver(() => {
                o.hasAttribute(e) || (t.disconnect(), a());
              });
              return (
                t.observe(o, { attributes: !0, attributeFilter: [e] }),
                void i?.addEventListener("abort", () => t.disconnect(), { once: !0 })
              );
            }
            n.request(a);
          });
        })(r, n);
      f.useEffect(() => {
        if (!t) return;
        let e = new AbortController();
        return (
          l(o, e.signal),
          () => {
            e.abort();
          }
        );
      }, [t, n, o, l]);
    }
    let ob = (((s = {}).startingStyle = "data-starting-style"), (s.endingStyle = "data-ending-style"), s),
      ox = { "data-starting-style": "" },
      ok = { "data-ending-style": "" },
      ow = { transitionStatus: (e) => ("starting" === e ? ox : "ending" === e ? ok : null) };
    function oS(e, t = !1, n = !1) {
      let [r, i] = f.useState(e && t ? "idle" : void 0),
        [o, l] = f.useState(e);
      return (
        e && !o && (l(!0), i("starting")),
        e || !o || "ending" === r || n || i("ending"),
        e || o || "ending" !== r || i(void 0),
        iI(() => {
          if (!e && o && "ending" !== r && n) {
            let e = om.request(() => {
              i("ending");
            });
            return () => {
              om.cancel(e);
            };
          }
        }, [e, o, r, n]),
        iI(() => {
          if (!e || t) return;
          let n = om.request(() => {
            i(void 0);
          });
          return () => {
            om.cancel(n);
          };
        }, [t, e]),
        iI(() => {
          if (!e || !t) return;
          e && o && "idle" !== r && i("starting");
          let n = om.request(() => {
            i("idle");
          });
          return () => {
            om.cancel(n);
          };
        }, [t, e, o, r]),
        { mounted: o, setMounted: l, transitionStatus: r }
      );
    }
    let oC = { ...iK, ...ow },
      oE = f.forwardRef(function (e, t) {
        let { render: n, id: r, className: i, match: o, style: l, ...a } = e,
          s = i4(r),
          { validityData: u, state: c, name: p } = iG(!1),
          { setMessageIds: h } = i3(),
          { errors: m } = iZ(),
          g = p && Object.hasOwn(m, p) ? m[p] : null,
          v = !!(Array.isArray(g) ? g.length : g),
          y = "string" == typeof o,
          b = !1,
          {
            mounted: x,
            transitionStatus: k,
            setMounted: w,
          } = oS((b = !0 === o || (!c.disabled && (y ? !!u.state[o] : v || !1 === u.state.valid))));
        iI(() => {
          if (b && s)
            return (
              h((e) => e.concat(s)),
              () => {
                h((e) => e.filter((e) => e !== s));
              }
            );
        }, [b, s, h]);
        let S = f.useRef(null),
          [C, E] = f.useState(null),
          [j, R] = f.useState(null),
          P = u.error;
        !y && v ? (P = g) : u.errors.length > 1 && (P = u.errors);
        let T = P;
        Array.isArray(P) &&
          (T =
            P.length > 1 ? (0, d.jsx)("ul", { children: P.map((e) => (0, d.jsx)("li", { children: e }, e)) }) : P[0]);
        let A = Array.isArray(P) ? JSON.stringify(P) : P;
        (b && A !== j && (R(A), E(T)),
          oy({
            open: b,
            ref: S,
            onComplete() {
              b || w(!1);
            },
          }));
        let O = rl("div", e, {
          ref: [t, S],
          state: { ...c, transitionStatus: k },
          props: [{ id: s, children: b ? T : C }, a],
          stateAttributesMapping: oC,
          enabled: x,
        });
        return x ? O : null;
      }),
      oj = f.forwardRef(function (e, t) {
        let { render: n, id: r, className: i, style: o, ...l } = e,
          a = i4(r),
          s = iG(!1),
          u = od(),
          { setMessageIds: c } = i3(),
          d = { ...s.state, disabled: s.disabled || u.disabled };
        return (
          iI(() => {
            if (a)
              return (
                c((e) => e.concat(a)),
                () => {
                  c((e) => e.filter((e) => e !== a));
                }
              );
          }, [a, c]),
          rl("p", e, { ref: t, state: d, props: [{ id: a }, l], stateAttributesMapping: iK })
        );
      });
    function oR({ controlled: e, default: t, name: n, state: r = "value" }) {
      let { current: i } = f.useRef(void 0 !== e),
        [o, l] = f.useState(t),
        a = f.useCallback((e) => {
          i || l(e);
        }, []);
      return [i ? e : o, a];
    }
    function oP(e, t, n, r) {
      let i = !1,
        o = !1,
        l = r ?? ro;
      return {
        reason: e,
        event: t ?? new Event("base-ui"),
        cancel() {
          i = !0;
        },
        allowPropagation() {
          o = !0;
        },
        get isCanceled() {
          return i;
        },
        get isPropagationAllowed() {
          return o;
        },
        trigger: n,
        ...l,
      };
    }
    e.s(
      [
        "cancelOpen",
        0,
        "cancel-open",
        "chipRemovePress",
        0,
        "chip-remove-press",
        "clearPress",
        0,
        "clear-press",
        "closePress",
        0,
        "close-press",
        "closeWatcher",
        0,
        "close-watcher",
        "decrementPress",
        0,
        "decrement-press",
        "disabled",
        0,
        "disabled",
        "drag",
        0,
        "drag",
        "escapeKey",
        0,
        "escape-key",
        "focusOut",
        0,
        "focus-out",
        "imperativeAction",
        0,
        "imperative-action",
        "incrementPress",
        0,
        "increment-press",
        "initial",
        0,
        "initial",
        "inputBlur",
        0,
        "input-blur",
        "inputChange",
        0,
        "input-change",
        "inputClear",
        0,
        "input-clear",
        "inputPaste",
        0,
        "input-paste",
        "inputPress",
        0,
        "input-press",
        "itemPress",
        0,
        "item-press",
        "keyboard",
        0,
        "keyboard",
        "linkPress",
        0,
        "link-press",
        "listNavigation",
        0,
        "list-navigation",
        "missing",
        0,
        "missing",
        "none",
        0,
        "none",
        "outsidePress",
        0,
        "outside-press",
        "pointer",
        0,
        "pointer",
        "scrub",
        0,
        "scrub",
        "siblingOpen",
        0,
        "sibling-open",
        "swipe",
        0,
        "swipe",
        "trackPress",
        0,
        "track-press",
        "triggerFocus",
        0,
        "trigger-focus",
        "triggerHover",
        0,
        "trigger-hover",
        "triggerPress",
        0,
        "trigger-press",
        "wheel",
        0,
        "wheel",
        "windowResize",
        0,
        "window-resize",
      ],
      16856,
    );
    var oT = e.i(16856),
      oT = oT;
    let oA = f.forwardRef(function (e, t) {
        let {
            render: n,
            className: r,
            id: i,
            name: o,
            value: l,
            disabled: a = !1,
            onValueChange: s,
            defaultValue: u,
            autoFocus: c = !1,
            style: d,
            ...p
          } = e,
          {
            state: h,
            name: m,
            disabled: g,
            setTouched: v,
            setDirty: y,
            validityData: b,
            setFocused: x,
            setFilled: k,
            validationMode: w,
            validation: S,
          } = iG(),
          { clearErrors: C } = iZ(),
          E = g || a,
          j = m ?? o,
          R = { ...h, disabled: E },
          { labelId: P } = i3(),
          T = (function (e = {}) {
            let { id: t, implicit: n = !1, controlRef: r } = e,
              { controlId: i, registerControlId: o } = i3(),
              l = i4(t),
              a = n ? i : void 0,
              s = n9(() => Symbol()),
              u = f.useRef(!1),
              c = f.useRef(null != t),
              d = iT(() => {
                u.current && o !== rr && ((u.current = !1), o(s.current, void 0));
              });
            return (
              iI(() => {
                let e;
                if (o !== rr) {
                  if (n) {
                    let n = r?.current;
                    e = ik(n) && null != n.closest("label") ? (t ?? null) : (a ?? l);
                  } else if (null != t) ((c.current = !0), (e = t));
                  else {
                    if (!c.current) return void d();
                    e = l;
                  }
                  if (void 0 === e) return void d();
                  ((u.current = !0), o(s.current, e));
                }
              }, [t, r, a, o, n, l, s, d]),
              f.useEffect(() => d, [d]),
              i ?? l
            );
          })({ id: i });
        iI(() => {
          let e = null != l;
          S.inputRef.current?.value || (e && "" !== l) ? k(!0) : e && "" === l && k(!1);
        }, [S.inputRef, k, l]);
        let A = f.useRef(null);
        iI(() => {
          c && A.current === oa(ol(A.current)) && x(!0);
        }, [c, x]);
        let [O] = oR({ controlled: l, default: u, name: "FieldControl", state: "value" }),
          I = void 0 !== l,
          M = I ? O : void 0,
          N = iT(() => S.inputRef.current?.value);
        return (
          !(function (e, t, n, r, i = !0, o) {
            let { registerFieldControl: l } = iG(),
              a = n9(() => Symbol());
            (iI(() => {
              let s = a.current;
              i ? l(s, { controlRef: e, getValue: r, id: t, name: o, value: n }) : l(s, void 0);
            }, [e, i, r, t, o, l, a, n]),
              iI(() => {
                let e = a.current;
                return () => {
                  l(e, void 0);
                };
              }, [l, a]));
          })(S.inputRef, T, M, N, !E, o),
          rl("input", e, {
            ref: [t, A],
            state: R,
            props: [
              {
                id: T,
                disabled: E,
                name: j,
                ref: S.inputRef,
                "aria-labelledby": P,
                autoFocus: c,
                ...(I ? { value: M } : { defaultValue: u }),
                onChange(e) {
                  let t = e.currentTarget.value;
                  (s?.(t, oP(oT.none, e.nativeEvent)),
                    y(t !== (b.initialValue ?? "")),
                    k("" !== t),
                    e.nativeEvent.defaultPrevented || (C(j), S.change(t)));
                },
                onFocus() {
                  x(!0);
                },
                onBlur(e) {
                  (v(!0), x(!1), "onBlur" === w && S.commit(e.currentTarget.value));
                },
                onKeyDown(e) {
                  "INPUT" === e.currentTarget.tagName && "Enter" === e.key && (v(!0), S.commit(e.currentTarget.value));
                },
              },
              p,
              (e) => S.getValidationProps(E, e),
            ],
            stateAttributesMapping: iK,
          })
        );
      }),
      oO = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, disabled: o = !1, ...l } = e,
          { state: a, disabled: s } = iG(!1),
          u = s || o,
          c = { ...a, disabled: u },
          p = f.useMemo(() => ({ disabled: u }), [u]),
          h = rl("div", e, { ref: t, state: c, props: l, stateAttributesMapping: iK });
        return (0, d.jsx)(i6, { children: (0, d.jsx)(oc.Provider, { value: p, children: h }) });
      });
    e.s(
      [
        "Control",
        0,
        oA,
        "Description",
        0,
        oj,
        "Error",
        0,
        oE,
        "Item",
        0,
        oO,
        "Label",
        0,
        of,
        "Root",
        0,
        oo,
        "Validity",
        0,
        function (e) {
          let { children: t } = e,
            { validityData: n, invalid: r } = iG(!1),
            i = f.useMemo(() => oe(n, r), [n, r]),
            { transitionStatus: o } = oS(!1 === i.state.valid),
            l = f.useMemo(() => ({ ...i, validity: i.state, transitionStatus: o }), [i, o]);
          return (0, d.jsx)(f.Fragment, { children: t(l) });
        },
      ],
      5359,
    );
    var oI = e.i(5359),
      oI = oI;
    let oM = f.forwardRef(function (e, t) {
      return (0, d.jsx)(oI.Control, { ref: t, ...e });
    });
    function oN({ className: e, type: t, ...n }) {
      return (0, d.jsx)(oM, {
        type: t,
        "data-slot": "input",
        className: ih(
          "h-8 w-full min-w-0 rounded-lg border border-input bg-transparent px-2.5 py-1 text-base transition-colors outline-none file:inline-flex file:h-6 file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:pointer-events-none disabled:cursor-not-allowed disabled:bg-input/50 disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 md:text-sm dark:bg-input/30 dark:disabled:bg-input/80 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40",
          e,
        ),
        ...n,
      });
    }
    (e.s([], 73176), e.i(73176));
    let oz = f.createContext(void 0);
    function oD() {
      let e = f.useContext(oz);
      if (void 0 === e) throw Error(n3(53));
      return e;
    }
    function oL(e, t, n) {
      if (!e) return 0;
      let r = getComputedStyle(e),
        i = `${t}${"x" === n ? "Inline" : "Block"}`,
        o = parseFloat(r[`${i}Start`]);
      return "x" === n && "margin" === t ? 2 * o : o + parseFloat(r[`${i}End`]);
    }
    let o$ = "base-ui-disable-scrollbar",
      oF = (e) => (t) => (t ? { [e]: "" } : null),
      o_ = {
        hasOverflowX: oF("data-has-overflow-x"),
        hasOverflowY: oF("data-has-overflow-y"),
        overflowXStart: oF("data-overflow-x-start"),
        overflowXEnd: oF("data-overflow-x-end"),
        overflowYStart: oF("data-overflow-y-start"),
        overflowYEnd: oF("data-overflow-y-end"),
        cornerHidden: () => null,
      },
      oB = f.createContext(void 0),
      oH = { disableStyleElements: !1 };
    function oq() {
      return f.useContext(oB) ?? oH;
    }
    let oU = { x: 0, y: 0 },
      oW = { width: 0, height: 0 },
      oV = { xStart: !1, xEnd: !1, yStart: !1, yEnd: !1 },
      oK = { x: !0, y: !0, corner: !0 },
      oX = f.forwardRef(function (e, t) {
        var n;
        let r,
          i,
          { render: o, className: l, overflowEdgeThreshold: a, style: s, ...u } = e,
          {
            xStart: c,
            xEnd: p,
            yStart: h,
            yEnd: m,
          } = ((r = "number" == typeof (n = a) ? { xStart: n, xEnd: n, yStart: n, yEnd: n } : n),
          {
            xStart: Math.max(0, r?.xStart || 0),
            xEnd: Math.max(0, r?.xEnd || 0),
            yStart: Math.max(0, r?.yStart || 0),
            yEnd: Math.max(0, r?.yEnd || 0),
          }),
          g = i4(),
          v = i8(),
          y = i8(),
          { nonce: b, disableStyleElements: x } = oq(),
          [k, w] = f.useState(!1),
          [S, C] = f.useState(!1),
          [E, j] = f.useState(!1),
          [R, P] = f.useState(!1),
          [T, A] = f.useState(!1),
          [O, I] = f.useState(oW),
          [M, N] = f.useState(oW),
          [z, D] = f.useState(oV),
          [L, $] = f.useState(oK),
          F = f.useRef(null),
          _ = f.useRef(null),
          B = f.useRef(null),
          H = f.useRef(null),
          q = f.useRef(null),
          U = f.useRef(null),
          W = f.useRef(null),
          V = f.useRef(null),
          K = f.useRef(0),
          X = f.useRef(0),
          Y = f.useRef(0),
          G = f.useRef(0),
          J = f.useRef("vertical"),
          Q = f.useRef(oU),
          Z = f.useRef(null);
        function ee(e) {
          let t = e ? j : C;
          (t(!0),
            (e ? v : y).start(500, () => {
              t(!1);
            }));
        }
        let et = iT((e) => {
            let t = e.x - Q.current.x,
              n = e.y - Q.current.y;
            ((Q.current = e), 0 !== n && ee(!0), 0 !== t && ee(!1));
          }),
          en = iT(() => {
            let e = _.current;
            e && null === Z.current && ((Z.current = e.style.scrollSnapType), (e.style.scrollSnapType = "none"));
          }),
          er = iT((e) => {
            if (0 !== e.button) return;
            if (null !== V.current) {
              let e = "vertical" === J.current ? q.current : U.current;
              if (e?.hasPointerCapture(V.current)) return;
            }
            ((V.current = e.pointerId),
              (K.current = e.clientY),
              (X.current = e.clientX),
              (J.current = e.currentTarget.getAttribute("data-orientation")));
            let t = _.current;
            t && ((Y.current = t.scrollTop), (G.current = t.scrollLeft), en());
            let n = "vertical" === J.current ? q.current : U.current;
            n?.setPointerCapture(e.pointerId);
          }),
          ei = iT((e) => {
            if (e.pointerId !== V.current) return;
            ((V.current = null),
              ("vertical" === J.current ? j : C)(!1),
              null !== Z.current && (_.current && (_.current.style.scrollSnapType = Z.current), (Z.current = null)));
            let t = "vertical" === J.current ? q.current : U.current;
            t?.hasPointerCapture(e.pointerId) && t.releasePointerCapture(e.pointerId);
          }),
          eo = iT((e) => {
            if (e.pointerId !== V.current) return;
            if (e.buttons % 2 == 0) return void ei(e);
            let t = _.current;
            if (!t) return;
            let n = "vertical" === J.current,
              r = n ? q.current : U.current,
              i = n ? B.current : H.current;
            if (!r || !i) return;
            let o = n ? "y" : "x",
              l = oL(i, "padding", o),
              a = oL(r, "margin", o),
              s = n ? r.offsetHeight : r.offsetWidth,
              u = (n ? i.offsetHeight : i.offsetWidth) - s - l - a,
              c = n ? e.clientY - K.current : e.clientX - X.current,
              d = n ? t.scrollHeight : t.scrollWidth,
              f = n ? t.clientHeight : t.clientWidth,
              p = (n ? Y.current : G.current) + (u <= 0 ? 0 : c / u) * (d - f);
            (n ? (t.scrollTop = p) : (t.scrollLeft = p), e.preventDefault(), ee(n));
          });
        function el(e) {
          P("touch" === e.pointerType);
        }
        function ea(e) {
          (el(e), "touch" !== e.pointerType && w(os(F.current, e.target)));
        }
        let es = f.useMemo(
            () => ({
              scrolling: S || E,
              hasOverflowX: !L.x,
              hasOverflowY: !L.y,
              overflowXStart: z.xStart,
              overflowXEnd: z.xEnd,
              overflowYStart: z.yStart,
              overflowYEnd: z.yEnd,
              cornerHidden: L.corner,
            }),
            [S, E, L.x, L.y, L.corner, z],
          ),
          eu = rl("div", e, {
            state: es,
            ref: [t, F],
            props: [
              {
                role: "presentation",
                onPointerEnter: ea,
                onPointerMove: ea,
                onPointerDown: el,
                onPointerLeave() {
                  w(!1);
                },
                style: {
                  position: "relative",
                  "--scroll-area-corner-height": `${O.height}px`,
                  "--scroll-area-corner-width": `${O.width}px`,
                },
              },
              u,
            ],
            stateAttributesMapping: o_,
          }),
          ec = f.useMemo(
            () => ({
              handlePointerDown: er,
              handlePointerMove: eo,
              handlePointerUp: ei,
              handleScroll: et,
              disableViewportSnap: en,
              cornerSize: O,
              setCornerSize: I,
              thumbSize: M,
              setThumbSize: N,
              hasMeasuredScrollbar: T,
              setHasMeasuredScrollbar: A,
              touchModality: R,
              cornerRef: W,
              scrollingX: S,
              scrollingY: E,
              hovering: k,
              setHovering: w,
              viewportRef: _,
              scrollbarYRef: B,
              scrollbarXRef: H,
              thumbYRef: q,
              thumbXRef: U,
              rootId: g,
              hiddenState: L,
              setHiddenState: $,
              overflowEdges: z,
              setOverflowEdges: D,
              viewportState: es,
              overflowEdgeThreshold: { xStart: c, xEnd: p, yStart: h, yEnd: m },
            }),
            [er, eo, ei, et, en, O, M, T, R, S, E, k, g, L, z, es, c, p, h, m],
          );
        return (0, d.jsxs)(oz.Provider, {
          value: ec,
          children: [
            !x &&
              ((i = b),
              (0, d.jsx)("style", {
                nonce: i,
                href: o$,
                precedence: "base-ui:low",
                children: `.${o$}{scrollbar-width:none}.${o$}::-webkit-scrollbar{display:none}`,
              })),
            eu,
          ],
        });
      });
    (e.s([], 64949), e.i(64949));
    let {
        userAgent: oY,
        platform: oG,
        maxTouchPoints: oJ,
      } = "u" < typeof navigator
        ? { userAgent: "", platform: "", maxTouchPoints: 0 }
        : {
            userAgent: navigator.userAgent,
            platform: navigator.platform ?? "",
            maxTouchPoints: navigator.maxTouchPoints ?? 0,
          },
      oQ = oY.toLowerCase(),
      oZ = oG.toLowerCase(),
      o0 = /^i(os$|p)/.test(oZ) || ("macintel" === oZ && oJ > 1),
      o1 = "android",
      o2 = oZ === o1 || oQ.includes(o1),
      o4 = !o0 && oZ.startsWith("mac"),
      o5 = oZ.startsWith("win"),
      o3 = !o2 && /^(linux|chrome os)/.test(oZ),
      o6 = o4 || o0;
    e.s(["android", 0, o2, "apple", 0, o6, "ios", 0, o0, "linux", 0, o3, "mac", 0, o4, "windows", 0, o5], 3720);
    var o9 = e.i(3720);
    let o7 = "u" > typeof CSS && !!CSS.supports?.("-webkit-backdrop-filter:none"),
      o8 = !o7 && oQ.includes("firefox"),
      le = !o7 && oQ.includes("chrom");
    e.s(["blink", 0, le, "gecko", 0, o8, "webkit", 0, o7], 79850);
    var lt = e.i(79850);
    e.s(["voiceOver", 0, o6], 99170);
    var ln = e.i(99170);
    let lr = /jsdom|happydom/.test(oQ);
    e.s(["jsdom", 0, lr], 36174);
    var li = e.i(36174);
    e.s(["engine", 0, lt, "env", 0, li, "os", 0, o9, "screenReader", 0, ln], 79214);
    var lo = e.i(79214),
      lo = lo;
    let ll = f.createContext(void 0),
      la = f.createContext(void 0);
    function ls() {
      let e = f.useContext(la);
      return e?.direction ?? "ltr";
    }
    function lu(e, t = Number.MIN_SAFE_INTEGER, n = Number.MAX_SAFE_INTEGER) {
      return Math.max(t, Math.min(e, n));
    }
    function lc(e, t) {
      if (t <= 0) return 0;
      let n = lu(e, 0, t),
        r = t - n,
        i = n <= 1,
        o = r <= 1;
      return i && o ? (n <= r ? 0 : t) : i ? 0 : o ? t : n;
    }
    let ld = [
        "--scroll-area-overflow-x-start",
        "--scroll-area-overflow-x-end",
        "--scroll-area-overflow-y-start",
        "--scroll-area-overflow-y-end",
      ],
      lf = !1,
      lp = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, ...o } = e,
          {
            viewportRef: l,
            scrollbarYRef: a,
            scrollbarXRef: s,
            thumbYRef: u,
            thumbXRef: c,
            cornerRef: p,
            cornerSize: h,
            setCornerSize: m,
            setThumbSize: g,
            rootId: v,
            setHiddenState: y,
            hiddenState: b,
            setHasMeasuredScrollbar: x,
            handleScroll: k,
            touchModality: w,
            setHovering: S,
            setOverflowEdges: C,
            overflowEdgeThreshold: E,
            viewportState: j,
          } = oD(),
          R = ls(),
          P = f.useRef(!0),
          T = f.useRef([NaN, NaN, NaN, NaN]),
          A = i8(),
          O = i8(),
          I = iT(() => {
            var e;
            let t,
              n,
              r = l.current,
              i = a.current,
              o = s.current,
              d = u.current,
              f = c.current,
              v = p.current;
            if (!r) return;
            let b = r.scrollHeight,
              k = r.scrollWidth,
              w = r.clientHeight,
              S = r.clientWidth,
              j = r.scrollTop,
              P = r.scrollLeft,
              A = T.current,
              O = Number.isNaN(A[0]);
            if (((A[0] = w), (A[1] = b), (A[2] = S), (A[3] = k), O && x(!0), 0 === b || 0 === k)) return;
            let I =
                ((t = (e = r).clientHeight >= e.scrollHeight),
                { y: t, x: (n = e.clientWidth >= e.scrollWidth), corner: t || n }),
              M = I.y,
              N = I.x,
              z = S / k,
              D = w / b,
              L = Math.max(0, k - S),
              $ = Math.max(0, b - w),
              F = 0,
              _ = 0;
            N || ((F = lc("rtl" === R ? -P : P, L)), (_ = L - F));
            let B = M ? 0 : lc(j, $),
              H = M ? 0 : $ - B,
              q = N ? 0 : S,
              U = M ? 0 : w,
              W = 0,
              V = 0;
            N || M || ((W = i?.offsetWidth || 0), (V = o?.offsetHeight || 0));
            let K = 0 === h.width && 0 === h.height,
              X = K ? W : 0,
              Y = K ? V : 0,
              G = oL(o, "padding", "x"),
              J = oL(i, "padding", "y"),
              Q = oL(f, "margin", "x"),
              Z = oL(d, "margin", "y"),
              ee = q - G - Q,
              et = U - J - Z,
              en = o ? Math.min(o.offsetWidth - X, ee) : ee,
              er = i ? Math.min(i.offsetHeight - Y, et) : et,
              ei = Math.max(16, en * z),
              eo = Math.max(16, er * D);
            if ((g((e) => lh(e, { width: ei, height: eo })), i && d)) {
              let e = i.offsetHeight - eo - J - Z,
                t = lm(d, "--scroll-area-thumb-height", j, $, b, eo, e);
              d.style.transform = `translate3d(0,${t}px,0)`;
            }
            if (o && f) {
              let e = o.offsetWidth - ei - G - Q,
                t = lm(f, "--scroll-area-thumb-width", "rtl" === R ? -P : P, L, k, ei, e);
              f.style.transform = `translate3d(${"rtl" === R ? -t : t}px,0,0)`;
            }
            let el = [F, _, B, H];
            (ld.forEach((e, t) => {
              r.style.setProperty(e, `${el[t]}px`);
            }),
              v && m((e) => lh(e, { width: W, height: V })),
              y((e) => lh(e, I)));
            let ea = {
              xStart: !N && F > E.xStart,
              xEnd: !N && _ > E.xEnd,
              yStart: !M && B > E.yStart,
              yEnd: !M && H > E.yEnd,
            };
            C((e) => lh(e, ea));
          });
        function M() {
          P.current = !1;
        }
        (iI(() => {
          lf ||
            lo.engine.webkit ||
            ("u" > typeof CSS &&
              "registerProperty" in CSS &&
              ld.forEach((e) => {
                try {
                  CSS.registerProperty({ name: e, syntax: "<length>", inherits: !1, initialValue: "0px" });
                } catch {}
              }),
            (lf = !0));
        }, []),
          iI(() => {
            queueMicrotask(I);
          }, [I, b, R, E.xStart, E.xEnd, E.yStart, E.yEnd]),
          iI(() => {
            l.current?.matches(":hover") && S(!0);
          }, [l, S]),
          iI(() => {
            let e = l.current;
            if ("u" < typeof ResizeObserver || !e) return;
            let t = !1,
              n = new ResizeObserver(() => {
                if (!t) {
                  t = !0;
                  let n = T.current;
                  if (
                    n[0] === e.clientHeight &&
                    n[1] === e.scrollHeight &&
                    n[2] === e.clientWidth &&
                    n[3] === e.scrollWidth
                  )
                    return;
                }
                I();
              });
            return (
              n.observe(e),
              O.start(0, () => {
                let t = e.getAnimations({ subtree: !0 });
                0 !== t.length &&
                  Promise.allSettled(t.map((e) => e.finished))
                    .then(I)
                    .catch(() => {});
              }),
              () => {
                (n.disconnect(), O.clear());
              }
            );
          }, [I, l, O]));
        let N = {
            role: "presentation",
            ...(v && { "data-id": `${v}-viewport` }),
            tabIndex: b.x && b.y ? -1 : 0,
            className: o$,
            style: { overflow: "scroll" },
            onScroll() {
              l.current &&
                (I(),
                (w || !P.current) && k({ x: l.current.scrollLeft, y: l.current.scrollTop }),
                A.start(100, () => {
                  P.current = !0;
                }));
            },
            onWheel: M,
            onPointerMove: M,
            onPointerEnter: M,
            onKeyDown: M,
          },
          z = rl("div", e, { ref: [t, l], state: j, props: [N, o], stateAttributesMapping: o_ }),
          D = f.useMemo(() => ({ computeThumbPosition: I }), [I]);
        return (0, d.jsx)(ll.Provider, { value: D, children: z });
      });
    function lh(e, t) {
      for (let n in t) if (e[n] !== t[n]) return t;
      return e;
    }
    function lm(e, t, n, r, i, o, l) {
      let a = lu(n, 0, r),
        s = n - a,
        u = Math.max(16, (o * i) / (i + Math.abs(s)));
      return (e.style.setProperty(t, s ? `${u}px` : ""), (r ? (a / r) * l : 0) + (s > 0 ? o - u : 0));
    }
    function lg(e, t, n, r) {
      return (
        e.addEventListener(t, n, r),
        () => {
          e.removeEventListener(t, n, r);
        }
      );
    }
    let lv = f.createContext(void 0),
      ly = f.forwardRef(function (e, t) {
        let { render: n, className: r, orientation: i = "vertical", keepMounted: o = !1, style: l, ...a } = e,
          {
            hovering: s,
            scrollingX: u,
            scrollingY: c,
            hiddenState: p,
            scrollbarYRef: h,
            scrollbarXRef: m,
            viewportRef: g,
            thumbYRef: v,
            thumbXRef: y,
            handlePointerDown: b,
            handlePointerUp: x,
            handleScroll: k,
            disableViewportSnap: w,
            rootId: S,
            thumbSize: C,
            hasMeasuredScrollbar: E,
            viewportState: j,
          } = oD(),
          R = "vertical" === i,
          P = { ...j, hovering: s, scrolling: R ? c : u, orientation: i },
          T = ls(),
          A = !E && !o,
          O = R ? p.y : p.x,
          I = o || !O;
        f.useEffect(() => {
          if (!I) return;
          let e = g.current,
            t = R ? h.current : m.current;
          if (t)
            return lg(
              t,
              "wheel",
              function (t) {
                if (!e || t.ctrlKey) return;
                let n = !R,
                  r = n ? "scrollLeft" : "scrollTop",
                  i = n ? t.deltaX : t.deltaY;
                if (0 === i) return;
                let o = n ? e.scrollWidth - e.clientWidth : e.scrollHeight - e.clientHeight,
                  l = n && "rtl" === T ? -o : 0,
                  a = n && "rtl" === T ? 0 : o,
                  s = e[r];
                (s <= l && i < 0) ||
                  (s >= a && i > 0) ||
                  (t.preventDefault(),
                  (e[r] = Math.min(a, Math.max(l, s + i))),
                  k({ x: e.scrollLeft, y: e.scrollTop }));
              },
              { passive: !1 },
            );
        }, [T, k, R, m, h, I, g]);
        let M = {
            ...(S && { "data-id": `${S}-scrollbar` }),
            onPointerDown(e) {
              if (0 !== e.button) return;
              let t = ou(e.nativeEvent),
                n = R ? v.current : y.current;
              if (n && os(n, t)) return;
              let r = g.current;
              if (!r) return;
              let i = R ? h.current : m.current;
              if (!n || !i) return;
              let o = R ? "y" : "x",
                l = oL(n, "margin", o),
                a = oL(i, "padding", o),
                s = R ? n.offsetHeight : n.offsetWidth,
                u = i.getBoundingClientRect(),
                c = R ? e.clientY - u.top - s / 2 - a + l / 2 : e.clientX - u.left - s / 2 - a + l / 2,
                d = R ? r.scrollHeight : r.scrollWidth,
                f = R ? r.clientHeight : r.clientWidth,
                p = (R ? i.offsetHeight : i.offsetWidth) - s - a - l;
              if (p <= 0) return;
              let x = c / p,
                S = d - f;
              (w(),
                R ? (r.scrollTop = x * S) : "rtl" === T ? (r.scrollLeft = -(1 - x) * S) : (r.scrollLeft = x * S),
                k({ x: r.scrollLeft, y: r.scrollTop }),
                b(e));
            },
            onPointerUp: x,
            onPointerCancel: x,
            style: {
              position: "absolute",
              touchAction: "none",
              WebkitUserSelect: "none",
              userSelect: "none",
              visibility: A ? "hidden" : void 0,
              ...(R
                ? {
                    top: 0,
                    bottom: "var(--scroll-area-corner-height)",
                    insetInlineEnd: 0,
                    "--scroll-area-thumb-height": `${C.height}px`,
                  }
                : {
                    insetInlineStart: 0,
                    insetInlineEnd: "var(--scroll-area-corner-width)",
                    bottom: 0,
                    "--scroll-area-thumb-width": `${C.width}px`,
                  }),
            },
          },
          N = rl("div", e, { ref: [t, R ? h : m], state: P, props: [M, a], stateAttributesMapping: o_ });
        return I ? (0, d.jsx)(lv.Provider, { value: i, children: N }) : null;
      }),
      lb = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, ...o } = e,
          { computeThumbPosition: l } = (function () {
            let e = f.useContext(ll);
            if (void 0 === e) throw Error(n3(55));
            return e;
          })(),
          { hasMeasuredScrollbar: a, viewportState: s } = oD(),
          u = f.useRef(null),
          c = f.useRef(a);
        return (
          iI(() => {
            if ("u" < typeof ResizeObserver) return;
            let e = !1,
              t = new ResizeObserver(() => {
                (e || ((e = !0), c.current)) && l();
              });
            return (
              u.current && t.observe(u.current),
              () => {
                t.disconnect();
              }
            );
          }, [l]),
          rl("div", e, {
            ref: [t, u],
            state: s,
            stateAttributesMapping: o_,
            props: [{ role: "presentation", style: { minWidth: "fit-content" } }, o],
          })
        );
      }),
      lx = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, ...o } = e,
          {
            thumbYRef: l,
            thumbXRef: a,
            handlePointerDown: s,
            handlePointerMove: u,
            handlePointerUp: c,
            scrollingX: d,
            scrollingY: p,
            hasMeasuredScrollbar: h,
          } = oD(),
          m = (function () {
            let e = f.useContext(lv);
            if (void 0 === e) throw Error(n3(54));
            return e;
          })(),
          g = "vertical" === m;
        return rl("div", e, {
          ref: [t, g ? l : a],
          state: { scrolling: g ? p : d, orientation: m },
          props: [
            {
              onPointerDown: s,
              onPointerMove: u,
              onPointerUp: c,
              onPointerCancel: c,
              style: {
                visibility: h ? void 0 : "hidden",
                ...(g ? { height: "var(--scroll-area-thumb-height)" } : { width: "var(--scroll-area-thumb-width)" }),
              },
            },
            o,
          ],
        });
      }),
      lk = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, ...o } = e,
          { cornerRef: l, cornerSize: a, hiddenState: s } = oD(),
          u = rl("div", e, {
            ref: [t, l],
            props: [
              { style: { position: "absolute", bottom: 0, insetInlineEnd: 0, width: a.width, height: a.height } },
              o,
            ],
          });
        return s.corner ? null : u;
      });
    e.s(
      ["Content", 0, lb, "Corner", 0, lk, "Root", 0, oX, "Scrollbar", 0, ly, "Thumb", 0, lx, "Viewport", 0, lp],
      36093,
    );
    var lw = e.i(36093),
      lw = lw;
    function lS({ className: e, children: t, ...n }) {
      return (0, d.jsxs)(lw.Root, {
        "data-slot": "scroll-area",
        className: ih("relative", e),
        ...n,
        children: [
          (0, d.jsx)(lw.Viewport, {
            "data-slot": "scroll-area-viewport",
            className:
              "size-full rounded-[inherit] transition-[color,box-shadow] outline-none focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1",
            children: t,
          }),
          (0, d.jsx)(lC, {}),
          (0, d.jsx)(lw.Corner, {}),
        ],
      });
    }
    function lC({ className: e, orientation: t = "vertical", ...n }) {
      return (0, d.jsx)(lw.Scrollbar, {
        "data-slot": "scroll-area-scrollbar",
        "data-orientation": t,
        orientation: t,
        className: ih(
          "flex touch-none p-px transition-colors select-none data-[orientation=horizontal]:h-2.5 data-[orientation=horizontal]:flex-col data-[orientation=horizontal]:border-t data-[orientation=horizontal]:border-t-transparent data-[orientation=vertical]:h-full data-[orientation=vertical]:w-2.5 data-[orientation=vertical]:border-l data-[orientation=vertical]:border-l-transparent",
          e,
        ),
        ...n,
        children: (0, d.jsx)(lw.Thumb, {
          "data-slot": "scroll-area-thumb",
          className: "relative flex-1 rounded-full bg-border",
        }),
      });
    }
    let lE = f.forwardRef(function (e, t) {
      let { className: n, render: r, orientation: i = "horizontal", style: o, ...l } = e;
      return rl("div", e, {
        state: { orientation: i },
        ref: t,
        props: [{ role: "separator", "aria-orientation": i }, l],
      });
    });
    function lj({ className: e, orientation: t = "horizontal", ...n }) {
      return (0, d.jsx)(lE, {
        "data-slot": "separator",
        orientation: t,
        className: ih(
          "shrink-0 bg-border data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:w-px data-[orientation=vertical]:self-stretch",
          e,
        ),
        ...n,
      });
    }
    (e.s([], 14651), e.i(14651));
    let lR = f.createContext(void 0);
    function lP(e) {
      let t = f.useContext(lR);
      if (!e && void 0 === t) throw Error(n3(27));
      return t;
    }
    (((u = {}).open = "data-open"),
      (u.closed = "data-closed"),
      (u[(u.startingStyle = ob.startingStyle)] = "startingStyle"),
      (u[(u.endingStyle = ob.endingStyle)] = "endingStyle"),
      (u.anchorHidden = "data-anchor-hidden"),
      (u.side = "data-side"),
      (u.align = "data-align"));
    let lT = { "data-popup-open": "" },
      lA = { "data-open": "" },
      lO = { "data-closed": "" },
      lI = { "data-anchor-hidden": "" },
      lM = { open: (e) => (e ? lT : null) },
      lN = { open: (e) => (e ? lA : lO), anchorHidden: (e) => (e ? lI : null) },
      lz = { ...lN, ...ow },
      lD = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, forceRender: o = !1, ...l } = e,
          a = lP(),
          s = a.useState("open"),
          u = a.useState("nested"),
          c = a.useState("mounted");
        return rl("div", e, {
          state: { open: s, transitionStatus: a.useState("transitionStatus") },
          ref: [a.context.backdropRef, t],
          stateAttributesMapping: lz,
          props: [{ role: "presentation", hidden: !c, style: { userSelect: "none", WebkitUserSelect: "none" } }, l],
          enabled: o || !u,
        });
      });
    var oT = oT;
    let lL = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, disabled: o = !1, nativeButton: l = !0, ...a } = e,
          s = lP(),
          u = s.useState("open"),
          { getButtonProps: c, buttonRef: d } = iD({ disabled: o, native: l });
        return rl("button", e, {
          state: { disabled: o },
          ref: [t, d],
          props: [
            {
              onClick: function (e) {
                u && s.setOpen(!1, oP(oT.closePress, e.nativeEvent));
              },
            },
            a,
            c,
          ],
        });
      }),
      l$ = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, id: o, ...l } = e,
          a = lP(),
          s = i4(o);
        return (a.useSyncedValueWithCleanup("descriptionElementId", s), rl("p", e, { ref: t, props: [{ id: s }, l] }));
      });
    function lF(...e) {
      return () => {
        for (let t = 0; t < e.length; t += 1) {
          let n = e[t];
          n && n();
        }
      };
    }
    function l_(e) {
      let t = n9(lB, e).current;
      return ((t.next = e), iI(t.effect), t);
    }
    function lB(e) {
      let t = {
        current: e,
        next: e,
        effect: () => {
          t.current = t.next;
        },
      };
      return t;
    }
    var lo = lo,
      lo = lo;
    let lH = {
        clipPath: "inset(50%)",
        overflow: "hidden",
        whiteSpace: "nowrap",
        border: 0,
        padding: 0,
        width: 1,
        height: 1,
        margin: -1,
      },
      lq = { ...lH, position: "fixed", top: 0, left: 0 };
    ({ ...lH, position: "absolute" });
    let lU = f.forwardRef(function (e, t) {
        let [n, r] = f.useState();
        return (
          iI(() => {
            lo.screenReader.voiceOver && lo.engine.webkit && r("button");
          }, []),
          (0, d.jsx)("span", {
            ...e,
            ref: t,
            style: lq,
            "aria-hidden": !n || void 0,
            tabIndex: 0,
            role: n,
            "data-base-ui-focus-guard": "",
          })
        );
      }),
      lW = "data-base-ui-focusable";
    function lV(e, t) {
      return (
        null != t && ("composedPath" in e ? e.composedPath().includes(t) : null != e.target && t.contains(e.target))
      );
    }
    function lK(e) {
      return (
        iw(e) &&
        e.matches(
          "input:not([type='hidden']):not([disabled]),[contenteditable]:not([contenteditable='false']),textarea:not([disabled])",
        )
      );
    }
    function lX(e) {
      return !!e && "combobox" === e.getAttribute("role") && lK(e);
    }
    function lY(e) {
      return e ? (e.hasAttribute(lW) ? e : e.querySelector(`[${lW}]`) || e) : null;
    }
    var lo = lo;
    function lG(e) {
      return (
        !lo.env.jsdom &&
        ((!lo.os.android && 0 === e.width && 0 === e.height) ||
          (lo.os.android &&
            1 === e.width &&
            1 === e.height &&
            0 === e.pressure &&
            0 === e.detail &&
            "mouse" === e.pointerType) ||
          (e.width < 1 && e.height < 1 && 0 === e.pressure && 0 === e.detail && "touch" === e.pointerType))
      );
    }
    function lJ(e, t) {
      let n = ["mouse", "pen"];
      return (t || n.push("", void 0), n.includes(e));
    }
    function lQ(e, t) {
      return t < 0 || t >= e.length;
    }
    function lZ(e, { startingIndex: t = -1, decrement: n = !1, disabledIndices: r, amount: i = 1 } = {}) {
      let o = t;
      do o += n ? -i : i;
      while (o >= 0 && o <= e.length - 1 && l0(e, o, r));
      return o;
    }
    function l0(e, t, n) {
      if ("function" == typeof n ? n(t) : (n?.includes(t) ?? !1)) return !0;
      let r = e[t];
      return (
        !!r &&
        (!!(!l1(r) || r.matches(":disabled")) ||
          (!n && (r.hasAttribute("disabled") || "true" === r.getAttribute("aria-disabled"))))
      );
    }
    function l1(e, t = e ? iE(e) : null) {
      var n;
      return (
        !!e &&
        !!e.isConnected &&
        !!t &&
        "hidden" !== (n = t).visibility &&
        "collapse" !== n.visibility &&
        ("function" == typeof e.checkVisibility
          ? e.checkVisibility()
          : "none" !== t.display && "contents" !== t.display)
      );
    }
    function l2(e) {
      for (let t of Array.from(e.children)) if ("summary" === iy(t)) return t;
      return null;
    }
    function l4(e) {
      let t = e ? iy(e) : "";
      return (
        null != e &&
        e.matches(
          'a[href],button,input,select,textarea,summary,details,iframe,object,embed,[tabindex],[contenteditable]:not([contenteditable="false"]),audio[controls],video[controls]',
        ) &&
        ("summary" !== t ||
          (null != e.parentElement && "details" === iy(e.parentElement) && l2(e.parentElement) === e)) &&
        ("details" !== t || null == l2(e)) &&
        ("input" !== t || "hidden" !== e.type)
      );
    }
    function l5(e) {
      if (!l4(e) || !e.isConnected || e.matches(":disabled")) return !1;
      for (
        let t = e;
        t;
        t = (function (e) {
          let t = e.assignedSlot;
          if (t) return t;
          if (e.parentElement) return e.parentElement;
          let n = e.getRootNode();
          return iS(n) ? n.host : null;
        })(t)
      ) {
        let n = t !== e,
          r = "slot" === iy(t);
        if (
          t.hasAttribute("inert") ||
          (n &&
            "details" === iy(t) &&
            !t.open &&
            !(function (e, t) {
              let n = l2(t);
              return !!n && (e === n || os(n, e));
            })(e, t)) ||
          t.hasAttribute("hidden") ||
          (!r &&
            !(function (e, t) {
              let n = iE(e);
              return t ? "none" !== n.display : l1(e, n);
            })(t, n))
        )
          return !1;
      }
      return !0;
    }
    function l3(e) {
      let t = e.tabIndex;
      if (t < 0) {
        let t = iy(e);
        if ("details" === t || "audio" === t || "video" === t || (iw(e) && e.isContentEditable)) return 0;
      }
      return t;
    }
    function l6(e) {
      return "input" !== iy(e) ? null : "radio" === e.type && "" !== e.name ? e : null;
    }
    function l9(e) {
      if (iw(e) && "slot" === iy(e)) {
        let t = e.assignedElements({ flatten: !0 });
        if (t.length > 0) return t;
      }
      return iw(e) && e.shadowRoot ? Array.from(e.shadowRoot.children) : Array.from(e.children);
    }
    function l7(e) {
      return l5(e) && l3(e) >= 0;
    }
    function l8(e) {
      let t = [];
      return (
        !(function e(t, n) {
          l9(t).forEach((t) => {
            (l4(t) && n.push(t), e(t, n));
          });
        })(e, t),
        t.filter(l5)
      );
    }
    function ae(e) {
      let t = l8(e);
      return t.filter(
        (e) =>
          l3(e) >= 0 &&
          (function (e, t) {
            let n = l6(e);
            if (!n) return !0;
            let r = t.find((e) => {
              let t = l6(e);
              return t?.name === n.name && t.form === n.form && t.checked;
            });
            return r
              ? r === n
              : t.find((e) => {
                  let t = l6(e);
                  return t?.name === n.name && t.form === n.form;
                }) === n;
          })(e, t),
      );
    }
    function at(e, t) {
      let n = ae(e),
        r = n.length;
      if (0 === r) return;
      let i = oa(ol(e)),
        o = n.indexOf(i);
      return n[-1 === o ? (1 === t ? 0 : r - 1) : o + t];
    }
    function an(e) {
      return at(ol(e).body, 1) || e;
    }
    function ar(e) {
      return at(ol(e).body, -1) || e;
    }
    function ai(e, t) {
      let n = t || e.currentTarget,
        r = e.relatedTarget;
      return !r || !os(n, r);
    }
    function ao(e) {
      let t = [];
      (!(function e(t, n, r) {
        l9(t).forEach((t) => {
          (iw(t) && t.matches(n) && r.push(t), e(t, n, r));
        });
      })(e, "[data-tabindex]", t),
        t.forEach((e) => {
          let t = e.dataset.tabindex;
          (delete e.dataset.tabindex, t ? e.setAttribute("tabindex", t) : e.removeAttribute("tabindex"));
        }));
    }
    function al(e, t, n = !0) {
      return e
        .filter((e) => e.parentId === t)
        .flatMap((t) => [...(!n || t.context?.open ? [t] : []), ...al(e, t.id, n)]);
    }
    function aa(e, t) {
      let n = [],
        r = e.find((e) => e.id === t)?.parentId;
      for (; r; ) {
        let t = e.find((e) => e.id === r);
        ((r = t?.parentId), t && (n = n.concat(t)));
      }
      return n;
    }
    var oT = oT;
    function as(e) {
      return `data-base-ui-${e}`;
    }
    let au = 0;
    function ac(e, t = {}) {
      let { preventScroll: n = !1, sync: r = !1, shouldFocus: i } = t;
      function o() {
        (!i || i()) && e?.focus({ preventScroll: n });
      }
      if ((cancelAnimationFrame(au), r)) return (o(), rr);
      let l = requestAnimationFrame(o);
      return (
        (au = l),
        () => {
          au === l && (cancelAnimationFrame(l), (au = 0));
        }
      );
    }
    let ad = { inert: new WeakMap(), "aria-hidden": new WeakMap() },
      af = "data-base-ui-inert",
      ap = { inert: new WeakSet(), "aria-hidden": new WeakSet() },
      ah = new WeakMap(),
      am = 0,
      ag = (e, t) =>
        t
          .map((t) => {
            if (e.contains(t)) return t;
            let n = (function e(t) {
              return t ? (iS(t) ? t.host : e(t.parentNode)) : null;
            })(t);
            return e.contains(n) ? n : null;
          })
          .filter((e) => null != e),
      av = (e) => {
        let t = new Set();
        return (
          e.forEach((e) => {
            let n = e;
            for (; n && !t.has(n); ) (t.add(n), (n = n.parentNode));
          }),
          t
        );
      },
      ay = (e, t, n) => {
        let r = [],
          i = (e) => {
            !e ||
              n.has(e) ||
              Array.from(e.children).forEach((e) => {
                "script" !== iy(e) && (t.has(e) ? i(e) : r.push(e));
              });
          };
        return (i(e), r);
      };
    function ab(e, t = {}) {
      let { ariaHidden: n = !1, inert: r = !1, mark: i = !0 } = t,
        o = ol(e[0]).body;
      return (function (e, t, n, r, { mark: i = !0 }) {
        let o = null;
        r ? (o = "inert") : n && (o = "aria-hidden");
        let l = null,
          a = null,
          s = ag(t, e),
          u = i ? ay(t, av(s), new Set(s)) : [],
          c = [],
          d = [];
        if (o) {
          let e = ad[o],
            n = ap[o];
          ((a = n), (l = e));
          let r = ag(t, Array.from(t.querySelectorAll("[aria-live]"))),
            i = s.concat(r);
          ay(t, av(i), new Set(i)).forEach((t) => {
            let r = t.getAttribute(o),
              i = null !== r && "false" !== r,
              l = (e.get(t) || 0) + 1;
            (e.set(t, l), c.push(t), 1 === l && i && n.add(t), i || t.setAttribute(o, "inert" === o ? "" : "true"));
          });
        }
        return (
          i &&
            u.forEach((e) => {
              let t = (ah.get(e) || 0) + 1;
              (ah.set(e, t), d.push(e), 1 === t && e.setAttribute(af, ""));
            }),
          (am += 1),
          () => {
            (l &&
              c.forEach((e) => {
                let t = (l.get(e) || 0) - 1;
                (l.set(e, t), t || (!a?.has(e) && o && e.removeAttribute(o), a?.delete(e)));
              }),
              i &&
                d.forEach((e) => {
                  let t = (ah.get(e) || 0) - 1;
                  (ah.set(e, t), t || e.removeAttribute(af));
                }),
              (am -= 1) ||
                ((ad.inert = new WeakMap()),
                (ad["aria-hidden"] = new WeakMap()),
                (ap.inert = new WeakSet()),
                (ap["aria-hidden"] = new WeakSet()),
                (ah = new WeakMap())));
          }
        );
      })(e, o, n, r, { mark: i });
    }
    var oT = oT;
    let ax = "data-base-ui-click-trigger",
      ak = { clipPath: "inset(50%)", position: "fixed", top: 0, left: 0 },
      aw = f.createContext(null),
      aS = as("portal"),
      aC = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, children: o, container: l, ...a } = e,
          {
            node: s,
            nodeId: u,
            subtree: c,
          } = (function (e = {}) {
            let { ref: t, container: n, componentProps: r = ro, elementProps: i } = e,
              o = i2(),
              l = f.useContext(aw),
              a = l?.portalNode,
              [s, u] = f.useState(null),
              [c, d] = f.useState(null),
              p = iT((e) => {
                null !== e && d(e);
              }),
              h = f.useRef(null);
            iI(() => {
              if (null === n) {
                h.current && ((h.current = null), d(null), u(null));
                return;
              }
              let e = (n && (ix(n) ? n : n.current)) ?? a ?? document.body;
              if (null == e) {
                h.current && ((h.current = null), d(null), u(null));
                return;
              }
              h.current !== e && ((h.current = e), d(null), u(e));
            }, [n, a]);
            let m = rl("div", r, { ref: [t, p], props: [{ id: o, [aS]: "" }, i] }),
              g = s && m ? op.createPortal(m, s) : null;
            return { node: c, nodeId: f.isValidElement(m) ? m.props.id : void 0, subtree: g };
          })({ container: l, ref: t, componentProps: e, elementProps: a }),
          p = f.useRef(null),
          h = f.useRef(null),
          m = f.useRef(null),
          g = f.useRef(null),
          [v, y] = f.useState(null),
          b = f.useRef(!1),
          x = v?.modal,
          k = v?.open,
          w = !!v && !v.modal && v.open && !!s;
        (f.useEffect(() => {
          if (s && !x) return lF(lg(s, "focusin", e, !0), lg(s, "focusout", e, !0));
          function e(e) {
            s &&
              e.relatedTarget &&
              ai(e) &&
              ("focusin" === e.type
                ? b.current && (ao(s), (b.current = !1))
                : (ae(s).forEach((e) => {
                    ((e.dataset.tabindex = e.getAttribute("tabindex") || ""), e.setAttribute("tabindex", "-1"));
                  }),
                  (b.current = !0)));
          }
        }, [s, x]),
          iI(() => {
            s && !0 === k && b.current && (ao(s), (b.current = !1));
          }, [k, s]));
        let S = f.useMemo(
          () => ({
            beforeOutsideRef: p,
            afterOutsideRef: h,
            beforeInsideRef: m,
            afterInsideRef: g,
            portalNode: s,
            setFocusManagerState: y,
          }),
          [s],
        );
        return (0, d.jsxs)(f.Fragment, {
          children: [
            c,
            (0, d.jsxs)(aw.Provider, {
              value: S,
              children: [
                w &&
                  s &&
                  (0, d.jsx)(lU, {
                    "data-type": "outside",
                    ref: p,
                    onFocus: (e) => {
                      if (ai(e, s)) m.current?.focus();
                      else {
                        let e = ar(v ? v.domReference : null);
                        e?.focus();
                      }
                    },
                  }),
                w && s && (0, d.jsx)("span", { "aria-owns": u, style: ak }),
                s && op.createPortal(o, s),
                w &&
                  s &&
                  (0, d.jsx)(lU, {
                    "data-type": "outside",
                    ref: h,
                    onFocus: (e) => {
                      if (ai(e, s)) g.current?.focus();
                      else {
                        let t = an(v ? v.domReference : null);
                        (t?.focus(), v?.closeOnFocusOut && v?.onOpenChange(!1, oP(oT.focusOut, e.nativeEvent)));
                      }
                    },
                  }),
              ],
            }),
          ],
        });
      }),
      aE = f.createContext(null),
      aj = f.createContext(null),
      aR = (e) => {
        let t = f.useContext(aj);
        return e ?? t;
      },
      aP = [];
    function aT() {
      aP = aP.filter((e) => e.deref()?.isConnected);
    }
    function aA(e) {
      (aT(), e && "body" !== iy(e) && (aP.push(new WeakRef(e)), aP.length > 20 && (aP = aP.slice(-20))));
    }
    function aO() {
      return (aT(), aP[aP.length - 1]?.deref());
    }
    function aI(e) {
      if (
        (e.hasAttribute("tabindex") && !e.hasAttribute("data-tabindex")) ||
        !e.getAttribute("role")?.includes("dialog")
      )
        return;
      let t = l8(e).filter((e) => {
          let t = e.getAttribute("data-tabindex") || "";
          return l7(e) || (e.hasAttribute("data-tabindex") && !t.startsWith("-"));
        }),
        n = e.getAttribute("tabindex");
      0 === t.length
        ? "0" !== n && (e.setAttribute("tabindex", "0"), e.setAttribute("data-tabindex", "0"))
        : ("-1" !== n || (e.hasAttribute("data-tabindex") && "-1" !== e.getAttribute("data-tabindex"))) &&
          (e.setAttribute("tabindex", "-1"), e.setAttribute("data-tabindex", "-1"));
    }
    function aM(e) {
      let {
          context: t,
          children: n,
          disabled: r = !1,
          initialFocus: i = !0,
          returnFocus: o = !0,
          restoreFocus: l = !1,
          modal: a = !0,
          closeOnFocusOut: s = !0,
          openInteractionType: u = "",
          nextFocusableElement: c,
          previousFocusableElement: p,
          beforeContentFocusGuardRef: h,
          externalTree: m,
          getInsideElements: g,
        } = e,
        v = "rootStore" in t ? t.rootStore : t,
        y = v.useState("open"),
        b = v.useState("domReferenceElement"),
        x = v.useState("floatingElement"),
        { events: k, dataRef: w } = v.context,
        S = iT(() => w.current.floatingContext?.nodeId),
        C = lX(b) && !1 === i,
        E = l_(i),
        j = l_(o),
        R = l_(u),
        P = l_(y),
        T = aR(m),
        A = f.useContext(aw),
        O = f.useRef(!1),
        I = f.useRef(!1),
        M = f.useRef(!1),
        N = f.useRef(null),
        z = f.useRef(""),
        D = f.useRef(""),
        L = f.useRef(null),
        $ = f.useRef(null),
        F = n7(L, h, A?.beforeInsideRef),
        _ = n7($, A?.afterInsideRef),
        B = i8(),
        H = i8(),
        q = og(),
        U = null != A,
        W = lY(x),
        V = iT((e = W) => (e ? ae(e) : [])),
        K = iT(() => g?.().filter((e) => null != e) ?? []);
      (f.useEffect(() => {
        if (!r && a)
          return lg(ol(W), "keydown", function (e) {
            "Tab" === e.key && os(W, oa(ol(W))) && 0 === V().length && !C && (e.preventDefault(), e.stopPropagation());
          });
      }, [r, W, a, C, V]),
        f.useEffect(() => {
          if (r || !y) return;
          let e = ol(W);
          function t() {
            M.current = !1;
          }
          return lF(
            lg(
              e,
              "pointerdown",
              function (e) {
                let t = ou(e),
                  n = K();
                ((M.current = !(os(x, t) || os(b, t) || os(A?.portalNode, t) || n.some((e) => e === t || os(e, t)))),
                  (D.current = e.pointerType || "keyboard"),
                  t?.closest(`[${ax}]`) &&
                    ((I.current = !0),
                    H.start(0, () => {
                      I.current = !1;
                    })));
              },
              !0,
            ),
            lg(e, "pointerup", t, !0),
            lg(e, "pointercancel", t, !0),
            lg(
              e,
              "keydown",
              function () {
                D.current = "keyboard";
              },
              !0,
            ),
            t,
          );
        }, [r, x, b, W, y, A, H, K]),
        f.useEffect(() => {
          if (r || !s) return;
          let e = ol(W);
          function t(t) {
            let n = t.relatedTarget,
              r = t.currentTarget,
              i = ou(t);
            (a && null == n && null != i && os(x, i) && aA(i),
              queueMicrotask(() => {
                let o = S(),
                  s = v.context.triggerElements,
                  u = K(),
                  d =
                    n?.hasAttribute(as("focus-guard")) &&
                    [
                      L.current,
                      $.current,
                      A?.beforeInsideRef.current,
                      A?.afterInsideRef.current,
                      A?.beforeOutsideRef.current,
                      A?.afterOutsideRef.current,
                      ov(p),
                      ov(c),
                    ].includes(n),
                  f = !(
                    os(b, n) ||
                    os(x, n) ||
                    os(n, x) ||
                    os(A?.portalNode, n) ||
                    u.some((e) => e === n || os(e, n)) ||
                    s.hasMatchingElement((e) => os(e, n)) ||
                    d ||
                    (T &&
                      (al(T.nodesRef.current, o).find(
                        (e) => os(e.context?.elements.floating, n) || os(e.context?.elements.domReference, n),
                      ) ||
                        aa(T.nodesRef.current, o).find(
                          (e) =>
                            [e.context?.elements.floating, lY(e.context?.elements.floating)].includes(n) ||
                            e.context?.elements.domReference === n,
                        )))
                  );
                if ((r === b && W && aI(W), l && r !== b && !l1(i) && oa(e) === e.body)) {
                  if (iw(W) && (W.focus(), "popup" === l))
                    return void q.request(() => {
                      W.focus();
                    });
                  let e = V(),
                    t = N.current,
                    n = (t && e.includes(t) ? t : null) || e[e.length - 1] || W;
                  iw(n) && n.focus();
                }
                if (w.current.insideReactTree) {
                  w.current.insideReactTree = !1;
                  return;
                }
                (C || !a) &&
                  n &&
                  f &&
                  !I.current &&
                  (C || n !== aO()) &&
                  ((O.current = !0), v.setOpen(!1, oP(oT.focusOut, t)));
              }));
          }
          let n = iw(b) ? b : null;
          if (x || n)
            return lF(
              n && lg(n, "focusout", t),
              n &&
                lg(n, "pointerdown", function () {
                  ((I.current = !0),
                    H.start(0, () => {
                      I.current = !1;
                    }));
                }),
              x &&
                lg(x, "focusin", function (e) {
                  let t = ou(e);
                  l7(t) && (N.current = t);
                }),
              x && lg(x, "focusout", t),
              x &&
                A &&
                lg(
                  x,
                  "focusout",
                  function () {
                    M.current ||
                      ((w.current.insideReactTree = !0),
                      B.start(0, () => {
                        w.current.insideReactTree = !1;
                      }));
                  },
                  !0,
                ),
            );
        }, [r, b, x, W, a, T, A, v, s, l, V, C, S, w, B, H, q, c, p, K]),
        f.useEffect(() => {
          if (r || !x || !y) return;
          let e = Array.from(A?.portalNode?.querySelectorAll(`[${as("portal")}]`) || []),
            t = T ? aa(T.nodesRef.current, S()) : [],
            n = t.find((e) => lX(e.context?.elements.domReference || null))?.context?.elements.domReference,
            i = ab(
              [
                x,
                ...e,
                L.current,
                $.current,
                A?.beforeOutsideRef.current,
                A?.afterOutsideRef.current,
                ...K(),
                n,
                ov(p),
                ov(c),
                C ? b : null,
              ].filter((e) => null != e),
              { ariaHidden: a || C, mark: !1 },
            ),
            o = ab([x, ...e].filter((e) => null != e));
          return () => {
            (o(), i());
          };
        }, [y, r, b, x, a, A, C, T, S, c, p, K]),
        iI(() => {
          if (!y || r || !iw(W)) return;
          ((z.current = ""), (D.current = ""));
          let e = ol(W),
            t = oa(e);
          queueMicrotask(() => {
            let n,
              r = E.current,
              i = "function" == typeof r ? r(R.current || "") : r;
            if (void 0 === i || !1 === i || os(W, t)) return;
            let o = null,
              l = () => (null == o && (o = V(W)), o[0] || W);
            n = (n = !0 === i || null === i ? l() : ov(i)) || l();
            let a = os(W, oa(e));
            ac(n, {
              preventScroll: n === W,
              shouldFocus() {
                if (!P.current) return !1;
                if (a) return !0;
                let t = oa(e);
                return !(t !== n && os(W, t));
              },
            });
          });
        }, [r, y, W, V, E, R, P]),
        iI(() => {
          if (r || !W) return;
          let e = ol(W),
            t = oa(e),
            n = null == R.current;
          function i(e) {
            var t, n, r;
            let i;
            if (
              (e.open ||
                ((t = e.nativeEvent),
                (n = D.current),
                (i = ib(ou(t))),
                (z.current =
                  t instanceof i.KeyboardEvent
                    ? "keyboard"
                    : t instanceof i.FocusEvent
                      ? n || "keyboard"
                      : "pointerType" in t
                        ? t.pointerType || "keyboard"
                        : "touches" in t
                          ? "touch"
                          : t instanceof i.MouseEvent
                            ? n || (0 === t.detail ? "keyboard" : "mouse")
                            : "")),
              e.reason === oT.triggerHover && "mouseleave" === e.nativeEvent.type && (O.current = !0),
              e.reason === oT.outsidePress)
            )
              if (e.nested) O.current = !1;
              else if (
                ("" === (r = e.nativeEvent).pointerType && r.isTrusted) ||
                (lo.os.android && r.pointerType
                  ? "click" === r.type && 1 === r.buttons
                  : 0 === r.detail && !r.pointerType) ||
                lG(e.nativeEvent)
              )
                O.current = !1;
              else {
                let e = !1;
                (ol(W)
                  .createElement("div")
                  .focus({
                    get preventScroll() {
                      return ((e = !0), !1);
                    },
                  }),
                  e ? (O.current = !1) : (O.current = !0));
              }
          }
          return (
            aA(t),
            k.on("openchange", i),
            () => {
              k.off("openchange", i);
              let r = oa(e),
                o = K(),
                l =
                  os(x, r) ||
                  o.some((e) => e === r || os(e, r)) ||
                  (T && al(T.nodesRef.current, S(), !1).some((e) => os(e.context?.elements.floating, r))),
                a = j.current,
                s = z.current,
                u = (function (e) {
                  let r = j.current,
                    i = "function" == typeof r ? r(e) : r;
                  if (void 0 === i || !1 === i) return null;
                  null === i && (i = !0);
                  let o = b?.isConnected ? b : null,
                    l = t?.isConnected && "body" !== iy(t) ? t : null,
                    a = n ? l || o : o || l;
                  return (a || (a = aO() || null), "boolean" == typeof i) ? a : ov(i) || a || null;
                })(s);
              queueMicrotask(() => {
                let t = u ? (l7(u) ? u : ae(u)[0] || u) : null;
                if (a && !O.current && iw(t) && ("boolean" != typeof a || t === r || r === e.body || l)) {
                  let e = { preventScroll: !0 };
                  ("keyboard" === s && (e.focusVisible = !0), t.focus(e));
                }
                O.current = !1;
              });
            }
          );
        }, [r, x, W, j, R, k, T, b, S, K]),
        iI(() => {
          if (!lo.engine.webkit || y || !x) return;
          let e = oa(ol(x));
          iw(e) && lK(e) && os(x, e) && e.blur();
        }, [y, x]),
        iI(() => {
          if (!r && A)
            return (
              A.setFocusManagerState({
                modal: a,
                closeOnFocusOut: s,
                open: y,
                onOpenChange: v.setOpen,
                domReference: b,
              }),
              () => {
                A.setFocusManagerState(null);
              }
            );
        }, [r, A, a, y, v, s, b]),
        iI(() => {
          if (!r && W)
            return (
              aI(W),
              () => {
                queueMicrotask(aT);
              }
            );
        }, [r, W]));
      let X = !r && (!a || !C) && (U || a);
      return (0, d.jsxs)(f.Fragment, {
        children: [
          X &&
            (0, d.jsx)(lU, {
              "data-type": "inside",
              ref: F,
              onFocus: (e) => {
                if (a) {
                  let e = V();
                  ac(e[e.length - 1]);
                } else if (A?.portalNode)
                  if (((O.current = !1), ai(e, A.portalNode))) {
                    let e = an(b);
                    e?.focus();
                  } else ov(p ?? A.beforeOutsideRef)?.focus();
              },
            }),
          n,
          X &&
            (0, d.jsx)(lU, {
              "data-type": "inside",
              ref: _,
              onFocus: (e) => {
                if (a) ac(V()[0]);
                else if (A?.portalNode)
                  if ((s && (O.current = !0), ai(e, A.portalNode))) {
                    let e = ar(b);
                    e?.focus();
                  } else ov(c ?? A.afterOutsideRef)?.focus();
              },
            }),
        ],
      });
    }
    let aN = f.createContext(void 0);
    function az() {
      let e = f.useContext(aN);
      if (void 0 === e) throw Error(n3(26));
      return e;
    }
    let aD = "ArrowUp",
      aL = "ArrowDown",
      a$ = "ArrowLeft",
      aF = "ArrowRight",
      a_ = "Home",
      aB = new Set([aD, aL, a$, aF, a_, "End"]),
      aH = ["Shift", "Control", "Alt", "Meta"];
    function aq(e) {
      return !!((iw(e) && "INPUT" === e.tagName && null != e.selectionStart) || (iw(e) && "TEXTAREA" === e.tagName));
    }
    function aU(e, t, n, r) {
      if (!e || !t || !t.scrollTo) return;
      let i = e.scrollLeft,
        o = e.scrollTop,
        l = e.clientWidth < e.scrollWidth,
        a = e.clientHeight < e.scrollHeight;
      if (l && "vertical" !== r) {
        let r = aW(e, t, "left"),
          o = aV(e),
          l = aV(t);
        ("ltr" === n &&
          (r + t.offsetWidth + l.scrollMarginRight > e.scrollLeft + e.clientWidth - o.scrollPaddingRight
            ? (i = r + t.offsetWidth + l.scrollMarginRight - e.clientWidth + o.scrollPaddingRight)
            : r - l.scrollMarginLeft < e.scrollLeft + o.scrollPaddingLeft &&
              (i = r - l.scrollMarginLeft - o.scrollPaddingLeft)),
          "rtl" === n &&
            (r - l.scrollMarginLeft < e.scrollLeft + o.scrollPaddingLeft
              ? (i = r - l.scrollMarginLeft - o.scrollPaddingLeft)
              : r + t.offsetWidth + l.scrollMarginRight > e.scrollLeft + e.clientWidth - o.scrollPaddingRight &&
                (i = r + t.offsetWidth + l.scrollMarginRight - e.clientWidth + o.scrollPaddingRight)));
      }
      if (a && "horizontal" !== r) {
        let n = aW(e, t, "top"),
          r = aV(e),
          i = aV(t);
        n - i.scrollMarginTop < e.scrollTop + r.scrollPaddingTop
          ? (o = n - i.scrollMarginTop - r.scrollPaddingTop)
          : n + t.offsetHeight + i.scrollMarginBottom > e.scrollTop + e.clientHeight - r.scrollPaddingBottom &&
            (o = n + t.offsetHeight + i.scrollMarginBottom - e.clientHeight + r.scrollPaddingBottom);
      }
      e.scrollTo({ left: i, top: o, behavior: "auto" });
    }
    function aW(e, t, n) {
      let r = "left" === n ? "offsetLeft" : "offsetTop",
        i = 0;
      for (; t.offsetParent && ((i += t[r]), t.offsetParent !== e); ) t = t.offsetParent;
      return i;
    }
    function aV(e) {
      let t = getComputedStyle(e);
      return {
        scrollMarginTop: parseFloat(t.scrollMarginTop) || 0,
        scrollMarginRight: parseFloat(t.scrollMarginRight) || 0,
        scrollMarginBottom: parseFloat(t.scrollMarginBottom) || 0,
        scrollMarginLeft: parseFloat(t.scrollMarginLeft) || 0,
        scrollPaddingTop: parseFloat(t.scrollPaddingTop) || 0,
        scrollPaddingRight: parseFloat(t.scrollPaddingRight) || 0,
        scrollPaddingBottom: parseFloat(t.scrollPaddingBottom) || 0,
        scrollPaddingLeft: parseFloat(t.scrollPaddingLeft) || 0,
      };
    }
    var aK = e.i(2239),
      aX = e.i(30224);
    let aY =
      rt >= 19
        ? function (e, t, n, r, i) {
            let o;
            if (!l) {
              let o;
              return (
                (o = f.useCallback(() => t(e.getSnapshot(), n, r, i), [e, t, n, r, i])),
                (0, aK.useSyncExternalStore)(e.subscribe, o, o)
              );
            }
            let a = l.syncIndex;
            return (
              (l.syncIndex += 1),
              l.didInitialize
                ? ((o = l.syncHooks[a]).store === e &&
                    o.selector === t &&
                    Object.is(o.a1, n) &&
                    Object.is(o.a2, r) &&
                    Object.is(o.a3, i)) ||
                  (o.store !== e && (l.didChangeStore = !0),
                  (o.store = e),
                  (o.selector = t),
                  (o.a1 = n),
                  (o.a2 = r),
                  (o.a3 = i),
                  (o.value = t(e.getSnapshot(), n, r, i)))
                : ((o = { store: e, selector: t, a1: n, a2: r, a3: i, value: t(e.getSnapshot(), n, r, i) }),
                  l.syncHooks.push(o)),
              o.value
            );
          }
        : function (e, t, n, r, i) {
            return (0, aX.useSyncExternalStoreWithSelector)(e.subscribe, e.getSnapshot, e.getSnapshot, (e) =>
              t(e, n, r, i),
            );
          };
    [].push({
      before(e) {
        ((e.syncIndex = 0),
          e.didInitialize ||
            ((e.syncTick = 1),
            (e.syncHooks = []),
            (e.didChangeStore = !0),
            (e.getSnapshot = () => {
              let t = !1;
              for (let n = 0; n < e.syncHooks.length; n += 1) {
                let r = e.syncHooks[n],
                  i = r.selector(r.store.state, r.a1, r.a2, r.a3);
                Object.is(r.value, i) || ((t = !0), (r.value = i));
              }
              return (t && (e.syncTick += 1), e.syncTick);
            })));
      },
      after(e) {
        e.syncHooks.length > 0 &&
          (e.didChangeStore &&
            ((e.didChangeStore = !1),
            (e.subscribe = (t) => {
              let n = new Set();
              for (let t of e.syncHooks) n.add(t.store);
              let r = [];
              for (let e of n) r.push(e.subscribe(t));
              return () => {
                for (let e of r) e();
              };
            })),
          (0, aK.useSyncExternalStore)(e.subscribe, e.getSnapshot, e.getSnapshot));
      },
    });
    class aG {
      constructor(e) {
        ((this.state = e), (this.listeners = new Set()), (this.updateTick = 0));
      }
      subscribe = (e) => (
        this.listeners.add(e),
        () => {
          this.listeners.delete(e);
        }
      );
      getSnapshot = () => this.state;
      setState(e) {
        if (this.state === e) return;
        ((this.state = e), (this.updateTick += 1));
        let t = this.updateTick;
        for (let n of this.listeners) {
          if (t !== this.updateTick) return;
          n(e);
        }
      }
      update(e) {
        for (let t in e) if (!Object.is(this.state[t], e[t])) return void this.setState({ ...this.state, ...e });
      }
      set(e, t) {
        Object.is(this.state[e], t) || this.setState({ ...this.state, [e]: t });
      }
      notifyAll() {
        let e = { ...this.state };
        this.setState(e);
      }
      use(e, t, n, r) {
        return aY(this, e, t, n, r);
      }
    }
    class aJ extends aG {
      constructor(e, t = {}, n) {
        (super(e), (this.context = t), (this.selectors = n));
      }
      useSyncedValue(e, t) {
        f.useDebugValue(e);
        let n = this;
        iI(() => {
          n.state[e] !== t && n.set(e, t);
        }, [n, e, t]);
      }
      useSyncedValueWithCleanup(e, t) {
        let n = this;
        iI(
          () => (
            n.state[e] !== t && n.set(e, t),
            () => {
              n.set(e, void 0);
            }
          ),
          [n, e, t],
        );
      }
      useSyncedValues(e) {
        let t = this;
        iI(() => {
          t.update(e);
        }, [t, ...Object.values(e)]);
      }
      useControlledProp(e, t) {
        f.useDebugValue(e);
        let n = this,
          r = void 0 !== t;
        iI(() => {
          r && !Object.is(n.state[e], t) && n.setState({ ...n.state, [e]: t });
        }, [n, e, t, r]);
      }
      select(e, t, n, r) {
        return (0, this.selectors[e])(this.state, t, n, r);
      }
      useState(e, t, n, r) {
        return (f.useDebugValue(e), aY(this, this.selectors[e], t, n, r));
      }
      useContextCallback(e, t) {
        f.useDebugValue(e);
        let n = iT(t ?? rr);
        this.context[e] = n;
      }
      useStateSetter(e) {
        let t = f.useRef(void 0);
        return (
          void 0 === t.current &&
            (t.current = (t) => {
              this.set(e, t);
            }),
          t.current
        );
      }
      observe(e, t) {
        let n,
          r = (n = "function" == typeof e ? e : this.selectors[e])(this.state);
        return (
          t(r, r, this),
          this.subscribe((e) => {
            let i = n(e);
            if (!Object.is(r, i)) {
              let e = r;
              ((r = i), t(i, e, this));
            }
          })
        );
      }
    }
    let aQ = {
      open: (e) => e.open,
      transitionStatus: (e) => e.transitionStatus,
      domReferenceElement: (e) => e.domReferenceElement,
      referenceElement: (e) => e.positionReference ?? e.referenceElement,
      floatingElement: (e) => e.floatingElement,
      floatingId: (e) => e.floatingId,
    };
    class aZ extends aJ {
      constructor(e) {
        const { syncOnly: t, nested: n, onOpenChange: r, triggerElements: i, ...o } = e;
        (super(
          { ...o, positionReference: o.referenceElement, domReferenceElement: o.referenceElement },
          {
            onOpenChange: r,
            dataRef: { current: {} },
            events: (function () {
              let e = new Map();
              return {
                emit(t, n) {
                  e.get(t)?.forEach((e) => e(n));
                },
                on(t, n) {
                  (e.has(t) || e.set(t, new Set()), e.get(t).add(n));
                },
                off(t, n) {
                  e.get(t)?.delete(n);
                },
              };
            })(),
            nested: n,
            triggerElements: i,
          },
          aQ,
        ),
          (this.syncOnly = t));
      }
      syncOpenEvent = (e, t) => {
        let n;
        (e &&
          this.state.open &&
          (null == t || ("click" !== (n = t.type) && "mousedown" !== n && "keydown" !== n && "keyup" !== n))) ||
          (this.context.dataRef.current.openEvent = e ? t : void 0);
      };
      dispatchOpenChange = (e, t) => {
        this.syncOpenEvent(e, t.event);
        let n = {
          open: e,
          reason: t.reason,
          nativeEvent: t.event,
          nested: this.context.nested,
          triggerElement: t.trigger,
        };
        this.context.events.emit("openchange", n);
      };
      setOpen = (e, t) => {
        (this.syncOnly || this.dispatchOpenChange(e, t), this.context.onOpenChange?.(e, t));
      };
    }
    var oT = oT;
    let a0 = { tabIndex: -1, [lW]: "" };
    function a1({ handle: e, store: t }) {
      return (iI(() => e.attachStore(t), [e, t]), null);
    }
    let a2 = { ...lN, ...ow, nestedDialogOpen: (e) => (e ? { "data-nested-dialog-open": "" } : null) },
      a4 = f.forwardRef(function (e, t) {
        var n;
        let { render: r, className: i, style: o, finalFocus: l, initialFocus: a, ...s } = e,
          u = lP(),
          c = u.useState("descriptionElementId"),
          f = u.useState("disablePointerDismissal"),
          p = u.useState("floatingRootContext"),
          h = u.useState("popupProps"),
          m = u.useState("modal"),
          g = u.useState("mounted"),
          v = u.useState("nested"),
          y = u.useState("nestedOpenDialogCount"),
          b = u.useState("open"),
          x = u.useState("openMethod"),
          k = u.useState("titleElementId"),
          w = u.useState("transitionStatus"),
          S = u.useState("role"),
          C = p.useState("floatingId");
        (az(),
          oy({
            open: b,
            ref: u.context.popupRef,
            onComplete() {
              b && u.context.onOpenChangeComplete?.(!0);
            },
          }));
        let E = void 0 === a ? ((n = u.context.popupRef), (e) => "touch" !== e || n.current) : a,
          j = u.useStateSetter("popupElement"),
          R = rl("div", e, {
            state: { open: b, nested: v, transitionStatus: w, nestedDialogOpen: y > 0 },
            props: [
              h,
              {
                id: C,
                "aria-labelledby": k,
                "aria-describedby": c,
                role: S,
                ...a0,
                hidden: !g,
                onKeyDown(e) {
                  aB.has(e.key) && e.stopPropagation();
                },
                style: { "--nested-dialogs": y },
              },
              s,
            ],
            ref: [t, u.context.popupRef, j],
            stateAttributesMapping: a2,
          });
        return (0, d.jsx)(aM, {
          context: p,
          openInteractionType: x,
          disabled: !g,
          closeOnFocusOut: !f,
          initialFocus: E,
          returnFocus: l,
          modal: !1 !== m,
          restoreFocus: "popup",
          children: R,
        });
      });
    function a5(e) {
      return rt >= 19 ? e : e ? "true" : void 0;
    }
    let a3 = f.forwardRef(function (e, t) {
        let n,
          { cutout: r, ...i } = e;
        if (r) {
          let e = r.getBoundingClientRect();
          n = `polygon(0% 0%,100% 0%,100% 100%,0% 100%,0% 0%,${e.left}px ${e.top}px,${e.left}px ${e.bottom}px,${e.right}px ${e.bottom}px,${e.right}px ${e.top}px,${e.left}px ${e.top}px)`;
        }
        return (0, d.jsx)("div", {
          ref: t,
          role: "presentation",
          "data-base-ui-inert": "",
          ...i,
          style: { position: "fixed", inset: 0, userSelect: "none", WebkitUserSelect: "none", clipPath: n },
        });
      }),
      a6 = f.forwardRef(function (e, t) {
        let { keepMounted: n = !1, ...r } = e,
          i = lP(),
          o = i.useState("mounted"),
          l = i.useState("modal"),
          a = i.useState("open");
        return o || n
          ? (0, d.jsx)(aN.Provider, {
              value: n,
              children: (0, d.jsxs)(aC, {
                ref: t,
                ...r,
                children: [
                  o && !0 === l && (0, d.jsx)(a3, { ref: i.context.internalBackdropRef, inert: a5(!a) }),
                  e.children,
                ],
              }),
            })
          : null;
      });
    var lo = lo;
    let a9 = {},
      a7 = {},
      a8 = "";
    function se(e, t) {
      return !(function (e) {
        let { overflow: t, overflowX: n, overflowY: r, display: i } = iE(e);
        return /auto|scroll|overlay|hidden|clip/.test(t + r + n) && "inline" !== i && "contents" !== i;
      })(e)
        ? t
        : e;
    }
    function st(e, t, n) {
      return /hidden|clip/.test(e.getComputedStyle(se(t, n)).overflowY);
    }
    class sn {
      lockCount = 0;
      restore = null;
      timeoutLock = i7.create();
      timeoutUnlock = i7.create();
      acquire(e) {
        return (
          (this.lockCount += 1),
          1 === this.lockCount && null === this.restore && this.timeoutLock.start(0, () => this.lock(e)),
          this.release
        );
      }
      release = () => {
        ((this.lockCount -= 1), 0 === this.lockCount && this.restore && this.timeoutUnlock.start(0, this.unlock));
      };
      unlock = () => {
        0 === this.lockCount && this.restore && (this.restore?.(), (this.restore = null));
      };
      lock(e) {
        let t, n, r;
        if (0 === this.lockCount || null !== this.restore) return;
        let i = ol(e),
          o = i.documentElement,
          l = i.body,
          a = ib(o);
        if (st(a, o, l)) {
          let t = new a.MutationObserver(() => {
              st(a, o, l) || (t.disconnect(), (this.restore = null), this.lock(e));
            }),
            n = { attributes: !0 };
          (t.observe(o, n), t.observe(l, n), (this.restore = () => t.disconnect()));
          return;
        }
        let s =
          lo.os.ios ||
          !(function (e) {
            if ("u" < typeof document) return !1;
            let t = ol(e);
            return ib(t).innerWidth - t.documentElement.clientWidth > 0;
          })(e);
        this.restore = s
          ? ((r = {
              overflowY: (n = se((t = ol(e)).documentElement, t.body)).style.overflowY,
              overflowX: n.style.overflowX,
            }),
            Object.assign(n.style, { overflowY: "hidden", overflowX: "hidden" }),
            () => {
              Object.assign(n.style, r);
            })
          : (function (e) {
              let t = ol(e),
                n = t.documentElement,
                r = t.body,
                i = ib(n),
                o = 0,
                l = 0,
                a = !1,
                s = om.create();
              if (lo.engine.webkit && (i.visualViewport?.scale ?? 1) !== 1) return () => {};
              function u() {
                let t = i.getComputedStyle(n),
                  s = i.getComputedStyle(r),
                  u = (t.scrollbarGutter || "").includes("both-edges") ? "stable both-edges" : "stable";
                ((o = n.scrollTop),
                  (l = n.scrollLeft),
                  (a9 = {
                    scrollbarGutter: n.style.scrollbarGutter,
                    overflowY: n.style.overflowY,
                    overflowX: n.style.overflowX,
                  }),
                  (a8 = n.style.scrollBehavior),
                  (a7 = {
                    position: r.style.position,
                    height: r.style.height,
                    width: r.style.width,
                    boxSizing: r.style.boxSizing,
                    overflowY: r.style.overflowY,
                    overflowX: r.style.overflowX,
                    scrollBehavior: r.style.scrollBehavior,
                  }));
                let c = n.scrollHeight > n.clientHeight,
                  d = n.scrollWidth > n.clientWidth,
                  f = "scroll" === t.overflowY || "scroll" === s.overflowY,
                  p = "scroll" === t.overflowX || "scroll" === s.overflowX,
                  h = Math.max(0, i.innerWidth - r.clientWidth),
                  m = Math.max(0, i.innerHeight - r.clientHeight),
                  g = parseFloat(s.marginTop) + parseFloat(s.marginBottom),
                  v = parseFloat(s.marginLeft) + parseFloat(s.marginRight),
                  y = se(n, r);
                if (
                  (a = (function (e) {
                    if (
                      !("u" > typeof CSS && CSS.supports && CSS.supports("scrollbar-gutter", "stable")) ||
                      "u" < typeof document
                    )
                      return !1;
                    let t = ol(e),
                      n = t.documentElement,
                      r = se(n, t.body),
                      i = r.style.overflowY,
                      o = n.style.scrollbarGutter;
                    ((n.style.scrollbarGutter = "stable"), (r.style.overflowY = "scroll"));
                    let l = r.offsetWidth;
                    r.style.overflowY = "hidden";
                    let a = r.offsetWidth;
                    return ((r.style.overflowY = i), (n.style.scrollbarGutter = o), l === a);
                  })(e))
                ) {
                  ((n.style.scrollbarGutter = u), (y.style.overflowY = "hidden"), (y.style.overflowX = "hidden"));
                  return;
                }
                (Object.assign(n.style, { scrollbarGutter: u, overflowY: "hidden", overflowX: "hidden" }),
                  (c || f) && (n.style.overflowY = "scroll"),
                  (d || p) && (n.style.overflowX = "scroll"),
                  Object.assign(r.style, {
                    position: "relative",
                    height: g || m ? `calc(100dvh - ${g + m}px)` : "100dvh",
                    width: v || h ? `calc(100vw - ${v + h}px)` : "100vw",
                    boxSizing: "border-box",
                    overflowY: "hidden",
                    overflowX: "hidden",
                    scrollBehavior: "unset",
                  }),
                  (r.scrollTop = o),
                  (r.scrollLeft = l),
                  n.setAttribute("data-base-ui-scroll-locked", ""),
                  (n.style.scrollBehavior = "unset"));
              }
              function c() {
                (Object.assign(n.style, a9),
                  Object.assign(r.style, a7),
                  a ||
                    ((n.scrollTop = o),
                    (n.scrollLeft = l),
                    n.removeAttribute("data-base-ui-scroll-locked"),
                    (n.style.scrollBehavior = a8)));
              }
              u();
              let d = lg(i, "resize", function () {
                (c(), s.request(u));
              });
              return () => {
                (s.cancel(), c(), "function" == typeof i.removeEventListener && d());
              };
            })(e);
      }
    }
    let sr = new sn();
    var lo = lo,
      oT = oT;
    function si() {
      return !1;
    }
    function so({ store: e, parentContext: t, isDrawer: n }) {
      var r;
      let i = e.useState("open"),
        o = e.useState("disablePointerDismissal"),
        l = e.useState("modal"),
        a = e.useState("popupElement"),
        s = e.useState("floatingRootContext"),
        [u, c] = f.useState(0),
        [d, p] = f.useState(0),
        h = 0 === u,
        m = (function (e, t = {}) {
          let {
              enabled: n = !0,
              escapeKey: r = !0,
              outsidePress: i = !0,
              outsidePressEvent: o = "sloppy",
              referencePress: l = si,
              bubbles: a,
              externalTree: s,
            } = t,
            u = "rootStore" in e ? e.rootStore : e,
            c = u.useState("open"),
            d = u.useState("floatingElement"),
            { dataRef: p } = u.context,
            h = aR(s),
            m = iT("function" == typeof i ? i : () => !1),
            g = "function" == typeof i ? m : i,
            v = !1 !== g,
            y = iT(() => o),
            { escapeKey: b, outsidePress: x } = {
              escapeKey: "boolean" == typeof a ? a : (a?.escapeKey ?? !1),
              outsidePress: "boolean" == typeof a ? a : (a?.outsidePress ?? !0),
            },
            k = f.useRef(!1),
            w = f.useRef(!1),
            S = f.useRef(!1),
            C = f.useRef(!1),
            E = f.useRef(""),
            j = f.useRef(null),
            R = i8(),
            P = i8(),
            T = iT(() => {
              (P.clear(), (p.current.insideReactTree = !1));
            }),
            A = iT((e) => {
              let t = p.current.floatingContext?.nodeId;
              return (h ? al(h.nodesRef.current, t) : []).some((t) => t.context?.open && !t.context.dataRef.current[e]);
            }),
            O = iT((e) => lV(e, u.select("floatingElement")) || lV(e, u.select("domReferenceElement"))),
            I = iT((e) => {
              l() && u.setOpen(!1, oP(oT.triggerPress, e.nativeEvent));
            }),
            M = iT((e) => {
              if (!c || !n || !r || "Escape" !== e.key || C.current || (!b && A("__escapeKeyBubbles"))) return;
              let t = "nativeEvent" in e ? e.nativeEvent : e,
                i = oP(oT.escapeKey, t);
              (u.setOpen(!1, i),
                i.isCanceled || e.preventDefault(),
                b || i.isPropagationAllowed || e.stopPropagation());
            }),
            N = iT(() => {
              ((p.current.insideReactTree = !0), P.start(0, T));
            }),
            z = iT((e) => {
              if (!c || !n || 0 !== e.button) return;
              let t = ou(e.nativeEvent);
              os(u.select("floatingElement"), t) && (k.current || ((k.current = !0), (w.current = !1)));
            }),
            D = iT((e) => {
              !c || !n || ((e.defaultPrevented || e.nativeEvent.defaultPrevented) && k.current && (w.current = !0));
            });
          f.useEffect(() => {
            if (!c || !n) return T;
            ((p.current.__escapeKeyBubbles = b), (p.current.__outsidePressBubbles = x));
            let e = new i7(),
              t = new i7();
            function i() {
              ((S.current = !0),
                t.start(0, () => {
                  S.current = !1;
                }));
            }
            function o() {
              ((k.current = !1), (w.current = !1));
            }
            function l() {
              let e = E.current,
                t = y(),
                n = "function" == typeof t ? t() : t;
              return "string" == typeof n ? n : n["pen" !== e && e ? e : "mouse"];
            }
            function a(e) {
              let t = p.current.floatingContext?.nodeId,
                n = h && al(h.nodesRef.current, t).some((t) => lV(e, t.context?.elements.floating));
              return O(e) || n;
            }
            function s(e) {
              let n;
              if (("intentional" === (n = l()) && "click" !== e.type) || ("sloppy" === n && "click" === e.type)) {
                ("click" === e.type || O(e) || (t.clear(), (S.current = !1)), T());
                return;
              }
              if (p.current.insideReactTree) return void T();
              let r = ou(e),
                i = `[${as("inert")}]`,
                o = ik(r) ? r.getRootNode() : null,
                s = Array.from((iS(o) ? o : ol(u.select("floatingElement"))).querySelectorAll(i)),
                c = u.context.triggerElements;
              if (r && (c.hasElement(r) || c.hasMatchingElement((e) => os(e, r)))) return;
              let d = ik(r) ? r : null;
              for (; d && !iC(d); ) {
                let e = (function (e) {
                  var t;
                  if ("html" === iy(e)) return e;
                  let n =
                    e.assignedSlot ||
                    e.parentNode ||
                    (iS(e) && e.host) ||
                    (null == (t = (ix(e) ? e.ownerDocument : e.document) || window.document)
                      ? void 0
                      : t.documentElement);
                  return iS(n) ? n.host : n;
                })(d);
                if (iC(e) || !ik(e)) break;
                d = e;
              }
              if (
                !(
                  s.length &&
                  ik(r) &&
                  !r.matches("html,body") &&
                  !os(r, u.select("floatingElement")) &&
                  s.every((e) => !os(d, e))
                )
              ) {
                if (iw(r) && !("touches" in e)) {
                  let t = iC(r),
                    n = iE(r),
                    i = /auto|scroll/,
                    o = t || i.test(n.overflowX),
                    l = t || i.test(n.overflowY),
                    a = o && r.clientWidth > 0 && r.scrollWidth > r.clientWidth,
                    s = l && r.clientHeight > 0 && r.scrollHeight > r.clientHeight,
                    u = "rtl" === n.direction,
                    c = s && (u ? e.offsetX <= r.offsetWidth - r.clientWidth : e.offsetX > r.clientWidth),
                    d = a && e.offsetY > r.clientHeight;
                  if (c || d) return;
                }
                if (!a(e)) {
                  if ("intentional" === l() && S.current) {
                    (t.clear(), (S.current = !1));
                    return;
                  }
                  ("function" == typeof g && !g(e)) ||
                    A("__outsidePressBubbles") ||
                    (u.setOpen(!1, oP(oT.outsidePress, e)), T());
                }
              }
            }
            function f(e) {
              if ("sloppy" !== l() || !u.select("open") || !n || O(e)) return;
              let t = e.touches[0];
              t &&
                ((j.current = {
                  startTime: Date.now(),
                  startX: t.clientX,
                  startY: t.clientY,
                  dismissOnTouchEnd: !1,
                  dismissOnMouseDown: !0,
                }),
                R.start(1e3, () => {
                  j.current && ((j.current.dismissOnTouchEnd = !1), (j.current.dismissOnMouseDown = !1));
                }));
            }
            function m(e, t) {
              let n = ou(e);
              if (!n) return;
              let r = lg(n, e.type, () => {
                (t(e), r());
              });
            }
            function P(e) {
              (R.clear(),
                "pointerdown" === e.type && (E.current = e.pointerType),
                ("mousedown" !== e.type || !j.current || j.current.dismissOnMouseDown) &&
                  m(e, (e) => {
                    if ("pointerdown" === e.type)
                      "sloppy" !== l() || "touch" === e.pointerType || !u.select("open") || !n || O(e) || s(e);
                    else s(e);
                  }));
            }
            function I(e) {
              if (!k.current) return;
              let n = w.current;
              if ((o(), "intentional" === l())) {
                if ("pointercancel" === e.type) {
                  n && i();
                  return;
                }
                a(e) || (n ? i() : ("function" != typeof g || g(e)) && (t.clear(), (S.current = !0), T()));
              }
            }
            function N(e) {
              if ("sloppy" !== l() || !j.current || O(e)) return;
              let t = e.touches[0];
              if (!t) return;
              let n = Math.abs(t.clientX - j.current.startX),
                r = Math.abs(t.clientY - j.current.startY),
                i = Math.sqrt(n * n + r * r);
              (i > 5 && (j.current.dismissOnTouchEnd = !0), i > 10 && (s(e), R.clear(), (j.current = null)));
            }
            function z(e) {
              "sloppy" !== l() ||
                !j.current ||
                O(e) ||
                (j.current.dismissOnTouchEnd && s(e), R.clear(), (j.current = null));
            }
            let D = ol(d),
              L = lF(
                r &&
                  lF(
                    lg(D, "keydown", M),
                    lg(D, "compositionstart", function () {
                      (e.clear(), (C.current = !0));
                    }),
                    lg(D, "compositionend", function () {
                      e.start(5 * !!lo.engine.webkit, () => {
                        C.current = !1;
                      });
                    }),
                  ),
                v &&
                  lF(
                    lg(D, "click", P, !0),
                    lg(D, "pointerdown", P, !0),
                    lg(D, "pointerup", I, !0),
                    lg(D, "pointercancel", I, !0),
                    lg(D, "mousedown", P, !0),
                    lg(D, "mouseup", I, !0),
                    lg(
                      D,
                      "touchstart",
                      function (e) {
                        ((E.current = "touch"), m(e, f));
                      },
                      !0,
                    ),
                    lg(
                      D,
                      "touchmove",
                      function (e) {
                        m(e, N);
                      },
                      !0,
                    ),
                    lg(
                      D,
                      "touchend",
                      function (e) {
                        m(e, z);
                      },
                      !0,
                    ),
                  ),
              );
            return () => {
              (L(), e.clear(), t.clear(), o(), (S.current = !1), T());
            };
          }, [p, d, r, v, g, c, n, b, x, M, T, y, A, O, h, u, R]);
          let L = f.useMemo(() => ({ onKeyDown: M, onPointerDown: I, onClick: I }), [M, I]),
            $ = f.useMemo(
              () => ({
                onKeyDown: M,
                onPointerDown: D,
                onMouseDown: D,
                onClickCapture: N,
                onMouseDownCapture(e) {
                  (N(), z(e));
                },
                onPointerDownCapture(e) {
                  (N(), z(e));
                },
                onMouseUpCapture: N,
                onTouchEndCapture: N,
                onTouchMoveCapture: N,
              }),
              [M, N, z, D],
            );
          return f.useMemo(() => (n ? { reference: L, floating: $, trigger: L } : {}), [n, L, $]);
        })(s, {
          outsidePressEvent: () =>
            e.context.internalBackdropRef.current || e.context.backdropRef.current
              ? "intentional"
              : { mouse: "trap-focus" === l ? "sloppy" : "intentional", touch: "sloppy" },
          outsidePress(t) {
            if (!e.context.outsidePressEnabledRef.current || ("button" in t && 0 !== t.button)) return !1;
            if ("touches" in t) {
              if ("touchend" === t.type) {
                if (1 !== t.changedTouches.length || 0 !== t.touches.length) return !1;
              } else if (1 !== t.touches.length) return !1;
            }
            let n = ou(t);
            if (h && !o) {
              if (l) {
                let t = e.context.internalBackdropRef.current,
                  r = e.context.backdropRef.current;
                return (!t && !r) || t === n || r === n || (os(n, a) && !n?.hasAttribute("data-base-ui-portal"));
              }
              return !0;
            }
            return !1;
          },
          escapeKey: h,
        });
      return (
        !(function (e = !0, t = null) {
          iI(() => {
            if (e) return sr.acquire(t);
          }, [e, t]);
        })(i && !0 === l, a),
        e.useContextCallback("onNestedDialogOpen", (e, t) => {
          (c(e), p(t));
        }),
        iI(
          () => (
            t?.onNestedDialogOpen && (i ? t.onNestedDialogOpen(u + 1, d + +!!n) : t.onNestedDialogOpen(0, 0)),
            () => {
              t?.onNestedDialogOpen && i && t.onNestedDialogOpen(0, 0);
            }
          ),
          [n, i, u, d, t],
        ),
        (r = {
          activeTriggerProps: m.reference,
          inactiveTriggerProps: m.trigger,
          popupProps: m.floating,
          nestedOpenDialogCount: u,
          nestedOpenDrawerCount: d,
        }),
        e.useSyncedValues(r),
        iI(
          () => () => {
            e.update({ activeTriggerProps: ro, inactiveTriggerProps: ro, popupProps: ro });
          },
          [e],
        ),
        null
      );
    }
    class sl extends aJ {
      setState(e) {}
      update(e) {}
      set(e, t) {}
      notifyAll() {}
    }
    class sa {
      constructor() {
        this.idMap = new Map();
      }
      add(e, t) {
        this.idMap.set(e, t);
      }
      delete(e) {
        this.idMap.delete(e);
      }
      hasElement(e) {
        for (let t of this.idMap.values()) if (t === e) return !0;
        return !1;
      }
      hasMatchingElement(e) {
        for (let t of this.idMap.values()) if (e(t)) return !0;
        return !1;
      }
      getById(e) {
        return this.idMap.get(e);
      }
      entries() {
        return this.idMap.entries();
      }
      elements() {
        return this.idMap.values();
      }
      get size() {
        return this.idMap.size;
      }
    }
    let ss = (e) => e.triggerIdProp ?? e.activeTriggerId,
      su = (e) => e.openProp ?? e.open,
      sc = (e) => (e.popupElement?.id ?? e.floatingId) || void 0;
    function sd(e, t) {
      return void 0 !== t && su(e) && ss(e) === t;
    }
    let sf = {
      open: su,
      mounted: (e) => e.mounted,
      transitionStatus: (e) => e.transitionStatus,
      floatingRootContext: (e) => e.floatingRootContext,
      triggerCount: (e) => e.triggerCount,
      preventUnmountingOnClose: (e) => e.preventUnmountingOnClose,
      payload: (e) => e.payload,
      activeTriggerId: ss,
      activeTriggerElement: (e) => (e.mounted ? e.activeTriggerElement : null),
      popupId: sc,
      isTriggerActive: (e, t) => void 0 !== t && ss(e) === t,
      isOpenedByTrigger: (e, t) => sd(e, t),
      isMountedByTrigger: (e, t) => void 0 !== t && ss(e) === t && e.mounted,
      triggerProps: (e, t) => (t ? e.activeTriggerProps : e.inactiveTriggerProps),
      triggerPopupId: (e, t) =>
        sd(e, t) || (void 0 !== t && su(e) && null == ss(e) && 1 === e.triggerCount) ? sc(e) : void 0,
      popupProps: (e) => e.popupProps,
      popupElement: (e) => e.popupElement,
      positionerElement: (e) => e.positionerElement,
      modal: (e) => e.modal,
      nested: (e) => e.nested,
      nestedOpenDialogCount: (e) => e.nestedOpenDialogCount,
      nestedOpenDrawerCount: (e) => e.nestedOpenDrawerCount,
      disablePointerDismissal: (e) => e.disablePointerDismissal,
      openMethod: (e) => e.openMethod,
      descriptionElementId: (e) => e.descriptionElementId,
      titleElementId: (e) => e.titleElementId,
      viewportElement: (e) => e.viewportElement,
      role: (e) => e.role,
    };
    class sp extends aJ {
      constructor(e, t, n) {
        const r = new sa();
        super(sh(e, r, t, n), sm(r), sf);
      }
      setOpen = (e, t) => {
        if (
          ((t.preventUnmountOnClose = () => {
            this.set("preventUnmountingOnClose", !0);
          }),
          e ||
            null != t.trigger ||
            null == this.state.activeTriggerId ||
            (t.trigger = this.state.activeTriggerElement ?? void 0),
          this.context.onOpenChange?.(e, t),
          t.isCanceled)
        )
          return;
        this.state.floatingRootContext.dispatchOpenChange(e, t);
        let n = { open: e };
        (!(function (e, t, n, r = !1) {
          t ? (e.preventUnmountingOnClose = !1) : r && (e.preventUnmountingOnClose = !0);
          let i = n?.id ?? null;
          (i || t) && ((e.activeTriggerId = i), (e.activeTriggerElement = n ?? null));
        })(n, e, t.trigger),
          this.update(n));
      };
    }
    function sh(e, t, n, r = !1) {
      let i = {
        ...{
          open: !1,
          openProp: void 0,
          mounted: !1,
          transitionStatus: void 0,
          floatingRootContext: new aZ({
            open: !1,
            transitionStatus: void 0,
            floatingElement: null,
            referenceElement: null,
            triggerElements: new sa(),
            floatingId: void 0,
            syncOnly: !1,
            nested: !1,
            onOpenChange: void 0,
          }),
          floatingId: void 0,
          triggerCount: 0,
          preventUnmountingOnClose: !1,
          payload: void 0,
          activeTriggerId: null,
          activeTriggerElement: null,
          triggerIdProp: void 0,
          popupElement: null,
          positionerElement: null,
          activeTriggerProps: ro,
          inactiveTriggerProps: ro,
          popupProps: ro,
        },
        modal: !0,
        disablePointerDismissal: !1,
        viewportElement: null,
        descriptionElementId: void 0,
        titleElementId: void 0,
        openMethod: null,
        nested: !1,
        nestedOpenDialogCount: 0,
        nestedOpenDrawerCount: 0,
        role: "dialog",
        ...e,
      };
      return (
        (i.floatingRootContext = (function (e, t, n = !1) {
          return new aZ({
            open: !1,
            transitionStatus: void 0,
            floatingElement: null,
            referenceElement: null,
            triggerElements: e,
            floatingId: t,
            syncOnly: !0,
            nested: n,
            onOpenChange: void 0,
          });
        })(t, n, r)),
        i
      );
    }
    function sm(e) {
      return {
        popupRef: f.createRef(),
        backdropRef: f.createRef(),
        internalBackdropRef: f.createRef(),
        outsidePressEnabledRef: { current: !0 },
        triggerElements: e,
        onOpenChange: void 0,
        onOpenChangeComplete: void 0,
      };
    }
    var oT = oT;
    let sg = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, children: o, ...l } = e,
          a = az(),
          s = lP(),
          u = s.useState("open"),
          c = s.useState("nested"),
          d = s.useState("transitionStatus"),
          f = s.useState("nestedOpenDialogCount"),
          p = s.useState("mounted");
        return rl("div", e, {
          enabled: a || p,
          state: { open: u, nested: c, transitionStatus: d, nestedDialogOpen: f > 0 },
          ref: [t, s.useStateSetter("viewportElement")],
          stateAttributesMapping: a2,
          props: [{ role: "presentation", hidden: !p, style: { pointerEvents: u ? void 0 : "none" }, children: o }, l],
        });
      }),
      sv = f.forwardRef(function (e, t) {
        let { render: n, className: r, style: i, id: o, ...l } = e,
          a = lP(),
          s = i4(o);
        return (a.useSyncedValueWithCleanup("titleElementId", s), rl("h2", e, { ref: t, props: [{ id: s }, l] }));
      });
    var oT = oT,
      lo = lo;
    let sy = f.forwardRef(function (e, t) {
      var n;
      let r,
        i,
        o,
        l,
        a,
        s,
        u,
        c,
        {
          render: d,
          className: p,
          style: h,
          disabled: m = !1,
          nativeButton: g = !0,
          id: v,
          payload: y,
          handle: b,
          ...x
        } = e,
        k = lP(!0),
        w =
          ((r = f.useCallback((e) => (void 0 === b ? rr : b.subscribeStore(e)), [b])),
          (i = f.useCallback(() => (void 0 === b ? void 0 : b.store), [b])),
          (0, aK.useSyncExternalStore)(r, i, () => b?.serverStore) ?? k);
      if (!w) throw Error(n3(79));
      let S = i4(v),
        C = w.useState("floatingRootContext"),
        E = w.useState("isOpenedByTrigger", S),
        j = w.useState("triggerPopupId", S),
        R = f.useRef(null),
        { registerTrigger: P, isMountedByThisTrigger: T } =
          ((n = { payload: y }),
          (o = w.useState("isMountedByTrigger", S)),
          (l = f.useRef(null)),
          (a = f.useRef(null)),
          (s = f.useCallback(
            (e) => {
              if (void 0 === S) return;
              let t = !1;
              if (null !== l.current) {
                let e = l.current,
                  n = a.current,
                  r = w.context.triggerElements.getById(e);
                (n && r === n && (w.context.triggerElements.delete(e), (t = !0)),
                  (l.current = null),
                  (a.current = null));
              }
              if (
                (null !== e && ((l.current = S), (a.current = e), w.context.triggerElements.add(S, e), (t = !0)), t)
              ) {
                let e = w.context.triggerElements.size;
                w.select("open") && w.state.triggerCount !== e && w.set("triggerCount", e);
              }
            },
            [w, S],
          )),
          (u = iT((e) => {
            let t = w.select("open"),
              r = w.select("activeTriggerId");
            r === S
              ? w.update({ activeTriggerElement: e, ...(t ? n : null) })
              : null == r && t && w.update({ activeTriggerId: S, activeTriggerElement: e, ...n });
          })),
          (c = f.useCallback(
            (e) => {
              (s(e), e && u(e));
            },
            [s, u],
          )),
          iI(() => {
            o && w.update({ activeTriggerElement: R.current, ...n });
          }, [o, w, R, ...Object.values(n)]),
          { registerTrigger: c, isMountedByThisTrigger: o }),
        { getButtonProps: A, buttonRef: O } = iD({ disabled: m, native: g }),
        I = (function (e, t = {}) {
          let {
              enabled: n = !0,
              event: r = "click",
              toggle: i = !0,
              ignoreMouse: o = !1,
              stickIfOpen: l = !0,
              touchOpenDelay: a = 0,
              reason: s = oT.triggerPress,
            } = t,
            u = "rootStore" in e ? e.rootStore : e,
            c = u.context.dataRef,
            d = f.useRef(void 0),
            p = og(),
            h = i8(),
            m = f.useMemo(() => {
              function e(e, t, n, r) {
                let i = oP(s, t, n);
                e && "touch" === r && a > 0
                  ? h.start(a, () => {
                      u.setOpen(!0, i);
                    })
                  : u.setOpen(e, i);
              }
              function t(e, t, n) {
                let r = c.current.openEvent,
                  o = u.select("domReferenceElement") !== t;
                return (!!e && !!o) || !e || !i || (!!r && !!l && !n(r.type));
              }
              return {
                onPointerDown(e) {
                  d.current = lJ(e.pointerType, !0) && lG(e.nativeEvent) ? "virtual" : e.pointerType;
                },
                onMouseDown(n) {
                  let i = d.current,
                    l = n.nativeEvent,
                    a = u.select("open");
                  if (0 !== n.button || "click" === r || (lJ(i, !0) && o)) return;
                  let s = t(a, n.currentTarget, (e) => "click" === e || "mousedown" === e),
                    c = ou(l);
                  if (lK(c)) return void e(s, l, c, i);
                  let f = n.currentTarget;
                  p.request(() => {
                    e(s, l, f, i);
                  });
                },
                onClick(n) {
                  if ("mousedown-only" === r) return;
                  let i = d.current;
                  if ("mousedown" === r && i) {
                    d.current = void 0;
                    return;
                  }
                  (lJ(i, !0) && o) ||
                    e(
                      t(
                        u.select("open"),
                        n.currentTarget,
                        (e) => "click" === e || "mousedown" === e || "keydown" === e || "keyup" === e,
                      ),
                      n.nativeEvent,
                      n.currentTarget,
                      i,
                    );
                },
                onKeyDown() {
                  d.current = void 0;
                },
              };
            }, [c, r, o, s, u, l, i, p, h, a]);
          return f.useMemo(() => (n ? { reference: m } : ro), [n, m]);
        })(C),
        M = (function (e, t) {
          var n;
          let r,
            i,
            { onClick: o, onPointerDown: l } =
              ((n = iT((n, r) => {
                ("function" == typeof e ? e() : e) || t(r || (lo.os.ios ? "touch" : ""));
              })),
              (r = f.useRef("")),
              (i = f.useCallback(
                (e) => {
                  e.defaultPrevented || ((r.current = e.pointerType), n(e, e.pointerType));
                },
                [n],
              )),
              {
                onClick: f.useCallback(
                  (e) => {
                    0 === e.detail
                      ? n(e, "keyboard")
                      : ("pointerType" in e ? n(e, e.pointerType) : n(e, r.current), (r.current = ""));
                  },
                  [n],
                ),
                onPointerDown: i,
              });
          return f.useMemo(() => ({ onClick: o, onPointerDown: l }), [o, l]);
        })(
          () => w.select("open"),
          (e) => {
            w.set("openMethod", e);
          },
        ),
        N = w.useState("triggerProps", T);
      return rl("button", e, {
        state: { disabled: m, open: E },
        ref: [O, t, P, R],
        props: [
          I.reference,
          N,
          M,
          { [ax]: "", id: S, "aria-haspopup": "dialog", "aria-expanded": E, "aria-controls": j },
          x,
          A,
        ],
        stateAttributesMapping: lM,
      });
    });
    var oT = oT,
      oT = oT;
    class sb {
      attachedStores = [];
      attachedStoreValue = null;
      storeListeners = new Set();
      constructor(e, t, n = !0) {
        ((this.fallbackStore = e), (this.componentName = t), (this.throwOnMissingTrigger = n));
      }
      get attachedStore() {
        return this.attachedStoreValue;
      }
      get store() {
        return this.attachedStoreValue ?? this.fallbackStore;
      }
      get serverStore() {
        return this.fallbackStore;
      }
      subscribeStore(e) {
        return (
          this.storeListeners.add(e),
          () => {
            this.storeListeners.delete(e);
          }
        );
      }
      attachStore(e) {
        return (
          this.attachedStores.push(e),
          this.setActiveStore(e),
          () => {
            let t = this.attachedStores.lastIndexOf(e);
            (-1 !== t && this.attachedStores.splice(t, 1),
              this.setActiveStore(this.attachedStores[this.attachedStores.length - 1] ?? null));
          }
        );
      }
      setActiveStore(e) {
        this.attachedStoreValue !== e &&
          ((this.attachedStoreValue = e),
          this.storeListeners.forEach((e) => {
            e();
          }));
      }
      openByTrigger(e) {
        let t,
          n = this.attachedStore;
        if (null !== n) {
          if (e) {
            for (let n = this.attachedStores.length - 1; n >= 0 && !t; n -= 1)
              t = this.attachedStores[n].context.triggerElements.getById(e);
            t ??= this.fallbackStore.context.triggerElements.getById(e);
          }
          if (e && !t && this.throwOnMissingTrigger) throw Error(n3(99, this.componentName, e, this.componentName));
          n.setOpen(!0, oP(oT.imperativeAction, void 0, t));
        }
      }
      closePopup() {
        let e = this.attachedStore;
        null === e || e.setOpen(!1, oP(oT.imperativeAction));
      }
    }
    class sx extends sb {
      constructor() {
        super(
          (function () {
            let e = new sa();
            return new sl(Object.freeze(sh(void 0, e)), Object.freeze(sm(e)), sf);
          })(),
          "Dialog",
          !1,
        );
      }
      open(e) {
        this.openByTrigger(e);
      }
      openWithPayload(e) {
        let t = this.attachedStore;
        null === t || (t.set("payload", e), t.setOpen(!0, oP(oT.imperativeAction)));
      }
      close() {
        this.closePopup();
      }
      get isOpen() {
        return this.attachedStore?.select("open") ?? !1;
      }
    }
    e.s(
      [
        "Backdrop",
        0,
        lD,
        "Close",
        0,
        lL,
        "Description",
        0,
        l$,
        "Handle",
        0,
        sx,
        "Popup",
        0,
        a4,
        "Portal",
        0,
        a6,
        "Root",
        0,
        function (e) {
          return (function (e, t) {
            var n;
            let {
                children: r,
                open: i,
                defaultOpen: o = !1,
                onOpenChange: l,
                onOpenChangeComplete: a,
                disablePointerDismissal: s = !1,
                modal: u = !0,
                actionsRef: c,
                handle: p,
                triggerId: h,
                defaultTriggerId: m = null,
              } = t,
              g = "alert-dialog" === e,
              v = lP(!0),
              y = {
                modal: !!g || u,
                disablePointerDismissal: g || s,
                nested: null != v,
                role: g ? "alertdialog" : "dialog",
              },
              b = (function (e, t = !1) {
                let n = i2(),
                  r = null != (f.useContext(aE)?.id || null),
                  i = n9(() => e(n, r)).current;
                return (
                  !(function (e) {
                    let {
                        popupStore: t,
                        treatPopupAsFloatingElement: n = !1,
                        floatingRootContext: r,
                        floatingId: i,
                        nested: o,
                        onOpenChange: l,
                      } = e,
                      a = t.useState("open"),
                      s = t.useState("activeTriggerElement"),
                      u = t.useState(n ? "popupElement" : "positionerElement"),
                      c = t.context.triggerElements,
                      d = f.useRef(null);
                    void 0 === r &&
                      null === d.current &&
                      (d.current = new aZ({
                        open: a,
                        transitionStatus: void 0,
                        referenceElement: s,
                        floatingElement: u,
                        triggerElements: c,
                        onOpenChange: l,
                        floatingId: i,
                        syncOnly: !0,
                        nested: o,
                      }));
                    let p = r ?? d.current;
                    (t.useSyncedValue("floatingId", i),
                      iI(() => {
                        let e = { open: a, floatingId: i, referenceElement: s, floatingElement: u };
                        (ik(s) && (e.domReferenceElement = s),
                          p.state.positionReference === p.state.referenceElement && (e.positionReference = s),
                          p.update(e));
                      }, [a, i, s, u, p]),
                      (p.context.onOpenChange = l),
                      (p.context.nested = o));
                  })({
                    popupStore: i,
                    treatPopupAsFloatingElement: t,
                    floatingRootContext: i.state.floatingRootContext,
                    floatingId: n,
                    nested: r,
                    onOpenChange: i.setOpen,
                  }),
                  i
                );
              })((e, t) => new sp({ open: o, openProp: i, activeTriggerId: m, triggerIdProp: h, ...y }, e, t), !0);
            (b.useControlledProp("openProp", i),
              b.useControlledProp("triggerIdProp", h),
              b.useSyncedValues(y),
              b.useContextCallback("onOpenChange", l),
              b.useContextCallback("onOpenChangeComplete", a));
            let x = b.useState("open"),
              k = b.useState("mounted"),
              w = b.useState("payload");
            (iI(() => {
              n || null === b.state.openMethod || b.set("openMethod", null);
            }, [(n = x), b]),
              iI(
                () => () => {
                  null !== b.state.openMethod && b.set("openMethod", null);
                },
                [b],
              ),
              (function (e, t = {}) {
                let { closeOnActiveTriggerUnmount: n = !1 } = t,
                  r = f.useRef(null),
                  i = e.useState("open"),
                  o = e.useState("triggerCount"),
                  l = e.useState("activeTriggerId"),
                  a = e.useState("activeTriggerElement");
                iI(() => {
                  if (!i) {
                    ((r.current = null), 0 !== e.state.triggerCount && e.set("triggerCount", 0));
                    return;
                  }
                  let t = e.context.triggerElements.size,
                    o = {};
                  e.state.triggerCount !== t && (o.triggerCount = t);
                  let l = e.select("activeTriggerId"),
                    a = null;
                  if (l) {
                    let t = e.context.triggerElements.getById(l);
                    if (t) ((r.current = l), t !== e.state.activeTriggerElement && (o.activeTriggerElement = t));
                    else {
                      for (let [t, n] of e.context.triggerElements.entries())
                        if (n === e.state.activeTriggerElement) {
                          ((o.activeTriggerId = t), (o.activeTriggerElement = n), (r.current = t));
                          break;
                        }
                      void 0 === o.activeTriggerId && (r.current === l ? (a = l) : (r.current = null));
                    }
                  } else r.current = null;
                  if (!a && !l && 1 === t) {
                    let t = e.context.triggerElements.entries().next();
                    if (!t.done) {
                      let [e, n] = t.value;
                      ((o.activeTriggerId = e), (o.activeTriggerElement = n), (r.current = e));
                    }
                  }
                  ((void 0 !== o.triggerCount || void 0 !== o.activeTriggerId || void 0 !== o.activeTriggerElement) &&
                    e.update(o),
                    a &&
                      n &&
                      queueMicrotask(() => {
                        if (
                          e.select("open") &&
                          e.select("activeTriggerId") === a &&
                          !e.context.triggerElements.getById(a)
                        ) {
                          let t = oP(oT.none);
                          (e.setOpen(!1, t),
                            t.isCanceled || e.update({ activeTriggerId: null, activeTriggerElement: null }));
                        }
                      }));
                }, [i, e, o, l, a, n]);
              })(b));
            let { forceUnmount: S } = (function (e, t) {
              let { mounted: n, setMounted: r, transitionStatus: i } = oS(e),
                o = t.useState("preventUnmountingOnClose"),
                l = !e && o;
              t.useSyncedValues({ mounted: n, transitionStatus: i, preventUnmountingOnClose: l });
              let a = iT(() => {
                (r(!1),
                  t.update({
                    activeTriggerId: null,
                    activeTriggerElement: null,
                    mounted: !1,
                    preventUnmountingOnClose: !1,
                  }),
                  t.context.onOpenChangeComplete?.(!1));
              });
              return (
                oy({
                  enabled: n && !e && !l,
                  open: e,
                  ref: t.context.popupRef,
                  onComplete() {
                    e || a();
                  },
                }),
                { forceUnmount: a, transitionStatus: i }
              );
            })(x, b);
            f.useImperativeHandle(c, () => ({ unmount: S, close: () => b.setOpen(!1, oP(oT.imperativeAction)) }), [
              S,
              b,
            ]);
            let C = x || k;
            return (0, d.jsxs)(lR.Provider, {
              value: b,
              children: [
                p && (0, d.jsx)(a1, { handle: p, store: b }),
                C && (0, d.jsx)(so, { store: b, parentContext: v?.context, isDrawer: "drawer" === e }),
                "function" == typeof r ? r({ payload: w }) : r,
              ],
            });
          })("dialog", e);
        },
        "Title",
        0,
        sv,
        "Trigger",
        0,
        sy,
        "Viewport",
        0,
        sg,
        "createHandle",
        0,
        function () {
          return new sx();
        },
      ],
      28376,
    );
    var sk = e.i(28376),
      sk = sk;
    let sw = y("x", [
      ["path", { d: "M18 6 6 18", key: "1bl5f8" }],
      ["path", { d: "m6 6 12 12", key: "d8bk6v" }],
    ]);
    function sS({ ...e }) {
      return (0, d.jsx)(sk.Root, { "data-slot": "sheet", ...e });
    }
    function sC({ ...e }) {
      return (0, d.jsx)(sk.Trigger, { "data-slot": "sheet-trigger", ...e });
    }
    function sE({ ...e }) {
      return (0, d.jsx)(sk.Portal, { "data-slot": "sheet-portal", ...e });
    }
    function sj({ className: e, ...t }) {
      return (0, d.jsx)(sk.Backdrop, {
        "data-slot": "sheet-overlay",
        className: ih(
          "fixed inset-0 z-50 bg-black/10 transition-opacity duration-150 data-[ending-style]:opacity-0 data-[starting-style]:opacity-0 supports-backdrop-filter:backdrop-blur-xs",
          e,
        ),
        ...t,
      });
    }
    function sR({ className: e, children: t, side: n = "right", showCloseButton: r = !0, ...i }) {
      return (0, d.jsxs)(sE, {
        children: [
          (0, d.jsx)(sj, {}),
          (0, d.jsxs)(sk.Popup, {
            "data-slot": "sheet-content",
            "data-side": n,
            className: ih(
              "fixed z-50 flex flex-col gap-4 bg-popover bg-clip-padding text-sm text-popover-foreground shadow-lg transition duration-200 ease-in-out data-[ending-style]:opacity-0 data-[starting-style]:opacity-0 data-[side=bottom]:inset-x-0 data-[side=bottom]:bottom-0 data-[side=bottom]:h-auto data-[side=bottom]:border-t data-[side=bottom]:data-[ending-style]:translate-y-[2.5rem] data-[side=bottom]:data-[starting-style]:translate-y-[2.5rem] data-[side=left]:inset-y-0 data-[side=left]:left-0 data-[side=left]:h-full data-[side=left]:w-3/4 data-[side=left]:border-r data-[side=left]:data-[ending-style]:translate-x-[-2.5rem] data-[side=left]:data-[starting-style]:translate-x-[-2.5rem] data-[side=right]:inset-y-0 data-[side=right]:right-0 data-[side=right]:h-full data-[side=right]:w-3/4 data-[side=right]:border-l data-[side=right]:data-[ending-style]:translate-x-[2.5rem] data-[side=right]:data-[starting-style]:translate-x-[2.5rem] data-[side=top]:inset-x-0 data-[side=top]:top-0 data-[side=top]:h-auto data-[side=top]:border-b data-[side=top]:data-[ending-style]:translate-y-[-2.5rem] data-[side=top]:data-[starting-style]:translate-y-[-2.5rem] data-[side=left]:sm:max-w-sm data-[side=right]:sm:max-w-sm",
              e,
            ),
            ...i,
            children: [
              t,
              r &&
                (0, d.jsxs)(sk.Close, {
                  "data-slot": "sheet-close",
                  render: (0, d.jsx)(i_, { variant: "ghost", className: "absolute top-3 right-3", size: "icon-sm" }),
                  children: [(0, d.jsx)(sw, {}), (0, d.jsx)("span", { className: "sr-only", children: "Close" })],
                }),
            ],
          }),
        ],
      });
    }
    function sP({ className: e, ...t }) {
      return (0, d.jsx)("div", { "data-slot": "sheet-header", className: ih("flex flex-col gap-0.5 p-4", e), ...t });
    }
    function sT({ className: e, ...t }) {
      return (0, d.jsx)(sk.Title, {
        "data-slot": "sheet-title",
        className: ih("font-heading text-base font-medium text-foreground", e),
        ...t,
      });
    }
    (e.s([], 59657), e.i(59657));
    let sA = f.createContext({
      register: () => {},
      unregister: () => {},
      subscribeMapChange: () => () => {},
      nextIndexRef: { current: 0 },
    });
    function sO(e) {
      let { children: t, elementsRef: n, labelsRef: r, onMapChange: i } = e,
        o = iT(i),
        [, l] = f.useState(!1),
        a = n9(sM).current,
        s = n9(sI).current,
        u = f.useRef(0),
        c = f.useRef(!0),
        p = f.useRef([]),
        h = f.useRef(null),
        m = iT(() => {
          c.current || ((c.current = !0), l((e) => !e));
        }),
        g = iT((e, t) => {
          (s.set(e, t), m());
        }),
        v = iT((e) => {
          (s.delete(e), m());
        }),
        y = iT((e) => {
          let t = new Map();
          return (
            (n.current.length = 0),
            r && (r.current.length = 0),
            e.forEach((e) => {
              (t.set(e.element, { ...(e.registration.metadata ?? {}), index: e.index }),
                (n.current[e.index] = e.element),
                r &&
                  (r.current[e.index] =
                    void 0 !== e.registration.label
                      ? e.registration.label
                      : (e.registration.textRef?.current?.textContent ?? e.element.textContent)));
            }),
            (u.current = n.current.length),
            t
          );
        }),
        b = iT(() => {
          var e;
          let t,
            n,
            r,
            i,
            [l, u] =
              ((e = s),
              (t = new Set()),
              (n = []),
              (r = []),
              e.forEach((e, i) => {
                if (!i.isConnected) return;
                let o = e.index,
                  l = { index: o ?? -1, element: i, registration: e };
                null === o ? r.push(l) : o >= 0 && (t.add(o), n.push(l));
              }),
              (i = 0),
              r.sort((e, t) => sN(e.element, t.element)),
              r.forEach((e) => {
                for (; t.has(i); ) i += 1;
                ((e.index = i), n.push(e), (i += 1));
              }),
              t.size > 0 && n.sort((e, t) => e.index - t.index),
              [n, r.map((e) => e.element)]),
            d = y(l);
          (!(function (e) {
            if ((h.current?.disconnect(), (h.current = null), "function" != typeof MutationObserver || e.length < 2))
              return;
            let t = new MutationObserver((n) => {
              if (
                !(function (e) {
                  for (let t of e)
                    for (let e = 0; e < t.removedNodes.length; e += 1) if (t.removedNodes[e].isConnected) return !0;
                  return !1;
                })(n)
              )
                return;
              let r = null;
              for (let n of e)
                if (n.isConnected) {
                  if (r && sN(r, n) > 0) {
                    (t.disconnect(), m());
                    return;
                  }
                  r = n;
                }
            });
            h.current = t;
            let n = new Set();
            for (let t = 1; t < e.length; t += 1) {
              let r = (function (e, t) {
                let n = e.parentElement;
                for (; n && !n.contains(t); ) n = n.parentElement;
                return n;
              })(e[t - 1], e[t]);
              r && n.add(r);
            }
            n.forEach((e) => t.observe(e, { childList: !0 }));
          })(u),
            (p.current = l),
            (c.current = !1),
            a.forEach((e) => e(d)),
            o(d));
        });
      (iI(
        () => (
          c.current || y(p.current),
          () => {
            ((n.current = []), r && (r.current = []));
          }
        ),
        [n, r, y],
      ),
        iI(() => {
          c.current && b();
        }),
        iI(
          () => () => {
            (h.current?.disconnect(), (c.current = !0));
          },
          [],
        ));
      let x = iT(
          (e) => (
            a.add(e),
            () => {
              a.delete(e);
            }
          ),
        ),
        k = f.useMemo(() => ({ register: g, unregister: v, subscribeMapChange: x, nextIndexRef: u }), [g, v, x, u]);
      return (0, d.jsx)(sA.Provider, { value: k, children: t });
    }
    function sI() {
      return new Map();
    }
    function sM() {
      return new Set();
    }
    function sN(e, t) {
      return e.compareDocumentPosition(t) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
    }
    let sz = f.createContext(void 0);
    function sD() {
      let e = f.useContext(sz);
      if (void 0 === e) throw Error(n3(64));
      return e;
    }
    let sL = { tabActivationDirection: (e) => ({ "data-activation-direction": e }) };
    var oT = oT;
    let s$ = f.forwardRef(function (e, t) {
      let {
          className: n,
          defaultValue: r = 0,
          onValueChange: i,
          orientation: o = "horizontal",
          render: l,
          value: a,
          style: s,
          ...u
        } = e,
        c = void 0 !== e.defaultValue,
        p = f.useRef([]),
        [h, m] = f.useState(() => new Map()),
        [g, v] = oR({ controlled: a, default: r, name: "Tabs", state: "value" }),
        y = void 0 !== a,
        [b, x] = f.useState(() => new Map()),
        k = f.useRef(void 0),
        w = f.useCallback((e) => sF(b, e), [b]),
        [S, C] = f.useState(() => ({ previousValue: g, tabActivationDirection: "none" })),
        { previousValue: E, tabActivationDirection: j } = S,
        R = j,
        P = !1;
      E !== g && ((R = s_(E, g, o, b)), (P = null != E && null != g && null == w(g)));
      let T = P ? E : g,
        A = E !== T || j !== R;
      iI(() => {
        A && C({ previousValue: T, tabActivationDirection: R });
      }, [T, A, R]);
      let O = iT((e, t) => {
          ((t.activationDirection = s_(g, e, o, b)), i?.(e, t), t.isCanceled || v(e));
        }),
        I = iT((e, t) => {
          i?.(e, oP(t, void 0, void 0, { activationDirection: "none" }));
        }),
        M = iT(
          (e, t) => (
            m((n) => {
              let r = new Map(n);
              return (r.set(e, t), r);
            }),
            () => {
              m((n) => {
                if (n.get(e) !== t) return n;
                let r = new Map(n);
                return (r.delete(e), r);
              });
            }
          ),
        ),
        N = f.useCallback((e) => h.get(e), [h]),
        z = f.useCallback(
          (e) => {
            for (let t of b.values()) if (e === t.value) return t.id;
          },
          [b],
        ),
        D = f.useMemo(
          () => ({
            getTabElementBySelectedValue: w,
            getTabIdByPanelValue: z,
            getTabPanelIdByValue: N,
            onValueChange: O,
            orientation: o,
            registerMountedTabPanel: M,
            setTabMap: x,
            tabActivationDirection: R,
            value: g,
          }),
          [w, z, N, O, o, M, x, R, g],
        ),
        L = f.useMemo(() => {
          for (let e of b.values()) if (e.value === g) return e;
        }, [b, g]),
        $ = f.useMemo(() => {
          for (let e of b.values()) if (!e.disabled) return e.value;
        }, [b]),
        F = f.useRef(!c),
        _ = f.useRef(r),
        B = f.useRef(c),
        H = f.useRef(!1);
      iI(() => {
        if (y) return;
        function e(e, t) {
          (v(e), C({ previousValue: e, tabActivationDirection: "none" }), I(e, t), (F.current = !1));
        }
        if (0 === b.size) {
          H.current && null !== g && !k.current?.isConnected && e(null, oT.missing);
          return;
        }
        ((H.current = !0), (k.current = b.keys().next().value));
        let t = L?.disabled,
          n = null == L && null !== g;
        if ((t || g !== _.current || (B.current = !1), B.current && t && g === _.current)) return;
        let r = F.current;
        if (t || n) {
          let n = $ ?? null;
          if (g === n) {
            F.current = !1;
            return;
          }
          let i = oT.missing;
          (r ? (i = oT.initial) : t && (i = oT.disabled), e(n, i));
          return;
        }
        r && null != L && (I(g, oT.initial), (F.current = !1));
      }, [$, y, I, L, v, b, g]);
      let q = rl("div", e, {
        state: { orientation: o, tabActivationDirection: R },
        ref: t,
        props: u,
        stateAttributesMapping: sL,
      });
      return (0, d.jsx)(sz.Provider, { value: D, children: (0, d.jsx)(sO, { elementsRef: p, children: q }) });
    });
    function sF(e, t) {
      for (let [n, r] of e.entries()) if (t === r.value) return n;
      return null;
    }
    function s_(e, t, n, r) {
      if (null == e || null == t) return "none";
      let [i, o, l] = "horizontal" === n ? ["left", "left", "right"] : ["top", "up", "down"],
        a = sF(r, e),
        s = sF(r, t);
      if (null == a || null == s)
        return a !== s && ("number" == typeof e || "string" == typeof e) && typeof e == typeof t
          ? t > e
            ? l
            : o
          : "none";
      let u = a.getBoundingClientRect()[i],
        c = s.getBoundingClientRect()[i];
      return c < u ? o : c > u ? l : "none";
    }
    let sB = "data-composite-item-active";
    function sH(e = {}) {
      let { guess: t, label: n, metadata: r, textRef: i, index: o } = e,
        { register: l, unregister: a, subscribeMapChange: s, nextIndexRef: u } = f.useContext(sA),
        c = f.useRef(-1),
        [d, p] = f.useState(
          null == o && t
            ? () => {
                if (-1 === c.current) {
                  let e = u.current;
                  ((u.current += 1), (c.current = e));
                }
                return c.current;
              }
            : -1,
        ),
        h = o ?? d,
        m = f.useRef(null),
        g = f.useCallback(
          (e) => {
            let t = m.current;
            (t && a(t), (m.current = e), e && l(e, { metadata: r ?? null, index: o ?? null, label: n, textRef: i }));
          },
          [o, l, a, r, n, i],
        );
      return (
        iI(() => {
          if (null == o)
            return s((e) => {
              let t = m.current ? e.get(m.current)?.index : null;
              null != t && p(t);
            });
        }, [o, s]),
        { ref: g, index: h }
      );
    }
    let sq = f.createContext(void 0);
    function sU() {
      let e = f.useContext(sq);
      if (void 0 === e) throw Error(n3(65));
      return e;
    }
    var oT = oT;
    let sW = f.forwardRef(function (e, t) {
        let { className: n, disabled: r = !1, render: i, value: o, id: l, nativeButton: a = !0, style: s, ...u } = e,
          { value: c, getTabPanelIdByValue: d, onValueChange: p, orientation: h, tabActivationDirection: m } = sD(),
          { activateOnFocus: g, registerTabResizeObserverElement: v, tabsListElement: y } = sU(),
          { highlightedIndex: b, onHighlightedIndexChange: x } = iN(),
          k = i4(l),
          {
            compositeProps: w,
            compositeRef: S,
            index: C,
          } = (function (e = {}) {
            let { highlightItemOnHover: t, highlightedIndex: n, onHighlightedIndexChange: r } = iN(),
              { ref: i, index: o } = sH(e),
              l = n === o,
              a = f.useRef(null),
              s = n7(i, a);
            return {
              compositeProps: {
                tabIndex: l ? 0 : -1,
                onFocus() {
                  r(o);
                },
                onMouseMove() {
                  let e = a.current;
                  if (!t || !e) return;
                  let n = e.hasAttribute("disabled") || "true" === e.ariaDisabled;
                  l || n || e.focus();
                },
              },
              compositeRef: s,
              index: o,
            };
          })({ metadata: f.useMemo(() => ({ disabled: r, id: k, value: o }), [r, k, o]) }),
          E = o === c,
          j = f.useRef(!1),
          R = f.useRef(null),
          P = iT((e) => {
            (R.current?.(), (R.current = e ? v(e) : null));
          });
        iI(() => {
          if (j.current) {
            j.current = !1;
            return;
          }
          if (E && C > -1 && b !== C) {
            if (null != y) {
              let e = oa(ol(y));
              if (e && os(y, e)) return;
            }
            r || x(C);
          }
        }, [E, C, b, x, r, y]);
        let { getButtonProps: T, buttonRef: A } = iD({ disabled: r, native: a, focusableWhenDisabled: !0 }),
          O = d(o),
          I = f.useRef(!1),
          M = f.useRef(!1);
        function N(e) {
          p(o, oP(oT.none, e.nativeEvent, void 0, { activationDirection: "none" }));
        }
        return rl("button", e, {
          state: { disabled: r, active: E, orientation: h, tabActivationDirection: m },
          ref: [t, A, S, P],
          props: [
            w,
            {
              role: "tab",
              "aria-controls": O,
              "aria-selected": E,
              id: k,
              onClick: function (e) {
                E || r || N(e);
              },
              onFocus: function (e) {
                E || r || (g && (!I.current || M.current) && N(e));
              },
              onPointerDown: function (e) {
                if (E || r) return;
                ((I.current = !0), (M.current = 0 === e.button));
                let t = ol(e.currentTarget);
                function n() {
                  ((I.current = !1),
                    (M.current = !1),
                    t.removeEventListener("pointerup", n),
                    t.removeEventListener("pointercancel", n));
                }
                (t.addEventListener("pointerup", n), t.addEventListener("pointercancel", n));
              },
              [sB]: E ? "" : void 0,
              onKeyDownCapture() {
                j.current = !0;
              },
            },
            u,
            T,
          ],
          stateAttributesMapping: sL,
        });
      }),
      sV = Math.round;
    function sK(e) {
      let t = iE(e),
        n = parseFloat(t.width) || 0,
        r = parseFloat(t.height) || 0,
        i = iw(e),
        o = i ? e.offsetWidth : n,
        l = i ? e.offsetHeight : r;
      return ((sV(n) !== o || sV(r) !== l) && ((n = o), (r = l)), { width: n, height: r });
    }
    function sX() {
      return rr;
    }
    function sY() {
      return !1;
    }
    function sG() {
      return !0;
    }
    function sJ(e) {
      let { script: t } = e,
        { nonce: n } = oq();
      return (0, aK.useSyncExternalStore)(sX, sY, sG)
        ? (0, d.jsx)("script", { nonce: n, dangerouslySetInnerHTML: { __html: t }, suppressHydrationWarning: !0 })
        : null;
    }
    let sQ = { ...sL, activeTabPosition: () => null, activeTabSize: () => null },
      sZ = f.forwardRef(function (e, t) {
        let { className: n, render: r, renderBeforeHydration: i = !1, style: o, ...l } = e,
          { getTabElementBySelectedValue: a, orientation: s, tabActivationDirection: u, value: p } = sD(),
          { tabsListElement: h, registerIndicatorUpdateListener: m } = sU(),
          g = (function () {
            let [, e] = f.useState({});
            return f.useCallback(() => {
              e({});
            }, []);
          })();
        f.useEffect(() => m(g), [m, g]);
        let v = 0,
          y = 0,
          b = 0,
          x = 0,
          k = 0,
          w = 0,
          S = !1;
        if (null != p && null != h) {
          let e = a(p);
          if (null != e) {
            S = !0;
            let { width: t, height: n } = sK(e),
              { width: r, height: i } = sK(h),
              o = e.getBoundingClientRect(),
              l = h.getBoundingClientRect(),
              a = r > 0 ? l.width / r : 1,
              s = i > 0 ? l.height / i : 1;
            if (a > Number.EPSILON && s > Number.EPSILON) {
              let e = o.left - l.left,
                t = o.top - l.top;
              ((v = e / a + h.scrollLeft - h.clientLeft), (b = t / s + h.scrollTop - h.clientTop));
            } else ((v = e.offsetLeft), (b = e.offsetTop));
            ((k = t), (w = n), (y = h.scrollWidth - v - k), (x = h.scrollHeight - b - w));
          }
        }
        let C = S ? { left: v, right: y, top: b, bottom: x } : null,
          E = S ? { width: k, height: w } : null,
          j = rl("span", e, {
            state: { orientation: s, activeTabPosition: C, activeTabSize: E, tabActivationDirection: u },
            ref: t,
            props: [
              {
                role: "presentation",
                style: S
                  ? {
                      "--active-tab-left": `${v}px`,
                      "--active-tab-right": `${y}px`,
                      "--active-tab-top": `${b}px`,
                      "--active-tab-bottom": `${x}px`,
                      "--active-tab-width": `${k}px`,
                      "--active-tab-height": `${w}px`,
                    }
                  : void 0,
                hidden: !(S && k > 0 && w > 0),
              },
              l,
              { suppressHydrationWarning: !0 },
            ],
            stateAttributesMapping: sQ,
          });
        return null == p
          ? null
          : (0, d.jsxs)(f.Fragment, { children: [j, i && (c || (c = (0, d.jsx)(sJ, { script: "" })))] });
      }),
      s0 = { ...sL, ...ow },
      s1 = f.forwardRef(function (e, t) {
        let { className: n, value: r, render: i, keepMounted: o = !1, style: l, ...a } = e,
          {
            value: s,
            getTabIdByPanelValue: u,
            orientation: c,
            tabActivationDirection: d,
            registerMountedTabPanel: p,
          } = sD(),
          h = i4(),
          { ref: m, index: g } = sH(),
          v = r === s,
          { mounted: y, transitionStatus: b, setMounted: x } = oS(v),
          k = !y,
          w = u(r),
          S = f.useRef(null),
          C = rl("div", e, {
            state: { hidden: k, orientation: c, tabActivationDirection: d, transitionStatus: b },
            ref: [t, m, S],
            props: [
              {
                "aria-labelledby": w,
                hidden: k,
                id: h,
                role: "tabpanel",
                tabIndex: v ? 0 : -1,
                inert: a5(!v),
                "data-index": g,
              },
              a,
            ],
            stateAttributesMapping: s0,
          });
        return (oy({
          open: v,
          ref: S,
          onComplete() {
            v || x(!1);
          },
        }),
        iI(() => {
          if (null != h && (!k || o)) return p(r, h);
        }, [k, o, r, h, p]),
        o || y)
          ? C
          : null;
      }),
      s2 = [];
    function s4(e) {
      let {
          render: t,
          className: n,
          style: r,
          refs: i = ri,
          props: o = ri,
          state: l = ro,
          stateAttributesMapping: a,
          highlightedIndex: s,
          onHighlightedIndexChange: u,
          orientation: c,
          grid: p,
          loopFocus: h,
          onLoop: m,
          enableHomeAndEndKeys: g,
          onMapChange: v,
          stopEventPropagation: y = !0,
          rootRef: b,
          disabledIndices: x,
          modifierKeys: k,
          highlightItemOnHover: w = !1,
          tag: S = "div",
          ...C
        } = e,
        {
          props: E,
          highlightedIndex: j,
          onHighlightedIndexChange: R,
          elementsRef: P,
          onMapChange: T,
          relayKeyboardEvent: A,
        } = (function (e) {
          let {
              loopFocus: t = !0,
              orientation: n = "both",
              grid: r,
              onLoop: i,
              direction: o,
              highlightedIndex: l,
              onHighlightedIndexChange: a,
              rootRef: s,
              enableHomeAndEndKeys: u = !1,
              stopEventPropagation: c,
              disabledIndices: d,
              modifierKeys: p = s2,
            } = e,
            [h, m] = f.useState(0),
            g = null != r,
            v = f.useRef(null),
            y = n7(v, s),
            b = f.useRef([]),
            x = f.useRef(!1),
            k = l ?? h,
            w = iT((e, t = !1) => {
              if (((a ?? m)(e), t)) {
                let t = b.current[e];
                aU(v.current, t, o, n);
              }
            }),
            S = iT((e) => {
              if (0 === e.size || x.current) return;
              x.current = !0;
              let t = Array.from(e.keys()),
                r = t.find((e) => e?.hasAttribute(sB)) ?? null,
                i = r ? (e.get(r)?.index ?? -1) : -1;
              if (-1 !== i) w(i);
              else if (l0(t, k, d)) {
                let e = lZ(t, { disabledIndices: d });
                lQ(t, e) || w(e);
              }
              aU(v.current, r, o, n);
            });
          iI(() => {
            if (null == d || null != l || !x.current) return;
            let e = b.current;
            if (l0(e, k, d)) {
              let t = lZ(e, { disabledIndices: d });
              lQ(e, t) || w(t);
            }
          }, [d, l, k, b, w]);
          let C = iT((e, t, n) => (i ? i(e, t, n, b) : n)),
            E = iT((e) => {
              let l = e.key === a_ || "End" === e.key;
              if (
                !aB.has(e.key) ||
                (!u && l) ||
                (function (e, t) {
                  for (let n of aH) if (!t.includes(n) && e.getModifierState(n)) return !0;
                  return !1;
                })(e, p) ||
                !v.current
              )
                return;
              let a = "rtl" === o,
                s = a ? a$ : aF,
                f = a ? aF : a$,
                h = "vertical" === n ? aL : s,
                m = "vertical" === n ? aD : f,
                y = ou(e.nativeEvent);
              if (
                null != y &&
                aq(y) &&
                !(null == y || y.hasAttribute("disabled") || "true" === y.getAttribute("aria-disabled"))
              ) {
                let t = y.selectionStart,
                  n = y.selectionEnd,
                  r = y.value;
                if (null == t || e.shiftKey || t !== n || (e.key !== m && t < r.length) || (e.key !== h && t > 0))
                  return;
              }
              let x = k,
                S = lZ(b.current, { disabledIndices: d }),
                E = lZ(b.current, { decrement: !0, startingIndex: b.current.length, disabledIndices: d });
              null != r &&
                (x = r({
                  disabledIndices: d,
                  elementsRef: b,
                  event: e,
                  highlightedIndex: k,
                  loopFocus: t,
                  maxIndex: E,
                  minIndex: S,
                  onLoop: C,
                  orientation: n,
                  rtl: a,
                }));
              let j = ("vertical" !== n && e.key === s) || ("horizontal" !== n && e.key === aL),
                R = ("vertical" !== n && e.key === f) || ("horizontal" !== n && e.key === aD);
              (u && (e.key === a_ ? (x = S) : "End" === e.key && (x = E)),
                x === k &&
                  (j || R) &&
                  (t && x === E && j
                    ? ((x = S), i && (x = i(e, k, x, b)))
                    : t && x === S && R
                      ? ((x = E), i && (x = i(e, k, x, b)))
                      : (x = lZ(b.current, { startingIndex: x, decrement: R, disabledIndices: d }))),
                x === k ||
                  lQ(b.current, x) ||
                  (c && e.stopPropagation(),
                  (g || l || j || R) && e.preventDefault(),
                  w(x, !0),
                  queueMicrotask(() => {
                    b.current[x]?.focus();
                  })));
            });
          return {
            props: {
              ref: y,
              onFocus(e) {
                let t = v.current,
                  n = ou(e.nativeEvent);
                t && null != n && aq(n) && n.setSelectionRange(0, n.value.length);
              },
              onKeyDown: E,
            },
            highlightedIndex: k,
            onHighlightedIndexChange: w,
            elementsRef: b,
            onMapChange: S,
            relayKeyboardEvent: E,
          };
        })({
          grid: p,
          loopFocus: h,
          onLoop: m,
          orientation: c,
          highlightedIndex: s,
          onHighlightedIndexChange: u,
          rootRef: b,
          stopEventPropagation: y,
          enableHomeAndEndKeys: g,
          direction: ls(),
          disabledIndices: x,
          modifierKeys: k,
        }),
        O = rl(S, e, { state: l, ref: i, props: [E, ...o, C], stateAttributesMapping: a }),
        I = f.useMemo(
          () => ({ highlightedIndex: j, onHighlightedIndexChange: R, highlightItemOnHover: w, relayKeyboardEvent: A }),
          [j, R, w, A],
        );
      return (0, d.jsx)(iM.Provider, {
        value: I,
        children: (0, d.jsx)(sO, {
          elementsRef: P,
          onMapChange: (e) => {
            (v?.(e), T(e));
          },
          children: O,
        }),
      });
    }
    let s5 = f.forwardRef(function (e, t) {
      let { activateOnFocus: n = !1, className: r, loopFocus: i = !0, render: o, style: l, ...a } = e,
        { orientation: s, setTabMap: u, tabActivationDirection: c } = sD(),
        [p, h] = f.useState(0),
        [m, g] = f.useState(null),
        v = f.useRef(new Set()),
        y = f.useRef(new Set()),
        b = f.useRef(null);
      iI(() => {
        if ("u" < typeof ResizeObserver) return;
        let e = new ResizeObserver(() => {
          v.current.forEach((e) => {
            e();
          });
        });
        return (
          (b.current = e),
          m && e.observe(m),
          y.current.forEach((t) => {
            e.observe(t);
          }),
          () => {
            (e.disconnect(), (b.current = null));
          }
        );
      }, [m]);
      let x = iT(
          (e) => (
            v.current.add(e),
            () => {
              v.current.delete(e);
            }
          ),
        ),
        k = iT(
          (e) => (
            y.current.add(e),
            b.current?.observe(e),
            () => {
              (y.current.delete(e), b.current?.unobserve(e));
            }
          ),
        ),
        w = f.useMemo(
          () => ({
            activateOnFocus: n,
            registerIndicatorUpdateListener: x,
            registerTabResizeObserverElement: k,
            tabsListElement: m,
          }),
          [n, x, k, m],
        );
      return (0, d.jsx)(sq.Provider, {
        value: w,
        children: (0, d.jsx)(s4, {
          render: o,
          className: r,
          style: l,
          state: { orientation: s, tabActivationDirection: c },
          refs: [t, g],
          props: [{ "aria-orientation": "vertical" === s ? "vertical" : void 0, role: "tablist" }, a],
          stateAttributesMapping: sL,
          highlightedIndex: p,
          enableHomeAndEndKeys: !0,
          loopFocus: i,
          orientation: s,
          onHighlightedIndexChange: h,
          onMapChange: u,
          disabledIndices: ri,
        }),
      });
    });
    e.s(["Indicator", 0, sZ, "List", 0, s5, "Panel", 0, s1, "Root", 0, s$, "Tab", 0, sW], 69281);
    var s3 = e.i(69281),
      s3 = s3;
    function s6({ className: e, orientation: t = "horizontal", ...n }) {
      return (0, d.jsx)(s3.Root, {
        "data-slot": "tabs",
        "data-orientation": t,
        className: ih("group/tabs flex gap-2 data-[orientation=horizontal]:flex-col", e),
        ...n,
      });
    }
    let s9 = rc(
      "group/tabs-list inline-flex w-fit items-center justify-center rounded-lg p-[3px] text-muted-foreground group-data-horizontal/tabs:h-8 group-data-vertical/tabs:h-fit group-data-vertical/tabs:flex-col data-[variant=line]:rounded-none",
      {
        variants: { variant: { default: "bg-muted", line: "gap-1 bg-transparent" } },
        defaultVariants: { variant: "default" },
      },
    );
    function s7({ className: e, variant: t = "default", ...n }) {
      return (0, d.jsx)(s3.List, {
        "data-slot": "tabs-list",
        "data-variant": t,
        className: ih(s9({ variant: t }), e),
        ...n,
      });
    }
    function s8({ className: e, ...t }) {
      return (0, d.jsx)(s3.Tab, {
        "data-slot": "tabs-trigger",
        className: ih(
          "relative inline-flex h-[calc(100%-1px)] flex-1 items-center justify-center gap-1.5 rounded-md border border-transparent px-1.5 py-0.5 text-sm font-medium whitespace-nowrap text-foreground/60 transition-all group-data-[orientation=vertical]/tabs:w-full group-data-[orientation=vertical]/tabs:justify-start hover:text-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1 focus-visible:outline-ring disabled:pointer-events-none disabled:opacity-50 has-data-[icon=inline-end]:pr-1 has-data-[icon=inline-start]:pl-1 aria-disabled:pointer-events-none aria-disabled:opacity-50 dark:text-muted-foreground dark:hover:text-foreground group-data-[variant=default]/tabs-list:data-[active]:shadow-sm group-data-[variant=line]/tabs-list:data-[active]:shadow-none [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
          "group-data-[variant=line]/tabs-list:bg-transparent group-data-[variant=line]/tabs-list:data-[active]:bg-transparent dark:group-data-[variant=line]/tabs-list:data-[active]:border-transparent dark:group-data-[variant=line]/tabs-list:data-[active]:bg-transparent",
          "data-[active]:bg-background data-[active]:text-foreground dark:data-[active]:border-input dark:data-[active]:bg-input/30 dark:data-[active]:text-foreground",
          "after:absolute after:bg-foreground after:opacity-0 after:transition-opacity group-data-[orientation=horizontal]/tabs:after:inset-x-0 group-data-[orientation=horizontal]/tabs:after:bottom-[-5px] group-data-[orientation=horizontal]/tabs:after:h-0.5 group-data-[orientation=vertical]/tabs:after:inset-y-0 group-data-[orientation=vertical]/tabs:after:-right-1 group-data-[orientation=vertical]/tabs:after:w-0.5 group-data-[variant=line]/tabs-list:data-[active]:after:opacity-100",
          e,
        ),
        ...t,
      });
    }
    function ue({ className: e, ...t }) {
      return (0, d.jsx)(s3.Panel, {
        "data-slot": "tabs-content",
        className: ih("flex-1 text-sm outline-none", e),
        ...t,
      });
    }
    function ut({ className: e, ...t }) {
      return (0, d.jsx)("textarea", {
        "data-slot": "textarea",
        className: ih(
          "flex field-sizing-content min-h-16 w-full rounded-lg border border-input bg-transparent px-2.5 py-2 text-base transition-colors outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:bg-input/50 disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 md:text-sm dark:bg-input/30 dark:disabled:bg-input/80 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40",
          e,
        ),
        ...t,
      });
    }
    let un = new Set(["delete", "get", "head", "options", "patch", "post", "put", "trace"]),
      ur = new Set([
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "false",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "none",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "true",
        "try",
        "while",
        "with",
        "yield",
      ]);
    function ui(e) {
      let t =
        e
          .replace(/[’']s\b/g, "")
          .replace(/([a-z0-9])([A-Z])/g, "$1_$2")
          .replace(/[^a-zA-Z0-9]+/g, "_")
          .replace(/^_+|_+$/g, "")
          .toLowerCase() || "value";
      return ur.has(t) ? `${t}_` : /^[a-z_]/.test(t) ? t : `_${t}`;
    }
    function uo(e, t = !1, n = !1) {
      let r = (e) => {
        let t = encodeURIComponent(String(e));
        return n
          ? t.replace(/%(3A|2F|3F|23|5B|5D|40|21|24|26|27|28|29|2A|2B|2C|3B|3D)/gi, (e) => decodeURIComponent(e))
          : t;
      };
      return Array.isArray(e)
        ? e.map(r).join(",")
        : e && "object" == typeof e
          ? Object.entries(e)
              .flatMap(([e, n]) => (t ? `${r(e)}=${r(n)}` : [r(e), r(n)]))
              .join(",")
          : r(e);
    }
    function ul(e, t, n = "form", r = !0, i = !1) {
      let o = (e, t = !1) => {
          let n = encodeURIComponent(String(e));
          return t
            ? n.replace(/%(3A|2F|3F|23|5B|5D|40|21|24|26|27|28|29|2A|2B|2C|3B|3D)/gi, (e) => decodeURIComponent(e))
            : n;
        },
        l = (e, t) => `${o(e)}=${o(t, i)}`;
      if (Array.isArray(t))
        return "form" === n && r
          ? t.map((t) => l(e, t)).join("&")
          : l(e, t.join("spaceDelimited" === n ? " " : "pipeDelimited" === n ? "|" : ","));
      if (t && "object" == typeof t) {
        let i = Object.entries(t);
        return "deepObject" === n
          ? i.map(([t, n]) => l(`${e}[${t}]`, n)).join("&")
          : r
            ? i.map(([e, t]) => l(e, t)).join("&")
            : l(e, i.flat().join(","));
      }
      return l(e, t);
    }
    function ua(e) {
      return e.endsWith("ies") ? `${e.slice(0, -3)}y` : e.endsWith("s") ? e.slice(0, -1) : e;
    }
    function us(e) {
      let t = ui(e.summary ?? e.id).split("_"),
        n = t.shift() ?? e.method,
        r =
          "get" === n || "check" === n || "download" === n || "summarize" === n
            ? "retrieve"
            : "view" === n
              ? t.some((e) => "history" === e || e.endsWith("s"))
                ? "list"
                : "retrieve"
              : n,
        i = new Set(["a", "an", "new", "someone", "the", "to", "your"]),
        o = ua(ui(e.tag));
      return ui([r, ...t.filter((e) => !i.has(e) && ua(e) !== o)].join("_"));
    }
    function uu(e) {
      let t = [],
        n = new Map();
      for (let [r, i] of Object.entries(e.paths)) {
        let o = (i.parameters ?? []).map((t) => ud(e, t));
        for (let [l, a] of Object.entries(i)) {
          if (!un.has(l) || !a) continue;
          let s = a.tags?.[0] ?? "Other",
            u = ui(s),
            c = [...o];
          for (let t of (a.parameters ?? []).map((t) => ud(e, t))) {
            let e = c.findIndex((e) => e.in === t.in && e.name === t.name);
            -1 === e ? c.push(t) : (c[e] = t);
          }
          let d = {
              ...a,
              id: a.operationId ?? `${l}-${r}`,
              method: l,
              path: r,
              parameters: c,
              requestBody: (function (e, t) {
                if (!t || !("$ref" in t)) return t;
                let n = e.components?.requestBodies?.[uc(t.$ref, "requestBodies")];
                if (!n) throw Error(`Unknown request body reference: ${t.$ref}`);
                return n;
              })(e, a.requestBody),
              responses: Object.fromEntries(
                Object.entries(a.responses ?? {}).map(([t, n]) => [
                  t,
                  (function (e, t) {
                    if (!("$ref" in t)) return t;
                    let n = e.components?.responses?.[uc(t.$ref, "responses")];
                    if (!n) throw Error(`Unknown response reference: ${t.$ref}`);
                    return n;
                  })(e, n),
                ]),
              ),
              server: a.servers?.[0] ?? i.servers?.[0] ?? e.servers?.[0],
              tag: s,
            },
            f = n.get(u) ?? new Set(),
            p = (function (e) {
              let t = e.path.split("/").filter(Boolean).slice(1);
              if (ua(ui(t[0] ?? "")) !== ua(ui(e.tag)) || ("post" === e.method && /^get\b/i.test(e.summary ?? "")))
                return us(e);
              let n = t.some((e) => e.startsWith("{")),
                r = t.slice(1).filter((e) => !e.startsWith("{")),
                i =
                  "get" === e.method
                    ? /^(list|view)\b/i.test(e.summary ?? "")
                      ? "list"
                      : n || r.length
                        ? "retrieve"
                        : "list"
                    : "post" === e.method
                      ? "create"
                      : "put" === e.method || "patch" === e.method
                        ? "update"
                        : "delete" === e.method
                          ? "delete"
                          : e.method;
              if (!r.length) return i;
              let o = r.at(-1) ?? "";
              return "post" === e.method &&
                new Set([
                  "archive",
                  "cancel",
                  "check",
                  "clone",
                  "complete",
                  "create",
                  "delete",
                  "empty",
                  "ingest",
                  "merge",
                  "predict",
                  "redistribute",
                  "restore",
                  "revoke",
                  "start",
                  "stop",
                  "track-download",
                  "transfer-ownership",
                ]).has(o)
                ? ui([o, ...r.slice(0, -1)].join("_"))
                : ui([i, ...r].join("_"));
            })(d);
          if (f.has(p)) {
            let e = (p = `${p}_${us(d).replace(/^(get|list|create|update|delete)_/, "")}`);
            for (let t = 2; f.has(p); t += 1) p = `${e}_${t}`;
          }
          (f.add(p),
            n.set(u, f),
            t.push({ ...d, id: d.id, method: l, path: r, parameters: c, resource: u, sdkMethod: p, tag: s }));
        }
      }
      return t;
    }
    function uc(e, t) {
      let n = `#/components/${t}/`;
      if (!e.startsWith(n)) throw Error(`Unsupported reference: ${e}`);
      return decodeURIComponent(e.slice(n.length));
    }
    function ud(e, t) {
      let n;
      if ("$ref" in t && t.$ref.startsWith("#/components/parameters/")) {
        let r = decodeURIComponent(t.$ref.slice(24)),
          i = e.components?.parameters?.[r];
        if (!i) throw Error(`Unknown parameter reference: ${t.$ref}`);
        n = i;
      } else n = t;
      if (n.content) throw Error(`Unsupported content parameter: ${n.in} ${n.name}`);
      return n;
    }
    function uf(e) {
      return e.url.replace(/{([^}]+)}/g, (t, n) => e.variables?.[n]?.default ?? `{${n}}`);
    }
    function up(e, t) {
      let n = new Set(
          (t ? (t.security ?? e.security ?? []) : uu(e).flatMap((t) => t.security ?? e.security ?? [])).flatMap((e) =>
            Object.keys(e),
          ),
        ),
        r = [...n].flatMap((t) => {
          let n = e.components?.securitySchemes?.[t];
          return n?.type === "apiKey" && "header" === n.in && n.name
            ? [{ header: n.name, prefix: "" }]
            : n?.type === "http" && n.scheme?.toLowerCase() === "bearer"
              ? [{ header: "Authorization", prefix: "Bearer " }]
              : [];
        });
      if (r.length !== n.size) throw Error("Unsupported authentication scheme");
      let i = [...new Map(r.map((e) => [`${e.header}:${e.prefix}`, e])).values()];
      if (i.length > 1) throw Error("Multiple authentication schemes require separate generated clients");
      return i[0];
    }
    function uh(e, t, n = new Set()) {
      if (!t?.$ref?.startsWith("#/components/schemas/")) return t;
      let r = decodeURIComponent(t.$ref.slice(21));
      if (n.has(r)) return t;
      let i = e.components?.schemas?.[r];
      if (!i) return t;
      let o = uh(e, i, new Set([...n, r])),
        l = { ...t };
      return (
        delete l.$ref,
        {
          ...o,
          ...l,
          properties: o?.properties || l.properties ? { ...o?.properties, ...l.properties } : void 0,
          required: o?.required || l.required ? [...new Set([...(o?.required ?? []), ...(l.required ?? [])])] : void 0,
        }
      );
    }
    function um(e, t) {
      let n = uh(e, t);
      if (!n) return;
      if (n.allOf?.length) {
        let t = n.allOf.map((t) => um(e, t)).filter((e) => e?.properties);
        if (t.length)
          return {
            ...n,
            properties: Object.assign({}, n.properties, ...t.map((e) => e?.properties)),
            required: [...new Set([...(n.required ?? []), ...t.flatMap((e) => e?.required ?? [])])],
            type: "object",
          };
      }
      let r = n.anyOf ?? n.oneOf;
      if (!r?.length) return n;
      let i = r.map((t) => um(e, t)).filter((e) => e?.properties);
      if (!i.length) return n;
      let o = new Set(i[0]?.required ?? []);
      for (let e of i.slice(1)) {
        let t = new Set(e?.required ?? []);
        for (let e of o) t.has(e) || o.delete(e);
      }
      for (let e of n.required ?? []) o.add(e);
      let l = { ...n.properties };
      for (let e of i)
        for (let [t, n] of Object.entries(e?.properties ?? {})) {
          let e = l[t];
          l[t] =
            e && JSON.stringify(e) !== JSON.stringify(n)
              ? { anyOf: [...(e.anyOf ?? [e]), n], description: e.description ?? n.description }
              : n;
        }
      return { ...n, properties: l, required: [...o], type: "object" };
    }
    function ug(e, t, n = 0) {
      if (!t || n > 5) return null;
      let r = uh(e, t) ?? t;
      if (void 0 !== r.example) return r.example;
      if (void 0 !== r.default) return r.default;
      if (void 0 !== r.const) return r.const;
      if (r.enum?.length) return r.enum[0];
      let i = r.oneOf ?? r.anyOf;
      if (i?.length) {
        let t = ug(e, i[0], n + 1);
        if (t && "object" == typeof t && !Array.isArray(t) && r.properties) {
          let i = ug(e, { ...r, anyOf: void 0, oneOf: void 0 }, n + 1);
          if (i && "object" == typeof i && !Array.isArray(i)) return { ...i, ...t };
        }
        return t;
      }
      if (r.allOf?.length) {
        let t = um(e, r);
        if (t?.properties) return ug(e, { ...t, allOf: void 0 }, n + 1);
      }
      let o = Array.isArray(r.type) ? r.type.find((e) => "null" !== e) : r.type;
      return "array" === o
        ? [ug(e, r.items, n + 1)]
        : "boolean" !== o &&
            ("integer" === o || "number" === o
              ? 0
              : "object" === o || r.properties
                ? Object.fromEntries(Object.entries(r.properties ?? {}).map(([t, r]) => [t, ug(e, r, n + 1)]))
                : "date-time" === r.format
                  ? "2026-01-01T00:00:00Z"
                  : "string");
    }
    function uv(e, t) {
      if (!t) return "any";
      let n = uh(e, t) ?? t;
      return t.$ref
        ? (t.$ref.split("/").at(-1) ?? "object")
        : n.enum
          ? n.enum.map(String).join(" | ")
          : n.oneOf || n.anyOf
            ? (n.oneOf ?? n.anyOf ?? []).map((t) => uv(e, t)).join(" | ")
            : Array.isArray(n.type)
              ? n.type.join(" | ")
              : "array" === n.type
                ? `${uv(e, n.items)}[]`
                : (n.type ?? (n.properties ? "object" : "any"));
    }
    function uy(e) {
      return ub(e.requestBody?.content);
    }
    function ub(e) {
      let t = Object.entries(e ?? {}).map(([e, t]) => [e.toLowerCase(), t]);
      return (
        t.find(([e]) => "application/json" === e) ??
        t.find(([e]) => e.endsWith("+json")) ??
        t.find(([e]) => ["multipart/form-data", "application/x-www-form-urlencoded"].includes(e)) ??
        t.find(([e]) => e.startsWith("text/")) ??
        t[0]
      );
    }
    let ux = {
      delete: "destructive",
      get: "secondary",
      head: "outline",
      options: "outline",
      patch: "outline",
      post: "default",
      put: "default",
      trace: "outline",
    };
    function uk(e, t) {
      let n = uy(t);
      if (!n) return "";
      let r = n[1].example ?? ug(e, n[1].schema),
        i = um(e, n[1].schema);
      if (r && "object" == typeof r && !Array.isArray(r))
        for (let [t, n] of ((r = { ...r }), Object.entries(i?.properties ?? {}))) uh(e, n)?.readOnly && delete r[t];
      return n[0].startsWith("text/") && "string" == typeof r ? r : JSON.stringify(r, null, 2);
    }
    function uw(e, t, n) {
      let r = uh(e, t.schema),
        i = Array.isArray(r?.type) ? r.type.find((e) => "null" !== e) : r?.type;
      if ("array" !== i && "object" !== i && !r?.properties) return n;
      try {
        return JSON.parse(n);
      } catch {
        throw Error(`Enter valid JSON for ${t.name}.`);
      }
    }
    function uS(e) {
      return `'${String(e).replaceAll("'", "'\"'\"'")}'`;
    }
    function uC(e) {
      return Object.entries(e).flatMap(([e, t]) =>
        Array.isArray(t) ? t.map((t) => [e, t]) : t && "object" == typeof t ? Object.entries(t) : [[e, t]],
      );
    }
    function uE({ code: e }) {
      let [t, n] = (0, f.useState)(!1);
      async function r() {
        (await navigator.clipboard.writeText(e), n(!0), window.setTimeout(() => n(!1), 1500));
      }
      return (0, d.jsxs)("div", {
        className: "relative overflow-hidden rounded-lg border bg-zinc-950 text-zinc-50",
        children: [
          (0, d.jsx)(i_, {
            "aria-label": "Copy code",
            className: "absolute top-2 right-2 text-zinc-300 hover:bg-zinc-800 hover:text-white",
            onClick: r,
            size: "icon-sm",
            variant: "ghost",
            children: t ? (0, d.jsx)(b, { "aria-hidden": "true" }) : (0, d.jsx)(x, { "aria-hidden": "true" }),
          }),
          (0, d.jsx)("pre", {
            className: "overflow-x-auto p-4 pr-12 font-mono text-xs leading-relaxed",
            children: (0, d.jsx)("code", { children: e }),
          }),
        ],
      });
    }
    function uj({ onQueryChange: e, query: t, selectedId: n, tags: r }) {
      return (0, d.jsxs)("div", {
        className: "flex min-h-0 flex-1 flex-col",
        children: [
          (0, d.jsx)("div", {
            className: "p-4",
            children: (0, d.jsxs)("div", {
              className: "relative",
              children: [
                (0, d.jsx)(E, {
                  "aria-hidden": "true",
                  className: "absolute top-1/2 left-2.5 size-4 -translate-y-1/2 text-muted-foreground",
                }),
                (0, d.jsx)(oN, {
                  "aria-label": "Search operations",
                  autoComplete: "off",
                  className: "pl-8",
                  name: "api-search",
                  onChange: (t) => e(t.target.value),
                  placeholder: "Search API",
                  value: t,
                }),
              ],
            }),
          }),
          (0, d.jsx)(lj, {}),
          (0, d.jsx)(lS, {
            className: "min-h-0 flex-1",
            children: (0, d.jsxs)("nav", {
              className: "space-y-5 p-3",
              "aria-label": "API operations",
              children: [
                (0, d.jsx)("a", {
                  className: ih(
                    "block rounded-lg px-2 py-2 text-sm font-medium transition-colors hover:bg-sidebar-accent focus-visible:ring-2 focus-visible:ring-ring",
                    !n && "bg-sidebar-accent text-sidebar-accent-foreground",
                  ),
                  href: "#overview",
                  children: "Overview",
                }),
                [...r].map(([e, t]) =>
                  (0, d.jsxs)(
                    "div",
                    {
                      children: [
                        (0, d.jsx)("p", {
                          className: "mb-1 px-2 text-xs font-semibold tracking-wide text-muted-foreground uppercase",
                          children: e,
                        }),
                        (0, d.jsx)("div", {
                          className: "space-y-0.5",
                          children: t.map((e) =>
                            (0, d.jsxs)(
                              "a",
                              {
                                className: ih(
                                  "operation-list-item flex w-full items-center gap-2 rounded-lg px-2 py-2 text-left text-sm transition-colors hover:bg-sidebar-accent",
                                  n === e.id && "bg-sidebar-accent text-sidebar-accent-foreground",
                                ),
                                href: `#operation=${encodeURIComponent(e.id)}`,
                                children: [
                                  (0, d.jsx)("span", {
                                    className:
                                      "w-10 shrink-0 font-mono text-[10px] font-semibold uppercase text-muted-foreground",
                                    children: e.method,
                                  }),
                                  (0, d.jsx)("span", { className: "truncate", children: e.summary ?? e.path }),
                                ],
                              },
                              e.id,
                            ),
                          ),
                        }),
                      ],
                    },
                    e,
                  ),
                ),
              ],
            }),
          }),
        ],
      });
    }
    function uR({ direction: e, document: t, schema: n }) {
      let r = (function e(t, n, r, i = 0, o = "", l = new Set()) {
        if (!n || i > 4 || (n.$ref && l.has(n.$ref))) return [];
        let a = n.$ref ? new Set([...l, n.$ref]) : l,
          s = uh(t, n),
          u = um(
            t,
            Array.isArray(s?.type) ? (s.type.includes("array") ? s.items : s) : s?.type === "array" ? s.items : s,
          ),
          c = new Set(u?.required ?? []);
        return Object.entries(u?.properties ?? {}).flatMap(([n, l]) => {
          let s = uh(t, l);
          if (("request" === r && s?.readOnly) || ("response" === r && s?.writeOnly)) return [];
          let u = `${o}${n}${s?.type === "array" ? "[]" : ""}`;
          return [
            { depth: i, description: s?.description, name: u, required: c.has(n), schema: l },
            ...e(t, l, r, i + 1, `${u}.`, a),
          ];
        });
      })(t, n, e);
      return r.length
        ? (0, d.jsx)("div", {
            className: "divide-y rounded-xl border",
            children: r.map((e) =>
              (0, d.jsxs)(
                "div",
                {
                  className: "grid gap-2 p-4 sm:grid-cols-[minmax(200px,0.4fr)_1fr]",
                  children: [
                    (0, d.jsxs)("div", {
                      className: "min-w-0",
                      style: { paddingLeft: `${16 * e.depth}px` },
                      children: [
                        (0, d.jsxs)("div", {
                          className: "flex flex-wrap items-center gap-2",
                          children: [
                            (0, d.jsx)("code", {
                              className: "break-all font-mono text-sm font-medium",
                              children: e.name,
                            }),
                            e.required ? (0, d.jsx)(ig, { variant: "outline", children: "required" }) : null,
                          ],
                        }),
                        (0, d.jsx)("p", { className: "mt-1 text-xs text-muted-foreground", children: uv(t, e.schema) }),
                      ],
                    }),
                    (0, d.jsx)("p", {
                      className: "text-sm leading-6 text-muted-foreground",
                      children: e.description ?? "No description provided.",
                    }),
                  ],
                },
                e.name,
              ),
            ),
          })
        : null;
    }
    function uP({ document: e, specUrl: t }) {
      let n = uu(e),
        r = new Map(e.tags?.map((e) => [e.name, e.description])),
        i = new Map();
      for (let e of n) i.set(e.tag, (i.get(e.tag) ?? 0) + 1);
      let o = Object.entries(e.components?.securitySchemes ?? {});
      return (0, d.jsx)("main", {
        className: "min-w-0 flex-1 px-5 py-10 lg:px-10",
        id: "main-content",
        children: (0, d.jsxs)("div", {
          className: "mx-auto max-w-5xl space-y-10",
          children: [
            (0, d.jsxs)("section", {
              children: [
                (0, d.jsxs)("div", {
                  className: "mb-4 flex flex-wrap gap-2",
                  children: [
                    (0, d.jsxs)(ig, { variant: "secondary", children: ["OpenAPI ", e.openapi] }),
                    (0, d.jsxs)(ig, { variant: "outline", children: ["API ", e.info.version] }),
                    (0, d.jsxs)(ig, { variant: "outline", children: [n.length, " operations"] }),
                  ],
                }),
                (0, d.jsx)("h1", {
                  className: "text-pretty font-heading text-4xl font-semibold tracking-tight",
                  id: "overview",
                  children: e.info.title,
                }),
                e.info.description
                  ? (0, d.jsx)("div", {
                      className: "mt-5 max-w-3xl text-sm leading-7 text-muted-foreground",
                      children: (0, d.jsx)(nW, { children: e.info.description }),
                    })
                  : null,
                (0, d.jsx)(i_, {
                  className: "mt-6",
                  render: (0, d.jsx)("a", { download: !0, href: t }),
                  variant: "outline",
                  children: "Download OpenAPI contract",
                }),
              ],
            }),
            e.servers?.length
              ? (0, d.jsxs)("section", {
                  className: "space-y-4",
                  children: [
                    (0, d.jsx)("h2", { className: "font-heading text-2xl font-semibold", children: "Servers" }),
                    (0, d.jsx)("div", {
                      className: "divide-y rounded-xl border",
                      children: e.servers.map((e) =>
                        (0, d.jsxs)(
                          "div",
                          {
                            className: "grid gap-2 p-4 sm:grid-cols-[minmax(260px,0.6fr)_1fr]",
                            children: [
                              (0, d.jsx)("code", { className: "break-all font-mono text-sm", children: uf(e) }),
                              (0, d.jsx)("p", {
                                className: "text-sm text-muted-foreground",
                                children: e.description ?? "API server",
                              }),
                            ],
                          },
                          e.url,
                        ),
                      ),
                    }),
                  ],
                })
              : null,
            o.length
              ? (0, d.jsxs)("section", {
                  className: "space-y-4",
                  children: [
                    (0, d.jsx)("h2", { className: "font-heading text-2xl font-semibold", children: "Authentication" }),
                    o.map(([e, t]) =>
                      (0, d.jsx)(
                        iB,
                        {
                          children: (0, d.jsxs)(iH, {
                            children: [
                              (0, d.jsx)(iq, {
                                className: "text-base",
                                children: "http" === t.type ? (t.scheme ?? e) : (t.name ?? e),
                              }),
                              (0, d.jsx)(iU, {
                                className: "[&_a]:text-link [&_a]:underline",
                                children: (0, d.jsx)(nW, { children: t.description ?? "Authentication required." }),
                              }),
                            ],
                          }),
                        },
                        e,
                      ),
                    ),
                  ],
                })
              : null,
            (0, d.jsxs)("section", {
              className: "space-y-4",
              children: [
                (0, d.jsx)("h2", { className: "font-heading text-2xl font-semibold", children: "Resources" }),
                (0, d.jsx)("div", {
                  className: "grid gap-4 sm:grid-cols-2",
                  children: [...i].map(([e, t]) =>
                    (0, d.jsxs)(
                      iB,
                      {
                        children: [
                          (0, d.jsxs)(iH, {
                            children: [
                              (0, d.jsx)(iq, { className: "text-base", children: e }),
                              (0, d.jsx)(iU, {
                                className: "[&_a]:text-link [&_a]:underline",
                                children: (0, d.jsx)(nW, { children: r.get(e) ?? `${t} API operations` }),
                              }),
                            ],
                          }),
                          (0, d.jsxs)(iW, { className: "text-xs text-muted-foreground", children: [t, " operations"] }),
                        ],
                      },
                      e,
                    ),
                  ),
                }),
              ],
            }),
          ],
        }),
      });
    }
    function uT({ apiKey: e, document: t, environment: n, operation: r, python: i }) {
      let o,
        l,
        [a, s] = (0, f.useState)({}),
        [u, c] = (0, f.useState)(() => uk(t, r)),
        [p, h] = (0, f.useState)({}),
        [m, g] = (0, f.useState)(""),
        [v, y] = (0, f.useState)(),
        [b, x] = (0, f.useState)(!1),
        [k, S] = (0, f.useState)(""),
        E = r.parameters ?? [],
        j = E.some((e) => "cookie" === e.in),
        R = uy(r),
        P = um(t, R?.[1].schema),
        T = Object.entries(P?.properties ?? {}).filter(([, e]) => uh(t, e)?.format === "binary"),
        A =
          ((o = Object.entries(r.responses ?? {})),
          (l = o.find(([e]) => /^2\d\d$/.test(e))?.[1] ?? o.find(([e]) => /^2xx$/i.test(e))?.[1])
            ? ub(l.content)
            : void 0),
        O = up(t, r),
        I = (0, f.useMemo)(
          () =>
            (function (e, t, n, r, i, o) {
              let l,
                a = t.server ?? e.servers?.[0],
                s = a ? uf(a) : void 0,
                u = s && i ? new URL(s, `${i}/`).toString() : (s ?? i),
                c = new Map(
                  (t.parameters ?? []).filter((e) => e.required).map((t) => [`${t.in}:${t.name}`, ug(e, t.schema)]),
                ),
                d = t.path;
              for (let e of (t.parameters ?? []).filter((e) => "path" === e.in))
                d = d.replace(`{${e.name}}`, uo(c.get(`path:${e.name}`), e.explode, e.allowReserved));
              let f = (t.parameters ?? [])
                  .filter((e) => "query" === e.in && e.required)
                  .map((e) => ul(e.name, c.get(`query:${e.name}`), e.style, e.explode, e.allowReserved))
                  .join("&"),
                p = `${u.replace(/\/$/, "")}/${d.replace(/^\//, "")}${f ? `?${f}` : ""}`,
                h = uy(t),
                m = up(e, t),
                g = h?.[0] === "application/json" || h?.[0].endsWith("+json"),
                v = um(e, h?.[1].schema),
                y = Object.fromEntries(Object.entries(v?.properties ?? {}).filter(([, t]) => !uh(e, t)?.readOnly)),
                b = h ? ug(e, h[1].schema) : void 0,
                x = {};
              try {
                (b = JSON.parse(n)) && "object" == typeof b && !Array.isArray(b) && (x = b);
              } catch {
                h?.[0].startsWith("text/") && (b = n);
              }
              let k = [
                  `curl --request ${t.method.toUpperCase()}`,
                  `  --url ${uS(p)}`,
                  m ? `  --header ${uS(`${m.header}: ${m.prefix}`)}"$${r}"` : "",
                  ...(t.parameters ?? [])
                    .filter((e) => "header" === e.in && e.required)
                    .map((e) => `  --header ${uS(`${e.name}: ${uo(c.get(`header:${e.name}`), e.explode)}`)}`),
                  ...(t.parameters ?? [])
                    .filter((e) => "cookie" === e.in && e.required)
                    .map(
                      (e) =>
                        `  --cookie ${uS(ul(e.name, c.get(`cookie:${e.name}`), "form", e.explode).replaceAll("&", "; "))}`,
                    ),
                  h && "multipart/form-data" !== h[0] ? `  --header ${uS(`Content-Type: ${h[0]}`)}` : "",
                  g ? `  --data ${uS(n)}` : "",
                  h?.[0] === "application/x-www-form-urlencoded"
                    ? uC(x)
                        .map(([e, t]) => `  --data-urlencode ${uS(`${e}=${t}`)}`)
                        .join(" \\\n")
                    : "",
                  h && !g && !["application/x-www-form-urlencoded", "multipart/form-data"].includes(h[0])
                    ? `  --data ${uS(n)}`
                    : "",
                  h?.[0] === "multipart/form-data"
                    ? Object.entries(y)
                        .map(
                          ([t, n]) =>
                            `  --form ${uS(`${t}=${uh(e, n)?.format === "binary" ? "@path/to/file" : (x[t] ?? "value")}`)}`,
                        )
                        .join(" \\\n")
                    : "",
                ]
                  .filter(Boolean)
                  .join(" \\\n"),
                w = [
                  ...(t.parameters ?? [])
                    .filter((e) => e.required)
                    .map((t) => ({ location: t.in, name: t.name, value: ug(e, t.schema) })),
                  ...(v?.required ?? [])
                    .filter((e) => y[e])
                    .map((t) => ({ location: "body", name: t, value: x[t] ?? ug(e, y[t]) })),
                  ...(!v?.properties && h?.[1].schema && t.requestBody?.required
                    ? [{ location: "body", name: "body", value: b }]
                    : []),
                ],
                S =
                  ((l = new Set(["self"])),
                  w.map(({ location: e, name: t }) => {
                    let n = ui(t),
                      r = n;
                    l.has(r) && (r = `${n}_${e}`);
                    for (let e = 2; l.has(r); e += 1) r = `${n}_${e}`;
                    return (l.add(r), r);
                  })),
                C = w.map(
                  (e, t) =>
                    `${S[t]}=${(function e(t) {
                      return null === t
                        ? "None"
                        : !0 === t
                          ? "True"
                          : !1 === t
                            ? "False"
                            : Array.isArray(t)
                              ? `[${t.map(e).join(", ")}]`
                              : "object" == typeof t
                                ? `{${Object.entries(t)
                                    .map(([t, n]) => `${JSON.stringify(t)}: ${e(n)}`)
                                    .join(", ")}}`
                                : JSON.stringify(t);
                    })(e.value)}`,
                );
              return {
                curl: k,
                python: [
                  `from ${o.package} import ${o.client}`,
                  "",
                  `client = ${o.client}()  # ${r}`,
                  C.length
                    ? `response = client.${t.resource}.${t.sdkMethod}(
${C.map((e) => `    ${e},`).join("\n")}
)`
                    : `response = client.${t.resource}.${t.sdkMethod}()`,
                  "print(response)",
                ].join("\n"),
              };
            })(t, r, u, n, k, i),
          [u, t, n, r, k, i],
        );
      async function M() {
        let n,
          i = E.find((e) => e.required && !a[`${e.in}:${e.name}`]);
        if (i) return void g(`Enter ${i.name} before sending the request.`);
        let o = r.path;
        try {
          for (let e of E.filter((e) => "path" === e.in)) {
            let n = uw(t, e, a[`path:${e.name}`] ?? "");
            o = o.replace(`{${e.name}}`, uo(n, e.explode, e.allowReserved));
          }
        } catch (e) {
          g(e instanceof Error ? e.message : "Invalid path parameter");
          return;
        }
        let l = (function (e, t = "http://localhost:3000", n) {
            let r = n?.server ?? e.servers?.[0];
            return new URL(r ? uf(r) : t, t).toString().replace(/\/$/, "");
          })(t, window.location.origin, r),
          s = `${l.replace(/\/$/, "")}/${o.replace(/^\//, "")}`;
        try {
          let e = E.filter((e) => "query" === e.in && a[`query:${e.name}`])
            .map((e) => ul(e.name, uw(t, e, a[`query:${e.name}`] ?? ""), e.style, e.explode, e.allowReserved))
            .join("&");
          e && (s += `?${e}`);
        } catch (e) {
          g(e instanceof Error ? e.message : "Invalid query parameter");
          return;
        }
        let c = new URL(s, window.location.origin),
          d = A ? { Accept: A[0] } : {};
        (e && O && (d[O.header] = `${O.prefix}${e}`),
          R && "multipart/form-data" !== R[0] && (d["Content-Type"] = R[0]));
        try {
          for (let e of E.filter((e) => "header" === e.in)) {
            let n = a[`header:${e.name}`];
            n && (d[e.name] = uo(uw(t, e, n), e.explode));
          }
        } catch (e) {
          g(e instanceof Error ? e.message : "Invalid header parameter");
          return;
        }
        if (
          ((R?.[0] === "application/json" || R?.[0].endsWith("+json")) && (n = u),
          R?.[0] === "application/x-www-form-urlencoded")
        )
          try {
            let e = new URLSearchParams();
            for (let [t, n] of uC(JSON.parse(u))) e.append(t, String(n));
            n = e;
          } catch {
            g("Enter valid JSON request values before sending the request.");
            return;
          }
        if (R?.[0] === "multipart/form-data") {
          let e = new FormData(),
            r = {};
          try {
            r = JSON.parse(u);
          } catch {
            g("Enter valid JSON request values before sending the request.");
            return;
          }
          for (let [n, i] of Object.entries(r))
            uh(t, P?.properties?.[n])?.format !== "binary" &&
              null != i &&
              e.append(n, "string" == typeof i ? i : JSON.stringify(i));
          for (let [t, n] of Object.entries(p)) e.append(t, n);
          let i = T.find(([e]) => P?.required?.includes(e) && !p[e]);
          if (i) return void g(`Choose ${i[0]} before sending the request.`);
          n = e;
        }
        (R &&
          !["application/json", "application/x-www-form-urlencoded", "multipart/form-data"].includes(R[0]) &&
          (n = u),
          x(!0),
          g(""),
          y(void 0));
        try {
          let e = await fetch(c, { body: n, headers: d, method: r.method.toUpperCase() }),
            t = await e.text();
          y(e.status);
          try {
            g(JSON.stringify(JSON.parse(t), null, 2));
          } catch {
            g(t || e.statusText);
          }
        } catch (e) {
          g(e instanceof Error ? e.message : "Request failed");
        } finally {
          x(!1);
        }
      }
      return (
        (0, f.useEffect)(() => S(window.location.origin), []),
        (0, f.useEffect)(() => {
          (s({}), c(uk(t, r)), h({}), g(""), y(void 0));
        }, [t, r]),
        (0, d.jsx)("main", {
          className: "min-w-0 flex-1 px-5 py-8 lg:px-10",
          id: "main-content",
          children: (0, d.jsxs)("div", {
            className: "mx-auto grid max-w-6xl gap-8 xl:grid-cols-[minmax(0,1fr)_minmax(340px,0.8fr)]",
            children: [
              (0, d.jsxs)("div", {
                className: "min-w-0 space-y-8",
                children: [
                  (0, d.jsxs)("section", {
                    children: [
                      (0, d.jsxs)("div", {
                        className: "mb-4 flex flex-wrap items-center gap-2",
                        children: [
                          (0, d.jsx)(ig, { variant: ux[r.method], children: r.method.toUpperCase() }),
                          (0, d.jsx)("code", { className: "break-all font-mono text-sm", children: r.path }),
                        ],
                      }),
                      (0, d.jsx)("h1", {
                        className: "font-heading text-3xl font-semibold tracking-tight",
                        children: r.summary ?? r.id,
                      }),
                      r.description
                        ? (0, d.jsx)("div", {
                            className: "mt-4 text-sm leading-7 text-muted-foreground [&_a]:text-link [&_a]:underline",
                            children: (0, d.jsx)(nW, { children: r.description }),
                          })
                        : null,
                    ],
                  }),
                  E.length
                    ? (0, d.jsxs)("section", {
                        className: "space-y-4",
                        children: [
                          (0, d.jsxs)("div", {
                            children: [
                              (0, d.jsx)("h2", {
                                className: "font-heading text-xl font-semibold",
                                children: "Parameters",
                              }),
                              (0, d.jsx)("p", {
                                className: "text-sm text-muted-foreground",
                                children: "Path, query, and header values for this request.",
                              }),
                            ],
                          }),
                          (0, d.jsx)("div", {
                            className: "divide-y rounded-xl border",
                            children: E.map((e) =>
                              (0, d.jsxs)(
                                "div",
                                {
                                  className: "grid gap-3 p-4 sm:grid-cols-[minmax(150px,0.35fr)_1fr]",
                                  children: [
                                    (0, d.jsxs)("div", {
                                      children: [
                                        (0, d.jsxs)("div", {
                                          className: "flex items-center gap-2",
                                          children: [
                                            (0, d.jsx)("code", {
                                              className: "font-mono text-sm font-medium",
                                              children: e.name,
                                            }),
                                            e.required
                                              ? (0, d.jsx)(ig, { variant: "outline", children: "required" })
                                              : null,
                                          ],
                                        }),
                                        (0, d.jsxs)("p", {
                                          className: "mt-1 text-xs text-muted-foreground",
                                          children: [e.in, " · ", uv(t, e.schema)],
                                        }),
                                      ],
                                    }),
                                    (0, d.jsxs)("div", {
                                      children: [
                                        (0, d.jsx)(oN, {
                                          "aria-label": e.name,
                                          autoComplete: "off",
                                          name: `${e.in}-${e.name}`,
                                          onChange: (t) => {
                                            var n, r, i;
                                            return (
                                              (n = e.in),
                                              (r = e.name),
                                              (i = t.target.value),
                                              void s((e) => ({ ...e, [`${n}:${r}`]: i }))
                                            );
                                          },
                                          placeholder: e.description ?? e.name,
                                          required: e.required,
                                          value: a[`${e.in}:${e.name}`] ?? "",
                                        }),
                                        e.description
                                          ? (0, d.jsx)("p", {
                                              className: "mt-2 text-xs text-muted-foreground",
                                              children: e.description,
                                            })
                                          : null,
                                      ],
                                    }),
                                  ],
                                },
                                `${e.in}:${e.name}`,
                              ),
                            ),
                          }),
                        ],
                      })
                    : null,
                  R
                    ? (0, d.jsxs)("section", {
                        className: "space-y-4",
                        children: [
                          (0, d.jsxs)("div", {
                            children: [
                              (0, d.jsx)("h2", {
                                className: "font-heading text-xl font-semibold",
                                children: "Request body",
                              }),
                              (0, d.jsxs)("p", {
                                className: "text-sm text-muted-foreground",
                                children: [R[0], " · ", uv(t, R[1].schema)],
                              }),
                            ],
                          }),
                          (0, d.jsx)(ut, {
                            "aria-label": "Request body",
                            autoComplete: "off",
                            className: "min-h-64 font-mono text-xs leading-relaxed",
                            name: "request-body",
                            onChange: (e) => c(e.target.value),
                            spellCheck: !1,
                            value: u,
                          }),
                          (0, d.jsx)(uR, { direction: "request", document: t, schema: R[1].schema }),
                          T.map(([e]) =>
                            (0, d.jsx)(
                              oN,
                              {
                                "aria-label": e,
                                name: e,
                                onChange: (t) => {
                                  let n = t.target.files?.[0];
                                  n && h((t) => ({ ...t, [e]: n }));
                                },
                                required: P?.required?.includes(e),
                                type: "file",
                              },
                              e,
                            ),
                          ),
                        ],
                      })
                    : null,
                  (0, d.jsxs)("section", {
                    className: "space-y-4",
                    children: [
                      (0, d.jsxs)("div", {
                        children: [
                          (0, d.jsx)("h2", { className: "font-heading text-xl font-semibold", children: "Response" }),
                          (0, d.jsx)("p", {
                            className: "text-sm text-muted-foreground",
                            children: A ? `${A[0]} \xb7 ${uv(t, A[1].schema)}` : "See documented status codes below.",
                          }),
                        ],
                      }),
                      (0, d.jsx)("div", {
                        className: "divide-y rounded-xl border",
                        children: Object.entries(r.responses ?? {}).map(([e, t]) =>
                          (0, d.jsxs)(
                            "div",
                            {
                              className: "grid grid-cols-[72px_1fr] gap-3 p-4 text-sm",
                              children: [
                                (0, d.jsx)("code", { className: "font-mono font-medium", children: e }),
                                (0, d.jsx)("span", { className: "text-muted-foreground", children: t.description }),
                              ],
                            },
                            e,
                          ),
                        ),
                      }),
                      A?.[1].schema
                        ? (0, d.jsx)(uR, { direction: "response", document: t, schema: A[1].schema })
                        : null,
                      A ? (0, d.jsx)(uE, { code: JSON.stringify(A[1].example ?? ug(t, A[1].schema), null, 2) }) : null,
                    ],
                  }),
                ],
              }),
              (0, d.jsx)("aside", {
                className: "min-w-0 xl:sticky xl:top-24 xl:h-fit",
                children: (0, d.jsxs)(iB, {
                  children: [
                    (0, d.jsxs)(iH, {
                      children: [
                        (0, d.jsx)(iq, { children: "Try it" }),
                        (0, d.jsx)(iU, {
                          children: j
                            ? "Browser requests cannot set cookie parameters. Use the Python or cURL example."
                            : "Your API key is kept only in this page and is never added to code examples.",
                        }),
                      ],
                    }),
                    (0, d.jsxs)(iW, {
                      className: "space-y-5",
                      children: [
                        (0, d.jsxs)(i_, {
                          className: "w-full",
                          disabled: b || j,
                          onClick: M,
                          children: [
                            b
                              ? (0, d.jsx)(w, { "aria-hidden": "true", className: "animate-spin" })
                              : (0, d.jsx)(C, { "aria-hidden": "true" }),
                            "Send request",
                          ],
                        }),
                        (0, d.jsxs)(s6, {
                          defaultValue: "python",
                          children: [
                            (0, d.jsxs)(s7, {
                              children: [
                                (0, d.jsx)(s8, { value: "python", children: "Python" }),
                                (0, d.jsx)(s8, { value: "curl", children: "cURL" }),
                              ],
                            }),
                            (0, d.jsx)(ue, { value: "python", children: (0, d.jsx)(uE, { code: I.python }) }),
                            (0, d.jsx)(ue, { value: "curl", children: (0, d.jsx)(uE, { code: I.curl }) }),
                          ],
                        }),
                        m
                          ? (0, d.jsxs)("div", {
                              "aria-live": "polite",
                              className: "space-y-2",
                              children: [
                                (0, d.jsxs)("div", {
                                  className: "flex items-center justify-between text-xs font-medium",
                                  children: [
                                    (0, d.jsx)("span", { children: "Response" }),
                                    v
                                      ? (0, d.jsx)(ig, { variant: v < 400 ? "secondary" : "destructive", children: v })
                                      : null,
                                  ],
                                }),
                                (0, d.jsx)(uE, { code: m }),
                              ],
                            })
                          : null,
                      ],
                    }),
                  ],
                }),
              }),
            ],
          }),
        })
      );
    }
    e.s(
      [
        "ApiReference",
        0,
        function ({ apiKeyEnvironment: e, python: t, specUrl: n }) {
          let [r, i] = (0, f.useState)(""),
            [o, l] = (0, f.useState)(),
            [a, s] = (0, f.useState)(""),
            [u, c] = (0, f.useState)(!1),
            [p, h] = (0, f.useState)(""),
            [m, g] = (0, f.useState)(),
            v = (0, f.useDeferredValue)(p),
            y = (0, f.useMemo)(() => (o ? uu(o) : []), [o]),
            b = (0, f.useMemo)(() => {
              let e = v.trim().toLowerCase();
              return e
                ? y.filter((t) => `${t.method} ${t.path} ${t.summary ?? ""} ${t.tag}`.toLowerCase().includes(e))
                : y;
            }, [v, y]),
            x = y.find((e) => e.id === m),
            C = (0, f.useMemo)(() => {
              let e = new Map();
              for (let t of b) e.set(t.tag, [...(e.get(t.tag) ?? []), t]);
              return e;
            }, [b]);
          if (
            ((0, f.useEffect)(() => {
              fetch(n)
                .then((e) => {
                  if (!e.ok) throw Error(`Failed to load ${n}: ${e.status}`);
                  return e.json();
                })
                .then((e) => l(e))
                .catch((e) => s(e instanceof Error ? e.message : "Failed to load OpenAPI document"));
            }, [n]),
            (0, f.useEffect)(() => {
              function e() {
                let e = window.location.hash.slice(1);
                (g(e.startsWith("operation=") ? decodeURIComponent(e.slice(10)) : void 0),
                  c(!1),
                  window.scrollTo(0, 0));
              }
              return (e(), window.addEventListener("hashchange", e), () => window.removeEventListener("hashchange", e));
            }, []),
            a)
          )
            return (0, d.jsx)("div", { className: "p-8 text-sm text-destructive", children: a });
          if (!o)
            return (0, d.jsxs)("div", {
              "aria-live": "polite",
              className: "flex min-h-screen items-center justify-center text-sm text-muted-foreground",
              children: [
                (0, d.jsx)(w, { "aria-hidden": "true", className: "mr-2 size-4 animate-spin" }),
                " Loading API reference…",
              ],
            });
          let E = y.some((e) => up(o, e));
          return (0, d.jsxs)("div", {
            className: "min-h-screen bg-background",
            children: [
              (0, d.jsx)("header", {
                className: "sticky top-0 z-30 border-b bg-background/95 backdrop-blur",
                children: (0, d.jsxs)("div", {
                  className: "flex h-16 items-center gap-4 px-4 lg:px-6",
                  children: [
                    (0, d.jsxs)(sS, {
                      onOpenChange: c,
                      open: u,
                      children: [
                        (0, d.jsx)(sC, {
                          render: (0, d.jsx)(i_, {
                            "aria-label": "Open API navigation",
                            className: "lg:hidden",
                            size: "icon-sm",
                            variant: "ghost",
                          }),
                          children: (0, d.jsx)(S, { "aria-hidden": "true" }),
                        }),
                        (0, d.jsxs)(sR, {
                          className: "gap-0 p-0",
                          side: "left",
                          children: [
                            (0, d.jsx)(sP, { children: (0, d.jsx)(sT, { children: "API reference" }) }),
                            (0, d.jsx)(lj, {}),
                            (0, d.jsx)(uj, { onQueryChange: h, query: p, selectedId: m, tags: C }),
                          ],
                        }),
                      ],
                    }),
                    (0, d.jsxs)("a", {
                      className:
                        "flex min-w-0 items-center gap-3 rounded-md focus-visible:ring-2 focus-visible:ring-ring",
                      href: "#overview",
                      children: [
                        (0, d.jsx)("div", {
                          className:
                            "size-7 rounded-lg bg-linear-to-br from-(--ultralytics-logo-gradient-start) to-(--ultralytics-logo-gradient-end)",
                        }),
                        (0, d.jsxs)("div", {
                          className: "min-w-0",
                          children: [
                            (0, d.jsx)("p", {
                              className: "truncate font-heading text-sm font-semibold",
                              children: o.info.title,
                            }),
                            (0, d.jsxs)("p", {
                              className: "text-xs text-muted-foreground",
                              children: ["API ", o.info.version],
                            }),
                          ],
                        }),
                      ],
                    }),
                    E
                      ? (0, d.jsxs)("div", {
                          className: "ml-auto flex w-full max-w-sm items-center gap-2",
                          children: [
                            (0, d.jsx)(k, {
                              "aria-hidden": "true",
                              className: "size-4 shrink-0 text-muted-foreground",
                            }),
                            (0, d.jsx)(oN, {
                              "aria-label": "API key",
                              autoComplete: "off",
                              name: "api-key",
                              onChange: (e) => i(e.target.value),
                              placeholder: e,
                              type: "password",
                              value: r,
                            }),
                          ],
                        })
                      : null,
                  ],
                }),
              }),
              (0, d.jsxs)("div", {
                className: "flex min-h-[calc(100vh-4rem)]",
                children: [
                  (0, d.jsx)("aside", {
                    className: "sticky top-16 hidden h-[calc(100vh-4rem)] w-80 shrink-0 border-r bg-sidebar lg:block",
                    children: (0, d.jsx)(uj, { onQueryChange: h, query: p, selectedId: m, tags: C }),
                  }),
                  x
                    ? (0, d.jsx)(uT, { apiKey: r, document: o, environment: e, operation: x, python: t })
                    : (0, d.jsx)(uP, { document: o, specUrl: n }),
                ],
              }),
            ],
          });
        },
      ],
      50341,
    );
  },
]);
