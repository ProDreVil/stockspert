import tkinter as tk
from tkinter import ttk
import subprocess
from pathlib import Path
import re
import random
from datetime import datetime, timedelta

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# --------------------------------------------------
# Colors
# --------------------------------------------------

BG_COLOR = "#121212"
PANEL_COLOR = "#1E1E1E"
INPUT_COLOR = "#2A2A2A"
TEXT_COLOR = "#EAEAEA"
SECONDARY_TEXT = "#AAAAAA"

ACCENT_COLOR = "#4A90E2"
BUY_COLOR = "#4CAF50"
HOLD_COLOR = "#FFC107"
SELL_COLOR = "#F44336"


# --------------------------------------------------
# CLIPS Configuration
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

CLIPS_PATH = r"C:\Program Files\CLIPS 6.31\CLIPSDOS64.exe"
CLIPS_FILE = BASE_DIR / "main.clp"


# --------------------------------------------------
# Simulation State
# --------------------------------------------------

current_date = datetime(2026, 1, 1)

current_price = 100.00

cash = 10000.00
shares = 0

price_history = [current_price]
date_history = [current_date]


# --------------------------------------------------
# Main Window
# --------------------------------------------------

root = tk.Tk()

root.title("Stock Market Expert System")
root.geometry("1100x850")
root.configure(bg=BG_COLOR)
root.resizable(False, False)


# --------------------------------------------------
# Styles
# --------------------------------------------------

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Dark.TCombobox",
    fieldbackground=INPUT_COLOR,
    background=INPUT_COLOR,
    foreground=TEXT_COLOR,
    arrowcolor=TEXT_COLOR,
    borderwidth=0
)

style.map(
    "Dark.TCombobox",
    fieldbackground=[("readonly", INPUT_COLOR)],
    foreground=[("readonly", TEXT_COLOR)]
)


# --------------------------------------------------
# Variables
# --------------------------------------------------

trend_var = tk.StringVar(value="Uptrend")
pe_var = tk.StringVar(value="Low")
revenue_var = tk.StringVar(value="Positive")
earnings_var = tk.StringVar(value="Positive")
volume_var = tk.StringVar(value="Average")

price_var = tk.StringVar(value="100.00")

time_amount_var = tk.StringVar(value="1")
time_unit_var = tk.StringVar(value="Day")

manual_mode = False


# --------------------------------------------------
# Header
# --------------------------------------------------

header = tk.Frame(root, bg=BG_COLOR)
header.pack(fill="x", padx=40, pady=(25, 10))

title = tk.Label(
    header,
    text="STOCK MARKET EXPERT SYSTEM",
    font=("Segoe UI", 18, "bold"),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
title.pack()

date_label = tk.Label(
    header,
    text="January 1, 2026",
    font=("Segoe UI", 10),
    fg=SECONDARY_TEXT,
    bg=BG_COLOR
)
date_label.pack(pady=(3, 0))


# --------------------------------------------------
# Main Content
# --------------------------------------------------

content = tk.Frame(root, bg=BG_COLOR)
content.pack(fill="both", expand=True, padx=40)


# --------------------------------------------------
# Left Column
# --------------------------------------------------

left_column = tk.Frame(content, bg=BG_COLOR)
left_column.pack(side="left", fill="both", expand=True, padx=(0, 10))


# --------------------------------------------------
# Graph Panel
# --------------------------------------------------

graph_panel = tk.Frame(
    left_column,
    bg=PANEL_COLOR
)
graph_panel.pack(fill="both", expand=True)

graph_title = tk.Label(
    graph_panel,
    text="PRICE HISTORY",
    font=("Segoe UI", 11, "bold"),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR
)
graph_title.pack(anchor="w", padx=20, pady=(15, 5))


figure = Figure(
    figsize=(6, 3.5),
    dpi=100,
    facecolor=PANEL_COLOR
)

axis = figure.add_subplot(111)
axis.set_facecolor(PANEL_COLOR)

axis.tick_params(
    colors=SECONDARY_TEXT
)

axis.set_xlabel(
    "Date",
    color=SECONDARY_TEXT
)

axis.set_ylabel(
    "Price",
    color=SECONDARY_TEXT
)

for spine in axis.spines.values():
    spine.set_color("#444444")


line, = axis.plot(
    date_history,
    price_history,
    linewidth=2
)


canvas = FigureCanvasTkAgg(
    figure,
    master=graph_panel
)

canvas.draw()

canvas.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)


