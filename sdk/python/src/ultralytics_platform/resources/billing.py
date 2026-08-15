# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import cast

import httpx

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    BillingTransactionsResponse,
    BillingUsageSummaryResponse,
)


class Billing:
    """Billing API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def transactions(
        self,
        *,
        from_: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> BillingTransactionsResponse:
        """View transaction history.

        Returns credit purchases, training charges, and other billing transactions.

        Args:
            from_ (str, optional): Earliest transaction timestamp
            to (str, optional): Latest transaction timestamp
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (BillingTransactionsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingTransactionsResponse,
            self._client.request(
                "GET",
                "/api/billing/transactions",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("from", from_, style="form", explode=True),
                    *_query_parameter("to", to, style="form", explode=True),
                ],
            ),
        )

    def usage_summary(
        self, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> BillingUsageSummaryResponse:
        """View plan and usage.

        Returns plan status, storage usage, training credit, feature access, seats, and billing totals.

        Args:
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (BillingUsageSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingUsageSummaryResponse,
            self._client.request(
                "GET",
                "/api/billing/usage-summary",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )


class AsyncBilling:
    """Asynchronous Billing API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def transactions(
        self,
        *,
        from_: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> BillingTransactionsResponse:
        """View transaction history.

        Returns credit purchases, training charges, and other billing transactions.

        Args:
            from_ (str, optional): Earliest transaction timestamp
            to (str, optional): Latest transaction timestamp
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (BillingTransactionsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingTransactionsResponse,
            await self._client.request(
                "GET",
                "/api/billing/transactions",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("from", from_, style="form", explode=True),
                    *_query_parameter("to", to, style="form", explode=True),
                ],
            ),
        )

    async def usage_summary(
        self, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> BillingUsageSummaryResponse:
        """View plan and usage.

        Returns plan status, storage usage, training credit, feature access, seats, and billing totals.

        Args:
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (BillingUsageSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingUsageSummaryResponse,
            await self._client.request(
                "GET",
                "/api/billing/usage-summary",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )
