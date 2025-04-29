import tkinter as tk

class SortComponent:

    def __init__(self, root, width: int = 900, height : int = 900) -> None:
        self.canvas : tk = tk.Canvas(root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.width : int = width
        self.height : int = height

    def draw_array(self, array : list[int], marked_index : int = None, sorted_index : int = None):
        self.canvas.delete("all")
        bar_width : float = self.width / len(array)
        max_value : int = max(array)

        for i, val in enumerate(array):
            x0 : float = i * bar_width
            y0 : int = self.height
            x1 : float = (i + 1) * bar_width
            y1 : float = self.height - (val / max_value * self.height)

            if i == marked_index:
                color : str  = "red"
            elif sorted_index is not None and i <= sorted_index:
                color : str = "green"
            else:
                color : str = "white"

            self.canvas.create_rectangle(x0, y1, x1, y0, fill=color)