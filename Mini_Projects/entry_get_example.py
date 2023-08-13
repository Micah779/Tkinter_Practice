import tkinter as tk
from tkinter import ttk

def button_func():
    # upadate the label
    label.config(text = entry_text.get())

# window/root/app
window = tk.Tk()
window.title("Getting and Setting Widgets")

# a label
label = ttk.Label(
    master=window,
    text="Some text"
)
label.pack()


# a entry widget
entry_text = tk.StringVar()
entry = ttk.Entry(
    master=window,
    textvariable=entry_text
)
entry.pack()


# a button
button = ttk.Button(
    master=window,
    text="The Button",
    command = button_func
)
button.pack()


# run
window.mainloop()

