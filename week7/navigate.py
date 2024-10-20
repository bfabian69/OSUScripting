# navigate.py

def navigate_file():
    """Allows user to navigate the lines of a text file."""
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        num_lines = len(lines)
        print(f"The file contains {num_lines} lines.")  
        while True:
            try:
                line_number = int(input(f"Enter a line number between 1 and {num_lines} (or 0 to quit): "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if line_number == 0:
                print("Exiting the program.")
                break
            elif 1 <= line_number <= num_lines:
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print(f"Invalid line number. Please enter a number between 1 and {num_lines}.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    navigate_file()
