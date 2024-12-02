# Advanced Function Questions

# Write a function that calculates the power of a number without using the ** operator.

def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base

    if exponent < 0:
     result = 1/ result
    return result
print(power(2, 7))
print(power(3, 7))


