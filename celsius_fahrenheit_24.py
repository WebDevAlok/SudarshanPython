# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

try:
    # Get user input for conversion choice
    choice = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").strip().upper()

    if choice == 'C':
        # Get user input for Celsius temperature
        celsius = float(input("Enter the temperature in Celsius: "))
        # Convert to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        # Print the result
        print(f"{celsius}°C is equal to {fahrenheit}°F")
        
    elif choice == 'F':
        # Get user input for Fahrenheit temperature
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        # Convert to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)
        # Print the result
        print(f"{fahrenheit}°F is equal to {celsius}°C")
        
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

except ValueError:
    print("Invalid input. Please enter a valid number for the temperature.")
