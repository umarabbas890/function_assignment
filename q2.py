# Basic Function Questions

# Take input from the user
numb1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Function to calculate the sum
def num_sum(num1, num2):
    sum = num1 + num2
    return sum

# Call the function and print the result
result = num_sum(numb1, num2)
print("The sum of", numb1, "and", num2, "is", result)


