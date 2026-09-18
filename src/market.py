import random
from datetime import datetime, timedelta


class Market:
    def __init__(self, starting_price=None):
        if starting_price is None:
            starting_price = random.uniform(500.00, 2000.00)
        self.current_price = starting_price
        self.eps = self.current_price / random.uniform(8.0, 35.0)
        self.pe_ratio = self.current_price / self.eps
        self.revenue_growth = random.uniform(-10.0, 10.0)
        self.earnings_growth = random.uniform(-10.0, 10.0)

        self.current_date = datetime.now()
        self.candles = []

        start_date = self.current_date - timedelta(days=29)

        for _ in range(30):
            self.current_date = start_date
            self._create_candle()
            start_date += timedelta(days=1)

        self.current_date = datetime.now()

    @property
    def price_history(self):
        return [candle["close"] for candle in self.candles]

    def _create_candle(self, days=1):
        open_price = self.current_price

        change_percent = random.uniform(-1.0, 1.0) * (days ** 0.5)
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
        self.pe_ratio = self.current_price / self.eps
        self.revenue_growth += random.uniform(-1.0, 1.0)
        self.earnings_growth += random.uniform(-1.0, 1.0)
        return candle

    def get_trend(self):
        if len(self.candles) < 5:
            return "Sideways"
        oldest_price = self.candles[-5]["close"]
        latest_price = self.candles[-1]["close"]
        change_percent = (
            (latest_price - oldest_price)
            / oldest_price
        ) * 100
        if change_percent > 1.5:
            return "Uptrend"
        if change_percent < -1.5:
            return "Downtrend"
        return "Sideways"

    def get_pe_classification(self):
        if self.pe_ratio < 15:
            return "Low"
        if self.pe_ratio > 25:
            return "High"
        return "Fair"

    def get_revenue_classification(self):
        if self.revenue_growth > 2:
            return "Positive"
        if self.revenue_growth < -2:
            return "Negative"
        return "Neutral"

    def get_earnings_classification(self):
        if self.earnings_growth > 2:
            return "Positive"
        return "Negative"

    def advance(self, days=1):
        for _ in range(days):
            self.current_date += timedelta(days=1)
            self._create_candle()

        return self.candles[-1]