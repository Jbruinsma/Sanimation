class SelectionSort:
    def __init__(self, array, canvas):
        self.array = array
        self.canvas = canvas
        self.i = 0
        self.j = 1
        self.min_index = 0
        self.after_id = None

    def step(self):
        if self.i >= len(self.array):
            return

        if self.j < len(self.array):
            if self.array[self.j] < self.array[self.min_index]:
                self.min_index = self.j
            self.j += 1
        else:
            self.array[self.i], self.array[self.min_index] = self.array[self.min_index], self.array[self.i]
            self.i += 1
            self.j = self.i + 1
            self.min_index = self.i

        self.canvas.draw_array(self.array,
                               marked_index= self.j if self.j < len(self.array) else None,
                               sorted_index= self.i - 1
                               )
        self.after_id = self.canvas.canvas.after(100, self.step)

    def cancel(self):
        if self.after_id:
            self.canvas.canvas.after_cancel(self.after_id)