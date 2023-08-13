import tkinter as tk
import ttkbootstrap as ttk

def printButton():
    print(entry_text.get())

# creating the main window/root/app
window = ttk.Window()
window.title("Text Widget Window")
window.geometry("1000x500")


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

# creating second label
label_two = ttk.Label(
    master=window,
    text="my label",
    font="Arial 20 bold")
label_two.pack()

# creating second button
button_two = ttk.Button(
    master=window,
    text="hello",
    command= lambda: print("Hello"))
button_two.pack()

# creating the print button
button = ttk.Button(
    master=window, 
    text="Print Button",
    command=printButton
    )
button.pack(pady=10)


# run
window.mainloop()
