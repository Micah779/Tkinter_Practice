import tkinter as tk
#from tkinter import ttk
#styling for tkinter
import ttkbootstrap as ttk

def convert():
    output_string.set((entry_int.get() - 32)*(5/9))   

window = ttk.Window(themename="journal")
window.title("Converter")
window.geometry("300x150")

#creating Label
convert_label = ttk.Label(
    master=window,
    text="Ferenheight to Celcius :)",
    font="Arial 24 bold"
    )

convert_label.pack()

#creating frame for converter
main_frame = ttk.Frame(master=window)
main_frame.pack(pady=10)

#creating the box to input the temp
#anything inputed into entry is stored in entryInt var
entry_int = tk.IntVar()
entry = ttk.Entry(
    master=main_frame, 
    textvariable=entry_int
    )

entry.pack(side="left", padx=10)

#the convert button
button = ttk.Button(
    master=main_frame, 
    text="Convert", 
    command = convert
    )

button.pack(side="left")

#output label
#output_string variable
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    text="Output", 
    font="Arial 24", 
    textvariable=output_string
    )

output_label.pack(pady=5)




window.mainloop()