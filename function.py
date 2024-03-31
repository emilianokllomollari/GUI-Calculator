from tkinter import *
from asteval import Interpreter

class CalculatorFunction:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.aval = Interpreter()

    def insert(self, digit):
        self.text_widget.insert(END, digit)

    def operator(self, operator):
        self.text_widget.insert(END, operator)

    def equal(self):
        user_input = self.text_widget.get("1.0", END).strip()
        result = self.aval(user_input)
        self.text_widget.insert(END, f"\n= {result}")

