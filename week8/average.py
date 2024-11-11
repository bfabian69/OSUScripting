def compute_average(filename):
    """Computes the average of numbers in the given file."""
    try:
        with open(filename, 'r') as file:
            numbers = list(map(float, filter(None, map(str.strip, file.readlines()))))
        if numbers:
            average = sum(numbers) / len(numbers)
            print(f"The average is: {average}")
        else:
            print("No numbers to calculate an average.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: The file contains invalid data that cannot be converted to numbers.")

if __name__ == "__main__":
    filename = input("Enter the name of the file containing numbers: ")
    compute_average(filename)
