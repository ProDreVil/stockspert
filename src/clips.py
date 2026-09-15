import subprocess
from pathlib import Path
import re


CLIPS_EXE = r"C:\Program Files\CLIPS 6.31\CLIPSDOS64.exe"
CLIPS_FILE = Path(__file__).resolve().parent.parent / "clips" / "main.CLP"


def get_recommendation(trend, pe, revenue, earnings, volume):
    clips_file = str(CLIPS_FILE).replace("\\", "/")
    commands = f"""
        (clear)
        (load "{clips_file}")
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
        capture_output=True
    )

    output = result.stdout

    match = re.search(
        r"RECOMMENDATION:\s*(BUY|HOLD|SELL)",
        output
    )

    if match:
        return match.group(1)

    if "NO CLEAR RECOMMENDATION" in output:
        return "N/A"

    return "ERROR"
    