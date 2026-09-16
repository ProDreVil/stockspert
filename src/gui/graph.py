import tkinter as tk

from config import ACCENT_COLOR, GRAPH_COLOR, SECONDARY_TEXT


class StockGraph:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg=GRAPH_COLOR)

        self.canvas = tk.Canvas(
            self.frame,
            bg=GRAPH_COLOR,
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

    def update(self, prices):
        self.canvas.delete("all")

        if len(prices) < 2:
            return

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Space reserved for the price labels on the right.
        price_width = 55

        graph_width = width - price_width

        minimum = min(prices)
        maximum = max(prices)

        price_range = maximum - minimum

        if price_range == 0:
            price_range = 1

        left = 10
        top = 10
        right = graph_width - 10
        bottom = height - 10

        graph_height = bottom - top

        grid_count = 5

        for index in range(grid_count):
            ratio = index / (grid_count - 1)
            y = top + ratio * graph_height

            self.canvas.create_line(
                left,
                y,
                right,
                y,
                fill="#1A1F2A"
            )

        for index in range(len(prices)):
            if len(prices) == 1:
                ratio = 0
            else:
                ratio = index / (len(prices) - 1)

            x = left + ratio * (right - left)

            self.canvas.create_line(
                x,
                top,
                x,
                bottom,
                fill="#1A1F2A"
            )

        for index in range(grid_count):
            ratio = index / (grid_count - 1)

            price = maximum - ratio * price_range
            y = top + ratio * graph_height

            self.canvas.create_text(
                width - 5,
                y,
                text=f"${price:.2f}",
                fill=SECONDARY_TEXT,
                anchor="e",
                font=("Segoe UI", 9)
            )

        points = []

        for index, price in enumerate(prices):
            ratio = index / (len(prices) - 1)

            x = left + ratio * (right - left)
            y = bottom - ((price - minimum) / price_range * graph_height)

            points.extend([x, y])

        self.canvas.create_line(
            *points,
            fill=ACCENT_COLOR,
            width=2
        )