import tkinter as tk
from gui.components import create_section, create_label, create_entry, create_dropdown, create_button

def build_simulation(parent):
    panel = create_section(parent, "SIMULATION")

    top = tk.Frame(panel, bg="#181818")
    top.pack(padx=15, pady=(10,15))

    create_label(top, "Advance", bg="#181818").pack(side="left")
    create_entry(top, width=5).pack(side="left", padx=5)

    create_dropdown(
        top,
        tk.StringVar(value="Day"),
        ["Day", "Week", "Month", "Year"]
    ).pack(side="left")

    create_button(panel, "NEXT", width=14).pack(pady=(5,8))
    create_button(panel, "RANDOM", width=14).pack()

    return panel