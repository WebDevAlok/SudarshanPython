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
            return False
    
    return True

# Taking input from the user
limit = int(input("Enter a number till which to print primes: "))

for i in range(1,limit):
# Checking if the number is prime
    if is_prime(i):
        print(f"{i} is a prime number.")
