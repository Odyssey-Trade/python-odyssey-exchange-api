from decimal import Decimal

from pydantic import BaseModel


class SpotTickerData(BaseModel):
    """
    An object with information about an asset per day.
    """

    time: int = 0
    """Timestamp"""
    high: Decimal = Decimal(0)
    """Highest price"""
    low: Decimal = Decimal(0)
    """Lowest price"""
    last: Decimal = Decimal(0)
    """Latest deal price"""
    vol: Decimal = Decimal(0)
    """Trade volume"""
    amount: Decimal = Decimal(0)
    """Trade amount"""
    buy: Decimal = Decimal(0)
    """The price in the buying book order at the first one"""
    sell: Decimal = Decimal(0)
    """The price in the selling book order at the first one"""
    rose: str = ""
    """Range of increase and decrease, + is increase, - is decrease, +0.05 means increase by 5%"""
