# Getting Started

A Python library for interacting with *[odyssey.trade](https://odyssey.trade)* API, allowing developers to easily
integrate trading functionalities into their applications.

## Features

- Full support of Odyssey Exchange Spot API at 15.07.2024.
- Synchronous and asynchronous support.
- All objects are typed and documented.

## Register on odyssey.trade and generate an API Key

To use methods that require a signature, you need to register on the exchange and get an API Key.

## Installation

You can install the library via pip:

```bash
pip install odyssey_exchange_api
```

## Usage

To get started with the library, import it in your Python script:

```python
import odyssey_exchange_api
```

### Example Initialization

#### Sync API

```python
from odyssey_exchange_api import SyncOdysseyExchangeAPI

api = SyncOdysseyExchangeAPI(api_key='YOUR_API_KEY', secret_key='YOUR_API_SECRET')
```

#### Async API

```python
from odyssey_exchange_api import AsyncOdysseyExchangeAPI

api = AsyncOdysseyExchangeAPI(api_key='YOUR_API_KEY', secret_key='YOUR_API_SECRET')
```
