import tkinter as tk

from config import (
    GRAPH_COLOR,
    SECONDARY_TEXT,
    BUY_COLOR,
    SELL_COLOR,
    TEXT_COLOR,
)

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

    pl_row = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )

    pl_row.pack(
        fill="x",
        padx=15,
        pady=(12, 2)
    )

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

    return_row = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )

    return_row.pack(
        fill="x",
        padx=15
    )

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

    trade = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )

    trade.pack(
        fill="x",
        padx=15,
        pady=(12, 10)
    )

    quantity_row = tk.Frame(
        trade,
        bg=GRAPH_COLOR
    )

    quantity_row.pack(
        pady=(0, 6)
    )

    create_label(
        quantity_row,
        "Quantity:",
        bg=GRAPH_COLOR,
        font=("Segoe UI", 10, "bold")
    ).pack(
        side="left"
    )

    quantity_entry = create_entry(
        quantity_row,
        width=7
    )

    quantity_entry.configure(
        font=("Consolas", 10, "bold")
    )

    quantity_entry.pack(
        side="left",
        padx=(6, 0)
    )

    buttons = tk.Frame(
        trade,
        bg=GRAPH_COLOR
    )

    buttons.pack(
        pady=(0, 2)
    )

    buy_button = create_button(
        buttons,
        "BUY"
    )

    buy_button.configure(
        bg=BUY_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 10, "bold")
    )

    buy_button.pack(
        side="left",
        padx=(0, 6),
        ipadx=10
    )

    sell_button = create_button(
        buttons,
        "SELL"
    )

    sell_button.configure(
        bg=SELL_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 10, "bold")
    )

    sell_button.pack(
        side="left",
        padx=(6, 0),
        ipadx=10
    )

    return {
        "frame": panel,
        "cash": stat_labels["Cash"],
        "shares": stat_labels["Shares"],
        "invested": stat_labels["Invested"],
        "value": stat_labels["Value"],
        "pl": pl_label,
        "return": return_label,
        "quantity_entry": quantity_entry,
        "buy_button": buy_button,
        "sell_button": sell_button,
    }