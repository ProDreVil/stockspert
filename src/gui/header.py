import tkinter as tk

from config import BG_COLOR, SECONDARY_TEXT, ACCENT_COLOR
from gui.components import create_label


def build_header(parent, date_text):
    header = tk.Frame(parent, bg=BG_COLOR)

    top = tk.Frame(header, bg=BG_COLOR)
    top.pack(fill="x")

    create_label(
        top,
        "STOCKSPERT",
        font=("Segoe UI", 20, "bold"),
        color=ACCENT_COLOR,
        bg=BG_COLOR
    ).pack(side="left")

    date_label = create_label(
        top,
        date_text,
        font=("Consolas", 10),
        color=SECONDARY_TEXT,
        bg=BG_COLOR
    )
    date_label.pack(side="right")

    simulation_day_label = create_label(
        header,
        "Day 1",
        font=("Consolas", 9),
        color=SECONDARY_TEXT,
        bg=BG_COLOR
    )
    simulation_day_label.pack(anchor="e", pady=(2, 0))

    create_label(
        header,
        "Stock Market Expert System & Simulation",
        font=("Consolas", 10),
        color=SECONDARY_TEXT,
        bg=BG_COLOR
    ).pack(anchor="w", pady=(2, 0))

    return header, date_label, simulation_day_label