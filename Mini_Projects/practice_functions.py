import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("buttons, functions and arguments")

def button_func(entry_string):
    print("Button was pressed")
    print(entry_string.get())

# widgets
entry_string = tk.StringVar(value = 'Test')
entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(
    window, 
    text="Button",
    command = button_func(entry_string)
    )
button.pack()

window.mainloop()