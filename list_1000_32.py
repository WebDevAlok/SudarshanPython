import random

def populate_list(n):
    L = [random.randint(1, 1000) for _ in range(n)]
    return L

def main():
    while True:
        try:
            n = int(input("Enter the number of random numbers you want in the list: "))
            if n <= 0:
                raise ValueError("The number must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    L = populate_list(n)
    print(f"The list of {n} random numbers is: {L}")

if __name__ == "__main__":
    main()
