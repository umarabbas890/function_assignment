# Dear students, please do the following assignment to practice functions:

# Basic Function Questions

# 3. Write a function to find the factorial of a number using recursion.
# Taking user input and converting it to an integer
num = int(input("Enter Your Number: "))

# Defining the recursive function to calculate the factorial
def factorial(n):
    # Base case: if n is 0, return 1 (since 0! = 1)
    if n == 0:
        return 1
    # Recursive case: return n * factorial of n-1
    else:
        return n * factorial(n - 1)

# Printing the result of the factorial calculation
print(f"The factorial of {num} is {factorial(num)}")
