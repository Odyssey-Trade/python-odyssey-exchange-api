from pydantic import Field

from odyssey_exchange_api.base import BASE_FUTURES_URL
from odyssey_exchange_api.objects import FuturesMyTrade
from odyssey_exchange_api.requests.base import SignedRequest


class FuturesMyTradesRequest(SignedRequest[list[FuturesMyTrade]]):
    """
    Receives data on the transactions records. Returns an array of :class:`odyssey_exchange_api.objects.FuturesMyTrade`.

    Source: https://exchangeopenapi.gitbook.io/pri-openapi/openapi-doc/futures-trading-api#transaction-record
    """

    _request_url = BASE_FUTURES_URL
    _request_method = "GET"
    _request_path = "/fapi/v1/myTrades"

    __returning__ = list[FuturesMyTrade]

    contract_name: str = Field(serialization_alias="contractName")
    """The uppercase contract name, e.g., E-BTC-USDT."""
    limit: int = 100
    """The maximum number of items that can be returned in the query result. The value must be a positive integer. The default value is 100, maximum value is 1000."""
    from_id: int | None = Field(serialization_alias="fromId", default=None)
    """Start searching from this record"""