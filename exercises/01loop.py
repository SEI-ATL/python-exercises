# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.

def p_times(statement, num):
    str(statement)
    add_space = statement + ' '
    return add_space * num
    
print(p_times('here I am', 5))

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
