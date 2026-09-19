import tkinter as tk

from config import (
    PANEL_COLOR,
    INPUT_COLOR,
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
    border.button = button

    return border


def build_simulation(
        parent,
        on_next=None,
        on_advance=None,
        on_return=None,
        on_randomize=None,
        on_reset=None,
        on_rise=None,
        on_stable=None,
        on_fall=None,
        on_auto=None
    ):

    frame = create_section(parent, "SIMULATION")

    # =========================
    # FIRST ROW
    # =========================

    controls = tk.Frame(
        frame,
        bg=PANEL_COLOR
    )

    controls.pack(
        fill="x",
        padx=12,
        pady=(10, 4)
    )

    controls.grid_columnconfigure(0, weight=0)
    controls.grid_columnconfigure(1, weight=0)

    left_top = tk.Frame(
        controls,
        bg=PANEL_COLOR
    )

    left_top.grid(
        row=0,
        column=0,
        sticky="w"
    )

    create_simulation_button(
        left_top,
        "NEXT",
        command=on_next,
        bg=NEXT_BUTTON_COLOR,
        border_color=NEXT_BUTTON_BORDER_COLOR
    ).pack(
        side="left",
        padx=2
    )

    create_simulation_button(
        left_top,
        "RANDOMIZE",
        command=on_randomize,
        bg=RANDOMIZE_BUTTON_COLOR,
        border_color=RANDOMIZE_BUTTON_BORDER_COLOR
    ).pack(
        side="left",
        padx=2
    )

    create_simulation_button(
        left_top,
        "RETURN",
        command=on_return,
        bg=RETURN_BUTTON_COLOR,
        border_color=RETURN_BUTTON_BORDER_COLOR
    ).pack(
        side="left",
        padx=2
    )

    advance = tk.Frame(
        controls,
        bg=PANEL_COLOR
    )

    advance.grid(
        row=0,
        column=1,
        sticky="e",
        padx=(20, 0)
    )

    create_simulation_button(
        advance,
        "ADVANCE",
        command=on_advance,
        bg=ADVANCE_BUTTON_COLOR,
        border_color=ADVANCE_BUTTON_BORDER_COLOR
    ).pack(
        side="left",
        padx=2
    )

    create_label(
        advance,
        "DAY:",
        font=("Segoe UI", 9, "bold")
    ).pack(
        side="left",
        padx=(8, 3)
    )

    day_entry = create_entry(
        advance,
        width=5
    )

    day_entry.configure(
        font=("Consolas", 10, "bold")
    )

    day_entry.pack(
        side="left",
        padx=2
    )

    create_label(
        advance,
        "WEEK:",
        font=("Segoe UI", 9, "bold")
    ).pack(
        side="left",
        padx=(8, 3)
    )

    week_entry = create_entry(
        advance,
        width=5
    )

    week_entry.configure(
        font=("Consolas", 10, "bold")
    )

    week_entry.pack(
        side="left",
        padx=2
    )

    create_label(
        advance,
        "MONTH:",
        font=("Segoe UI", 9, "bold")
    ).pack(
        side="left",
        padx=(8, 3)
    )

    month_entry = create_entry(
        advance,
        width=5
    )

    month_entry.configure(
        font=("Consolas", 10, "bold")
    )

    month_entry.pack(
        side="left",
        padx=2
    )

    # =========================
    # SECOND ROW
    # =========================

    controls_bottom = tk.Frame(
        frame,
        bg=PANEL_COLOR
    )

    controls_bottom.pack(
        fill="x",
        padx=12,
        pady=(4, 10)
    )

    controls_bottom.grid_columnconfigure(0, weight=0)
    controls_bottom.grid_columnconfigure(1, weight=0)

    left_bottom = tk.Frame(
        controls_bottom,
        bg=PANEL_COLOR
    )

    left_bottom.grid(
        row=0,
        column=0,
        sticky="w"
    )

    create_simulation_button(
        left_bottom,
        "↗ RISE",
        command=on_rise,
        bg=RISE_BUTTON_COLOR,
        border_color=RISE_BUTTON_BORDER_COLOR,
        text_color=RISE_BUTTON_BORDER_COLOR
    ).pack(
        side="left",
        padx=2
    )

    create_simulation_button(
        left_bottom,
        "→ STABLE",
        command=on_stable,
        bg=STABLE_BUTTON_COLOR,
        border_color=STABLE_BUTTON_BORDER_COLOR,
        text_color=STABLE_BUTTON_BORDER_COLOR
    ).pack(
        side="left",
        padx=2
    )

    create_simulation_button(
        left_bottom,
        "↘ FALL",
        command=on_fall,
        bg=FALL_BUTTON_COLOR,
        border_color=FALL_BUTTON_BORDER_COLOR,
        text_color=FALL_BUTTON_BORDER_COLOR
    ).pack(
        side="left",
        padx=2
    )

    auto = tk.Frame(
        controls_bottom,
        bg=PANEL_COLOR
    )

    auto.grid(
        row=0,
        column=1,
        sticky="e",
        padx=(20, 0)
    )

    auto_button = create_simulation_button(
        auto,
        "AUTO",
        command=on_auto,
        bg=AUTO_BUTTON_COLOR,
        border_color=AUTO_BUTTON_BORDER_COLOR
    )

    auto_button.pack(
        side="left",
        padx=2
    )

    create_label(
        auto,
        "SPEED:",
        font=("Segoe UI", 9, "bold")
    ).pack(
        side="left",
        padx=(8, 3)
    )

    speed_entry = create_entry(
        auto,
        width=5
    )

    speed_entry.configure(
        font=("Consolas", 10, "bold")
    )

    speed_entry.pack(
        side="left",
        padx=2
    )

    auto_progress = tk.Canvas(
        auto,
        width=120,
        height=8,
        bg=INPUT_COLOR,
        highlightthickness=0
    )

    auto_progress.pack(
        side="left",
        padx=(8, 2)
    )

    # =========================
    # THIRD ROW
    # =========================

    cash = tk.Frame(
        frame,
        bg=PANEL_COLOR
    )

    cash.pack(
        fill="x",
        padx=12,
        pady=(0, 10)
    )

    cash.grid_columnconfigure(0, weight=0)
    cash.grid_columnconfigure(1, weight=0)

    cash_left = tk.Frame(
        cash,
        bg=PANEL_COLOR
    )

    cash_left.grid(
        row=0,
        column=0,
        sticky="w"
    )

    create_label(
        cash_left,
        "ADD CASH:",
        font=("Segoe UI", 10, "bold")
    ).pack(
        side="left",
        padx=(0, 7)
    )

    cash_entry = create_entry(
        cash_left,
        width=12
    )

    cash_entry.configure(
        font=("Consolas", 10, "bold")
    )

    cash_entry.pack(
        side="left",
        padx=(0, 2)
    )

    create_simulation_button(
        cash_left,
        "ADD",
        bg=ADD_BUTTON_COLOR,
        border_color=ADD_BUTTON_BORDER_COLOR
    ).pack(
        side="left",
        padx=(30, 24)
    )

    create_simulation_button(
        cash,
        "RESET",
        command=on_reset,
        bg=RESET_BUTTON_COLOR,
        border_color=RESET_BUTTON_BORDER_COLOR,
        text_color=RESET_BUTTON_TEXT_COLOR
    ).grid(
        row=0,
        column=1,
        sticky="n",
        pady=0
    )

    return {
        "frame": frame,
        "day_entry": day_entry,
        "week_entry": week_entry,
        "month_entry": month_entry,
        "speed_entry": speed_entry,
        "cash_entry": cash_entry,
        "auto_progress": auto_progress,
        "auto_button": auto_button,
    }