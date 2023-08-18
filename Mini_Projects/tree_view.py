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
table.pack(fill = 'both', expand = True)

# insert values into a table
#table.insert(parent = '',
#             index = 0,
#             values = ('John', 'Doe', 'johndoe@gmail.com'))
for i in range(100):
    table.insert(
        parent = '',
        index = 0,
        values = (choice(first_name), choice(last_name), f'{choice(first_name)}{choice(last_name)}@gmail.com'))

# events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    print('delete')
    for i in table.selection():
        table.delete(i)

# events inside a table
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# run
window.mainloop()