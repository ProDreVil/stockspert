import tkinter as tk

from config import (
    GRAPH_COLOR,
    GRID_COLOR,
    UP_GRAPH_COLOR,
    DOWN_GRAPH_COLOR,
    SECONDARY_TEXT,
)

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
        self.candles = []
        self.canvas.bind(
            "<Configure>",
            self._on_resize
        )

    def _on_resize(self, event):
        if self.candles:
            self.update(self.candles)

    def update(self, candles):
        self.candles = candles
        self.canvas.delete("all")
        visible_candles = candles[-30:]
        if len(visible_candles) < 1:
            return
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        price_width = 55
        graph_width = width - price_width
        minimum = min(
            candle["low"]
            for candle in visible_candles
        )
        maximum = max(
            candle["high"]
            for candle in visible_candles
        )
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
                fill=GRID_COLOR
            )
        for index in range(len(visible_candles)):
            if len(visible_candles) == 1:
                ratio = 0
            else:
                ratio = index / (len(visible_candles) - 1)
            x = left + ratio * (right - left)
            self.canvas.create_line(
                x,
                top,
                x,
                bottom,
                fill=GRID_COLOR
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
        candle_width = max(
            4,
            (right - left) / len(visible_candles) * 0.55
        )
        for index, candle in enumerate(visible_candles):
            if len(visible_candles) == 1:
                ratio = 0.5
            else:
                ratio = index / (len(visible_candles) - 1)
            x = left + ratio * (right - left)
            open_price = candle["open"]
            high_price = candle["high"]
            low_price = candle["low"]
            close_price = candle["close"]
            high_y = bottom - (
                (high_price - minimum)
                / price_range
                * graph_height
            )
            low_y = bottom - (
                (low_price - minimum)
                / price_range
                * graph_height
            )
            open_y = bottom - (
                (open_price - minimum)
                / price_range
                * graph_height
            )
            close_y = bottom - (
                (close_price - minimum)
                / price_range
                * graph_height
            )
            if close_price >= open_price:
                candle_color = UP_GRAPH_COLOR
            else:
                candle_color = DOWN_GRAPH_COLOR
            self.canvas.create_line(
                x,
                high_y,
                x,
                low_y,
                fill=candle_color,
                width=1
            )
            body_top = min(open_y, close_y)
            body_bottom = max(open_y, close_y)
            if body_bottom - body_top < 2:
                body_bottom = body_top + 2
            self.canvas.create_rectangle(
                x - candle_width / 2,
                body_top,
                x + candle_width / 2,
                body_bottom,
                fill=candle_color,
                outline=candle_color
            )