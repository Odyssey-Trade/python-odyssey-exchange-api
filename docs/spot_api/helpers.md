# Helpers

## Enums

### SpotOrderSide

* **BUY** – indicates that the type of order was a purchase
* **SELL** – indicates that the type of order was a sale
* **buy** – indicates that the type of order was a purchase, it is duplicated due to the fact that the API can return
  the order type in two ways
* **sell** – indicates that the type of order was a sale, it is duplicated due to the fact that the API can return the
  order type in two ways

### SpotOrderType

* **LIMIT** – the order is a limit order
* **MARKET** – the order is a market order

### SpotOrderStatus

* **NEW** – this is a new order, no action has been taken, it is duplicated due to the fact that the API can return the
  order type in two ways
* **NEW_ORDER** – this is a new order, no action has been taken, it is duplicated due to the fact that the API can
  return the order type in two ways
* **PARTIALLY_FILLED** – the order was partially executed
* **FILLED** – the order was fully executed
* **CANCELLED** – the order was cancelled
* **TO_BE_CANCELLED** – the order will be cancelled
* **PARTIALLY_FILLED_OR_CANCELLED** – the order was partially executed or cancelled
* **REJECTED** – the order was rejected
