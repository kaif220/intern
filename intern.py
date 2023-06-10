def calculate_emi(principal, tenure, interest_rate):
    # Convert interest rate from percentage to decimal
    interest_rate_decimal = interest_rate / 100

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate_decimal / 12

    # Calculate number of monthly installments
    num_installments = tenure * 12

    # Calculate EMI
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** num_installments) / ((1 + monthly_interest_rate) ** num_installments - 1)

    return emi


# Get user input
principal_amount = float(input("Enter the principal amount: "))
tenure_years = int(input("Enter the tenure (in years): "))
interest_rate = float(input("Enter the interest rate (in percentage): "))

# Calculate and print EMI
emi_amount = calculate_emi(principal_amount, tenure_years, interest_rate)
print("The Equated Monthly Installment (EMI) amount is: ", round(emi_amount, 2))