import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Simple Canvas")

canvas = tk.Canvas(window,
                   bg = 'black'
                   )
canvas.pack()

def on_motion(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2, fill='white' )

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4
    print(event)

    brush_size = max(0, min(brush_size, 50))

brush_size = 4
canvas.bind('<Motion>', on_motion)
canvas.bind('<MouseWheel>', brush_size_adjust)

# run
window.mainloop()