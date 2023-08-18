import tkinter as tk
from tkinter import ttk
from random import choice

# window
window = tk.Tk()
window.title("Tree View")
window.geometry('600x400')

# data
first_name = ['Bob','Jon','Adam','Micah','Henry','Lisa','Clark','Anna']
last_name = ['Thai','Platt','Anderson','Colins','Martin','Chen','Zook','Aldrich']

# treeview
table = ttk.Treeview(
    window,
    columns = ('first', 'last', 'email'),
    show = 'headings'
    )
table.heading('first', text = 'First Name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'Email')
table.pack()

# insert values into a table
#table.insert(parent = '',
#             index = 0,
#             values = ('John', 'Doe', 'johndoe@gmail.com'))
for i in range(100):
    table.insert(
        parent = '',
        index = 0,
        values = (choice(first_name), choice(last_name), f'{choice(first_name)}{choice(last_name)}@gmail.com'))

# run
window.mainloop()