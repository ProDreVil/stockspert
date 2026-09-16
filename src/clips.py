import re
import subprocess
from pathlib import Path

from confidence import get_base_confidence

CLIPS_EXE = r"C:\Program Files\CLIPS 6.31\CLIPSDOS64.exe"
CLIPS_FILE = Path(__file__).resolve().parent.parent / "clips" / "main.CLP"


def get_recommendation(
    trend,
    pe,
    revenue,
    earnings,
    volume
):
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
            (volume {volume})))
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
        confidence = get_base_confidence(rule)
        return recommendation, rule, confidence

    if "RECOMMENDATION: N/A" in output:
        return "N/A", "NO-CLEAR-RECOMMENDATION", 0

    return "ERROR", "ERROR"