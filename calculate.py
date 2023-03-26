import tkinter as tk
import tkinter.ttk as ttk


class Calculator:
    def __init__(self, window):
        self.window=window
        window.title('Калькулятор')
        self.display = tk.Entry(master, width=30, borderwidth=5, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)
        self.create_button(".", 4, 0)
        self.create_button("C", 4, 2)
        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)
        self.create_button("=", 5, 3)


    def create_button(self, text, row, col):
        button = tk.Button(self.window, text=text, padx=20, pady=10, font=('Arial', 16),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
