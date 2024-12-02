# Intermediate Function Questions
# Create a function that accepts a dictionary and returns the key with the highest value.

def key_highest_value(d):
    return max(d, key=d.get)

dict= {"a": 10, "b":25, "c": 25, "e": 30}
print(f"The key with hight value is: {key_highest_value(dict)}")