def inputFloat(prompt="Please enter a floating-point number: "):
    """Prompts the user for a floating-point number, ensuring valid input."""
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            return value
        except ValueError:
            if user_input.count('.') > 1 or not all(c.isdigit() or c == '.' for c in user_input):
                print("Invalid input. Please enter a valid floating-point number.")
            else:
                print("Input could not be converted to a float. Please try again.")

if __name__ == "__main__":
    print("Testing inputFloat function...")
    float_number = inputFloat("Enter a floating-point number: ")
    print(f"You entered: {float_number}")
