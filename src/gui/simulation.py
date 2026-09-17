import tkinter as tk

from config import GRAPH_COLOR
from gui.components import (
    create_button,
    create_entry,
    create_label,
    create_section,
)


def build_simulation(parent, on_next=None, on_advance=None):
    panel = create_section(parent, "SIMULATION")

    top = tk.Frame(panel, bg=GRAPH_COLOR)
    top.pack(padx=15, pady=(10, 15))

    create_label(
        top,
        "Advance",
        bg=GRAPH_COLOR
    ).pack(side="left")

    create_label(
        top,
        "Day",
        bg=GRAPH_COLOR
    ).pack(side="left", padx=(15, 5))

    day_entry = create_entry(top, width=4)
    day_entry.pack(side="left")

    create_label(
        top,
        "Week",
        bg=GRAPH_COLOR
    ).pack(side="left", padx=(10, 5))

    week_entry = create_entry(top, width=4)
    week_entry.pack(side="left")

    create_label(
        top,
        "Month",
        bg=GRAPH_COLOR
    ).pack(side="left", padx=(10, 5))

    month_entry = create_entry(top, width=4)
    month_entry.pack(side="left")

    actions = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )
    actions.pack(pady=(5, 8))

    create_button(
        actions,
        "NEXT",
        command=on_next,
        width=12
    ).pack(side="left", padx=4)

    create_button(
        actions,
        "ADVANCE",
        command=on_advance,
        width=12
    ).pack(side="left", padx=4)

    create_button(
        actions,
        "RANDOMIZE",
        width=12
    ).pack(side="left", padx=4)

    direction = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )
    direction.pack(pady=(0, 8))

    create_button(
        direction,
        "↗ RISE",
        width=12
    ).pack(side="left", padx=4)

    create_button(
        direction,
        "→ STABLE",
        width=12
    ).pack(side="left", padx=4)

    create_button(
        direction,
        "↘ FALL",
        width=12
    ).pack(side="left", padx=4)

    cash = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )
    cash.pack(pady=(0, 10))

    create_label(
        cash,
        "Add Cash",
        bg=GRAPH_COLOR
    ).pack(side="left")

    create_entry(
        cash,
        width=10
    ).pack(side="left", padx=5)

    create_button(
        cash,
        "ADD",
        width=8
    ).pack(side="left", padx=4)

    create_button(
        cash,
        "RESET",
        width=8
    ).pack(side="left", padx=4)

    return {
        "frame": panel,
        "day_entry": day_entry,
        "week_entry": week_entry,
        "month_entry": month_entry
    }