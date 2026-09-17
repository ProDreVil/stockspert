from py_compile import main
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
        self.build_ui()
        self.graph.update(self.market.candles)
        self.initialize_analysis()

    def build_ui(self):
        current_date = datetime.now().strftime("%B %d, %Y")
        self.header, self.date_label = build_header(
            self.root,
            self.market.current_date.strftime("%B %d, %Y")
        )
        self.header.pack(
            fill="x",
            padx=25,
            pady=(18, 10)
        )

        main = tk.Frame(self.root, bg=BG_COLOR)
        main.pack(fill="both", expand=True, padx=25, pady=(10, 20))

        main.grid_columnconfigure(0, weight=40)
        main.grid_columnconfigure(1, weight=25)
        main.grid_columnconfigure(2, weight=35)

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
            on_advance=self.advance_by_input
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
        self.apply_market_changes(
            "100.00",
            "Uptrend",
            "Low",
            "Positive",
            "Positive",
            "Average",
        )

    def advance_simulation(self, days=1):
        self.market.advance(days)

        self.market_gui["price_var"].set(
            f"{self.market.current_price:.2f}"
        )

        self.date_label.configure(
            text=self.market.current_date.strftime("%B %d, %Y")
        )

        self.graph.update(self.market.candles)

    def advance_by_input(self):
        try:
            day = int(self.simulation["day_entry"].get() or 0)
            week = int(self.simulation["week_entry"].get() or 0)
            month = int(self.simulation["month_entry"].get() or 0)
        except ValueError:
            return
        total_days = (
            day
            + (week * 7)
            + (month * 30)
        )
        if total_days <= 0:
            return
        self.advance_simulation(total_days)

    def run(self):
        self.root.mainloop()