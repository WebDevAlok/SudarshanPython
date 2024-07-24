# Taking input from the user
n = int(input("Enter a number: "))

# Calculating the sum of all numbers from 1 to n
total_sum = 0
for i in range(1, n + 1):
    total_sum += i

# Printing the result
print(f"The sum of all numbers from 1 to {n} is {total_sum}")