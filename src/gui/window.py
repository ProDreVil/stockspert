import tkinter as tk
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
from gui.market import build_market
from gui.portfolio import build_portfolio
from gui.simulation import build_simulation
from gui.analysis import build_analysis
from gui.graph import StockGraph


class StockspertGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.configure(bg=BG_COLOR)

        if START_MAXIMIZED:
            self.root.state("zoomed")

        self.build_ui()

    def build_ui(self):
        header = build_header(self.root, "January 1, 2026")
        header.pack(fill="x", padx=25, pady=(18, 10))

        main = tk.Frame(self.root, bg=BG_COLOR)
        main.pack(fill="both", expand=True, padx=25, pady=(10, 20))

        main.grid_columnconfigure(0, weight=40)
        main.grid_columnconfigure(1, weight=25)
        main.grid_columnconfigure(2, weight=35)

        main.grid_rowconfigure(0, weight=3)
        main.grid_rowconfigure(1, weight=1)

        graph_panel = tk.Frame(main, bg=BG_COLOR)
        graph_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

        self.graph = StockGraph(graph_panel)
        self.graph.frame.pack(fill="both", expand=True)

        build_market(main, on_apply=self.apply_market_changes).grid(
            row=0, column=1,
            sticky="nsew", padx=5
        )

        build_portfolio(main).grid(
            row=0, column=2,
            sticky="nsew", padx=(5, 0)
        )

        build_simulation(main).grid(
            row=1, column=0,
            sticky="nsew", padx=(0, 5), pady=(10, 0)
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
        recommendation = get_recommendation(
            trend.lower(),
            pe.lower(),
            revenue.lower(),
            earnings.lower(),
            volume.lower()
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

        self.analysis["rule"].configure(
            text=f"Rule Fired: {recommendation}"
        )

    def run(self):
        self.root.mainloop()