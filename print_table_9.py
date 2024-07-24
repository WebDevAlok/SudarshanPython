# Taking input from the user
n = int(input("Enter the number for the multiplication table: "))
i = int(input("Enter the starting value of the range: "))
j = int(input("Enter the ending value of the range: "))

# Printing the multiplication table from i to j
print(f"Multiplication table for {n} from {i} to {j}:")
for num in range(i, j + 1):
    print(f"{n} x {num} = {n * num}")
