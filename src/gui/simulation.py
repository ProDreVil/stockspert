import tkinter as tk

from config import (
    PANEL_COLOR,
    TEXT_COLOR,

    BUTTON_COLOR,
    BUTTON_BORDER_COLOR,
    BUTTON_TEXT_COLOR,

    NEXT_BUTTON_COLOR,
    NEXT_BUTTON_BORDER_COLOR,
    RANDOMIZE_BUTTON_COLOR,
    RANDOMIZE_BUTTON_BORDER_COLOR,
    RETURN_BUTTON_COLOR,
    RETURN_BUTTON_BORDER_COLOR,
    ADVANCE_BUTTON_COLOR,
    ADVANCE_BUTTON_BORDER_COLOR,
    AUTO_BUTTON_COLOR,
    AUTO_BUTTON_BORDER_COLOR,
    ADD_BUTTON_COLOR,
    ADD_BUTTON_BORDER_COLOR,

    RISE_BUTTON_COLOR,
    RISE_BUTTON_BORDER_COLOR,
    STABLE_BUTTON_COLOR,
    STABLE_BUTTON_BORDER_COLOR,
    FALL_BUTTON_COLOR,
    FALL_BUTTON_BORDER_COLOR,
    RESET_BUTTON_COLOR,
    RESET_BUTTON_BORDER_COLOR,
    RESET_BUTTON_TEXT_COLOR,
)

from gui.components import (
    create_entry,
    create_label,
    create_section,
)


def create_simulation_button(
    parent,
    text,
    command=None,
    width=10,
    bg=BUTTON_COLOR,
    border_color=BUTTON_BORDER_COLOR,
    text_color=BUTTON_TEXT_COLOR
):
    border = tk.Frame(
        parent,
        bg=border_color,
        padx=1,
        pady=1
    )

    button = tk.Button(
        border,
        text=text,
        command=command,
        width=width,
        bg=bg,
        fg=text_color,
        activebackground=bg,
        activeforeground=text_color,
        relief="flat",
        bd=0,
        highlightthickness=0,
        font=("Segoe UI", 10, "bold"),
        padx=6,
        pady=5
    )

    button.pack()

    return border


def build_simulation(parent, on_next=None, on_advance=None):

    frame = create_section(parent, "SIMULATION")

    # =========================
    # TOP ROW
    # =========================

    controls = tk.Frame(frame, bg=PANEL_COLOR)
    controls.pack(fill="x", padx=12, pady=(10, 4))

    controls.grid_columnconfigure(0, weight=1)
    controls.grid_columnconfigure(1, weight=1)

    # LEFT — NEXT / RANDOMIZE / RETURN

    left_top = tk.Frame(controls, bg=PANEL_COLOR)
    left_top.grid(row=0, column=0, sticky="w")

    create_simulation_button(
        left_top,
        "NEXT",
        command=on_next,
        bg=NEXT_BUTTON_COLOR,
        border_color=NEXT_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=2)

    create_simulation_button(
        left_top,
        "RANDOMIZE",
        bg=RANDOMIZE_BUTTON_COLOR,
        border_color=RANDOMIZE_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=2)

    create_simulation_button(
        left_top,
        "RETURN",
        bg=RETURN_BUTTON_COLOR,
        border_color=RETURN_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=2)

    # RIGHT — ADVANCE

    advance = tk.Frame(controls, bg=PANEL_COLOR)
    advance.grid(row=0, column=1, sticky="e")

    create_simulation_button(
        advance,
        "ADVANCE",
        command=on_advance,
        bg=ADVANCE_BUTTON_COLOR,
        border_color=ADVANCE_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=2)

    create_label(
        advance,
        "DAY:",
        font=("Segoe UI", 9, "bold")
    ).pack(side="left", padx=(8, 3))

    day_entry = create_entry(
        advance,
        width=5
    )
    day_entry.pack(side="left", padx=2)

    create_label(
        advance,
        "WEEK:",
        font=("Segoe UI", 9, "bold")
    ).pack(side="left", padx=(8, 3))

    week_entry = create_entry(
        advance,
        width=5
    )
    week_entry.pack(side="left", padx=2)

    create_label(
        advance,
        "MONTH:",
        font=("Segoe UI", 9, "bold")
    ).pack(side="left", padx=(8, 3))

    month_entry = create_entry(
        advance,
        width=5
    )
    month_entry.pack(side="left", padx=2)

    # =========================
    # SECOND ROW
    # =========================

    controls_bottom = tk.Frame(frame, bg=PANEL_COLOR)
    controls_bottom.pack(fill="x", padx=12, pady=(4, 10))

    controls_bottom.grid_columnconfigure(0, weight=1)
    controls_bottom.grid_columnconfigure(1, weight=1)

    # LEFT — RISE / STABLE / FALL

    left_bottom = tk.Frame(controls_bottom, bg=PANEL_COLOR)
    left_bottom.grid(row=0, column=0, sticky="w")

    create_simulation_button(
        left_bottom,
        "↗ RISE",
        bg=RISE_BUTTON_COLOR,
        border_color=RISE_BUTTON_BORDER_COLOR,
        text_color=RISE_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=2)

    create_simulation_button(
        left_bottom,
        "→ STABLE",
        bg=STABLE_BUTTON_COLOR,
        border_color=STABLE_BUTTON_BORDER_COLOR,
        text_color=STABLE_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=2)

    create_simulation_button(
        left_bottom,
        "↘ FALL",
        bg=FALL_BUTTON_COLOR,
        border_color=FALL_BUTTON_BORDER_COLOR,
        text_color=FALL_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=2)

    # RIGHT — AUTO / RESET

    auto = tk.Frame(controls_bottom, bg=PANEL_COLOR)
    auto.grid(row=0, column=1, sticky="e", padx=(0, 82))

    create_simulation_button(
        auto,
        "AUTO",
        bg=AUTO_BUTTON_COLOR,
        border_color=AUTO_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=2)

    create_label(
        auto,
        "SPEED:",
        font=("Segoe UI", 9, "bold")
    ).pack(side="left", padx=(8, 3))

    speed_entry = create_entry(
        auto,
        width=5
    )
    speed_entry.pack(side="left", padx=2)

    create_simulation_button(
        auto,
        "RESET",
        bg=RESET_BUTTON_COLOR,
        border_color=RESET_BUTTON_BORDER_COLOR,
        text_color=RESET_BUTTON_TEXT_COLOR
    ).pack(side="left", padx=(8, 2))

    # =========================
    # ADD CASH
    # =========================

    cash = tk.Frame(frame, bg=PANEL_COLOR)
    cash.pack(fill="x", padx=12, pady=(0, 10))

    create_label(
        cash,
        "ADD CASH:",
        font=("Segoe UI", 10, "bold")
    ).pack(side="left", padx=(0, 8))

    cash_entry = create_entry(
        cash,
        width=12
    )
    cash_entry.pack(side="left", padx=2)

    create_simulation_button(
        cash,
        "ADD",
        bg=ADD_BUTTON_COLOR,
        border_color=ADD_BUTTON_BORDER_COLOR
    ).pack(side="left", padx=26)

    return {
        "frame": frame,
        "day_entry": day_entry,
        "week_entry": week_entry,
        "month_entry": month_entry,
        "speed_entry": speed_entry,
        "cash_entry": cash_entry
    }