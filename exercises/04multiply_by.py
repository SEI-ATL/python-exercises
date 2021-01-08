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

#mutate original
def multiply_by_mutate(numArr, n):
    for i in range(len(numArr)):
        numArr[i] = numArr[i] * n
    return numArr


numbers = [1,2,-3,4.5]
print(multiply_by_mutate(numbers, 2))
print(numbers)


#dont mutate 
def multiply_by(numArr, n):
    multArr =[]
    for i in range(len(numArr)):
        multArr.append(numArr[i] * n)
    return multArr


numbers2 = [1,2,-3,4.5]
print(multiply_by(numbers2, 2))
print(numbers2)

#or with map 
def multiply_by_map(numArr, n):
    map(lambda x : x*n, numArr)
    return numArr

numbers3 = [1,2,-3,4.5]
print(multiply_by_map(numbers3, 2))
print(numbers3)