import tkinter as tk
import random
from datetime import datetime

from clips import get_recommendation
from config import (
    BG_COLOR,
    BUY_COLOR,
    HOLD_COLOR,
    SELL_COLOR,
    START_MAXIMIZED,
    TEXT_COLOR,
    WINDOW_TITLE
)
from gui.header import build_header
from gui.stocks import build_market
from gui.portfolio import build_portfolio
from gui.simulation import build_simulation
from market import Market
from gui.analysis import (
    build_analysis,
    update_reasons,
)
from gui.graph import StockGraph


class StockspertGUI:
    def __init__(self, starting_price=None):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.configure(bg=BG_COLOR)

        if START_MAXIMIZED:
            self.root.state("zoomed")
        
        self.market = Market(starting_price=random.uniform(500.00, 2000.00))
        self.simulation_day = 1
        self.build_ui()
        self.graph.update(self.market.candles)
        self.initialize_analysis()

    def build_ui(self):
        self.header, self.date_label, self.simulation_day_label = build_header(
            self.root,
            self.market.current_date.strftime("%B %d, %Y")
        )
        self.header.pack(
            fill="x",
            padx=25,
            pady=(18, 10)
        )

        main = tk.Frame(self.root, bg=BG_COLOR)
        main.pack(fill="both", expand=True, padx=0, pady=(10, 20))

        main.grid_columnconfigure(0, minsize=500, weight=0)
        main.grid_columnconfigure(1, weight=250)
        main.grid_columnconfigure(2, weight=350)

        main.grid_rowconfigure(0, weight=2)
        main.grid_rowconfigure(1, weight=1, minsize=180)

        graph_panel = tk.Frame(main, bg=BG_COLOR)
        graph_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

        self.graph = StockGraph(graph_panel)
        self.graph.frame.pack(fill="both", expand=True)

        self.market_gui = build_market(
            main,
            on_apply=self.apply_market_changes,
            initial_price=self.market.current_price
        )

        self.market_gui["frame"].grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=5
        )

        build_portfolio(main).grid(
            row=0, column=2,
            sticky="nsew", padx=(5, 0)
        )

        self.simulation = build_simulation(
            main,
            on_next=self.advance_simulation,
            on_advance=self.advance_by_input,
            on_return=self.return_simulation
        )
        self.simulation["frame"].grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0, 5),
            pady=(10, 0)
        )

        self.analysis = build_analysis(main)
        self.analysis["frame"].grid(
            row=1,
            column=1,
            columnspan=2,
            sticky="nsew",
            padx=(5, 0),
            pady=(10, 0)
        )

    def apply_market_changes(
        self,
        price,
        trend,
        pe,
        revenue,
        earnings,
        volume
    ):
        recommendation, rule, confidence = get_recommendation(
            trend.lower(),
            pe.lower(),
            revenue.lower(),
            earnings.lower(),
            volume.lower(),
            self.market.price_history
        )

        recommendation_colors = {
            "BUY": BUY_COLOR,
            "HOLD": HOLD_COLOR,
            "SELL": SELL_COLOR
        }

        self.analysis["recommendation"].configure(
            text=recommendation,
            fg=recommendation_colors.get(
                recommendation,
                TEXT_COLOR
            )
        )

        self.analysis["confidence"].configure(
            text=f"Confidence: {confidence}%"
        )

        self.analysis["rule"].configure(
            text=f"Rule Fired: {rule}"
        )

        update_reasons(
            self.analysis["reasons"],
            rule
        )

    def initialize_analysis(self):
        self.refresh_market_ui()

    def refresh_market_ui(self):
        current_price = self.market.current_price
        self.market_gui["price_var"].set(f"${current_price:.2f}")
        previous_price = self.market.candles[-2]["close"]
        change = current_price - previous_price
        change_percent = (change / previous_price) * 100
        self.market_gui["change_var"].set(f"{'+$' if change >= 0 else '-$'}{abs(change):.2f} ({change_percent:+.2f}%)")
        self.market_gui["trend_var"].set(self.market.get_trend())
        trend_change = ((self.market.candles[-1]["close"] - self.market.candles[-5]["close"])/ self.market.candles[-5]["close"]) * 100
        self.market_gui["trend_change_var"].set(f"{trend_change:+.2f}%")
        self.market_gui["pe_value_var"].set(f"{self.market.pe_ratio:.2f}")
        self.market_gui["pe_var"].set(self.market.get_pe_classification())
        self.market_gui["revenue_value_var"].set(f"{self.market.revenue_growth:+.2f}%")
        self.market_gui["revenue_var"].set(self.market.get_revenue_classification())
        self.market_gui["earnings_value_var"].set(f"{self.market.earnings_growth:+.2f}%")
        self.market_gui["earnings_var"].set(self.market.get_earnings_classification())
        self.market_gui["volume_value_var"].set(f"{self.market.volume / 1000000:.2f}M")
        self.market_gui["volume_var"].set(self.market.get_volume_classification())

        self.date_label.configure(text=self.market.current_date.strftime("%B %d, %Y"))
        self.graph.update(self.market.candles)

        recommendation, rule, confidence = get_recommendation(
            self.market_gui["trend_var"].get().lower(),
            self.market_gui["pe_var"].get().lower(),
            self.market_gui["revenue_var"].get().lower(),
            self.market_gui["earnings_var"].get().lower(),
            self.market_gui["volume_var"].get().lower(),
            self.market.price_history
        )

        colors = {
            "BUY": BUY_COLOR,
            "HOLD": HOLD_COLOR,
            "SELL": SELL_COLOR
        }

        self.analysis["recommendation"].configure(
            text=recommendation,
            fg=colors.get(recommendation, TEXT_COLOR)
        )
        self.analysis["confidence"].configure(
            text=f"Confidence: {confidence}%"
        )
        self.analysis["rule"].configure(
            text=f"Rule Fired: {rule}"
        )

        update_reasons(self.analysis["reasons"], rule)

    def advance_simulation(self, days=1):
        self.market.advance(days)
        self.simulation_day += days
        self.simulation_day_label.configure(text=f"Day {self.simulation_day}")

        current_price = self.market.current_price
        previous_price = self.market.candles[-2]["close"]

        change = current_price - previous_price
        change_percent = (change / previous_price) * 100

        self.market_gui["price_var"].set(f"${current_price:.2f}")

        self.market_gui["change_var"].set(f"{'+$' if change >= 0 else '-$'}{abs(change):.2f} ({change_percent:+.2f}%)")

        trend = self.market.get_trend()
        self.market_gui["trend_var"].set(trend)

        trend_change = (
            (self.market.candles[-1]["close"] - self.market.candles[-5]["close"])
            / self.market.candles[-5]["close"]
        ) * 100

        self.market_gui["trend_change_var"].set(f"{trend_change:+.2f}%")

        self.market_gui["pe_value_var"].set(f"{self.market.pe_ratio:.2f}")

        self.market_gui["revenue_value_var"].set(f"{self.market.revenue_growth:+.2f}%")
        self.market_gui["revenue_var"].set(self.market.get_revenue_classification())

        self.market_gui["earnings_value_var"].set(f"{self.market.earnings_growth:+.2f}%")
        self.market_gui["earnings_var"].set(self.market.get_earnings_classification())

        self.market_gui["volume_value_var"].set(f"{self.market.volume / 1000000:.2f}M")
        self.market_gui["volume_var"].set(self.market.get_volume_classification())

        self.refresh_market_ui()

    def return_simulation(self):
        if not self.market.return_previous():
            return

        if self.simulation_day > 1:
            self.simulation_day -= 1

        self.simulation_day_label.configure(
            text=f"Day {self.simulation_day}"
        )

        self.refresh_market_ui()

    def advance_by_input(self):
        try:
            day = int(self.simulation["day_entry"].get() or 0)
            week = int(self.simulation["week_entry"].get() or 0)
            month = int(self.simulation["month_entry"].get() or 0)
        except ValueError:
            return
        total_days = day + (week * 7) + (month * 30)
        if total_days <= 0:
            return
        self.advance_simulation(total_days)

    def run(self):
        self.root.mainloop()