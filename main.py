from ui import CalculatorUI
from function import CalculatorFunction

def main():
    calc_ui = CalculatorUI()
    calc_function = CalculatorFunction(calc_ui)
    calc_ui.start()

if __name__ == '__main__':
    main()