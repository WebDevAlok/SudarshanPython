def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number

try:
    # Get user input for the decimal number
    decimal_number = int(input("Enter a decimal number to convert to binary: "))
    
    # Handle the case for negative numbers
    if decimal_number < 0:
        print("Please enter a non-negative integer.")
    else:
        # Convert decimal to binary
        binary_representation = decimal_to_binary(decimal_number)
        # Print the binary representation
        print(f"The binary representation of {decimal_number} is {binary_representation}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
