# Function to count vowels and consonants
def count_vowels_consonants(s):
    # Defining vowel characters
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    # Iterating through each character in the string
    for char in s:
        # Checking if the character is a vowel
        if char in vowels:
            vowel_count += 1
        # Checking if the character is a consonant
        elif char.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count

# Taking a string as input from the user
input_string = input("Enter a string: ")

# Counting vowels and consonants
vowel_count, consonant_count = count_vowels_consonants(input_string)

# Printing the results
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
