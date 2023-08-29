import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# window
window = tk.Tk()
window.title("Login Form")
window.geometry("340x440")

def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in")
    else:
        messagebox.showerror(title="Invalid Login", message="Credentials are invalid")

frame = tk.Frame()

# creating widgets
login_label = tk.Label(frame,
                       text="Login",
                       font=("Arial", 30))
username_label = tk.Label(frame,
                          text="Username",
                          font=("Arial", 16))
username_entry = tk.Entry(frame)
password_label = tk.Label(frame,
                          text="Password",
                          font=("Arial", 16))
password_entry = tk.Entry(frame, show="*",
                          font=("Arial", 16))
login_button = tk.Button(frame,
                         text="Login",
                         font=("Arial", 16),
                         command=login)

# placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2,column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2)

frame.pack()

# run
window.mainloop()