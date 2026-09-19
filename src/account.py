class Account:
    def __init__(self, starting_cash=10000.00):
        self.cash = starting_cash
        self.shares = 0
        self.invested = 0.00
        self.average_buy_price = 0.00

    def buy(self, price, quantity):
        total_cost = price * quantity

        if quantity <= 0:
            return False

        if total_cost > self.cash:
            return False

        old_total = self.average_buy_price * self.shares
        new_total = old_total + total_cost
        new_shares = self.shares + quantity

        self.average_buy_price = new_total / new_shares

        self.cash -= total_cost
        self.shares += quantity
        self.invested += total_cost

        return True

    def sell(self, price, quantity):
        if quantity <= 0:
            return False

        if quantity > self.shares:
            return False

        total_value = price * quantity

        self.cash += total_value
        self.shares -= quantity
        self.invested -= self.average_buy_price * quantity

        if self.shares == 0:
            self.average_buy_price = 0.00

        return True

    def get_value(self, current_price):
        return self.cash + (self.shares * current_price)

    def get_profit_loss(self, current_price):
        return self.get_value(current_price) - 10000.00

    def get_return(self, current_price):
        return (self.get_profit_loss(current_price) / 10000.00) * 100