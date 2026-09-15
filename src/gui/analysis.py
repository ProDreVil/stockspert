import tkinter as tk

from config import (
    BUY_COLOR,
    GRAPH_COLOR,
    HOLD_COLOR,
    SECONDARY_TEXT,
    SELL_COLOR,
    TEXT_COLOR,
)

from gui.components import create_section, create_label


def update_reasons(reasons_frame, rule):
    for widget in reasons_frame.winfo_children():
        widget.destroy()

    reason_map = {
        "BUY-UPTREND-LOW-PE": [
            ("Uptrend", BUY_COLOR),
            ("Low P/E Ratio", BUY_COLOR),
            ("Positive Revenue Growth", BUY_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "BUY-UPTREND-FAIR-PE": [
            ("Uptrend", BUY_COLOR),
            ("Fair P/E Ratio", HOLD_COLOR),
            ("Positive Revenue Growth", BUY_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "BUY-UPTREND-HIGH-VOLUME": [
            ("Uptrend", BUY_COLOR),
            ("Low P/E Ratio", BUY_COLOR),
            ("Positive Revenue Growth", BUY_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
            ("High Trading Volume", BUY_COLOR),
        ],

        "HOLD-SIDEWAYS-POSITIVE-EARNINGS": [
            ("Sideways Trend", HOLD_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "HOLD-UPTREND-LOW-PE-NEUTRAL-REVENUE": [
            ("Uptrend", BUY_COLOR),
            ("Low P/E Ratio", BUY_COLOR),
            ("Neutral Revenue Growth", HOLD_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "HOLD-UPTREND-FAIR-PE-NEUTRAL-REVENUE": [
            ("Uptrend", BUY_COLOR),
            ("Fair P/E Ratio", HOLD_COLOR),
            ("Neutral Revenue Growth", HOLD_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "HOLD-DOWNTREND-NEUTRAL-REVENUE": [
            ("Downtrend", SELL_COLOR),
            ("Neutral Revenue Growth", HOLD_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "HOLD-DOWNTREND-POSITIVE-FUNDAMENTALS": [
            ("Downtrend", SELL_COLOR),
            ("Positive Revenue Growth", BUY_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "HOLD-DOWNTREND-MIXED-FUNDAMENTALS": [
            ("Downtrend", SELL_COLOR),
            ("Positive Revenue Growth", BUY_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
        ],

        "HOLD-UPTREND-LOW-VOLUME": [
            ("Uptrend", BUY_COLOR),
            ("Low P/E Ratio", BUY_COLOR),
            ("Positive Revenue Growth", BUY_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
            ("Low Trading Volume", HOLD_COLOR),
        ],

        "SELL-DOWNTREND-NEGATIVE-FUNDAMENTALS": [
            ("Downtrend", SELL_COLOR),
            ("Negative Revenue Growth", SELL_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
        ],

        "SELL-SIDEWAYS-NEGATIVE-EARNINGS": [
            ("Sideways Trend", HOLD_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
        ],

        "SELL-DOWNTREND-HIGH-PE": [
            ("Downtrend", SELL_COLOR),
            ("High P/E Ratio", SELL_COLOR),
            ("Negative Revenue Growth", SELL_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "SELL-DOWNTREND-NEGATIVE-EARNINGS": [
            ("Downtrend", SELL_COLOR),
            ("Neutral Revenue Growth", HOLD_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
        ],
    }

    reasons = reason_map.get(rule, [])

    for reason, color in reasons:
        create_label(
            reasons_frame,
            f"• {reason}",
            color=color,
            bg=GRAPH_COLOR,
            justify="left"
        ).pack(
            anchor="w"
        )

def build_analysis(parent):
    panel = create_section(parent, "EXPERT SYSTEM ANALYSIS")

    recommendation = create_label(
        panel,
        "BUY",
        font=("Segoe UI", 24, "bold"),
        color=BUY_COLOR,
        bg=GRAPH_COLOR
    )
    recommendation.pack(
        pady=(15, 12)
    )

    info_row = tk.Frame(panel, bg=GRAPH_COLOR)
    info_row.pack(
        fill="x",
        padx=20,
        pady=(0, 10)
    )

    confidence = create_label(
        info_row,
        "Confidence: 69%",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR
    )
    confidence.pack(side="left")

    rule = create_label(
        info_row,
        "Rule Fired: BUY-UPTREND",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR
    )
    rule.pack(side="right")

    create_label(
        panel,
        "Reasons:",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR
    ).pack(
        anchor="w",
        padx=20,
        pady=(5, 3)
    )

    reasons_frame = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )
    reasons_frame.pack(
        anchor="w",
        padx=35
    )

    return {
        "frame": panel,
        "confidence": confidence,
        "recommendation": recommendation,
        "rule": rule,
        "reasons": reasons_frame
    }