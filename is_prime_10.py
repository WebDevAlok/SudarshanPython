# Function to check if a number is prime
def is_prime(n):
    # Edge cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check for factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            print(i)
            return False
    
    return True

# Taking input from the user
number = int(input("Enter a number to check if it is prime: "))

# Checking if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
