
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_YEAR = 365 

years = int(input("Enter the number of years: "))

minutes = years * DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR

print(f"The number of minutes in {years} years is: {minutes}")
