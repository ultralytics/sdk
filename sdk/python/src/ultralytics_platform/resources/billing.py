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
    BillingRetrieveBalanceResponse,
)


class Billing:
    """Billing API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve_balance(self, *, owner: str | None = None) -> BillingRetrieveBalanceResponse:
        """Check your credit balance.

        Args:
            owner (str, optional): Team username (to check team balance instead of personal)

        Returns:
            (BillingRetrieveBalanceResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingRetrieveBalanceResponse,
            self._client.request(
                "GET",
                "/api/billing/balance",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def list_transactions(self, *, owner: str | None = None) -> BillingListTransactionsResponse:
        """View transaction history.

        Returns credit purchases, training charges, and other billing transactions.

        Args:
            owner (str, optional): Team username

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
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def list_usage_summary(self, *, owner: str | None = None) -> BillingListUsageSummaryResponse:
        """View plan and usage.

        Returns plan status, storage usage, training credit, feature access, seats, and billing totals.

        Args:
            owner (str, optional): Team username

        Returns:
            (BillingListUsageSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingListUsageSummaryResponse,
            self._client.request(
                "GET",
                "/api/billing/usage-summary",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )


class AsyncBilling:
    """Asynchronous Billing API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve_balance(self, *, owner: str | None = None) -> BillingRetrieveBalanceResponse:
        """Check your credit balance.

        Args:
            owner (str, optional): Team username (to check team balance instead of personal)

        Returns:
            (BillingRetrieveBalanceResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingRetrieveBalanceResponse,
            await self._client.request(
                "GET",
                "/api/billing/balance",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def list_transactions(self, *, owner: str | None = None) -> BillingListTransactionsResponse:
        """View transaction history.

        Returns credit purchases, training charges, and other billing transactions.

        Args:
            owner (str, optional): Team username

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
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def list_usage_summary(self, *, owner: str | None = None) -> BillingListUsageSummaryResponse:
        """View plan and usage.

        Returns plan status, storage usage, training credit, feature access, seats, and billing totals.

        Args:
            owner (str, optional): Team username

        Returns:
            (BillingListUsageSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            BillingListUsageSummaryResponse,
            await self._client.request(
                "GET",
                "/api/billing/usage-summary",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )
