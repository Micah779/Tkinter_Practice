import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("600x400")
window.title("Canvas")

# canvas
canvas = tk.Canvas(
    window,
    bg = 'white'
    )
canvas.pack()

canvas.create_rectangle((50, 20, 100, 200), 
                        fill= 'red', 
                        outline='black'
                        )
canvas.create_line((0,0,100,150),
                   fill = 'green'
                   )
canvas.create_oval((0,0,100,150),
                   fill='blue'
                   )
canvas.create_polygon((0,0,100,200,300,50),
                      fill='black'
                      )
canvas.create_arc((0,0,100,150),
                  start = 45,
                  extent = 180,
                  style = tk.ARC,
                  width = 10
                  )
canvas.create_text((100,40), text="this is some text", fill='black')

canvas.create_window((150,10), window = ttk.Button(window, text = "this is text in canvas"))
# run
window.mainloop()