# --------------------------------------------------
# Market Status Panel
# --------------------------------------------------

status_panel = tk.Frame(
    left_column,
    bg=PANEL_COLOR
)

status_panel.pack(
    fill="x",
    pady=(10, 0)
)


price_title = tk.Label(
    status_panel,
    text="CURRENT PRICE",
    font=("Segoe UI", 9, "bold"),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR
)

price_title.grid(
    row=0,
    column=0,
    sticky="w",
    padx=20,
    pady=(12, 0)
)


price_display = tk.Label(
    status_panel,
    text="$100.00",
    font=("Segoe UI", 22, "bold"),
    fg=TEXT_COLOR,
    bg=PANEL_COLOR
)

price_display.grid(
    row=1,
    column=0,
    sticky="w",
    padx=20,
    pady=(0, 12)
)


# --------------------------------------------------
# Portfolio Panel
# --------------------------------------------------

portfolio_panel = tk.Frame(
    left_column,
    bg=PANEL_COLOR
)

portfolio_panel.pack(
    fill="x",
    pady=(10, 0)
)


portfolio_title = tk.Label(
    portfolio_panel,
    text="PORTFOLIO",
    font=("Segoe UI", 11, "bold"),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR
)

portfolio_title.pack(
    anchor="w",
    padx=20,
    pady=(12, 5)
)


portfolio_values = tk.Frame(
    portfolio_panel,
    bg=PANEL_COLOR
)

portfolio_values.pack(
    fill="x",
    padx=20,
    pady=(0, 12)
)


cash_label = tk.Label(
    portfolio_values,
    text="Cash\n$10,000.00",
    font=("Segoe UI", 10),
    fg=TEXT_COLOR,
    bg=PANEL_COLOR,
    justify="left"
)

cash_label.pack(
    side="left",
    expand=True,
    anchor="w"
)


shares_label = tk.Label(
    portfolio_values,
    text="Shares\n0",
    font=("Segoe UI", 10),
    fg=TEXT_COLOR,
    bg=PANEL_COLOR,
    justify="left"
)

shares_label.pack(
    side="left",
    expand=True,
    anchor="w"
)


portfolio_label = tk.Label(
    portfolio_values,
    text="Portfolio Value\n$10,000.00",
    font=("Segoe UI", 10),
    fg=TEXT_COLOR,
    bg=PANEL_COLOR,
    justify="left"
)

portfolio_label.pack(
    side="left",
    expand=True,
    anchor="w"
)


# --------------------------------------------------
# Trading Buttons
# --------------------------------------------------

trade_frame = tk.Frame(
    portfolio_panel,
    bg=PANEL_COLOR
)

trade_frame.pack(
    fill="x",
    padx=20,
    pady=(0, 15)
)


def buy_stock():
    global cash, shares

    if cash >= current_price:
        shares += 1
        cash -= current_price

    update_portfolio()


def sell_stock():
    global cash, shares

    if shares > 0:
        shares -= 1
        cash += current_price

    update_portfolio()


buy_button = tk.Button(
    trade_frame,
    text="BUY 1 SHARE",
    command=buy_stock,
    font=("Segoe UI", 9, "bold"),
    fg="white",
    bg=BUY_COLOR,
    relief="flat",
    padx=15,
    pady=7
)

buy_button.pack(
    side="left",
    padx=(0, 8)
)


