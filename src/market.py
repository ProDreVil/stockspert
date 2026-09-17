import random
from datetime import datetime, timedelta


class Market:
    def __init__(self, starting_price=None):
        if starting_price is None:
            starting_price = random.uniform(500.00, 2000.00)
        self.current_price = starting_price
        self.current_date = datetime.now()
        self.candles = []

        start_date = self.current_date - timedelta(days=6)

        for _ in range(7):
            self.current_date = start_date
            self._create_candle()
            start_date += timedelta(days=1)

        self.current_date = datetime.now()

    @property
    def price_history(self):
        return [candle["close"] for candle in self.candles]

    def _create_candle(self):
        open_price = self.current_price

        change_percent = random.uniform(-1.0, 1.0)
        change = open_price * (change_percent / 100)

        close_price = max(
            1.00,
            open_price + change
        )

        wick_percent = random.uniform(0.0, 0.5)
        high_price = (
            max(open_price, close_price)
            + open_price * (wick_percent / 100)
        )
        low_price = (
            min(open_price, close_price)
            - open_price * (wick_percent / 100)
        )

        low_price = max(1.00, low_price)

        candle = {
            "date": self.current_date,
            "open": open_price,
            "high": high_price,
            "low": low_price,
            "close": close_price
        }

        self.candles.append(candle)
        self.current_price = close_price

        return candle

    def advance(self, days=1):
        self.current_date += timedelta(days=days)

        return self._create_candle()