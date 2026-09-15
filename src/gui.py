import tkinter as tk
from tkinter import ttk


# Colors
BG_COLOR = "#121212"
PANEL_COLOR = "#1E1E1E"
TEXT_COLOR = "#EAEAEA"
SECONDARY_TEXT = "#AAAAAA"
ACCENT_COLOR = "#4A90E2"


class StockspertGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Stockspert")
        self.root.geometry("1100x800")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.setup_styles()
        self.create_layout()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Dark.TCombobox",
            fieldbackground=PANEL_COLOR,
            background=PANEL_COLOR,
            foreground=TEXT_COLOR,
            arrowcolor=TEXT_COLOR,
            borderwidth=0
        )

        style.map(
            "Dark.TCombobox",
            fieldbackground=[
                ("readonly", PANEL_COLOR)
            ],
            foreground=[
                ("readonly", TEXT_COLOR)
            ]
        )

    def create_layout(self):
        # Header
        header = tk.Frame(
            self.root,
            bg=BG_COLOR
        )
        header.pack(
            fill="x",
            padx=40,
            pady=(30, 20)
        )

        title = tk.Label(
            header,
            text="STOCKSPERT",
            font=("Segoe UI", 22, "bold"),
            fg=TEXT_COLOR,
            bg=BG_COLOR
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text="Stock Market Expert System",
            font=("Segoe UI", 10),
            fg=SECONDARY_TEXT,
            bg=BG_COLOR
        )
        subtitle.pack(pady=(4, 0))

        # Main content
        main_frame = tk.Frame(
            self.root,
            bg=BG_COLOR
        )
        main_frame.pack(
            fill="both",
            expand=True,
            padx=40
        )

        # Left panel
        left_panel = tk.Frame(
            main_frame,
            bg=PANEL_COLOR
        )
        left_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        # Right panel
        right_panel = tk.Frame(
            main_frame,
            bg=PANEL_COLOR
        )
        right_panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        # Left panel title
        tk.Label(
            left_panel,
            text="MARKET",
            font=("Segoe UI", 11, "bold"),
            fg=SECONDARY_TEXT,
            bg=PANEL_COLOR
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )

        tk.Label(
            left_panel,
            text="Stock Price",
            font=("Segoe UI", 10),
            fg=SECONDARY_TEXT,
            bg=PANEL_COLOR
        ).pack(
            anchor="w",
            padx=25
        )

        tk.Label(
            left_panel,
            text="$100.00",
            font=("Segoe UI", 28, "bold"),
            fg=TEXT_COLOR,
            bg=PANEL_COLOR
        ).pack(
            anchor="w",
            padx=25,
            pady=(2, 20)
        )

        # Placeholder for graph
        graph_placeholder = tk.Frame(
            left_panel,
            bg="#181818",
            height=300
        )
        graph_placeholder.pack(
            fill="x",
            padx=25,
            pady=10
        )
        graph_placeholder.pack_propagate(False)

        tk.Label(
            graph_placeholder,
            text="PRICE GRAPH",
            font=("Segoe UI", 10, "bold"),
            fg=SECONDARY_TEXT,
            bg="#181818"
        ).place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Right panel title
        tk.Label(
            right_panel,
            text="EXPERT SYSTEM",
            font=("Segoe UI", 11, "bold"),
            fg=SECONDARY_TEXT,
            bg=PANEL_COLOR
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )

        tk.Label(
            right_panel,
            text="Recommendation",
            font=("Segoe UI", 10),
            fg=SECONDARY_TEXT,
            bg=PANEL_COLOR
        ).pack(
            anchor="w",
            padx=25
        )

        tk.Label(
            right_panel,
            text="—",
            font=("Segoe UI", 30, "bold"),
            fg=TEXT_COLOR,
            bg=PANEL_COLOR
        ).pack(
            anchor="w",
            padx=25,
            pady=(2, 20)
        )

        # Placeholder sections
        self.create_section(
            right_panel,
            "MARKET INFORMATION",
            "Trend\nP/E Ratio\nRevenue Growth\nEarnings Growth\nTrading Volume"
        )

        self.create_section(
            right_panel,
            "SIMULATION",
            "Time Control\nRandom Market\nManual Market"
        )

        self.create_section(
            right_panel,
            "PORTFOLIO",
            "Cash\nShares\nPortfolio Value"
        )

    def create_section(self, parent, title, content):
        frame = tk.Frame(
            parent,
            bg="#181818"
        )
        frame.pack(
            fill="x",
            padx=25,
            pady=8
        )

        tk.Label(
            frame,
            text=title,
            font=("Segoe UI", 9, "bold"),
            fg=SECONDARY_TEXT,
            bg="#181818"
        ).pack(
            anchor="w",
            padx=15,
            pady=(12, 6)
        )

        tk.Label(
            frame,
            text=content,
            font=("Segoe UI", 10),
            fg=TEXT_COLOR,
            bg="#181818",
            justify="left"
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 12)
        )

    def run(self):
        self.root.mainloop()