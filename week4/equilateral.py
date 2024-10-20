

def is_equilateral(a, b, c):
    """Check if the triangle is equilateral"""
    if a == b == c:
        return True
    return False

def main():
    
    try:
        a = float(input("Enter the length of the first side: "))
        b = float(input("Enter the length of the second side: "))
        c = float(input("Enter the length of the third side: "))

       
        if is_equilateral(a, b, c):
            print("The triangle is an equilateral triangle.")
        else:
            print("The triangle is not an equilateral triangle.")
    except ValueError:
        print("Please enter valid numbers for the side lengths.")

if __name__ == "__main__":
    main()
