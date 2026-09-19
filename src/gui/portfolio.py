import tkinter as tk

from config import GRAPH_COLOR, SECONDARY_TEXT
from gui.components import (
    create_button,
    create_entry,
    create_label,
    create_section,
)


def build_portfolio(parent):

    panel = create_section(parent, "PORTFOLIO")

    stats = [
        ("Cash", "$10,000.00"),
        ("Shares", "0"),
        ("Invested", "$0.00"),
        ("Value", "$10,000.00"),
    ]

    stat_labels = {}

    for label, value in stats:
        row = tk.Frame(
            panel,
            bg=GRAPH_COLOR
        )
        row.pack(
            fill="x",
            padx=15,
            pady=2
        )

        create_label(
            row,
            label,
            color=SECONDARY_TEXT,
            bg=GRAPH_COLOR,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left")

        value_label = create_label(
            row,
            value,
            bg=GRAPH_COLOR,
            font=("Consolas", 10)
        )
        value_label.pack(side="right")

        stat_labels[label] = value_label

    pl_row = tk.Frame(panel, bg=GRAPH_COLOR)
    pl_row.pack(fill="x", padx=15, pady=(12, 2))

    create_label(
        pl_row,
        "P/L",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR,
        font=("Segoe UI", 10, "bold")
    ).pack(side="left")

    pl_label = create_label(
        pl_row,
        "$0.00",
        bg=GRAPH_COLOR,
        font=("Consolas", 10)
    )
    pl_label.pack(side="right")


    return_row = tk.Frame(panel, bg=GRAPH_COLOR)
    return_row.pack(fill="x", padx=15)

    create_label(
        return_row,
        "Return",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR,
        font=("Segoe UI", 10, "bold")
    ).pack(side="left")

    return_label = create_label(
        return_row,
        "0.00%",
        bg=GRAPH_COLOR,
        font=("Consolas", 10)
    )
    return_label.pack(side="right")

    buy = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )
    buy.pack(
        fill="x",
        padx=15,
        pady=(15, 5)
    )

    create_label(
        buy,
        "Buy",
        bg=GRAPH_COLOR
    ).pack(side="left")

    buy_entry = create_entry(
        buy,
        width=5
    )
    buy_entry.pack(
        side="left",
        padx=5
    )

    buy_button = create_button(
        buy,
        "BUY"
    )
    buy_button.pack(side="left")

    sell = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )
    sell.pack(
        fill="x",
        padx=15,
        pady=(0, 10)
    )

    create_label(
        sell,
        "Sell",
        bg=GRAPH_COLOR
    ).pack(side="left")

    sell_entry = create_entry(
        sell,
        width=5
    )
    sell_entry.pack(
        side="left",
        padx=5
    )

    sell_button = create_button(
        sell,
        "SELL"
    )
    sell_button.pack(side="left")

    return {
        "frame": panel,
        "cash": stat_labels["Cash"],
        "shares": stat_labels["Shares"],
        "invested": stat_labels["Invested"],
        "value": stat_labels["Value"],
        "pl": pl_label,
        "return": return_label,
        "buy_entry": buy_entry,
        "buy_button": buy_button,
        "sell_entry": sell_entry,
        "sell_button": sell_button,
    }