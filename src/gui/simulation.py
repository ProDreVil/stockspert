import tkinter as tk

from config import GRAPH_COLOR
from gui.components import (
    create_button,
    create_dropdown,
    create_entry,
    create_label,
    create_section,
)


def build_simulation(parent, on_next=None):

    panel = create_section(parent, "SIMULATION")

    top = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )

    top.pack(
        padx=15,
        pady=(10, 15)
    )

    create_label(
        top,
        "Advance",
        bg=GRAPH_COLOR
    ).pack(side="left")

    create_entry(
        top,
        width=5
    ).pack(
        side="left",
        padx=5
    )

    create_dropdown(
        top,
        tk.StringVar(value="Day"),
        ["Day", "Week", "Month", "Year"]
    ).pack(side="left")

    create_button(
        panel,
        "NEXT",
        command=on_next,
        width=14
    ).pack(pady=(5, 8))

    create_button(
        panel,
        "RANDOM",
        width=14
    ).pack()

    return panel