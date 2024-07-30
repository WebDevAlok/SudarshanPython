import math

def is_prime(n, known_primes):
    """Return True if n is a prime number using known primes for division test."""
    if n <= 1:
        return False
    for prime in known_primes:
        if prime > math.isqrt(n):  # No need to check beyond the square root of n
            break
        if n % prime == 0:
            return False
    return True

def primes_up_to_n(n):
    """Return a list of all prime numbers up to n (inclusive)."""
    if n < 2:
        return []

    # Start with the first prime number
    primes = [2]
    # Check only odd numbers starting from 3
    for num in range(3, n + 1, 2):
        if is_prime(num, primes):
            primes.append(num)
    return primes

def print_primes(primes):
    """Print the prime numbers in groups of 10 per line."""
    for i in range(0, len(primes), 10):
        print(" ".join(map(str, primes[i:i + 10])))

def main():
    # Get user input
    n = int(input("Enter a positive integer: "))
    primes = primes_up_to_n(n)
    
    print(f"Prime numbers up to {n}:")
    print_primes(primes)

if __name__ == "__main__":
    main()

