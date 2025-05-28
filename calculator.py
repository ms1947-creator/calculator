import tkinter as tk
import math

# Function to handle button clicks
def press(value):
    current = input_entry.get()
    input_entry.delete(0, tk.END)
    input_entry.insert(tk.END, current + str(value))

# Function to evaluate the expression
def evaluate():
    try:
        expression = input_entry.get()
        result = str(eval(expression, {
            "sin": lambda x: math.sin(math.radians(x)),  
            "cos": lambda x: math.cos(math.radians(x)),  
            "tan": lambda x: math.tan(math.radians(x)),  
            "asin": lambda x: math.degrees(math.asin(x)) if -1 <= x <= 1 else "Error",
            "acos": lambda x: math.degrees(math.acos(x)) if -1 <= x <= 1 else "Error",
            "atan": lambda x: math.degrees(math.atan(x)),
            "sqrt": lambda x: math.sqrt(x) if x >= 0 else "Error",
            "abs": abs,
            "math": math
        }))

        output_entry.delete(0, tk.END)
        output_entry.insert(tk.END, result if result != "Error" else "Math Error")
    except Exception:
        output_entry.delete(0, tk.END)
        output_entry.insert(tk.END, "Syntax Error")

# Function to clear input and output fields
def clear():
    input_entry.delete(0, tk.END)
    output_entry.delete(0, tk.END)

# Function for backspace
def backspace():
    current = input_entry.get()
    input_entry.delete(0, tk.END)
    input_entry.insert(tk.END, current[:-1])  # Remove last character

# Create main window
window = tk.Tk()
window.title("Scientific Calculator")
window.configure(bg="#333")  # Dark background

# Styling
btn_style = {"font": ("Arial", 14), "bg": "#444", "fg": "white", "bd": 2, "relief": "ridge"}
btn_width = 5
btn_height = 2
btn_padding = 3

# Input field
input_entry = tk.Entry(window, font=("Arial", 18), justify="right", bg="#222", fg="white", bd=5)
input_entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=5, pady=5, sticky="nsew")

# Output field
output_entry = tk.Entry(window, font=("Arial", 18), justify="right", bg="#222", fg="white", bd=5)
output_entry.grid(row=1, column=0, columnspan=4, ipadx=8, ipady=10, padx=5, pady=5, sticky="nsew")

# Button layout
buttons = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
    ('(', 5, 0), ('0', 5, 1), (')', 5, 2), ('/', 5, 3),
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('C', 6, 3),
    ('asin', 7, 0), ('acos', 7, 1), ('atan', 7, 2), ('=', 7, 3),
    ('sqrt', 8, 0), ('abs', 8, 1), ('⌫', 8, 2), ('.', 8, 3)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, command=evaluate, **btn_style)
    elif text == "C":
        button = tk.Button(window, text=text, command=clear, **btn_style)
    elif text == "⌫":
        button = tk.Button(window, text=text, command=backspace, **btn_style)
    else:
        button = tk.Button(window, text=text, command=lambda t=text: press(t), **btn_style)

    button.grid(row=row, column=col, padx=btn_padding, pady=btn_padding, ipadx=8, ipady=5, sticky="nsew")

# Make buttons expand with window resizing
for i in range(9):
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)

# Run the application
window.mainloop()