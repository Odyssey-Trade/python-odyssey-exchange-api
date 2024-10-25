from pydantic import Field

from odyssey_exchange_api.base import BASE_FUTURES_URL
from odyssey_exchange_api.enums import FuturesPositionType
from odyssey_exchange_api.requests.base import SignedRequest, ResponseType


class FuturesChangeMarginModelRequest(SignedRequest[bool]):
    """
    Change margin model. Returns a :class:`bool`.

    Source: https://exchangeopenapi.gitbook.io/pri-openapi/openapi-doc/futures-trading-api#change-margin-mode
    """

    _request_url = BASE_FUTURES_URL
    _request_method = "POST"
    _request_path = "/fapi/v1/edit_user_margin_model"

    __returning__ = bool

    contract_name: str = Field(serialization_alias="contractName")
    """The uppercase contract name, e.g., E-BTC-USDT."""
    margin_model: FuturesPositionType = Field(serialization_alias="marginModel")
    """The model of margin."""

    def make_response(self, data) -> ResponseType:
        if data.get("code") == "0" and data.get("msg") == "成功":
            return True
        return False