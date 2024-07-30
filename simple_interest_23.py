# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

try:
    # Get user input for principal, rate, and time
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = float(input("Enter the time (in years): "))

    # Calculate simple interest
    interest = calculate_simple_interest(principal, rate, time)

    # Print the result
    print(f"The simple interest is: {interest}")

except ValueError:
    print("Invalid input. Please enter valid numbers for principal, rate, and time.")
