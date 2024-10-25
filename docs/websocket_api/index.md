# Methods

## Public methods

To use public methods, you do not need API Key and API Secret, you can specify an empty string in their place.

```python
from odyssey_exchange_api import SyncOdysseyExchangeAPI

client = SyncOdysseyExchangeAPI(
    api_key="",
    secret_key=""
)
```

### Pong

Responds to the ping request.

```python
from odyssey_exchange_api.requests import WebsocketPongRequest

req = WebsocketPongRequest(pong=int(time.time() * 1000))
client.make_websocket_request(req)
```

### Subscription Full Depth

```python
from odyssey_exchange_api.requests import WebsocketFullDepthRequest

req = WebsocketFullDepthRequest(event="sub", symbol="btcusdt")
client.make_websocket_request(req)
```

### Subscription Real Time Trade

```python
from odyssey_exchange_api.requests import WebsocketRealTimeTradeRequest

req = WebsocketRealTimeTradeRequest(event="sub", symbol="btcusdt")
client.make_websocket_request(req)
```

### Subscription Kline Market

```python
from odyssey_exchange_api.requests import WebsocketKlineHistoryRequest

req = WebsocketKlineHistoryRequest(symbol="btcusdt", interval="60min")
client.make_websocket_request(req)
```

### Subscription Market Tickers

```python
from odyssey_exchange_api.requests import WebsocketMarketTickerRequest

req = WebsocketMarketTickerRequest(event="sub", symbol="btcusdt")
client.make_websocket_request(req)
```

### Request Kline History Data

```python
from odyssey_exchange_api.requests import WebsocketKlineHistoryRequest

req = WebsocketKlineHistoryRequest(symbol="btcusdt", interval="60min")
client.make_websocket_request(req)
```

### Request Trade History

```python
from odyssey_exchange_api.requests import WebsocketHistoryTradeRequest

req = WebsocketHistoryTradeRequest(symbol="btcusdt")
client.make_websocket_request(req)
```

