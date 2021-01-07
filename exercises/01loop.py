# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
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

def p_times(str, n):
    if n <= 0 : return
    arr = [str] * n
    printStr = "\n".join(arr)
    print(printStr)

p_times('Hello there', 5)

def p_times_loop(str, n):
    for i in range(n):
        print(str)

p_times('Goodbye', 5)