import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("buttons, functions and arguments")

def button_func(entry_string):
    print("Button was pressed")
    print(entry_string.get())

def outer_function(parameter):
    def inner_function():
        print("A button was pressed")
        print(parameter.get())
    return inner_function

# widgets
entry_string = tk.StringVar(value = 'Test')
entry = ttk.Entry(
    window,
    textvariable = entry_string)
entry.pack()

button = ttk.Button(
    window, 
    text="Button",
    # wrapping the function in lambda tells it to execute only when pressing the buttons
    command = lambda: outer_function(entry_string)
    )
button.pack()

window.mainloop()