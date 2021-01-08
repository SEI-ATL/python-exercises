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
    if num > 1:
        return (num * factorial(num - 1))
    elif num == 1:
        return 1
    else:
        print('please type in a positive number')
 
print(factorial(4))


def factorial2(num):
    if num < 1:
        raise ValueError('Number needs to be positive number') 
    result = 1
    
    for i in range(result, (num + 1)):
        result = result * i
    return result

print(factorial2(4))