import tkinter as tk
from clips import get_recommendation

from config import BG_COLOR, START_MAXIMIZED, WINDOW_TITLE
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

        # 40 / 25 / 35 layout
        main.grid_columnconfigure(0, weight=40)
        main.grid_columnconfigure(1, weight=25)
        main.grid_columnconfigure(2, weight=35)

        main.grid_rowconfigure(0, weight=3)
        main.grid_rowconfigure(1, weight=1)

        # Price History
        graph_panel = tk.Frame(main, bg=BG_COLOR)
        graph_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

        self.graph = StockGraph(graph_panel)
        self.graph.frame.pack(fill="both", expand=True)

        # Top-right
        build_market(main, on_apply=self.apply_market_changes).grid(
            row=0, column=1,
            sticky="nsew", padx=5
        )

        build_portfolio(main).grid(
            row=0, column=2,
            sticky="nsew", padx=(5, 0)
        )

        # Bottom
        build_simulation(main).grid(
            row=1, column=0,
            sticky="nsew", padx=(0, 5), pady=(10, 0)
        )

        build_analysis(main).grid(
            row=1, column=1,
            columnspan=2,
            sticky="nsew", padx=(5, 0), pady=(10, 0)
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

        print("Recommendation:", recommendation)

    def run(self):
        self.root.mainloop()