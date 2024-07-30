def populate_list(n):
    L = []
    for i in range(1, n+1):
        L.append(i)
    return L

def main():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n <= 0:
                raise ValueError("The number must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    L = populate_list(n)
    print(f"The first {n} natural numbers are: {L}")

if __name__ == "__main__":
    main()
