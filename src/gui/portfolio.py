import tkinter as tk
from gui.components import create_section, create_label, create_entry, create_button

def build_portfolio(parent):
    panel = create_section(parent, "PORTFOLIO")

    stats = [
        ("Cash", "$10,000"),
        ("Shares", "0"),
        ("Invested", "$0.00"),
        ("Value", "$10,000"),
    ]

    for label, value in stats:
        row = tk.Frame(panel, bg="#181818")
        row.pack(fill="x", padx=15, pady=2)

        create_label(row, label, color="#AAAAAA", bg="#181818").pack(side="left")
        create_label(row, value, bg="#181818").pack(side="right")

    create_label(panel, "P/L        $0.00",
                 color="#AAAAAA", bg="#181818").pack(anchor="w", padx=15, pady=(12,2))

    create_label(panel, "Return     0.00%",
                 color="#AAAAAA", bg="#181818").pack(anchor="w", padx=15)

    buy = tk.Frame(panel, bg="#181818")
    buy.pack(fill="x", padx=15, pady=(15,5))

    create_label(buy, "Buy", bg="#181818").pack(side="left")
    create_entry(buy, width=5).pack(side="left", padx=5)
    create_button(buy, "BUY").pack(side="left")

    sell = tk.Frame(panel, bg="#181818")
    sell.pack(fill="x", padx=15, pady=(0,10))

    create_label(sell, "Sell", bg="#181818").pack(side="left")
    create_entry(sell, width=5).pack(side="left", padx=5)
    create_button(sell, "SELL").pack(side="left")

    return panel