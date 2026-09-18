import tkinter as tk

from config import (
    BORDER_COLOR,
    GRAPH_COLOR,
    GRID_COLOR,
    PANEL_COLOR,
    TEXT_COLOR,
    UP_GRAPH_COLOR,
    DOWN_GRAPH_COLOR,
    SECONDARY_TEXT,
    SECONDARY_COLOR,
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
        self.candle_positions = []
        self.tooltip = None
        self.canvas.bind(
            "<Configure>",
            self._on_resize
        )
        self.canvas.bind(
            "<Motion>",
            self._on_hover
        )
        self.canvas.bind(
            "<Leave>",
            self._hide_tooltip
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
                font=("Consolas", 8)
            )
        candle_width = max(
            4,
            (right - left) / len(visible_candles) * 0.55
        )
        self.candle_positions = []
        for index, candle in enumerate(visible_candles):
            if len(visible_candles) == 1:
                ratio = 0.5
            else:
                ratio = index / (len(visible_candles) - 1)
            x = left + ratio * (right - left)
            self.candle_positions.append((x, candle_width, candle))
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

    def _on_hover(self, event):
        for index, (x, candle_width, candle) in enumerate(self.candle_positions):
            if (
                x - candle_width / 2
                <= event.x
                <= x + candle_width / 2
            ):
                self._show_tooltip(
                    event.x,
                    event.y,
                    candle,
                    index
                )
                return
        self._hide_tooltip()

    def _show_tooltip(self, x, y, candle, index):
        if candle["close"] >= candle["open"]:
            border_color = UP_GRAPH_COLOR
        else:
            border_color = DOWN_GRAPH_COLOR
        if index > 0:
            change = candle["close"] - candle["open"]
            change_percent = (change / candle["open"]) * 100
        else:
            change = 0
            change_percent = 0
        date_text = candle["date"].strftime("%B %d, %Y")
        text = (
            f"{date_text}\n\n"
            f"Open: ${candle['open']:.2f}\n"
            f"High: ${candle['high']:.2f}\n"
            f"Low: ${candle['low']:.2f}\n"
            f"Close: ${candle['close']:.2f}\n\n"
            f"Change: {'+$' if change >= 0 else '-$'}{abs(change):.2f} ({change_percent:+.2f}%)"
        )
        if self.tooltip is None:
            self.tooltip = tk.Toplevel(self.canvas)
            self.tooltip.overrideredirect(True)
            self.tooltip.configure(
                bg=border_color
            )

            tooltip_frame = tk.Frame(
                self.tooltip,
                bg=PANEL_COLOR,
                padx=10,
                pady=8
            )
            tooltip_frame.pack(
                padx=1,
                pady=1
            )

            tk.Label(
                tooltip_frame,
                text="OHLC",
                bg=PANEL_COLOR,
                fg=TEXT_COLOR,
                font=("Segoe UI", 9, "bold")
            ).pack(
                anchor="w",
                pady=(0, 5)
            )

            self.tooltip_label = tk.Label(
                tooltip_frame,
                bg=PANEL_COLOR,
                fg=SECONDARY_TEXT,
                font=("Consolas", 9),
                justify="left"
            )
            self.tooltip_label.pack(
                anchor="w"
            )

        self.tooltip_label.configure(text=text)
        self.tooltip.update_idletasks()

        tooltip_width = self.tooltip.winfo_width()
        tooltip_height = self.tooltip.winfo_height()

        screen_x = (
            self.canvas.winfo_rootx()
            + x
            + 12
        )

        screen_y = (
            self.canvas.winfo_rooty()
            + y
            - tooltip_height
            - 10
        )

        screen_width = self.canvas.winfo_screenwidth()
        screen_height = self.canvas.winfo_screenheight()

        if screen_x + tooltip_width > screen_width:
            screen_x = (
                self.canvas.winfo_rootx()
                + x
                - tooltip_width
                - 12
            )

        if screen_y < 0:
            screen_y = (
                self.canvas.winfo_rooty()
                + y
                + 12
            )

        self.tooltip.geometry(
            f"+{int(screen_x)}+{int(screen_y)}"
        )

    def _hide_tooltip(self, event=None):
        if self.tooltip is not None:
            self.tooltip.destroy()
            self.tooltip = None