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
from odyssey_exchange_api.requests import FuturesPingRequest

response = client.make_request(FuturesPingRequest())
print(response)
```

### Check server time

This interface checks connectivity to the server and retrieves server timestamp.

```python
from odyssey_exchange_api.requests import FuturesServerTimeRequest

response = client.make_request(FuturesServerTimeRequest())
print(response)
```

### Futures contracts list

Get a list of all contracts on the exchange.

```python
from odyssey_exchange_api.requests import FuturesContractsListRequest

response = client.make_request(FuturesContractsListRequest())
print(response)
```

### Depth

Market depth data.

```python
from odyssey_exchange_api.requests import FuturesDepthRequest

response = client.make_request(FuturesDepthRequest(
    symbol="E-BTC-USDT",
    limit=10
))
print(response)
```

### 24hrs ticker

24-hour price change data

```python
from odyssey_exchange_api.requests import FuturesTickerDataRequest

response = client.make_request(FuturesTickerDataRequest(
    contract_name="E-BTC-USDT"
))
print(response)
```

### Obtain index and tag price

Getting index and tag prices and additional funding data.

```python
from odyssey_exchange_api.requests import FuturesIndexTagPriceRequest

response = client.make_request(FuturesIndexTagPriceRequest(
    contract_name="E-BTC-USDT"
))
print(response)
```

### Kline/candlestick data

Retrieve Kline/candlestick data.

```python
from odyssey_exchange_api.requests import FuturesKlineDataRequest

response = client.make_request(FuturesKlineDataRequest(
    contract_name="E-BTC-USDT",
    interval="15min",
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
from odyssey_exchange_api.requests import FuturesCreateOrderRequest
from odyssey_exchange_api.enums import FuturesOrderSide, FuturesOrderType, FuturesPositionSide, FuturesPositionType

response = client.make_request(FuturesCreateOrderRequest(
    contract_name="E-BTC-USDT",
    volume=Decimal(1),
    side=FuturesOrderSide.SELL,
    type=FuturesOrderType.LIMIT,
    open=FuturesPositionSide.OPEN,
    position_type=FuturesPositionType.CROSS_MARGIN,
    price=Decimal(60000)
))
print(response)
```

### Create Condition Order

Create a new condition order.

```python
from odyssey_exchange_api.requests import FuturesCreateConditionOrderRequest
from odyssey_exchange_api.enums import FuturesOrderType, FuturesOrderSide, FuturesPositionSide, FuturesPositionType, FuturesTriggerType

response = client.make_request(FuturesCreateConditionOrderRequest(
    contract_name="E-BTC-USDT",
    volume=Decimal(10000),
    side=FuturesOrderSide.BUY,
    type=FuturesOrderType.LIMIT,
    open=FuturesPositionSide.OPEN,
    position_type=FuturesPositionType.ISOLATED_MARGIN,
    price=Decimal(50000),
    trigger_type=FuturesTriggerType.STOP_LOSS_LIMIT,
    trigger_price=Decimal(50000)
))
print(response)
```

### Cancel order

Cancel an order.

```python
from odyssey_exchange_api.requests import FuturesCancelOrderRequest
from odyssey_exchange_api.enums import SpotOrderSide, SpotOrderType
from odyssey_exchange_api.objects import SpotSingleBatchOrder

response = client.make_request(FuturesCancelOrderRequest(
    order_id="2282856894002934568",
    contract_name="E-BTC-USDT"
))
print(response)
```

### Order Information

Get the order data. 

```python
from odyssey_exchange_api.requests import FuturesOrderInfoRequest

response = client.make_request(FuturesOrderInfoRequest(
    order_id="2282856894002934568",
    contract_name="E-BTC-USDT"
))
print(response)
```

### Current orders information

Get a list of open orders.

```python
from odyssey_exchange_api.requests import FuturesOpenOrdersRequest

response = client.make_request(FuturesOpenOrdersRequest(
    contract_name="E-BTC-USDT"
))
print(response)
```

### Historical commission records

Receives data on the historical commission.

```python
from odyssey_exchange_api.requests import FuturesHistoricalCommissionRequest

response = client.make_request(FuturesHistoricalCommissionRequest(
    contract_name="E-BTC-USDT"
))
print(response)
```

### Profit and loss record

Receives data on the historical profits and losses.

```python
from odyssey_exchange_api.requests import FuturesProfitAndLossRequest

response = client.make_request(FuturesProfitAndLossRequest(
    contract_name="E-BTC-USDT",
))
print(response)
```

### Transaction Record

Receives data on the transactions records.

```python
from odyssey_exchange_api.requests import FuturesMyTradesRequest

response = client.make_request(FuturesMyTradesRequest(
    contract_name="E-BTC-USDT"
))
print(response)
```


### Change position model

Change position model.

```python
from odyssey_exchange_api.requests import FuturesChangePositionModelRequest
from odyssey_exchange_api.enums import FuturesPositionModel

response = client.make_request(FuturesChangePositionModelRequest(
    contract_name="E-BTC-USDT",
    position_model=FuturesPositionModel.NET
))
print(response)
```


### Change margin model

Change margin model.

```python
from odyssey_exchange_api.requests import FuturesChangeMarginModelRequest
from odyssey_exchange_api.enums import FuturesPositionType

response = client.make_request(FuturesChangeMarginModelRequest(
    contract_name="E-BTC-USDT",
    margin_model=FuturesPositionType.CROSS_MARGIN
))
print(response)
```


### Change leverage

Change leverage.

```python
from odyssey_exchange_api.requests import FuturesChangeLeverageRequest

response = client.make_request(FuturesChangeLeverageRequest(
    contract_name="E-BTC-USDT",
    now_level=5
))
print(response)
```

### Obtain the current trigger order

Get all trigger orders.

```python
from odyssey_exchange_api.requests import FuturesCurrentTriggerOrdersRequest

response = client.make_request(FuturesCurrentTriggerOrdersRequest(
    contract_name="E-BTC-USDT",
    page=1,
    limit=10
))
print(response)
```

### Cancel trigger order

Cancel trigger order.

```python
from odyssey_exchange_api.requests import FuturesCancelTriggerOrderRequest

response = client.make_request(FuturesCancelTriggerOrderRequest(
    contract_name="E-BTC-USDT",
    order_id="2282856894002934568"
))
print(response)
```


### Account Information

Get account information.

```python
from odyssey_exchange_api.requests import FuturesAccountInfoRequest

response = client.make_request(FuturesAccountInfoRequest())
print(response)
```

