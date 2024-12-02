# Advanced Function Questions
# Create a function to check if two strings are anagrams.



def is_anagram(string1, string2):
    string1 = " ".join(string1.split()).lower()
    string2 = " ".join(string2.split()).lower()

    return sorted(string1) == sorted(string2)
string1 = input("Enter your 1st string: ")
string2 = input("Enter your 2nd string: ")

if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams")
else:
    print(f"{string1} and {string2} are not anagram")
