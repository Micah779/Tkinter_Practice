import tkinter as tk

calculation = "" 

def add_to_calculation(symbol):
  global calculation
  calculation += str(symbol)
  text_result.delete(1.0, "end")
  text_result.insert(1.0, calculation)

def evaluate_calculation():
  global calculation
  try:
    calculation = str(eval(calculation))
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
  except:
    clear_field()
    text_result.insert(1.0, "Error")  

def clear_field():
  global calculation
  calculation = ""
  text_result.delete(1.0, "end")

def calculate_percentage():
  global calculation
  try:
    calculation = str(float(calculation) / 100)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
  except:
    clear_field()
    text_result.insert(1.0, "Error")

root = tk.Tk()
root.title("Calculator")

text_result = tk.Text(root, height=2, width=25, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

# Buttons for 2-9 and 0

btn_dec = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_dec.grid(row=5, column=1)

btn_percent = tk.Button(root, text="%", command=calculate_percentage, width=5, font=("Arial", 14)) 
btn_percent.grid(row=5, column=2)

btn_add = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_add.grid(row=2, column=4) 

# Other operator buttons (-, *, /)

btn_eq = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))  
btn_eq.grid(row=5, column=4)

btn_clear = tk.Button(root, text="Clear", command=clear_field, width=10, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
