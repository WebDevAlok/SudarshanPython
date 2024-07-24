# Function to check if a string is a palindrome
def is_palindrome(s):
    # Removing any spaces and converting to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Checking if the string is equal to its reverse
    return s == s[::-1]

# Taking a string as input from the user
input_string = input("Enter a string: ")

# Checking if the string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
