import tkinter as tk

from config import (
    WINDOW_TITLE,
    START_MAXIMIZED,
    BG_COLOR,
    PANEL_COLOR,
    GRAPH_COLOR,
    TEXT_COLOR,
    SECONDARY_TEXT,
)

from components import (
    create_label,
    create_panel,
    create_section,
)


class StockspertGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title(WINDOW_TITLE)
        self.root.configure(bg=BG_COLOR)

        if START_MAXIMIZED:
            self.root.state("zoomed")

        self.create_header()
        self.create_main_layout()

    def create_header(self):
        header = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        header.pack(
            fill="x",
            padx=40,
            pady=(30, 20)
        )

        create_label(
            header,
            "STOCKSPERT",
            font=("Segoe UI", 22, "bold"),
            color=TEXT_COLOR,
            bg=BG_COLOR
        ).pack()

    def create_main_layout(self):
        main_frame = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=40
        )

        self.create_market_panel(main_frame)
        self.create_expert_panel(main_frame)

    def create_market_panel(self, parent):
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
            font=("Segoe UI", 11, "bold"),
            color=SECONDARY_TEXT
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )

        create_label(
            panel,
            "Stock Price",
            font=("Segoe UI", 10),
            color=SECONDARY_TEXT
        ).pack(
            anchor="w",
            padx=25
        )

        create_label(
            panel,
            "$100.00",
            font=("Segoe UI", 28, "bold"),
            color=TEXT_COLOR
        ).pack(
            anchor="w",
            padx=25,
            pady=(2, 20)
        )

        graph = tk.Frame(
            panel,
            bg=GRAPH_COLOR,
            height=300
        )

        graph.pack(
            fill="x",
            padx=25,
            pady=10
        )

        graph.pack_propagate(False)

        create_label(
            graph,
            "PRICE GRAPH",
            font=("Segoe UI", 10, "bold"),
            color=SECONDARY_TEXT,
            bg=GRAPH_COLOR
        ).place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

    def create_expert_panel(self, parent):
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
            font=("Segoe UI", 11, "bold"),
            color=SECONDARY_TEXT
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )

        create_label(
            panel,
            "Recommendation",
            font=("Segoe UI", 10),
            color=SECONDARY_TEXT
        ).pack(
            anchor="w",
            padx=25
        )

        create_label(
            panel,
            "—",
            font=("Segoe UI", 30, "bold"),
            color=TEXT_COLOR
        ).pack(
            anchor="w",
            padx=25,
            pady=(2, 20)
        )

        market_info = create_section(
            panel,
            "MARKET INFORMATION"
        )

        market_info.pack(
            fill="x",
            padx=25,
            pady=8
        )

        create_label(
            market_info,
            "Trend\n"
            "P/E Ratio\n"
            "Revenue Growth\n"
            "Earnings Growth\n"
            "Trading Volume",
            bg=GRAPH_COLOR
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 12)
        )

        simulation = create_section(
            panel,
            "SIMULATION"
        )

        simulation.pack(
            fill="x",
            padx=25,
            pady=8
        )

        create_label(
            simulation,
            "Time Control\n"
            "Random Market\n"
            "Manual Market",
            bg=GRAPH_COLOR
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 12)
        )

        portfolio = create_section(
            panel,
            "PORTFOLIO"
        )

        portfolio.pack(
            fill="x",
            padx=25,
            pady=8
        )

        create_label(
            portfolio,
            "Cash\n"
            "Shares\n"
            "Portfolio Value",
            bg=GRAPH_COLOR
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 12)
        )

    def run(self):
        self.root.mainloop()