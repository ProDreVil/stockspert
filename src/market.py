import random
import copy
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
        self.volume = random.uniform(500000, 2000000)

        self.current_date = datetime.now()
        self.candles = []
        self.state_history = []
        self.max_history = 200

        start_date = self.current_date - timedelta(days=29)

        for _ in range(30):
            self.current_date = start_date
            self._create_candle()
            start_date += timedelta(days=1)

        self.current_date = datetime.now()

    @property
    def price_history(self):
        return [candle["close"] for candle in self.candles]

    def _create_candle(self, days=1, direction=None):
        open_price = self.current_price

        if direction == "rise":
            change_percent = random.uniform(0.5, 1.5) * (days ** 0.5)
        elif direction == "fall":
            change_percent = random.uniform(-1.5, -0.5) * (days ** 0.5)
        elif direction == "stable":
            change_percent = random.uniform(-0.3, 0.3) * (days ** 0.5)
        else:
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
        self.volume = random.uniform(500000, 2000000)
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

    def get_volume_classification(self):
        if self.volume < 800000:
            return "Low"
        if self.volume > 1500000:
            return "High"
        return "Average"

    def advance(self, days=1, direction=None):
        for _ in range(days):
            self.state_history.append({
                "current_price": self.current_price,
                "eps": self.eps,
                "pe_ratio": self.pe_ratio,
                "revenue_growth": self.revenue_growth,
                "earnings_growth": self.earnings_growth,
                "volume": self.volume,
                "current_date": self.current_date,
                "candles": copy.deepcopy(self.candles)
            })

            if len(self.state_history) > self.max_history:
                self.state_history.pop(0)

            self.current_date += timedelta(days=1)
            self._create_candle(direction=direction)

        return self.candles[-1]

    def return_previous(self):
        if not self.state_history:
            return False

        state = self.state_history.pop()

        self.current_price = state["current_price"]
        self.eps = state["eps"]
        self.pe_ratio = state["pe_ratio"]
        self.revenue_growth = state["revenue_growth"]
        self.earnings_growth = state["earnings_growth"]
        self.volume = state["volume"]
        self.current_date = state["current_date"]
        self.candles = state["candles"]

        return True


    def randomize(self):
        self.state_history.append({
            "current_price": self.current_price,
            "eps": self.eps,
            "pe_ratio": self.pe_ratio,
            "revenue_growth": self.revenue_growth,
            "earnings_growth": self.earnings_growth,
            "volume": self.volume,
            "current_date": self.current_date,
            "candles": copy.deepcopy(self.candles)
        })

        if len(self.state_history) > self.max_history:
            self.state_history.pop(0)

        self.current_date += timedelta(days=1)

        self.current_price = random.uniform(500.00, 2000.00)
        self.eps = self.current_price / random.uniform(8.0, 35.0)
        self.pe_ratio = self.current_price / self.eps
        self.revenue_growth = random.uniform(-10.0, 10.0)
        self.earnings_growth = random.uniform(-10.0, 10.0)
        self.volume = random.uniform(500000, 2000000)

        self._create_candle()

        if len(self.candles) > 30:
            self.candles.pop(0)

        return self.candles[-1]