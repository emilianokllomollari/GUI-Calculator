from tkinter import *
from function import CalculatorFunction

FONT = ("Ariel", 20)
class CalculatorUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.config(padx=20, pady=20)

        self.text_widget = Text(width=19, height=7, font=FONT)
        self.text_widget.grid(column=1, row=0, columnspan=4)

        self.calc = CalculatorFunction(self.text_widget)

        button_texts = [
            ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), ('+', 1, 4),
            ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('-', 2, 4),
            ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('*', 3, 4),
            ('0', 4, 1), ('.', 4, 2), ('=', 4, 3), ('/', 4, 4),
        ]

        for [text, row, col] in button_texts:
            if text.isdigit():
                action = lambda digit=text: self.calc.insert(digit)
            elif text == "=":
                action = self.calc.equal
            else:
                action = lambda op=text: self.calc.insert(op)
            btn = Button(text=text, command=action, font=FONT, width=2)
            btn.grid(column = col, row=row)


    def start(self):
        self.window.mainloop()