from tkinter import messagebox
from view import CalculatorView


class CalculatorController:
    """Controller class for the calculator."""

    def __init__(self, window) -> None:
        """
        Initialize the calculator controller.

        Args:
            window: The Tkinter window.
        """
        self.window = window
        self.view: CalculatorView = CalculatorView(self)

        self.current_expression = ''

    def button_click(self, value: str) -> None:
        """Handle button click events."""
        if value == '=':
            self.calculate_result()
        elif value == 'C':
            self.clear_entry()
        else:
            self.current_expression += value
            self.update_entry()

    def calculate_result(self) -> None:
        """Calculate and display the result."""
        try:
            result = str(eval(self.current_expression))
            self.current_expression = result
            self.update_entry()
        except Exception as e:
            messagebox.showerror('Error', 'Invalid Expression')
            self.clear_entry()

    def clear_entry(self) -> None:
        """Clear the entry."""
        self.current_expression = ''
        self.update_entry()

    def update_entry(self) -> None:
        """Update the entry widget with the current expression."""
        self.view.entry.configure(state='normal')
        self.view.entry.delete(0, 'end')
        self.view.entry.insert('end', self.current_expression)
        self.view.entry.configure(state='readonly')