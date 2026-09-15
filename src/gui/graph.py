import tkinter as tk

from config import GRAPH_COLOR


class StockGraph:
    def __init__(self, parent):
        self.frame = tk.Frame(
            parent,
            bg=GRAPH_COLOR
        )

        self.canvas = tk.Canvas(
            self.frame,
            bg=GRAPH_COLOR,
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

    def update(self, prices):
        self.canvas.delete("all")

        if len(prices) < 2:
            return

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        minimum = min(prices)
        maximum = max(prices)

        price_range = maximum - minimum

        if price_range == 0:
            price_range = 1

        points = []

        for index, price in enumerate(prices):
            x = index / (len(prices) - 1) * width

            y = height - (
                (price - minimum) / price_range * height
            )

            points.extend([x, y])

        self.canvas.create_line(
            *points,
            fill="#4A90E2",
            width=2
        )