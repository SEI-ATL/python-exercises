# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
def factorial(input):
    fact = 1
    for i in range(1, input+1):
        fact = fact * i
    return fact
user_input = input('Enter a number: ')
user_integer = int(user_input)
answer = str(factorial(user_integer))
print('The factorial of ' + user_input + ' is ' + answer)
# Example method call
#
# factorial(5)
#
# > 120
#
