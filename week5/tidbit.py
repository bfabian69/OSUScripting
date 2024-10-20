def display_payment_schedule():
    
    purchase_price = float(input("Enter the purchase price: "))

    
    down_payment = 0.10 * purchase_price
    annual_interest_rate = 0.12
    monthly_payment = 0.05 * purchase_price

    
    balance = purchase_price - down_payment

    
    print("\nPayment Schedule")
    print(f"{'Month':<6}{'Balance':<12}{'Interest':<12}{'Principal':<12}{'Payment':<12}{'Remaining Balance':<18}")
    print("-" * 72)

    month = 1
    while balance > 0:
        
        interest = balance * (annual_interest_rate / 12)
        
        
        principal = monthly_payment - interest

        
        if balance < monthly_payment:
            monthly_payment = balance + interest
            principal = balance

        
        remaining_balance = balance - principal

        
        print(f"{month:<6}${balance:<11,.2f}${interest:<11,.2f}${principal:<11,.2f}${monthly_payment:<11,.2f}${remaining_balance:<17,.2f}")

        
        balance = remaining_balance
        month += 1


display_payment_schedule()
