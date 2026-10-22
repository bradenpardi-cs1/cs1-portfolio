#LoanPayment.py


"""This program will calculate a monthly payment, total spend over the 
loan term, and how much the bank made for a morgage. The user will 
their principle, interest rate, and how many years the loan is for."""

def loan_payment(principle, interest, years):
    monthly_payment = (principle * (interest / 12)) / (1 - ((1 + (interest / 12)) ** ((-12) * (years))))
    return monthly_payment

def calc_month(principle, interest):
    month_chart = (principle * interest * (1 / 12))
    return month_chart

#Main Program

loan_amount = int(input("Enter the loan amount:"))
annual_rate = float(input("Enter annual rate as a decemial:"))
number_years = int(input("Enter the total number of years of the loan:"))

print()

total_payments = loan_payment(loan_amount, annual_rate, number_years) * (12) * number_years
interest_paid = total_payments - loan_amount

print(f"The monthly payment will be ${loan_payment(loan_amount, annual_rate, number_years):.2f}")
print(f"The total payments over {number_years} years will be ${total_payments:.2f}")
print(f"The total interest paid over {number_years} will be ${interest_paid:.2f}")

print()

print("loan Amorization Table:")
print("Month", "Interest Payment", "Principal Payment", "Remaining Balance", sep = "\t\t")

p_payment = loan_payment(loan_amount, annual_rate, number_years)

for month in range(number_years * 12):
    
    interest_payment = loan_amount * (annual_rate * (1 / 12))
    
    principal_payment = p_payment - interest_payment
    
    loan_amount = loan_amount -  principal_payment
    
    print(f"{month + 1:<11} {interest_payment:<23.2f} {principal_payment:<23.2f} {loan_amount:.2f}")
    
