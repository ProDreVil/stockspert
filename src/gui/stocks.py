import tkinter as tk

from config import GRAPH_COLOR, SECONDARY_TEXT
from gui.components import (
    create_button,
    create_dropdown,
    create_entry,
    create_label,
    create_section,
)


def build_market(parent, on_apply=None):
    panel = create_section(parent, "MARKET INFORMATION")

    price_var = tk.StringVar(value="100.00")
    trend_var = tk.StringVar(value="Uptrend")
    pe_var = tk.StringVar(value="Low")
    revenue_var = tk.StringVar(value="Positive")
    earnings_var = tk.StringVar(value="Positive")
    volume_var = tk.StringVar(value="Average")

    inputs = [
        ("Price", price_var, None),
        ("Trend", trend_var, ["Uptrend", "Sideways", "Downtrend"]),
        ("P/E", pe_var, ["Low", "Fair", "High"]),
        ("Revenue", revenue_var, ["Positive", "Neutral", "Negative"]),
        ("Earnings", earnings_var, ["Positive", "Negative"]),
        ("Volume", volume_var, ["Low", "Average", "High"]),
    ]

    def apply_changes(*args):
        if on_apply:
            on_apply(
                price_var.get(),
                trend_var.get(),
                pe_var.get(),
                revenue_var.get(),
                earnings_var.get(),
                volume_var.get()
            )

    price_var.trace_add("write", apply_changes)
    trend_var.trace_add("write", apply_changes)
    pe_var.trace_add("write", apply_changes)
    revenue_var.trace_add("write", apply_changes)
    earnings_var.trace_add("write", apply_changes)
    volume_var.trace_add("write", apply_changes)

    for label, variable, values in inputs:
        row = tk.Frame(panel, bg=GRAPH_COLOR)
        row.pack(fill="x", padx=15, pady=2)

        create_label(
            row,
            label,
            color=SECONDARY_TEXT,
            bg=GRAPH_COLOR
        ).pack(side="left")

        if values:
            create_dropdown(
                row,
                variable,
                values
            ).pack(side="right")
        else:
            create_entry(
                row,
                variable=variable,
                width=12
            ).pack(side="right")

    return panel