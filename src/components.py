import tkinter as tk
from tkinter import ttk

from config import (
    PANEL_COLOR,
    GRAPH_COLOR,
    TEXT_COLOR,
    SECONDARY_TEXT,
)


def create_label(
    parent,
    text,
    font=("Segoe UI", 10),
    color=TEXT_COLOR,
    bg=PANEL_COLOR,
    **kwargs
):
    return tk.Label(
        parent,
        text=text,
        font=font,
        fg=color,
        bg=bg,
        **kwargs
    )


def create_panel(parent, bg=PANEL_COLOR):
    return tk.Frame(
        parent,
        bg=bg
    )


def create_section(parent, title):
    section = tk.Frame(
        parent,
        bg=GRAPH_COLOR
    )

    create_label(
        section,
        title,
        font=("Segoe UI", 9, "bold"),
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR
    ).pack(
        anchor="w",
        padx=15,
        pady=(12, 8)
    )

    return section


def create_dropdown(parent, variable, values):
    style = ttk.Style()

    style.configure(
        "Stockspert.TCombobox",
        fieldbackground=GRAPH_COLOR,
        background=GRAPH_COLOR,
        foreground=TEXT_COLOR,
        arrowcolor=TEXT_COLOR,
        borderwidth=0
    )

    style.map(
        "Stockspert.TCombobox",
        fieldbackground=[
            ("readonly", GRAPH_COLOR)
        ],
        foreground=[
            ("readonly", TEXT_COLOR)
        ]
    )

    dropdown = ttk.Combobox(
        parent,
        textvariable=variable,
        values=values,
        state="readonly",
        style="Stockspert.TCombobox",
        font=("Segoe UI", 10)
    )

    return dropdown