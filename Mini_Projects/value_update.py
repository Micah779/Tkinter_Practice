import tkinter as tk
from tkinter import ttk

def set_label_func():
    label['text'] = entry_text.get()
    entry['state'] = 'disabled'

def clear_func():
    entry['state'] = 'enabled'

# window/root/app
window = tk.Tk()

# text variable
entry_text = tk.StringVar(value= "start value")

# the label
label = ttk.Label(
    master=window,
    textvariable=entry_text
)
label.pack()

# the entry
entry = ttk.Entry(
    master=window,
    textvariable=entry_text
)
entry.pack()

# the button
button = ttk.Button(
    master=window,
    text="Set Label",
    command= set_label_func
)
button.pack()

# clear title button
clear_button = ttk.Button(
    master=window,
    text="Clear",
    command= clear_func
)
clear_button.pack()

# run
window.mainloop()