sell_button = tk.Button(
    trade_frame,
    text="SELL 1 SHARE",
    command=sell_stock,
    font=("Segoe UI", 9, "bold"),
    fg="white",
    bg=SELL_COLOR,
    relief="flat",
    padx=15,
    pady=7
)

sell_button.pack(
    side="left"
)


# --------------------------------------------------
# Right Column
# --------------------------------------------------

right_column = tk.Frame(
    content,
    bg=BG_COLOR,
    width=350
)

right_column.pack(
    side="right",
    fill="y"
)

right_column.pack_propagate(False)


# --------------------------------------------------
# Market Information
# --------------------------------------------------

market_panel = tk.Frame(
    right_column,
    bg=PANEL_COLOR
)

market_panel.pack(
    fill="x"
)


market_title = tk.Label(
    market_panel,
    text="MARKET INFORMATION",
    font=("Segoe UI", 11, "bold"),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR
)

market_title.pack(
    anchor="w",
    padx=20,
    pady=(15, 10)
)


def create_dropdown(parent, label, variable, values):
    container = tk.Frame(
        parent,
        bg=PANEL_COLOR
    )

    container.pack(
        fill="x",
        padx=20,
        pady=4
    )

    label_widget = tk.Label(
        container,
        text=label,
        font=("Segoe UI", 9, "bold"),
        fg=TEXT_COLOR,
        bg=PANEL_COLOR,
        anchor="w"
    )

    label_widget.pack(
        fill="x",
        pady=(0, 4)
    )

    dropdown = ttk.Combobox(
        container,
        textvariable=variable,
        values=values,
        state="readonly",
        style="Dark.TCombobox",
        font=("Segoe UI", 9)
    )

    dropdown.pack(
        fill="x",
        ipady=3
    )

    return dropdown


def create_price_input(parent):
    container = tk.Frame(
        parent,
        bg=PANEL_COLOR
    )

    container.pack(
        fill="x",
        padx=20,
        pady=4
    )

    label = tk.Label(
        container,
        text="Stock Price",
        font=("Segoe UI", 9, "bold"),
        fg=TEXT_COLOR,
        bg=PANEL_COLOR
    )

    label.pack(
        fill="x",
        pady=(0, 4)
    )

    entry = tk.Entry(
        container,
        textvariable=price_var,
        font=("Segoe UI", 9),
        bg=INPUT_COLOR,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief="flat"
    )

    entry.pack(
        fill="x",
        ipady=5
    )

    return entry


price_entry = create_price_input(market_panel)

create_dropdown(
    market_panel,
    "Stock Trend",
    trend_var,
    ["Uptrend", "Sideways", "Downtrend"]
)

create_dropdown(
    market_panel,
    "P/E Ratio",
    pe_var,
    ["Low", "Fair", "High"]
)

create_dropdown(
    market_panel,
    "Revenue Growth",
    revenue_var,
    ["Positive", "Neutral", "Negative"]
)

create_dropdown(
    market_panel,
    "Earnings Growth",
    earnings_var,
    ["Positive", "Negative"]
)

create_dropdown(
    market_panel,
    "Trading Volume",
    volume_var,
    ["Low", "Average", "High"]
)


# --------------------------------------------------
# Manual Editor
# --------------------------------------------------

manual_apply_button = tk.Button(
    market_panel,
    text="APPLY MARKET CHANGES",
    command=lambda: apply_manual_changes(),
    font=("Segoe UI", 9, "bold"),
    fg="white",
    bg=ACCENT_COLOR,
    relief="flat",
    padx=10,
    pady=7
)

manual_apply_button.pack(
    fill="x",
    padx=20,
    pady=(10, 15)
)


# --------------------------------------------------
# Simulation Controls
# --------------------------------------------------

simulation_panel = tk.Frame(
    right_column,
    bg=PANEL_COLOR
)

simulation_panel.pack(
    fill="x",
    pady=(10, 0)
)


