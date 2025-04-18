from selection_sorter import SelectionSort
from sort_component import SortComponent
from random_array import random_array
import tkinter as tk

sorter= None

def start_sorting():
    global sorter
    if sorter:
        sorter.cancel()

    try:
        length = int(length_entry.get())
        max_val = int(max_entry.get())
    except ValueError:
        print("Invalid input!")
        return

    array = random_array(length=length, max_value=max_val)
    sort_component.draw_array(array)
    sorter = SelectionSort(array, sort_component)
    sorter.step()

root = tk.Tk()
length_label = tk.Label(root, text="Array Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "25")
length_entry.pack()

max_label = tk.Label(root, text="Max Value:")
max_label.pack()
max_entry = tk.Entry(root)
max_entry.insert(0, "25")
max_entry.pack()
sort_component = SortComponent(root)
button = tk.Button(root, text="Restart", command=start_sorting)
button.pack(pady=10)
start_sorting()
root.mainloop()