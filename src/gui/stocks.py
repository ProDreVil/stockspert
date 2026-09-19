import tkinter as tk

from config import (
    GRAPH_COLOR,
    SECONDARY_TEXT,
)
from gui.components import (
    create_label,
    create_section,
)


def build_market(parent, on_apply=None, initial_price=100.00):
    panel = create_section(parent, "MARKET INFORMATION")

    price_var = tk.StringVar(value=f"${initial_price:.2f}")
    change_var = tk.StringVar(value="+$0.00 (+0.00%)")
    trend_var = tk.StringVar(value="Uptrend")
    trend_change_var = tk.StringVar(value="+0.00%")
    pe_var = tk.StringVar(value="Fair")
    pe_value_var = tk.StringVar(value="18.7")
    revenue_var = tk.StringVar(value="Positive")
    revenue_value_var = tk.StringVar(value="+6.2%")
    earnings_var = tk.StringVar(value="Positive")
    earnings_value_var = tk.StringVar(value="+8.4%")
    volume_var = tk.StringVar(value="Average")
    volume_value_var = tk.StringVar(value="1.24M")
    updated_var = tk.StringVar(value="January 1, 2026")

    labels = {}

    def create_market_row(
        parent_frame,
        name,
        label,
        value_var,
        classification_var=None
    ):
        row = tk.Frame(
            parent_frame,
            bg=GRAPH_COLOR
        )
        row.pack(fill="x", pady=2)

        row.grid_columnconfigure(0, minsize=100)
        row.grid_columnconfigure(1, minsize=100)
        row.grid_columnconfigure(2, minsize=100)

        create_label(
            row,
            label,
            color=SECONDARY_TEXT,
            bg=GRAPH_COLOR,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        value_label = create_label(
            row,
            textvariable=value_var,
            bg=GRAPH_COLOR,
            font=("Consolas", 10, "bold")
        )

        value_label.grid(
            row=0,
            column=1,
            sticky="e"
        )

        classification_label = None

        if classification_var:
            classification_label = create_label(
                row,
                textvariable=classification_var,
                bg=GRAPH_COLOR,
                font=("Consolas", 10, "bold")
            )

            classification_label.grid(
                row=0,
                column=2,
                sticky="e"
            )

        labels[name] = {
            "value": value_label,
            "classification": classification_label
        }

    def create_group(pady):
        group = tk.Frame(
            panel,
            bg=GRAPH_COLOR
        )
        group.pack(
            fill="x",
            padx=15,
            pady=pady
        )
        return group

    price_group = create_group((5, 8))

    price_row = tk.Frame(
        price_group,
        bg=GRAPH_COLOR
    )
    price_row.pack(fill="x", pady=2)

    price_row.grid_columnconfigure(0, minsize=100)
    price_row.grid_columnconfigure(1, minsize=100)
    price_row.grid_columnconfigure(2, minsize=100)

    create_label(
        price_row,
        "Price",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR,
        font=("Segoe UI", 10, "bold")
    ).grid(row=0, column=0, sticky="w")

    create_label(
        price_row,
        textvariable=price_var,
        bg=GRAPH_COLOR,
        font=("Consolas", 10, "bold")
    ).grid(row=0, column=2, sticky="e")

    change_row = tk.Frame(
        price_group,
        bg=GRAPH_COLOR
    )
    change_row.pack(fill="x", pady=2)

    change_row.grid_columnconfigure(0, minsize=100)
    change_row.grid_columnconfigure(1, minsize=100)
    change_row.grid_columnconfigure(2, minsize=100)

    create_label(
        change_row,
        "Change",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR,
        font=("Segoe UI", 10, "bold")
    ).grid(row=0, column=0, sticky="w")

    create_label(
        change_row,
        textvariable=change_var,
        bg=GRAPH_COLOR,
        font=("Consolas", 10, "bold")
    ).grid(row=0, column=2, sticky="e")

    market_group = create_group(8)

    create_market_row(
        market_group,
        "trend",
        "Trend",
        trend_change_var,
        trend_var
    )

    create_market_row(
        market_group,
        "pe",
        "P/E",
        pe_value_var,
        pe_var
    )

    create_market_row(
        market_group,
        "revenue",
        "Revenue",
        revenue_value_var,
        revenue_var
    )

    create_market_row(
        market_group,
        "earnings",
        "Earnings",
        earnings_value_var,
        earnings_var
    )

    create_market_row(
        market_group,
        "volume",
        "Volume",
        volume_value_var,
        volume_var
    )

    return {
        "frame": panel,
        "price_var": price_var,
        "change_var": change_var,
        "trend_var": trend_var,
        "trend_change_var": trend_change_var,
        "pe_var": pe_var,
        "pe_value_var": pe_value_var,
        "revenue_var": revenue_var,
        "revenue_value_var": revenue_value_var,
        "earnings_var": earnings_var,
        "earnings_value_var": earnings_value_var,
        "volume_var": volume_var,
        "volume_value_var": volume_value_var,
        "updated_var": updated_var,
        "labels": labels,
    }