simulation_title = tk.Label(
    simulation_panel,
    text="SIMULATION",
    font=("Segoe UI", 11, "bold"),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR
)

simulation_title.pack(
    anchor="w",
    padx=20,
    pady=(15, 10)
)


time_frame = tk.Frame(
    simulation_panel,
    bg=PANEL_COLOR
)

time_frame.pack(
    fill="x",
    padx=20
)


tk.Label(
    time_frame,
    text="Skip",
    font=("Segoe UI", 9),
    fg=TEXT_COLOR,
    bg=PANEL_COLOR
).pack(
    side="left"
)


time_entry = tk.Entry(
    time_frame,
    textvariable=time_amount_var,
    width=6,
    font=("Segoe UI", 9),
    bg=INPUT_COLOR,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief="flat"
)

time_entry.pack(
    side="left",
    padx=8,
    ipady=4
)


time_dropdown = ttk.Combobox(
    time_frame,
    textvariable=time_unit_var,
    values=["Day", "Week", "Month", "Year"],
    state="readonly",
    width=9,
    style="Dark.TCombobox"
)

time_dropdown.pack(
    side="left",
    ipady=3
)


def advance_time():
    global current_date
    global current_price

    try:
        amount = int(time_amount_var.get())

        if amount <= 0:
            return

    except ValueError:
        return

    unit = time_unit_var.get()

    if unit == "Day":
        days = amount
    elif unit == "Week":
        days = amount * 7
    elif unit == "Month":
        days = amount * 30
    else:
        days = amount * 365

    # Generate simulated daily prices
    for _ in range(days):
        movement = random.uniform(-0.03, 0.03)

        current_price *= (1 + movement)

        current_price = max(
            1,
            round(current_price, 2)
        )

        current_date += timedelta(days=1)

        price_history.append(current_price)
        date_history.append(current_date)

    price_var.set(f"{current_price:.2f}")

    update_graph()
    update_display()
    analyze_stock()


next_button = tk.Button(
    time_frame,
    text="NEXT",
    command=advance_time,
    font=("Segoe UI", 9, "bold"),
    fg="white",
    bg=ACCENT_COLOR,
    relief="flat",
    padx=12,
    pady=6
)

next_button.pack(
    side="left",
    padx=(8, 0)
)


# --------------------------------------------------
# Random Market
# --------------------------------------------------

random_button = tk.Button(
    simulation_panel,
    text="RANDOM MARKET",
    command=lambda: randomize_market(),
    font=("Segoe UI", 9, "bold"),
    fg="white",
    bg="#6A3FB5",
    relief="flat",
    padx=12,
    pady=7
)

random_button.pack(
    fill="x",
    padx=20,
    pady=(10, 5)
)


manual_button = tk.Button(
    simulation_panel,
    text="MANUAL MARKET",
    command=lambda: toggle_manual(),
    font=("Segoe UI", 9, "bold"),
    fg="white",
    bg="#147D75",
    relief="flat",
    padx=12,
    pady=7
)

manual_button.pack(
    fill="x",
    padx=20,
    pady=(0, 15)
)


# --------------------------------------------------
# Expert System Output
# --------------------------------------------------

result_panel = tk.Frame(
    right_column,
    bg=PANEL_COLOR
)

result_panel.pack(
    fill="both",
    expand=True,
    pady=(10, 0)
)


result_title = tk.Label(
    result_panel,
    text="EXPERT SYSTEM ANALYSIS",
    font=("Segoe UI", 11, "bold"),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR
)

result_title.pack(
    anchor="w",
    padx=20,
    pady=(15, 5)
)


confidence_label = tk.Label(
    result_panel,
    text="Confidence: —",
    font=("Segoe UI", 9),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR
)

confidence_label.pack(
    anchor="w",
    padx=20
)


result_label = tk.Label(
    result_panel,
    text="—",
    font=("Segoe UI", 28, "bold"),
    fg=TEXT_COLOR,
    bg=PANEL_COLOR
)

