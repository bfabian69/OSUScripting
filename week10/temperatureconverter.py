import tkinter as tk
from tkinter import ttk, messagebox

class TemperatureConverter(tk.Tk):
    """A simple temperature converter application."""

    def __init__(self):
        """Initialize the GUI components."""
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("300x150")

        ttk.Label(self, text="Fahrenheit:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self, text="Celsius:").grid(row=0, column=1, padx=10, pady=10)

        self.fahrenheitField = ttk.Entry(self)
        self.fahrenheitField.grid(row=1, column=0, padx=10, pady=10)
        self.fahrenheitField.insert(0, "32.0")

        self.celsiusField = ttk.Entry(self)
        self.celsiusField.grid(row=1, column=1, padx=10, pady=10)
        self.celsiusField.insert(0, "0.0")

        self.toCelsiusButton = ttk.Button(self, text=">>>>>", command=self.convertToCelsius)
        self.toCelsiusButton.grid(row=2, column=0, padx=10, pady=10)

        self.toFahrenheitButton = ttk.Button(self, text="<<<<<", command=self.convertToFahrenheit)
        self.toFahrenheitButton.grid(row=2, column=1, padx=10, pady=10)

    def convertToCelsius(self):
        """Converts the Fahrenheit value to Celsius and updates the Celsius field."""
        try:
            fahrenheit = float(self.fahrenheitField.get())
            celsius = (fahrenheit - 32) * 5/9
            self.celsiusField.delete(0, tk.END)
            self.celsiusField.insert(0, f"{celsius:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for Fahrenheit.")

    def convertToFahrenheit(self):
        """Converts the Celsius value to Fahrenheit and updates the Fahrenheit field."""
        try:
            celsius = float(self.celsiusField.get())
            fahrenheit = (celsius * 9/5) + 32
            self.fahrenheitField.delete(0, tk.END)
            self.fahrenheitField.insert(0, f"{fahrenheit:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for Celsius.")

if __name__ == "__main__":
    app = TemperatureConverter()
    app.mainloop()
