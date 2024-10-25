# Exceptions

## UnknownException

Raised if a non JSON response is returned

## BaseExchangeException

On an API call error this exception will be raised.

The exception provides access to the

* code – code of API error, exception can be found at API documentation
* msg – error message
* reason – explanation of the error in English
* data – None or dict with extra data

