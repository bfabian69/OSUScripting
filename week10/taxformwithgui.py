import tkinter as tk
from tkinter import ttk, messagebox

class TaxCalculator(tk.Tk):
    """A simple tax calculator application."""

    def __init__(self):
        """Initialize the GUI components."""
        super().__init__()
        self.title("Tax Calculator")
        self.geometry("400x200")

        ttk.Label(self, text="Gross Income ($):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.grossIncomeField = ttk.Entry(self)
        self.grossIncomeField.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self, text="Number of Dependents:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.dependentsField = ttk.Entry(self)
        self.dependentsField.grid(row=1, column=1, padx=10, pady=10)

        calculateButton = ttk.Button(self, text="Calculate Tax", command=self.calculateTax)
        calculateButton.grid(row=2, column=0, columnspan=2, pady=10)

        self.resultLabel = ttk.Label(self, text="Tax Amount: $0.00")
        self.resultLabel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculateTax(self):
        """Calculate and display the tax amount."""
        try:
            grossIncome = float(self.grossIncomeField.get())
            dependents = int(self.dependentsField.get())

            if grossIncome < 0 or dependents < 0:
                messagebox.showerror("Input Error", "Income and dependents must be non-negative.")
                return

            STANDARD_DEDUCTION = 10000
            DEPENDENT_DEDUCTION = 3000
            TAX_RATE = 0.20

            taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * dependents)
            taxableIncome = max(taxableIncome, 0)

            tax = taxableIncome * TAX_RATE

            self.resultLabel.config(text=f"Tax Amount: ${tax:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for income and dependents.")

if __name__ == "__main__":
    app = TaxCalculator()
    app.mainloop()
