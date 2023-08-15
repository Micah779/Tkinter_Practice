import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("buttons, functions and arguments")

# widgets
entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(
    window, 
    text="Button",
    command = button_func
    )
button.pack()

window.mainloop()