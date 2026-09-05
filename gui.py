import tkinter as tk
from tkinter import ttk
import subprocess
from pathlib import Path
import re

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
# Main Window
# --------------------------------------------------

root = tk.Tk()
root.title("Stock Market Expert System")
root.geometry("700x700")
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
# Header
# --------------------------------------------------

header = tk.Frame(root, bg=BG_COLOR)
header.pack(fill="x", padx=40, pady=(30, 10))
title = tk.Label(
    header,
    text="STOCK MARKET RECOMMENDER",
    font=("Segoe UI", 18, "bold"),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
title.pack()

# --------------------------------------------------
# Input Panel
# --------------------------------------------------

input_panel = tk.Frame(root, bg=PANEL_COLOR)
input_panel.pack(fill="x", padx=40, pady=10)

# --------------------------------------------------
# Input Variables
# --------------------------------------------------

trend_var = tk.StringVar(value="Uptrend")
pe_var = tk.StringVar(value="Low")
revenue_var = tk.StringVar(value="Positive")
earnings_var = tk.StringVar(value="Positive")
volume_var = tk.StringVar(value="Average")

# --------------------------------------------------
# Helper Function
# --------------------------------------------------

def create_dropdown(parent, label, variable, values):
    container = tk.Frame(parent, bg=PANEL_COLOR)
    container.pack(fill="x", padx=25, pady=4)
    label_widget = tk.Label(
        container,
        text=label,
        font=("Segoe UI", 10, "bold"),
        fg=TEXT_COLOR,
        bg=PANEL_COLOR,
        anchor="w"
    )
    label_widget.pack(fill="x", pady=(0, 5))
    dropdown = ttk.Combobox(
        container,
        textvariable=variable,
        values=values,
        state="readonly",
        style="Dark.TCombobox",
        font=("Segoe UI", 10)
    )
    dropdown.pack(fill="x", ipady=4)
    return dropdown

# --------------------------------------------------
# Dropdowns
# --------------------------------------------------

create_dropdown(
    input_panel,
    "Stock Trend",
    trend_var,
    ["Uptrend", "Sideways", "Downtrend"]
)
create_dropdown(
    input_panel,
    "P/E Ratio",
    pe_var,
    ["Low", "Fair", "High"]
)
create_dropdown(
    input_panel,
    "Revenue Growth",
    revenue_var,
    ["Positive", "Neutral", "Negative"]
)
create_dropdown(
    input_panel,
    "Earnings Growth",
    earnings_var,
    ["Positive", "Negative"]
)
create_dropdown(
    input_panel,
    "Trading Volume",
    volume_var,
    ["Low", "Average", "High"]
)

# --------------------------------------------------
# Recommendation Panel
# --------------------------------------------------

result_panel = tk.Frame(
    root,
    bg=PANEL_COLOR
)
result_panel.pack(
    fill="x",
    padx=40,
    pady=(5, 10)
)
result_title = tk.Label(
    result_panel,
    text="RECOMMENDATION",
    font=("Segoe UI", 11, "bold"),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR
)
result_title.pack(pady=(20, 5))
result_label = tk.Label(
    result_panel,
    text="—",
    font=("Segoe UI", 28, "bold"),
    fg=TEXT_COLOR,
    bg=PANEL_COLOR
)
result_label.pack()
reason_label = tk.Label(
    result_panel,
    text="Enter the stock information and click Analyze Stock.",
    font=("Segoe UI", 10),
    fg=SECONDARY_TEXT,
    bg=PANEL_COLOR,
    wraplength=560,
    justify="center"
)
reason_label.pack(pady=(5, 10))

# --------------------------------------------------
# Analyze Function
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
            r"\(recommendation \(action (buy|hold|sell)\)\)",
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
            elif recommendation == "SELL":
                result_label.config(
                    text="SELL",
                    fg=SELL_COLOR
                )
            reason_label.config(
                text="Recommendation generated by the CLIPS expert system."
            )
        else:
            result_label.config(
                text="N/A",
                fg=TEXT_COLOR
            )
            reason_label.config(
                text="The current indicators do not strongly support "
                     "a BUY, HOLD, or SELL recommendation."
            )
    except FileNotFoundError:
        result_label.config(
            text="ERROR",
            fg=SELL_COLOR
        )
        reason_label.config(
            text="CLIPS could not be found. Check the CLIPS_PATH "
                 "in gui.py."
        )
    except Exception as e:
        result_label.config(
            text="ERROR",
            fg=SELL_COLOR
        )
        reason_label.config(
            text=f"An error occurred: {e}"
        )

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

analyze_button = tk.Button(
    root,
    text="ANALYZE STOCK",
    command=analyze_stock,
    font=("Segoe UI", 11, "bold"),
    fg="white",
    bg=ACCENT_COLOR,
    activeforeground="white",
    activebackground="#357ABD",
    relief="flat",
    cursor="hand2",
    padx=30,
    pady=12
)
analyze_button.pack(pady=(0, 15))

# --------------------------------------------------
# Start GUI
# --------------------------------------------------

root.mainloop()