

def calculate_total_distance(initial_height, bounciness_index, num_bounces):
    """Calculate the total distance traveled by the ball after a specified number of bounces."""
    total_distance = 0
    height = initial_height

    for _ in range(num_bounces):
        total_distance += height
        height *= bounciness_index
        total_distance += height

    return total_distance

def main():
    try:
        initial_height = float(input("Enter the initial height from which the ball is dropped (in feet): "))
        bounciness_index = float(input("Enter the bounciness index of the ball (between 0 and 1): "))
        num_bounces = int(input("Enter the number of bounces: "))

        if initial_height <= 0 or bounciness_index <= 0 or bounciness_index >= 1 or num_bounces < 0:
            print("Please enter valid inputs. The height must be positive, the bounciness index should be between 0 and 1, and the number of bounces should be non-negative.")
        else:
            total_distance = calculate_total_distance(initial_height, bounciness_index, num_bounces)
            print(f"The total distance traveled by the ball is {total_distance:.2f} feet.")
    except ValueError:
        print("Invalid input. Please enter numerical values for height, bounciness index, and number of bounces.")

if __name__ == "__main__":
    main()
