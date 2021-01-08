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

def p_times(statement, num):
    for i in range(num):
        print(statement)


p_times('hey', 3)

def p_times2(statement, num):
    statement = statement + '\n'
    print(statement * num)

p_times2('hello', 4)

def p_times3(statement, num):
    i = 0
    while i < num:
        print(statement)
        i += 1

p_times3('why',5)

    
