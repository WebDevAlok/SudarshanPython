def add(a, b):
    return a + b

def main():
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid numbers.")
    
    result = add(a, b)
    print(f"The sum of {a} and {b} is: {result}")

if __name__ == "__main__":
    main()
