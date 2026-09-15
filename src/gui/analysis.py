import tkinter as tk
from gui.components import create_section, create_label

def build_analysis(parent):
    panel = create_section(parent, "EXPERT SYSTEM ANALYSIS")

    row = tk.Frame(panel, bg="#181818")
    row.pack(fill="x", padx=15, pady=(10,5))

    create_label(row, "Confidence", color="#AAAAAA", bg="#181818").pack(side="left")
    create_label(row, "69%", font=("Segoe UI",10,"bold"), bg="#181818").pack(side="left", padx=(8,25))
    create_label(row, "● BUY", font=("Segoe UI",12,"bold"), bg="#181818").pack(side="left")

    create_label(panel, "Rule Fired: BUY-UPTREND",
                 color="#AAAAAA", bg="#181818").pack(anchor="w", padx=15)

    create_label(panel,
                 "Reasons: Uptrend • Low P/E • Positive Revenue",
                 color="#AAAAAA", bg="#181818").pack(anchor="w", padx=15, pady=(10,2))

    create_label(panel,
                 "         • Positive Earnings",
                 color="#AAAAAA", bg="#181818").pack(anchor="w", padx=15)

    return panel