# Taking two strings as input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Checking if the strings are of the same length
if len(string1) != len(string2):
    print("The strings must be of the same length.")
else:
    # Intersperse the second string into the first one
    interspersed_string = ''.join([string1[i] + string2[i] for i in range(len(string1))])

    # Printing the interspersed string
    print("Interspersed string:", interspersed_string)
