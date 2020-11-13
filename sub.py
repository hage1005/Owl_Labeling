import tkinter as tk

import csv

CSV_Data = []
CSV_Data.append(["image_path1", 0])
CSV_Data.append(["image_path2", 1])


def output_csv():
    print("producing csv file")
    with open('owl_file.csv', mode='a') as owl_file:
        owl_writer = csv.writer(owl_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in CSV_Data:
            owl_writer.writerow(row)


def increase(event):
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease(event):
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window = tk.Tk()
window.bind("<Down>", decrease)
window.bind("<Up>", increase)
btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

button = tk.Button(
    master=window,
    text="Click me!",
    width=25,
    height=5,
    command=output_csv
)
button.grid(row=0, column=3, sticky="nsew")
# button.pack()
window.mainloop()
