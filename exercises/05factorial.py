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
    fact_nums = [x for x in range(1,n+1)]
    total = 1
    for num in fact_nums:
        total *= num
    return total