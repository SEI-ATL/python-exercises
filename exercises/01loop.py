# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.

def p_times(statement, num):
    number = int(num)
    sentence = str(statement)
    add_space = sentence + ' '
    return add_space * number

# print(p_times('here I am', 5))
# print(p_times('its gonna rain', 11))
phrase = input('Enter a phrase: ')
number = input('Enter the number of repetitions: ')
strnum = str(number)

print(p_times(phrase, strnum))


# Example method call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there
