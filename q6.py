# Dear students, please do the following assignment to practice functions:

# Basic Function Questions


# 6. Write a function to count the vowels in a given string.

def count_vowels(s):
    # Define the vowels
    vowels = "aeiouAEIOU"
    # Initialize the counter for vowels
    count = 0
    
    # Iterate through each character in the string
    for char in s:
        # If the character is a vowel, increment the counter
        if char in vowels:
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print(f"The number of vowels in the string is: {vowel_count}")
