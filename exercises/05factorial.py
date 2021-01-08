# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#

def factorial(n):
    if n == 0:
        print(1)
    elif n <= 2:
        print(n)
    else:
        product = 1
        for i in range(1, n + 1):
            product *= i
        print(product)

factorial(5)