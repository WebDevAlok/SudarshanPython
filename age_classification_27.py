try:
    # Get user input for age
    age = int(input("Enter your age: "))

    # Determine the age category
    if age < 18:
        print("You are a minor.")
    elif 18 <= age <= 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

except ValueError:
    print("Invalid input. Please enter a valid integer for your age.")
