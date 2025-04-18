import tkinter as tk

class SortComponent:

    def __init__(self, root, width= 900, height= 900):
        self.canvas = tk.Canvas(root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.width = width
        self.height = height

    def draw_array(self, array, marked_index= None, sorted_index= None):
        self.canvas.delete("all")
        bar_width = self.width / len(array)
        max_value = max(array)

        for i, val in enumerate(array):
            x0 = i * bar_width
            y0 = self.height
            x1 = (i + 1) * bar_width
            y1 = self.height - (val / max_value * self.height)

            if i == marked_index:
                color = "red"
            elif sorted_index is not None and i <= sorted_index:
                color = "green"
            else:
                color = "white"

            self.canvas.create_rectangle(x0, y1, x1, y0, fill=color)