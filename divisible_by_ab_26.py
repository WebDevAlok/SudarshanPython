def is_divisible_by_a_and_b(number, a, b):
    return number % a == 0 and number % b == 0

try:
    # Get user input for the number, a, and b
    number = int(input("Enter a number: "))
    a = int(input("Enter the first divisor: "))
    b = int(input("Enter the second divisor: "))

    # Check if the number is divisible by both a and b
    if is_divisible_by_a_and_b(number, a, b):
        print(f"{number} is divisible by both {a} and {b}.")
    else:
        print(f"{number} is not divisible by both {a} and {b}.")

except ValueError:
    print("Invalid input. Please enter valid integers for the number and divisors.")
