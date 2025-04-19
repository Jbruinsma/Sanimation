class InsertionSort:
    def __init__(self, array, canvas):
        self.array = array
        self.canvas = canvas
        self.i = 1
        self.j = 1
        self.key = array[1]
        self.after_id = None
        self.state = "searching"

    def step(self):
        if self.i >= len(self.array):
            return

        if self.state == "searching":
            if self.j > 0 and self.array[self.j - 1] > self.key:
                self.array[self.j] = self.array[self.j - 1]
                self.j -= 1
            else:
                self.state = "inserting"
        elif self.state == "inserting":
            self.array[self.j] = self.key
            self.i += 1
            if self.i < len(self.array):
                self.key = self.array[self.i]
                self.j = self.i
                self.state = "searching"

        self.canvas.draw_array(
            self.array,
            marked_index=self.j,
            sorted_index=self.i - 1
        )

        self.after_id = self.canvas.canvas.after(100, self.step)

    def cancel(self):
        if self.after_id:
            self.canvas.canvas.after_cancel(self.after_id)
