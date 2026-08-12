# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import cast

from .._client import (
    AsyncAPIClient,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    BillingListTransactionsResponse,
    BillingListUsageSummaryResponse,
)


class Billing:
    """Billing API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list_transactions(self, *, from_: str | None = None, to: str | None = None) -> BillingListTransactionsResponse:
        """View transaction history.

        Returns credit purchases, training charges, and other billing transactions.

        Args:
            from_ (str, optional): Earliest transaction timestamp
            to (str, optional): Latest transaction timestamp

        Returns:
            (BillingListTransactionsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingListTransactionsResponse,
            self._client.request(
                "GET",
                "/api/billing/transactions",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("from", from_, style="form", explode=True),
                    *_query_parameter("to", to, style="form", explode=True),
                ],
            ),
        )

    def list_usage_summary(self) -> BillingListUsageSummaryResponse:
        """View plan and usage.

        Returns plan status, storage usage, training credit, feature access, seats, and billing totals.

        Returns:
            (BillingListUsageSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingListUsageSummaryResponse,
            self._client.request("GET", "/api/billing/usage-summary", auth=("Authorization", "Bearer ")),
        )


class AsyncBilling:
    """Asynchronous Billing API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list_transactions(
        self, *, from_: str | None = None, to: str | None = None
    ) -> BillingListTransactionsResponse:
        """View transaction history.

        Returns credit purchases, training charges, and other billing transactions.

        Args:
            from_ (str, optional): Earliest transaction timestamp
            to (str, optional): Latest transaction timestamp

        Returns:
            (BillingListTransactionsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingListTransactionsResponse,
            await self._client.request(
                "GET",
                "/api/billing/transactions",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("from", from_, style="form", explode=True),
                    *_query_parameter("to", to, style="form", explode=True),
                ],
            ),
        )

    async def list_usage_summary(self) -> BillingListUsageSummaryResponse:
        """View plan and usage.

        Returns plan status, storage usage, training credit, feature access, seats, and billing totals.

        Returns:
            (BillingListUsageSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingListUsageSummaryResponse,
            await self._client.request("GET", "/api/billing/usage-summary", auth=("Authorization", "Bearer ")),
        )
