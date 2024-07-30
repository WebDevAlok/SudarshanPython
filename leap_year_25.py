def is_leap_year(year):
    # A year is a leap year if it is divisible by 4, except for years that are divisible by 100,
    # unless they are also divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

try:
    # Get user input for the year
    year = int(input("Enter a year to check if it is a leap year: "))

    # Check if the year is a leap year
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

except ValueError:
    print("Invalid input. Please enter a valid year.")
