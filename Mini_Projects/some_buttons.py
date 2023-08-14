import tkinter as tk
from tkinter import ttk

# window/root/app
window = tk.Tk()
window.geometry("600x400")

# button
def button_func():
    print("a basic button")

button_string = tk.StringVar(value="a button with string var")

button = ttk.Button(
    master=window,
    text="Button",
    command= button_func,
    textvariable=button_string
)
button.pack()

# checkbox 1
check_var = tk.BooleanVar()
checkbox_1 = ttk.Checkbutton(
    master=window,
    text="checkbox 1",
    command = lambda: print(check_var.get()),
    variable= check_var
)
checkbox_1.pack()

# checkbox 2
checkbox_3 = ttk.Checkbutton(
    master=window,
    text="checkbox 2"
)
checkbox_3.pack()

# radio 1
radio_1 = ttk.Radiobutton(
    master=window,
    text="radio 1"
)
radio_1.pack()

# radio 2
radio_2 = ttk.Radiobutton(
    master=window,
    text="radio 2"
)
radio_2.pack()


# run
window.mainloop()