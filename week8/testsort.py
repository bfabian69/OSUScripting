def isSorted(lst):
    """Checks if the list is sorted in ascending order."""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

if __name__ == "__main__":

    test_cases = [
        ([], True),
        ([1], True),
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([1, 1, 2, 2, 3, 4, 5], True),
        ([1, 3, 2, 4, 5], False),
    ]

    for i, (lst, expected) in enumerate(test_cases, start=1):
        result = isSorted(lst)
        print(f"Test case {i}: {lst} - Expected: {expected}, Got: {result}")
        assert result == expected, f"Test case {i} failed!"

    print("All tests passed!")
