import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = choice.get()

    if operation == '1':
        result.set(add(num1, num2))
    elif operation == '2':
        result.set(subtract(num1, num2))
    elif operation == '3':
        result.set(multiply(num1, num2))
    elif operation == '4':
        res = divide(num1, num2)
        if isinstance(res, str):
            result.set(res)
        else:
            result.set(res)

root = tk.Tk()
root.title("Simple Calculator")

label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

choice = tk.StringVar()
choice.set('1')  # default operation (Addition)

radio_add = tk.Radiobutton(root, text="Addition", variable=choice, value='1')
radio_add.grid(row=2, column=0)

radio_subtract = tk.Radiobutton(root, text="Subtraction", variable=choice, value='2')
radio_subtract.grid(row=2, column=1)

radio_multiply = tk.Radiobutton(root, text="Multiplication", variable=choice, value='3')
radio_multiply.grid(row=3, column=0)

radio_divide = tk.Radiobutton(root, text="Division", variable=choice, value='4')
radio_divide.grid(row=3, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, columnspan=2)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=5, columnspan=2)

root.mainloop()
