# Write a method called `letter_count` to count the letter
# occurrence in a string. Use a dictionary.
#
# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)

def letter_count(string):
    # list = (string.splice())
    # print(list)
    list = [char for char in string]
    print(list)
    for l in string:
        list.count(string)
        if l in string:
            count = string.count(l)
            print(l + ' Occurs ' + str(count) + ' time(s)')
        

letter_count("alpha")



# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
# dd = {}
# dd["foo"] = 1
# dd["foo"] += 1
# if "foo" in dd:
#   print(dd["foo"])
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example method call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 3}


dd = {}
dd["foo"] = 1

print("foo" in dd)