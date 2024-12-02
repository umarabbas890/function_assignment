# Intermediate Function Questions
# Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.
# def gcd(a, b):
#     while b != 0:  # Repeat until the remainder is 0
#         a, b = b, a % b  # Update a to b, and b to the remainder of a divided by b
#     return a

# # Example usage
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")

def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter 2nd number: "))
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")