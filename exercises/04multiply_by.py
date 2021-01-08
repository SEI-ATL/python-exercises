# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]


# with lambda
def multiply_by(arr, num):
    return list(map(lambda x: x*num, arr))


print(multiply_by([1, 2, 3], 2))


# without lambda, map maps over the two parameters at each index
# #> brings them into the function that does the mapping,
# and you can return it to get the result
def multiply(a, b):
    return a*b


def multiply_by2(arr, num):
    return list(map(multiply, arr, [num]*len(arr)))


print(multiply_by2([1, 2, 3], 5))
