import tkinter as tk

from config import BG_COLOR, SECONDARY_TEXT
from gui.components import create_label


def build_header(parent, date_text):
    header = tk.Frame(parent, bg=BG_COLOR)

    top = tk.Frame(header, bg=BG_COLOR)
    top.pack(fill="x")

    create_label(
        top,
        "STOCKSPERT",
        font=("Segoe UI", 20, "bold"),
        bg=BG_COLOR
    ).pack(side="left")

    date_label = create_label(
        top,
        date_text,
        font=("Segoe UI", 10),
        color=SECONDARY_TEXT,
        bg=BG_COLOR
    )
    date_label.pack(side="right")

    create_label(
        header,
        "Stock Market Expert System",
        font=("Segoe UI", 10),
        color=SECONDARY_TEXT,
        bg=BG_COLOR
    ).pack(anchor="w", pady=(2, 0))

    return header, date_label