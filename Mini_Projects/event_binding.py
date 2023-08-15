import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Event Binding")

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(
    window,
    text = "Button"
    )
button.pack()

# events
button.bind("<Command-KeyPress-a>", lambda event: print(event))

window.bind("<Motion>", get_pos)

window.bind("<KeyPress>", lambda event: print(f"A button was pressed ({event.char})"))

entry.bind("<FocusIn>", lambda event: print("Entry Field was selected"))



window.mainloop()