import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Calculator")
window.geometry("500x800")

# result label
result = ttk.Label(
    window,
    text = "answer",
    background = 'white',
    foreground = 'black',
    font = 'Arial 12 bold',
    )
result.pack()

# buttons
button_1 = ttk.Button(window, text = '1')
button_1.pack()

button_2 = ttk.Button(window, text = '2')
button_2.pack()

button_3 = ttk.Button(window, text = '3')
button_3.pack()

button_4 = ttk.Button(window, text = '4')
button_4.pack()

button_5 = ttk.Button(window, text = '5')
button_5.pack()

button_6 = ttk.Button(window, text = '6')
button_6.pack()

button_7 = ttk.Button(window, text = '7')
button_7.pack()

button_8 = ttk.Button(window, text = '8')
button_8.pack()

button_9 = ttk.Button(window, text = '9')
button_9.pack()

button_0 = ttk.Button(window, text = '0')
button_0.pack()

# run
window.mainloop()
