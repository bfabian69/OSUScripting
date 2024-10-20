
hourlyWage = float(input("Enter the hourly wage: "))
regularHours = float(input("Enter the total number of regular hours: "))
overtimeHours = float(input("Enter the total number of overtime hours: "))

overtimePay = overtimeHours * hourlyWage * 1.5

totalPay = (regularHours * hourlyWage) + overtimePay

print(f"The employee's total weekly pay is: ${totalPay:.2f}")
