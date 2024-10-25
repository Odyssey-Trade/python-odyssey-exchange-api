from odyssey_exchange_api.enums import WebsocketEventType
from odyssey_exchange_api.requests.base import WebsocketRequest


class WebsocketFullDepthRequest(WebsocketRequest):
    event: WebsocketEventType
    symbol: str

    def build_request_data(self) -> dict:
        data = {
            "event": self.event,
            "params": {
                "channel": f"market_{self.symbol}_depth_step0",
            }
        }
        return data
