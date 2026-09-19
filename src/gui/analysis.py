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

        "BUY-LOW-PRICE-POSITIVE-EARNINGS": [
            ("Low Price vs Recent Range", BUY_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
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

        "HOLD-UPTREND-HIGH-PE": [
            ("Uptrend", BUY_COLOR),
            ("High P/E Ratio", SELL_COLOR),
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
            ("Low Volume", HOLD_COLOR),
        ],

        "HOLD-UPTREND-LOW-PE-NEGATIVE-EARNINGS": [
            ("Uptrend", BUY_COLOR),
            ("Low P/E Ratio", BUY_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
        ],

        "HOLD-UPTREND-LOW-PE-NEGATIVE-REVENUE": [
            ("Uptrend", BUY_COLOR),
            ("Low P/E Ratio", BUY_COLOR),
            ("Negative Revenue Growth", SELL_COLOR),
        ],

        "HOLD-UPTREND-FAIR-PE-NEGATIVE-REVENUE": [
            ("Uptrend", BUY_COLOR),
            ("Fair P/E Ratio", HOLD_COLOR),
            ("Negative Revenue Growth", SELL_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "HOLD-DOWNTREND-NEGATIVE-REVENUE": [
            ("Downtrend", SELL_COLOR),
            ("Negative Revenue Growth", SELL_COLOR),
            ("Positive Earnings Growth", BUY_COLOR),
        ],

        "HOLD-UPTREND-FAIR-PE-NEGATIVE-EARNINGS": [
            ("Uptrend", BUY_COLOR),
            ("Fair P/E Ratio", HOLD_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
        ],

        "HOLD-UPTREND-HIGH-PE-NEGATIVE-EARNINGS": [
            ("Uptrend", BUY_COLOR),
            ("High P/E Ratio", SELL_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
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

        "SELL-UPTREND-LOW-PE-NEGATIVE-FUNDAMENTALS": [
            ("Uptrend", BUY_COLOR),
            ("Low P/E Ratio", BUY_COLOR),
            ("Negative Revenue Growth", SELL_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
        ],

        "SELL-UPTREND-FAIR-PE-NEGATIVE-FUNDAMENTALS": [
            ("Uptrend", BUY_COLOR),
            ("Fair P/E Ratio", HOLD_COLOR),
            ("Negative Revenue Growth", SELL_COLOR),
            ("Negative Earnings Growth", SELL_COLOR),
        ],

        "SELL-UPTREND-HIGH-PE-NEGATIVE-FUNDAMENTALS": [
            ("Uptrend", BUY_COLOR),
            ("High P/E Ratio", SELL_COLOR),
            ("Negative Revenue Growth", SELL_COLOR),
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

    panel = create_section(
        parent,
        "EXPERT SYSTEM ANALYSIS"
    )

    content = tk.Frame(
        panel,
        bg=GRAPH_COLOR
    )
    content.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(5, 15)
    )

    left = tk.Frame(
        content,
        bg=GRAPH_COLOR,
        width=320
    )
    left.pack(
        side="left",
        fill="y"
    )
    left.pack_propagate(False)

    recommendation = create_label(
        left,
        "BUY",
        font=("Segoe UI", 24, "bold"),
        color=BUY_COLOR,
        bg=GRAPH_COLOR
    )
    recommendation.pack(
        anchor="w",
        pady=(10, 15)
    )

    confidence = create_label(
        left,
        "Confidence: 69%",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR
    )
    confidence.pack(
        anchor="w",
        pady=2
    )

    rule = create_label(
        left,
        "Rule Fired: BUY-UPTREND-LOW-PE",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR,
    )
    rule.pack(
        anchor="w",
        pady=2
    )

    right = tk.Frame(
        content,
        bg=GRAPH_COLOR
    )
    right.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(30, 0)
    )

    create_label(
        right,
        "Reasons:",
        color=SECONDARY_TEXT,
        bg=GRAPH_COLOR
    ).pack(
        anchor="w",
        pady=(10, 8)
    )

    reasons_frame = tk.Frame(
        right,
        bg=GRAPH_COLOR,
        height=120
    )
    reasons_frame.pack(
        anchor="w",
        fill="x"
    )
    reasons_frame.pack_propagate(False)

    return {
        "frame": panel,
        "confidence": confidence,
        "recommendation": recommendation,
        "rule": rule,
        "reasons": reasons_frame
    }