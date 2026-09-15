import tkinter as tk

from config import (
    BG_COLOR,
    PANEL_COLOR,
    SECONDARY_TEXT,
    START_MAXIMIZED,
    TEXT_COLOR,
    WINDOW_TITLE,
)

from gui.components import (
    create_label,
    create_panel,
    create_section,
)

from gui.graph import StockGraph


class StockspertGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.configure(bg=BG_COLOR)

        if START_MAXIMIZED:
            self.root.state("zoomed")

        self.build_header()
        self.build_main_area()

    def build_header(self):
        header = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        header.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        create_label(
            header,
            "STOCKSPERT",
            font=("Segoe UI", 20, "bold"),
            bg=BG_COLOR
        ).pack(anchor="w")

    def build_main_area(self):
        main = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(10, 25)
        )

        self.build_market_panel(main)
        self.build_expert_panel(main)

    def build_market_panel(self, parent):
        panel = create_panel(parent)

        panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        create_label(
            panel,
            "MARKET",
            font=("Segoe UI", 10, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        create_label(
            panel,
            "Stock Price",
            color=SECONDARY_TEXT
        ).pack(
            anchor="w",
            padx=15
        )

        create_label(
            panel,
            "$100.00",
            font=("Segoe UI", 28, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 15)
        )

        graph_container = tk.Frame(
            panel,
            bg=BG_COLOR
        )

        graph_container.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.graph = StockGraph(graph_container)
        self.graph.frame.pack(
            fill="both",
            expand=True
        )

    def build_expert_panel(self, parent):
        panel = create_panel(parent)

        panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        create_label(
            panel,
            "EXPERT SYSTEM",
            font=("Segoe UI", 10, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        recommendation = create_section(
            panel,
            "RECOMMENDATION"
        )

        recommendation.pack(
            fill="x",
            padx=15
        )

        create_label(
            recommendation,
            "WAITING FOR MARKET DATA",
            font=("Segoe UI", 18, "bold"),
            bg="#181818"
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 15)
        )

        market_info = create_section(
            panel,
            "MARKET INFORMATION"
        )

        market_info.pack(
            fill="x",
            padx=15,
            pady=(10, 0)
        )

        simulation = create_section(
            panel,
            "SIMULATION"
        )

        simulation.pack(
            fill="x",
            padx=15,
            pady=(10, 0)
        )

        portfolio = create_section(
            panel,
            "PORTFOLIO"
        )

        portfolio.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(10, 15)
        )

    def run(self):
        self.root.mainloop()