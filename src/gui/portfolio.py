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
        ("Cash", "$10,000"),
        ("Shares", "0"),
        ("Invested", "$0.00"),
        ("Value", "$10,000"),
    ]

    for label, value in stats:
        row = tk.Frame(panel, bg=GRAPH_COLOR)
        row.pack(fill="x", padx=15, pady=2)

        create_label(
            row,
            label,
            color=SECONDARY_TEXT,
            bg=GRAPH_COLOR
        ).pack(side="left")

        create_label(
            row,
            value,
            bg=GRAPH_COLOR
        ).pack(side="right")

    create_label(
        panel,
        "P/L        $0.00",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR
    ).pack(
        anchor="w",
        padx=15,
        pady=(12, 2)
    )

    create_label(
        panel,
        "Return     0.00%",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR
    ).pack(
        anchor="w",
        padx=15
    )

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

    create_entry(
        buy,
        width=5
    ).pack(
        side="left",
        padx=5
    )

    create_button(
        buy,
        "BUY"
    ).pack(side="left")

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

    create_entry(
        sell,
        width=5
    ).pack(
        side="left",
        padx=5
    )

    create_button(
        sell,
        "SELL"
    ).pack(side="left")

    return panel