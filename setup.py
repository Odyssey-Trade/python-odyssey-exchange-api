import setuptools

setuptools.setup(
    name="odyssey_exchange_api",
    version="0.0.1",
    author="author",
    description="",
    packages=[
        "odyssey_exchange_api",
        "odyssey_exchange_api.clients",
        "odyssey_exchange_api.enums",
        "odyssey_exchange_api.exceptions",
        "odyssey_exchange_api.objects",
        "odyssey_exchange_api.requests",
        "odyssey_exchange_api.responses",
    ],
    python_requires=">=3.10"
)
