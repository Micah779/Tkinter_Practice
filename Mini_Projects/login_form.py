import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Login")
window.geometry("300x300")

# dictionary to hold username and password data
user_data = {}

# function to save login information
def new_user_data():
    user_data[username2text.get()] = password2text.get()

# function to check if user/password is already in the system
def check_for_duplicate_user_data(dict, key):
    if key in user_data.keys():
        bottom_label2_text['value'] = "already a user"
    else:
        new_user_data()

# Notebook, Frames, Add frames to notebook
notebook = ttk.Notebook(window)
notebook.pack(expand=True)

frame1 = tk.Frame(window, width=300, height=300)
frame2 = tk.Frame(window, width=300, height=300)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text="Signup")
notebook.add(frame2, text="Login")

# (Login) Label top, Entry username, Entry password, Button submit, Label bottom

top_label = tk.Label(frame2,
                     text="Login Here",
                     font=("Arial", 24))
top_label.pack()

usernametext = tk.StringVar()
username = tk.Entry(frame2,
                    font=("Arial", 14),
                    textvariable=usernametext)
username.pack()

passwordtext = tk.IntVar()
password = tk.Entry(frame2,
                    font=("Arial", 14),
                    textvariable=passwordtext)
password.pack()

button = tk.Button(frame2,
                   text="Submit",
                   font=("Arial", 14))
button.pack()

bottom_label_text = tk.StringVar(value="Please Fill Form")
bottom_label = tk.Label(frame2,
                        font=("Arial", 14),
                        textvariable=bottom_label_text)
bottom_label.pack()

# (Signup) Label top, Entry username, Entry password, Password confirm, Button submit, Label bottom

top_label2 = tk.Label(frame1,
                      text="Sign up",
                      font=("Arial", 24))
top_label2.pack()

username2text = tk.StringVar()
username2 = tk.Entry(frame1,
                     font=("Arial", 14),
                     textvariable=username2text)
username2.pack()

password2text = tk.IntVar
password2 = tk.Entry(frame1,
                     font=("Arial", 14),
                     textvariable=password2text,
                     show="*")
password2.pack()

password2textcheck = tk.IntVar(value="")
password_confirm = tk.Entry(frame1,
                            font=("Arial", 14),
                            textvariable=password2textcheck)
password_confirm.pack()

button2 = tk.Button(frame1,
                    text="Submit",
                    font=("Arial", 14),
                    command = check_for_duplicate_user_data)
button2.pack()

bottom_label2_text = tk.StringVar(value = "Please Fill Form")
bottom_label2 = tk.Label(frame1,
                         font=("Arial", 14),
                         textvariable=bottom_label2_text)
bottom_label2.pack()

# run
window.mainloop()