import tkinter as tk
from tkinter import ttk

# window/root/app
window = tk.Tk()
window.geometry("300x130")

# button
button = ttk.Button(
    master=window,
    text="Button"
)
button.pack()

# checkbox 1
checkbox_2 = ttk.Checkbutton(
    master=window,
    text="checkbox 1"
)
checkbox_2.pack()

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