result_label.pack(
    anchor="w",
    padx=20,
    pady=(5, 5)
)


reason_label = tk.Label(
    result_panel,
    text="Waiting for market analysis...",
    font=("Segoe UI", 9),
    fg=TEXT_COLOR,
    bg=PANEL_COLOR,
    wraplength=310,
    justify="left"
)

reason_label.pack(
    anchor="w",
    padx=20,
    pady=(0, 10)
)


rule_label = tk.Label(
    result_panel,
    text="Rule Fired: —",
    font=("Segoe UI", 8),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR,
    wraplength=310,
    justify="left"
)

rule_label.pack(
    anchor="w",
    padx=20
)


# --------------------------------------------------
# Functions
# --------------------------------------------------

def update_graph():
    line.set_xdata(date_history)
    line.set_ydata(price_history)

    axis.relim()
    axis.autoscale_view()

    figure.autofmt_xdate()

    canvas.draw()


def update_display():
    price_display.config(
        text=f"${current_price:,.2f}"
    )

    date_label.config(
        text=current_date.strftime("%B %d, %Y")
    )

    update_portfolio()


def update_portfolio():
    portfolio_value = cash + (shares * current_price)

    cash_label.config(
        text=f"Cash\n${cash:,.2f}"
    )

    shares_label.config(
        text=f"Shares\n{shares}"
    )

    portfolio_label.config(
        text=f"Portfolio Value\n${portfolio_value:,.2f}"
    )


def randomize_market():
    global current_price

    trend = random.choice(
        ["Uptrend", "Sideways", "Downtrend"]
    )

    pe = random.choice(
        ["Low", "Fair", "High"]
    )

    revenue = random.choice(
        ["Positive", "Neutral", "Negative"]
    )

    earnings = random.choice(
        ["Positive", "Negative"]
    )

    volume = random.choice(
        ["Low", "Average", "High"]
    )

    trend_var.set(trend)
    pe_var.set(pe)
    revenue_var.set(revenue)
    earnings_var.set(earnings)
    volume_var.set(volume)

    movement = random.uniform(-0.10, 0.10)

    current_price *= (1 + movement)

    current_price = max(
        1,
        round(current_price, 2)
    )

    price_var.set(f"{current_price:.2f}")

    price_history.append(current_price)
    date_history.append(current_date)

    update_graph()
    update_display()
    analyze_stock()


def apply_manual_changes():
    global current_price

    try:
        new_price = float(price_var.get())

        if new_price <= 0:
            return

        current_price = new_price

    except ValueError:
        return

    price_var.set(f"{current_price:.2f}")

    price_history.append(current_price)
    date_history.append(current_date)

    update_graph()
    update_display()
    analyze_stock()


def toggle_manual():
    global manual_mode

    manual_mode = not manual_mode

    if manual_mode:
        manual_button.config(
            text="MANUAL MARKET: ON"
        )
    else:
        manual_button.config(
            text="MANUAL MARKET"
        )


# --------------------------------------------------
# CLIPS Analysis
# --------------------------------------------------

