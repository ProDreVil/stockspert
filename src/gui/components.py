import tkinter as tk
from tkinter import ttk

from config import (
    GRAPH_COLOR,
    PANEL_COLOR,
    SECONDARY_TEXT,
    TEXT_COLOR,
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
    return tk.Frame(parent, bg=bg)


def create_section(parent, title):
    section = tk.Frame(parent, bg=GRAPH_COLOR)

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


def create_button(
    parent,
    text,
    command=None,
    bg=GRAPH_COLOR,
    fg=TEXT_COLOR,
    **kwargs
):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        relief="flat",
        bd=0,
        font=("Segoe UI", 10),
        **kwargs
    )


def create_entry(parent, variable=None, **kwargs):
    return tk.Entry(
        parent,
        textvariable=variable,
        bg=GRAPH_COLOR,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief="flat",
        bd=0,
        font=("Segoe UI", 10),
        **kwargs
    )


def create_dropdown(parent, variable, values):
    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Stockspert.TCombobox",
        fieldbackground=GRAPH_COLOR,
        background=GRAPH_COLOR,
        foreground=TEXT_COLOR,
        arrowcolor=TEXT_COLOR,
        borderwidth=0,
        relief="flat"
    )

    style.map(
        "Stockspert.TCombobox",
        fieldbackground=[
            ("readonly", GRAPH_COLOR),
            ("focus", GRAPH_COLOR)
        ],
        foreground=[
            ("readonly", TEXT_COLOR),
            ("focus", TEXT_COLOR)
        ],
        selectbackground=[
            ("readonly", GRAPH_COLOR)
        ],
        selectforeground=[
            ("readonly", TEXT_COLOR)
        ]
    )

    return ttk.Combobox(
        parent,
        textvariable=variable,
        values=values,
        state="readonly",
        style="Stockspert.TCombobox",
        font=("Segoe UI", 10)
    )