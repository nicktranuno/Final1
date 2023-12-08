from tkinter import Tk, Button, Entry


class CalculatorView:
    """View class for the calculator."""

    def __init__(self, controller: 'CalculatorController') -> None:
        """
        Initialize the calculator view.

        controller (CalculatorController): The associated controller.
        """
        self.controller: 'CalculatorController' = controller

        # Entry to display the current expression
        self.entry = Entry(controller.window, width=16, font=('Arial', 16), bd=5, insertwidth=4, justify='right', state='readonly')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operators
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button_text in buttons:
            Button(controller.window, text=button_text, width=4, height=2, font=('Arial', 16),
                   command=lambda t=button_text: self.controller.button_click(t)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1