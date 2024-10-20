import math

def guess_number():
    print("Think of a number between the lower and upper bounds.")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    
    max_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    print(f"I will guess your number in no more than {max_guesses} attempts.")

    attempts = 0
    while lower_bound <= upper_bound:
        attempts += 1
        guess = (lower_bound + upper_bound) // 2
        print(f"Is your number {guess}?")
        
        hint = input("Enter 'high' if my guess is too high, 'low' if it's too low, or 'correct' if I guessed right: ").lower()

        
        if hint == 'high' and guess <= lower_bound:
            print("Your hint is inconsistent. Try again.")
        elif hint == 'low' and guess >= upper_bound:
            print("Your hint is inconsistent. Try again.")
        elif hint == 'correct':
            print(f"I guessed your number in {attempts} attempts!")
            break
        elif hint == 'high':
            upper_bound = guess - 1
        elif hint == 'low':
            lower_bound = guess + 1
        else:
            print("Invalid input. Please enter 'high', 'low', or 'correct'.")

        
        if lower_bound > upper_bound:
            print("It seems there were inconsistent hints. Please try again with consistent hints.")
            break


guess_number()
