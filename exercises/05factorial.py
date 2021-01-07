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

    # recursive
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


print(factorial(5))


def factorial2(n):

    fact = 1

    for i in range(1, n+1):
        fact = fact * i
    return fact


print(factorial2(5))
