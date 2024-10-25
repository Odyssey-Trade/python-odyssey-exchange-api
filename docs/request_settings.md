# Request Settings

Package uses the **[httpx](https://www.python-httpx.org/)** library.

You can see the all of the available options for client settings in the **[httpx](https://www.python-httpx.org/)** documentation.


## Proxies


You can use a proxy using the following method.

```python
client = Client("YOUR_API_KEY", "YOUR_API_SECRET", {"proxy": "http://localhost:8030"})
```

Or set an environment variable for your proxy if required to work across all requests.

An example for Linux environments from the requests Proxies documentation is as follows.


```bash
$ export HTTP_PROXY="http://10.10.1.10:3128"
$ export HTTPS_PROXY="http://10.10.1.10:1080"
```

For Windows environments

```
C:\>set HTTP_PROXY=http://10.10.1.10:3128
C:\>set HTTPS_PROXY=http://10.10.1.10:1080
```

## Timeouts


You can set a request timeout following method.

```python
client = Client("YOUR_API_KEY", "YOUR_API_SECRET", {"timeout": 30})
```
