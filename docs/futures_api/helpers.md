# Helpers

## Enums

### FuturesContractSide

* **REVERSE** — it means that the contract is the reverse
* **FORWARD** — it means that the contract is the forward


### FuturesContractStatus

* **NOT_TRADABLE** — the contract is not currently being traded
* **TRADABLE** — the contract is currently being traded



### FuturesContractType

* **PERPETUAL** — the contract is eternal
* **SIMULATED** — the contract is simulated, used for testing



### FuturesOrderSide

* **BUY** – indicates that the type of order was a purchase
* **SELL** – indicates that the type of order was a sale



### FuturesOrderStatus

* **INIT** – this is a new order, no action has been taken, it is duplicated due to the fact that the API can return the
  order type in three ways
* **NEW** – this is a new order, no action has been taken, it is duplicated due to the fact that the API can return the
  order type in three ways
* **NEW_ORDER** – this is a new order, no action has been taken, it is duplicated due to the fact that the API can
  return the order type in three ways
* **PARTIALLY_FILLED** – the order was partially executed
* **FILLED** – the order was fully executed
* **CANCELLED** – the order was cancelled
* **TO_BE_CANCELLED** – the order will be cancelled
* **PARTIALLY_FILLED_OR_CANCELLED** – the order was partially executed or cancelled
* **REJECTED** – the order was rejected



### FuturesOrderType

* **LIMIT** – the order is a limit order
* **MARKET** – the order is a market order


### FuturesPositionFrozenStatus

* **NORMAL** — the current status of the position is normal
* **LIQUIDATION_FROZEN** — the current status of the position is liquidation frozen
* **DELIVERY_FROZEN** — the current status of the position is delivery frozen



### FuturesPositionModel

* **NET** — is a net position
* **TWO_WAY** — is a two-way position



### FuturesPositionSide

* **OPEN** — side of the position, open a position
* **CLOSE** — side of the position, close a position



### FuturesPositionStatus

* **VALID** — the position status is valid
* **INVALID** — the position status is invalid



### FuturesPositionType

* **CROSS_MARGIN** — the position is open on a cross margin
* **ISOLATED_MARGIN** — the position is open on a isolated margin



### FuturesTimeInForce

* **IOC** — the type of position opening is to execute immediately or cancel
* **FOK** — the type of opening a position is to execute it completely immediately or cancel it
* **POST_ONLY** — the type of opening a order is a maker order on the order book, adding liquidity to the market, and never match with orders already on the book



### FuturesTriggerOrderStatus

* **VALID** — the trigger order status is valid
* **INVALID** — the trigger order status is invalid



### FuturesTriggerType

* **STOP_LOSS** — the type of trigger is stop loss
* **TAKE_PROFIT** — the type of trigger is take profit
* **STOP_LOSS_LIMIT** — the type of trigger is stop loss by limit order
* **TAKE_PROFIT_LIMIT** — the type of trigger is take profit by limit order

