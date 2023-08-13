import tkinter as tk
from tkinter import ttk

def button_func():
    # upadate the label
    label['text'] = entry_text.get()
    # disables the entry box
    entry['state'] = 'disabled'

def revert_button_func():
    label['text'] = "Some text"
    entry['state'] = 'enabled'

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
    text="Update Label",
    command = button_func
)
button.pack()

# revert text button
revert_button = ttk.Button(
    master=window,
    text="Revert Label",
    command = revert_button_func
)
revert_button.pack()

# run
window.mainloop()

