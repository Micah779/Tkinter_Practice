# i dont care what it is but i need to code before 11:59 (yes im going to do more tonight i jsut need that commit streak!)
import tkinter as tk
from tkinter import ttk

# window/root
window = tk.Tk()
window.title('fast one')
window.geometry('500x500')

# label
label = tk.Label(window,
                  text='Hello this is a fast program to save my commits :)',
                  font = 'Arial 25 bold'
                  )
label.pack()


# run
window.mainloop()