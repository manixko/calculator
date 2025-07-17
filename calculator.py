import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("320x600")
        self.configure(bg="#1c1c1c")
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.expression = ""
        self.result_var = tk.StringVar()

        # Fonts
        display_font = font.Font(family="Arial", size=24, weight="bold")
        button_font = font.Font(family="Arial", size=14, weight="bold")

        # Result display
        result_display = tk.Label(self, textvariable=self.result_var, font=display_font, bg="#1c1c1c", fg="#ffffff", anchor="e", padx=10)
        result_display.pack(expand=True, fill="both")

        # Button layout
        buttons = [
            '%', 'C', 'del', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            'AC', '0', '.', '='
        ]

        button_frame = tk.Frame(self, bg="#1c1c1c")
        button_frame.pack(expand=True, fill="both")

        # Creating buttons in a grid
        row_val = 0
        col_val = 0
        for button in buttons:
            if button in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                btn = tk.Button(button_frame, text=button, font=button_font, bg="#4e4e4e", fg="#ffffff", command=lambda b=button: self.update_expression(b))
            elif button in ['=', 'C', 'del', 'AC']:
                btn = tk.Button(button_frame, text=button, font=button_font, bg="#007acc", fg="#ffffff", command=lambda b=button: self.special_functions(b))
            else:
                btn = tk.Button(button_frame, text=button, font=button_font, bg="#007acc", fg="#ffffff", command=lambda b=button: self.update_expression(b))
            btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)

    def bind_keys(self):
        # Binding number keys
        for key in '0123456789':
            self.bind(f'<Key-{key}>', self.key_input)
        # Binding other keys
        self.bind('<Key-plus>', self.key_input)
        self.bind('<Key-equal>', self.key_input)
        self.bind('<Key-minus>', self.key_input)
        self.bind('<Key-asterisk>', self.key_input)
        self.bind('<Key-slash>', self.key_input)
        self.bind('<Key-period>', self.key_input)  
        self.bind('<Return>', self.key_input)
        self.bind('<BackSpace>', self.key_input)
        self.bind('<Delete>', self.key_input)
        self.bind('<Key-c>', self.key_input)
        self.bind('<Key-C>', self.key_input)

    def key_input(self, event):
        key = event.keysym
        if key in '0123456789':
            self.update_expression(key)
        elif key in ['plus', 'minus', 'asterisk', 'slash', 'equal']:
            self.update_expression({'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/', 'equal': '='}[key])
        elif key == 'Return':
            self.calculate()
        elif key == 'BackSpace':
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression)
        elif key in ['Delete', 'c', 'C']:
            self.clear()

    def update_expression(self, value):
        self.expression += value
        self.result_var.set(self.expression)

    def special_functions(self, key):
        if key == "C":
            self.clear()
        elif key == "del":
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression)
        elif key == "AC":
            self.clear()
        elif key == "=":
            self.calculate()

    def clear(self):
        self.expression = ""
        self.result_var.set("")

    def calculate(self):
        try:
            result = eval(self.expression)
            self.result_var.set(result)
            self.expression = str(result)
        except:
            self.result_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
    