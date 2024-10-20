def mean(numbers):
    """Computes the average (mean) of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Computes the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 1:  
        return sorted_numbers[mid]
    else:  
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

def mode(numbers):
    """Computes the mode of a list of numbers (most frequent value)."""
    if not numbers:
        return 0
    frequency_dict = {}
    for num in numbers:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1
  
    max_frequency = max(frequency_dict.values())
    modes = [key for key, value in frequency_dict.items() if value == max_frequency]

    return modes[0] if len(modes) == 1 else modes

def main():
    """Tests the mean, median, and mode functions with a given list of numbers."""
    test_numbers = [10, 20, 20, 30, 40, 40, 40, 50, 60, 60]

    print("Test list of numbers:", test_numbers)
    print("Mean:", mean(test_numbers))
    print("Median:", median(test_numbers))
    print("Mode:", mode(test_numbers))

if __name__ == "__main__":
    main()
