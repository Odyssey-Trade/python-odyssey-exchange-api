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

### Ping

This interface checks connectivity to the host.

```python
from odyssey_exchange_api.requests import SpotPingRequest

response = client.make_request(SpotPingRequest())
print(response)
```

### Check server time

This interface checks connectivity to the server and retrieves server timestamp.

```python
from odyssey_exchange_api.requests import SpotServerTimeRequest

response = client.make_request(SpotServerTimeRequest())
print(response)
```

### Symbol pair list

The supported symbol pair collection which in the exchange.

```python
from odyssey_exchange_api.requests import SpotPairListRequest

response = client.make_request(SpotPairListRequest())
print(response)
```

### Depth

Market depth data.

```python
from odyssey_exchange_api.requests import SpotDepthRequest

response = client.make_request(SpotDepthRequest(
    symbol="BTCUSDT",
    limit=10
))
print(response)
```

### 24hrs ticker

24-hour price change data

```python
from odyssey_exchange_api.requests import SpotTickerDataRequest

response = client.make_request(SpotTickerDataRequest(
    symbol="BTCUSDT"
))
print(response)
```

### Recent Trades List

Fetch recent trades for the specified asset.

```python
from odyssey_exchange_api.requests import SpotRecentTradesRequest

response = client.make_request(SpotRecentTradesRequest(
    symbol="BTCUSDT",
    limit=10
))
print(response)
```

### Kline/candlestick data

Retrieve Kline/candlestick data.

```python
from odyssey_exchange_api.requests import SpotKlineDataRequest

response = client.make_request(SpotKlineDataRequest(
    symbol="BTCUSDT",
    limit=10
))
print(response)
```

## Signed methods

To use signed methods, you need API Key and API Secret, you must specify them in the client.

```python
from odyssey_exchange_api import SyncOdysseyExchangeAPI

client = SyncOdysseyExchangeAPI(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_API_SECRET"
)
```

### Create new order

Create a new order.

```python
from odyssey_exchange_api.requests import SpotCreateOrderRequest
from odyssey_exchange_api.enums import SpotOrderSide, SpotOrderType

response = client.make_request(SpotCreateOrderRequest(
    symbol="BTCUSDT",
    volume=Decimal("0.01"),
    side=SpotOrderSide.BUY,
    type=SpotOrderType.LIMIT,
    price=Decimal("56000")
))
print(response)
```

### Test New Order

Create a new test order.

```python
from odyssey_exchange_api.requests import SpotTestCreateOrderRequest
from odyssey_exchange_api.enums import SpotOrderSide, SpotOrderType

response = client.make_request(SpotTestCreateOrderRequest(
    symbol="BTCUSDT",
    volume=Decimal("0.01"),
    side=SpotOrderSide.BUY,
    type=SpotOrderType.LIMIT,
    price=Decimal("56000")
))
print(response)
```

### Batch Orders

Place batch orders.

```python
from odyssey_exchange_api.requests import SpotBatchOrdersRequest
from odyssey_exchange_api.enums import SpotOrderSide, SpotOrderType
from odyssey_exchange_api.objects import SpotSingleBatchOrder

response = client.make_request(SpotBatchOrdersRequest(
    symbol="BTCUSDT",
    orders=[
        SpotSingleBatchOrder(
            volume=Decimal("0.01"),
            price=Decimal("56000"),
            side=SpotOrderSide.BUY,
            batch_type=SpotOrderType.LIMIT
        )
    ]
))
print(response)
```

### Query Order

Get the order data.

```python
from odyssey_exchange_api.requests import SpotQueryOrderRequest

response = client.make_request(SpotQueryOrderRequest(
    order_id="2282856894002934568",
    symbol="BTCUSDT"
))
print(response)
```

### Cancel Order

Cancel an order.

```python
from odyssey_exchange_api.requests import SpotCancelOrderRequest

response = client.make_request(SpotCancelOrderRequest(
    order_id="2282856894002934568",
    symbol="BTCUSDT"
))
print(response)
```

### Batch Cancel Order

Mass cancellation of orders, maximum 10 orders at a time.

```python
from odyssey_exchange_api.requests import SpotBatchCancelOrderRequest

response = client.make_request(SpotBatchCancelOrderRequest(
    order_ids=[
        2282856894002934568,
        2282856842463329886
    ],
    symbol="BTCUSDT"
))
print(response)
```

### Current Open Orders

Get a list of open orders.

```python
from odyssey_exchange_api.requests import SpotOpenOrdersRequest

response = client.make_request(SpotOpenOrdersRequest(
    symbol="BTCUSDT",
    limit=10
))
print(response)
```

### Trading records

Get a list of your own trades.

```python
from odyssey_exchange_api.requests import SpotMyTradesRequest

response = client.make_request(SpotMyTradesRequest(
    symbol="BTCUSDT",
    limit=10
))
print(response)
```

### Account Information

Get account information.

```python
from odyssey_exchange_api.requests import SpotAccountInfoRequest

response = client.make_request(SpotAccountInfoRequest())
print(response)
```

