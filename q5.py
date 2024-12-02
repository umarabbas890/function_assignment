# Dear students, please do the following assignment to practice functions:

# Basic Function Questions


# 5. Create a function to check if a given number is prime.
import math

def is_prime(n):
    # Numbers less than 2 are not prime
    if n <= 1:
        return False
    
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If n is divisible by i, it's not prime
            return False
    
    # If no divisors were found, it's a prime number
    return True

# Example usage
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
