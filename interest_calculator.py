# Interest Calculator

principal = float(input("Enter your initial amount of money: "))
rate = float(input("Enter the interest rate (%): "))
time = int(input("Enter the amount of time (in months): "))
interest_type = float(input("Enter the type of interest you have:\n1. Simple Interest\n2. Compound Interest\n"))

years = time/12
percent = rate/100

def interest_calculator(principal, percent, years):

    interest = principal * percent * years

    total = interest + principal

    print(f"You would receive an interest of {interest:.2f} after {time} months, and your total amount of money will be {total:.2f}.")

    
    if interest_type == 1:
        total_simple = principal + interest * 5 
        print(f"\nAfter 5 years, you will have a total of {total_simple:.2f} in money.")
    else:
        total_compound = principal * (1 + percent)**5
        print(f"\nAfter 5 years, you will have a total of {total_compound:.2f} in money.")

    
interest_calculator(principal, percent, years)
