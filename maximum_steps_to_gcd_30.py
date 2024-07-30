def gcd(a, b):
    steps = 0
    while b != 0:
        a, b = b, a % b
        steps += 1
    return a, steps

def find_max_steps_gcd(k):
    max_steps = 0
    max_a = 0
    max_b = 0
    lower_bound = 10**(k-1)
    upper_bound = 10**k - 1
    
    for a in range(lower_bound, upper_bound + 1):
        for b in range(lower_bound, upper_bound + 1):
            _, steps = gcd(a, b)
            if steps > max_steps:
                max_steps = steps
                max_a = a
                max_b = b
                
    return max_a, max_b, max_steps

try:
    # Get user input for the number of digits k
    k = int(input("Enter the number of digits k: "))

    # Find the two k-digit numbers that take the maximum number of steps to find the GCD
    max_a, max_b, max_steps = find_max_steps_gcd(k)

    # Print the results
    print(f"The two {k}-digit numbers that take the maximum number of steps ({max_steps}) to find the GCD are {max_a} and {max_b}.")

except ValueError:
    print("Invalid input. Please enter a valid integer for k.")
