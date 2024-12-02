# Advanced Function Questions
# Create a function that takes a string and counts the frequency of each character.

def count_character(string):
    frequency = {}
    for char in string:
        if char in frequency:
         
         frequency[char] += 1
        else:
         frequency[char] = 1
    return frequency

string = input("Enter Your String: ")
print("Character frequency:", count_character(string))    
