def calculate_population_growth(initial_population, growth_rate, growth_period, total_hours):
    """Calculate the total population after a given number of hours."""

    periods = total_hours // growth_period
    final_population = initial_population * (growth_rate ** periods)
    
    return final_population

def main():
    try:
        initial_population = int(input("Enter the initial number of organisms: "))
        growth_rate = float(input("Enter the rate of growth (e.g., 2 for doubling): "))
        growth_period = int(input("Enter the number of hours to achieve this growth rate: "))
        total_hours = int(input("Enter the total number of hours during which the population grows: "))

        if initial_population <= 0 or growth_rate <= 0 or growth_period <= 0 or total_hours < 0:
            print("Please enter valid inputs. Initial population, growth rate, and growth period must be greater than 0, and total hours must be non-negative.")
        else:
 
            final_population = calculate_population_growth(initial_population, growth_rate, growth_period, total_hours)
            print(f"The predicted total population after {total_hours} hours is {int(final_population)} organisms.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
