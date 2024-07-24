# Import math Library
import math

def print_star_pattern(n,c):
    mid = n/2 + 1
    for i in range(1, n + 1):
        y = math.floor((3*c*abs(mid-i))**2)
        print(' ' * y + '*')

def main():
    try:
        n = int(input("Enter the number of rows for the snake pattern: "))
        c = float(input("Enter the value of curvature  for the snake pattern: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        print("Snake pattern:")
        print_star_pattern(n,c)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()