# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.

# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
def multiply_by(array, multiplier):
    result = []
    for i in range(len(array)):
        item = array[i] * multiplier
        result.append(item)
    # print(result)
    return result
# arr = [1, 6, 5, 14, 2]
input1 = input('Enter your first number: ')
input2 = input('Enter your second number: ')
input3 = input('Enter your third number: ')
input4 = input('Enter your fourth number: ')
mult = input('Enter your multiplier: ')
num1 = int(input1)
num2 = int(input2)
num3 = int(input3)
num4 = int(input4)
multi = int(mult)
arr = [num1, num2, num3, num4]
print(multiply_by(arr, multi))
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]
