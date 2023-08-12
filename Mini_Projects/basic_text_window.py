import tkinter as tk
import ttkbootstrap as ttk

def printButton():
    print(entry_text.get())

# creating the main window/root/app
window = ttk.Window()
window.title("Text Widget Window")
window.geometry("800x500")


# creating the main frame
frame = ttk.Frame(master=window)
frame.pack()

# creating the main label
top_label = ttk.Label(
    master=frame, 
    text="Text Box", 
    font="Arial 20 bold"
    )
top_label.pack()

# creating the text box
text = ttk.Text(master=frame)
text.pack(
    pady=10, 
    padx=10
    )

# creating the lower entry box
entry_text = tk.StringVar()
entry = ttk.Entry(
    master=window,
    textvariable=entry_text)
entry.pack()

# creating the print button
button = ttk.Button(
    master=window, 
    text="Print Button",
    command=printButton
    )
button.pack()

# run
window.mainloop()
