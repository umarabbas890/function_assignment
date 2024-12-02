#Create a function that takes a list of integers and returns the sum of all even numbers.

def sum_evens(numbers):
    total = 0

    for num in numbers:
      if num % 2 == 0:
        total +=num
    return total
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f"The Sum of even numbers are:, {sum_evens(numbers)}")
