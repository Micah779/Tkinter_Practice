from tkinter import *
from tkinter import ttk
import math

#function for the clear button on the calculator

#function that will calculate the string (user input)


#creating the root window, toplevel window in Tkinter
root = Tk()
root.title("Basic Calculator")

#creating the mainframe which is where all of our calc GUI components go
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#creating the results bar (top of the calculator)
result_box = StringVar()
result = ttk.Label(mainframe, width=4, text="..." )
result.grid(column=1, row=1, sticky=(N, W))

#creating number buttons
button_1 = ttk.Button()

root.mainloop()