def analyze_stock():

    trend = trend_var.get().lower()
    pe = pe_var.get().lower()
    revenue = revenue_var.get().lower()
    earnings = earnings_var.get().lower()
    volume = volume_var.get().lower()

    clips_commands = f"""
        (load "{CLIPS_FILE.as_posix()}")
        (reset)
        (assert
        (stock
            (trend {trend})
            (pe {pe})
            (revenue {revenue})
            (earnings {earnings})
            (volume {volume})))
        (run)
        (facts)
        (exit)
    """

    try:

        result = subprocess.run(
            [CLIPS_PATH],
            input=clips_commands,
            text=True,
            capture_output=True,
            cwd=BASE_DIR
        )

        output = result.stdout + result.stderr

        match = re.search(
            r"\(recommendation\s+\(action\s+(buy|hold|sell)\)",
            output,
            re.IGNORECASE
        )

        if match:

            recommendation = match.group(1).upper()

            if recommendation == "BUY":
                result_label.config(
                    text="BUY",
                    fg=BUY_COLOR
                )

            elif recommendation == "HOLD":
                result_label.config(
                    text="HOLD",
                    fg=HOLD_COLOR
                )

            else:
                result_label.config(
                    text="SELL",
                    fg=SELL_COLOR
                )

            # Basic confidence calculation
            confidence = calculate_confidence(
                recommendation,
                trend,
                pe,
                revenue,
                earnings,
                volume
            )

            confidence_label.config(
                text=f"Confidence: {confidence}%"
            )

            reasons = build_reasons(
                recommendation,
                trend,
                pe,
                revenue,
                earnings,
                volume
            )

            reason_label.config(
                text=reasons
            )

            rule_label.config(
                text=f"Rule Fired: {recommendation}-RULE"
            )

        else:

            result_label.config(
                text="N/A",
                fg=TEXT_COLOR
            )

            confidence_label.config(
                text="Confidence: —"
            )

            reason_label.config(
                text="The current indicators do not strongly support a recommendation."
            )

            rule_label.config(
                text="Rule Fired: None"
            )

    except FileNotFoundError:

        result_label.config(
            text="ERROR",
            fg=SELL_COLOR
        )

        reason_label.config(
            text="CLIPS could not be found. Check CLIPS_PATH."
        )

    except Exception as error:

        result_label.config(
            text="ERROR",
            fg=SELL_COLOR
        )

        reason_label.config(
            text=f"An error occurred: {error}"
        )


# --------------------------------------------------
# Confidence
# --------------------------------------------------

def calculate_confidence(
    recommendation,
    trend,
    pe,
    revenue,
    earnings,
    volume
):

    score = 50

    if recommendation == "BUY":

        if trend == "uptrend":
            score += 15

        if pe == "low":
            score += 10

        if revenue == "positive":
            score += 10

        if earnings == "positive":
            score += 10

        if volume == "high":
            score += 5

    elif recommendation == "SELL":

        if trend == "downtrend":
            score += 15

        if pe == "high":
            score += 10

        if revenue == "negative":
            score += 10

        if earnings == "negative":
            score += 10

        if volume == "high":
            score += 5

    else:

        if trend == "sideways":
            score += 15

        if earnings == "positive":
            score += 10

        if pe == "fair":
            score += 10

    return min(score, 99)


# --------------------------------------------------
# Reasons
# --------------------------------------------------

def build_reasons(
    recommendation,
    trend,
    pe,
    revenue,
    earnings,
    volume
):

    reasons = []

    if recommendation == "BUY":

        if trend == "uptrend":
            reasons.append("• Uptrend detected")

        if pe == "low":
            reasons.append("• Low P/E ratio")

        if revenue == "positive":
            reasons.append("• Positive revenue growth")

        if earnings == "positive":
            reasons.append("• Positive earnings")

        if volume == "high":
            reasons.append("• High trading volume")

    elif recommendation == "SELL":

        if trend == "downtrend":
            reasons.append("• Downtrend detected")

        if pe == "high":
            reasons.append("• High P/E ratio")

        if revenue == "negative":
            reasons.append("• Negative revenue growth")

        if earnings == "negative":
            reasons.append("• Negative earnings")

        if volume == "high":
            reasons.append("• High trading volume")

    else:

        if trend == "sideways":
            reasons.append("• Sideways market trend")

        if earnings == "positive":
            reasons.append("• Earnings remain positive")

        if pe == "fair":
            reasons.append("• P/E ratio is fair")

    if not reasons:
        reasons.append("• Mixed market indicators")

    return "\n".join(reasons)


# --------------------------------------------------
# Initial State
# --------------------------------------------------

update_display()
analyze_stock()


# --------------------------------------------------
# Start GUI
# --------------------------------------------------

root.mainloop()