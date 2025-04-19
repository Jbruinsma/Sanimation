from insertion_sort import InsertionSort
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

    if selected_sort.get() == "Selection Sort":
        sorter = SelectionSort(array, sort_component)
    elif selected_sort.get() == "Insertion Sort":
        sorter = InsertionSort(array, sort_component)
    else:
        print("Unknown sort selected.")
        return

    sorter.step()

root = tk.Tk()
root.title("Python Sorting Visualizer")

SORT_OPTIONS = ["Selection Sort", "Insertion Sort"]
selected_sort = tk.StringVar()
selected_sort.set(SORT_OPTIONS[0])

length_label = tk.Label(root, text="Array Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "25")
length_entry.pack()

max_label = tk.Label(root, text="Max Value:")
max_label.pack()
max_entry = tk.Entry(root)
max_entry.insert(0, "50")
max_entry.pack()

dropdown_label = tk.Label(root, text="Choose Sorting Algorithm:")
dropdown_label.pack()
dropdown = tk.OptionMenu(root, selected_sort, *SORT_OPTIONS)
dropdown.pack()

sort_component = SortComponent(root)

button = tk.Button(root, text="Restart", command=start_sorting)
button.pack(pady=10)

start_sorting()
root.mainloop()