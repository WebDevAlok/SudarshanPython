# Function to calculate square, cube, and 2^n of a given number
def calculate_powers(n):
    square = n ** 2
    cube = n ** 3
    power_of_two = 2 ** n
    return square, cube, power_of_two

# Taking input from the user
n = int(input("Enter a number: "))

# Calculating the results
square, cube, power_of_two = calculate_powers(n)

# Printing the results
print(f"Square of {n}: {square}")
print(f"Cube of {n}: {cube}")
print(f"2^{n}: {power_of_two}")
