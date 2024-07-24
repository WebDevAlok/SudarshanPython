def print_star_pattern(n):
    for i in range(1, n + 1):
        print('*   ' * i)

def main():
    try:
        n = int(input("Enter the number of rows for the star pattern: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        print("Star pattern:")
        print_star_pattern(n)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
