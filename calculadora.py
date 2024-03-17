import tkinter as tk
from tkinter import font

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.configure(bg='aquamarine2')

        self.display_font = font.Font(family="Arial", size=20, weight="bold")
        self.display = tk.Entry(master, width=20, borderwidth=5, font=self.display_font)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3)
        ]

        for (text, row, column) in buttons:
            self.create_button(text, row, column)

    def create_button(self, text, row, column):
        button_font = font.Font(family="Arial", size=15, weight="bold")
        button = tk.Button(self.master, text=text, padx=20, pady=20, font=button_font, bg='aquamarine3', command=lambda: self.handle_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def handle_click(self, value):
        if value == "C":
            self.display.delete(0, tk.END)
        elif value == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            current_text = self.display.get()
            if current_text == "Error":
                self.display.delete(0, tk.END)
            self.display.insert(tk.END, value)

def main():
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()
