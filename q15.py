# Advanced Function Questions
# Write a function to flatten a nested list.
def flatten_list(nested_list):
    flat_list = []  # Initialize an empty list to store flattened items
    for item in nested_list:
        if isinstance(item, list):  # Check if the item is a list
            flat_list.extend(flatten_list(item))  # Recursively flatten it
        else:
            flat_list.append(item)  # If it's not a list, add it to the flat list
    return flat_list

# Example usage
nested = [1, [2, [3, 4]], 5, [6, [7, 8]]]
print("Flattened list:", flatten_list(nested))
