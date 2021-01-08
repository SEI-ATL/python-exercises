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
# assume positive 

from functools import reduce

def factorial(n):
    sum = 1
    while n > 1 :
        sum = sum * n
        n -= 1
    return sum

print(factorial(5))

def factorial_reduce(n):
    return reduce(lambda x,y: x*y, list(range(1, n+1)))

print(factorial_reduce(5))