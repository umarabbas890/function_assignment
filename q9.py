# Write a function to check whether a string is a palindrome.


def palindrom(phrase):
    return phrase == phrase[::-1]
phrase = input("Enter a string: ")
if palindrom(phrase):
    print(f'"{phrase}",  is a palindrom')
else:
    print(f'"{phrase}", is not a palindrom')
