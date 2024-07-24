def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    try:
        n = int(input("Enter the number of Fibonacci numbers to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        fib_sequence = fibonacci_sequence(n)
        print("Fibonacci sequence:")
        print(fib_sequence)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
