# Intermediate Function Questions

# 7. Create a function that takes a list of numbers and returns the largest number.
def find_largest(numbers):
    # Return the largest number using max()
    return max(numbers)

# Example usage
numbers_list = [12, 45, 67, 23, 89, 34]
largest_number = find_largest(numbers_list)
print("The largest number is:", largest_number)
