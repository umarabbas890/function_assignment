# Dear students, please do the following assignment to practice functions:

# Basic Function Questions


# 4. Write a function that takes a string and returns it reversed.
def reverse_string(s):
    # Return the string reversed using slicing
    return s[::-1]

# Example usage
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")
