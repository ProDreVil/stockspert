import tkinter as tk

from config import (
    BUY_COLOR,
    GRAPH_COLOR,
    SECONDARY_TEXT,
    TEXT_COLOR,
)

from gui.components import create_section, create_label


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

    reasons = create_label(
        panel,
        "• Uptrend\n"
        "• Low P/E\n"
        "• Positive Revenue\n"
        "• Positive Earnings",
        color=TEXT_COLOR,
        bg=GRAPH_COLOR,
        justify="left"
    )
    reasons.pack(
        anchor="w",
        padx=35
    )

    return {
        "frame": panel,
        "confidence": confidence,
        "recommendation": recommendation,
        "rule": rule,
        "reasons": reasons
    }