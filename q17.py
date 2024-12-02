# Advanced Function Questions
# Write a function that takes a list and removes all duplicate elements.
def remove_duplicates(lst):
    unique_list = []  # Initialize an empty list to store unique elements
    for item in lst:
        if item not in unique_list:  # Add item only if it's not already in unique_list
            unique_list.append(item)
    return unique_list
example_list = [1, 2, 2, 3, 4, 4, 5]
print(f"Original list: {example_list}")
print(f"List without duplicates: {remove_duplicates(example_list)}")
