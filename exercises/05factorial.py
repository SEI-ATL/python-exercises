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

def factorial(num):
    if num <= 1:
        return 1
    else:
        return (num * factorial(num - 1))

print(factorial(5))

# Class Example WITH Edge Cases
# def factorial(n):
#     if type(n) != int:
#         raise TypeError('Needs to be an integer')
#     if n < 1:
#         raise ValueError('Number needs to be a positive number')
#     result = 1

#     for i in range(result, (n + 1)):
#         result = result * i
#     return result


# print(factorial(5))