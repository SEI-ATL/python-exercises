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

def factorial(num):
    factorial_number = [i for i in range(1, num + 1)]
    sum = 1
    for number in factorial_number:
        sum *= number
    return sum

print(factorial(5))