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
    fact = 1
    
    list = []
    result = 1
    for i in range(1, num + 1):
        list.append(i)
        print(list)

    for i in range(1, num +1):
        fact = fact * i
    print(fact)
    # for i in list:
    #     if i != 0:
    #         result = result * i
    #         return print(result)
        

factorial(5)