from sort_component import SortComponent


class InsertionSort:
    def __init__(self, array : list[int], canvas : SortComponent) -> None:
        self.array : list[int] = array
        self.canvas : SortComponent = canvas
        self.i : int = 1
        self.j : int = 1
        self.key : int = array[1]
        self.after_id : int | None = None
        self.state : str = "searching"

    def step(self) -> None:
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

    def cancel(self) -> None:
        if self.after_id:
            self.canvas.canvas.after_cancel(self.after_id)
