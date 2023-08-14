import tkinter as tk
from tkinter import ttk

# window/root/app
window = tk.Tk()
window.geometry("600x400")

# button
def button_func():
    print("a basic button")
    print(radio_var.get())

button_string = tk.StringVar(value="a button with string var")

button = ttk.Button(
    master=window,
    text="Button",
    command= button_func,
    textvariable=button_string
)
button.pack()

# checkbox 1
check_var = tk.IntVar(value=10)
checkbox_1 = ttk.Checkbutton(
    master=window,
    text="checkbox 1",
    command = lambda: print(check_var.get()),
    variable= check_var,
    onvalue= 10,
    offvalue= 5
)
checkbox_1.pack()

# checkbox 2
checkbox_3 = ttk.Checkbutton(
    master=window,
    text="checkbox 2"
)
checkbox_3.pack()

# radio 1
# always set a 'value' for radios
radio_var = tk.StringVar()
radio_1 = ttk.Radiobutton(
    master=window,
    text="radio 1",
    value= 'radio 1',
    command = lambda: print(radio_var.get()),
    variable= radio_var
)
radio_1.pack()

# radio 2
radio_2 = ttk.Radiobutton(
    master=window,
    text="radio 2",
    value = 2,
    variable= radio_var
)
radio_2.pack()


# run
window.mainloop()