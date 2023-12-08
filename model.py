from tkinter import Tk
from controller import CalculatorController


def main():
    """Creates a tkinter window and starts main event loop"""
    window = Tk()
    window.title('Calculator')
    window.geometry('250x375')
    window.resizable(False, False)

    calculator_controller = CalculatorController(window)

    window.mainloop()


if __name__ == '__main__':
    main()