def display_salary_schedule():
   
    starting_salary = float(input("Enter the starting salary (use commas if needed): ").replace(',', ''))
    percentage_increase = float(input("Enter the annual percentage increase (e.g., enter 2 for 2%): "))
    years = int(input("Enter the number of years in the schedule: "))

    
    print("\nSalary Schedule")
    print("Year\tSalary")
    print("-" * 20)

    
    current_salary = starting_salary
    for year in range(1, years + 1):
        print(f"{year}\t${current_salary:,.2f}")
       
        current_salary += current_salary * (percentage_increase / 100)


display_salary_schedule()

