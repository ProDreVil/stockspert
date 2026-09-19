import re
import subprocess
from pathlib import Path

from confidence import calculate_confidence

CLIPS_EXE = r"C:\Program Files\CLIPS 6.31\CLIPSDOS64.exe"
CLIPS_FILE = Path(__file__).resolve().parent.parent / "clips" / "main.CLP"


def get_recommendation(
    trend,
    pe,
    revenue,
    earnings,
    volume,
    price_history,
    shares,
    average_buy_price
):
    price_history = price_history[-10:]
    lowest = min(price_history)
    highest = max(price_history)
    current = price_history[-1]

    if shares <= 0:
        position = "none"
    elif current > average_buy_price:
        position = "profit"
    else:
        position = "loss"

    price_range = highest - lowest

    low_boundary = lowest + price_range * 0.33
    high_boundary = lowest + price_range * 0.67

    if current <= low_boundary:
        price_level = "low"
    elif current >= high_boundary:
        price_level = "high"
    else:
        price_level = "fair"

    clips_file = str(CLIPS_FILE).replace("\\", "/")
    templates_file = str(CLIPS_FILE.parent / "templates.CLP").replace("\\", "/")
    output_file = str(CLIPS_FILE.parent / "output.CLP").replace("\\", "/")
    buy_file = str(CLIPS_FILE.parent / "rules" / "buy.CLP").replace("\\", "/")
    hold_file = str(CLIPS_FILE.parent / "rules" / "hold.CLP").replace("\\", "/")
    sell_file = str(CLIPS_FILE.parent / "rules" / "sell.CLP").replace("\\", "/")
    fallback_file = str(CLIPS_FILE.parent / "rules" / "fallback.CLP").replace("\\", "/")

    commands = f"""
        (clear)
        (load "{templates_file}")
        (load "{output_file}")
        (load "{buy_file}")
        (load "{hold_file}")
        (load "{sell_file}")
        (load "{fallback_file}")
        (assert
        (stock
            (trend {trend})
            (pe {pe})
            (revenue {revenue})
            (earnings {earnings})
            (volume {volume})
            (price {price_level})
            (shares {shares})
            (average-buy-price {average_buy_price})
            (position {position})))
        (run)
        (exit)
        """

    result = subprocess.run(
        [CLIPS_EXE],
        input=commands,
        text=True,
        capture_output=True,
        cwd=CLIPS_FILE.parent
    )

    output = result.stdout
    
    recommendation_match = re.search(
        r"RECOMMENDATION:\s*(BUY|HOLD|SELL)",
        output,
        re.IGNORECASE
    )

    rule_match = re.search(
        r"^\s*RULE:\s*(.+)$",
        output,
        re.MULTILINE | re.IGNORECASE
    )

    if recommendation_match:
        recommendation = recommendation_match.group(1).upper()
        rule = rule_match.group(1).strip() if rule_match else "UNKNOWN"
        confidence = calculate_confidence(
            rule,
            recommendation,
            price_history,
            volume,
            position
        )

        return recommendation, rule, confidence

    if "RECOMMENDATION: N/A" in output:
        return "N/A", "NO-CLEAR-RECOMMENDATION", 0

    return "ERROR", "ERROR"