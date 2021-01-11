# def p_times(str, n)
#     for i in 1..n # rnages are inclusive on both ends, 0...n prints n+1 times
#         puts str
#     end 
# end 

def p_times(str, n)
    n.times { puts str }
end

p_times('Learning Ruby', 3)

# def letter_count(str)
#     count = {}
#     str.each_char{ |char|
#         if !count[char] then 
#             count[char] = 1
#         else 
#             count[char] += 1
#         end
#     }
#     return count
# end

def letter_count(str)
    count = {}
    str.each_char{ |char|
        count[char] ||= 1
        count[char] += 1
    }
    return count
end

puts letter_count('Did this work?')

# def print_contacts(hash)
#     hash.each{ |key, value| 
#         puts "#{key} has a phone number of #{value}"
#     }
# end

def print_contacts(hash)
    hash.each do |key, value|
        puts "#{key} has a phone number of #{value}" 
    end
end

contacts = { 'Brian': '333-333-3333',
'Lenny': '444-444-4444',
'Daniel': '777-777-7777' }

print_contacts(contacts)

# def multiply_by(numArr, n) #non mutating
#     newArr = []
#     numArr.each{ |num| newArr.push(num*n)}
#     return newArr
# end

# nums = [1,2,3,4]
# puts multiply_by(nums, 5)
# puts nums

# def factorial_reduce(n)
#     return Array(2..n).reduce(1) {|product, num| product*num}   
# end

# def factorial_loop(n)
#     factorial = 1
#     for i in 2..n
#         factorial = factorial * i
#     end
#     return factorial
# end

# puts factorial_reduce(5)
# puts factorial_loop(5)

# # Class example in Ruby

# class Soup #camel case classnames
#     def initialize(name, temp, ingredients)
#         @name = name
#         @temperature = temp # hot or cold
#         @ingredients = ingredients
#     end

#     def get_shopping_list
#         return "- " + @ingredients.join("\n- ")
#     end

#     def get_opinion
#         opinions = ["ok...", "no.", "Gross", "But why though"]
#         ind = rand(opinions.length())
#         if @temperature == 'Cold' then return opinions[ind] end
#     end

# end

#  borscht = Soup.new("Borscht", "Cold", ["Beets", "Sour Cream", "Dill", "Potatoes (optional)"])

#  puts borscht.get_shopping_list
#  puts borscht.get_opinion


# Feedback from Pete Macaluso: 

# def p_times(str, n)
#     # for i in 1..n # rnages are inclusive on both ends, 0...n prints n+1 times
#     #     puts str
#     # end 
#     # more ruby idiomatic
#     # n.times do
#     #     puts str
#     # end
#     # when do/end blocks can fit on one line, this syntax is preferred
#     n.times { puts str }
# end 

# p_times('Learning Ruby', 3)
# def letter_count(str)
#     count = {}
#     # when blocks span >1 line, use do/end
#     str.each_char{ |char|
#         # v0
#         # if !count[char] then 
#         # unless is preferred over if !
#         # v1
#         # unless count[char] then 
#         # then is only used to do simple one-line conditionals eg
#         # v2
#         # unless count[char] then count[char] = 1
#         # but actually, there's a way to do 1-line conditionals that's preferred over then
#         # v3
#         # count[char] = 1 unless unless count[char]
#         # so then kinda never gets used at all, womp womp
#         # a rubyism is to prefer 1-line statements over branch conditionals when possible. in fact ruby linters usually yell at you if you have too much ABC, or assignment branch condition, ie if/else statements. 
#         # instead, try 1 liners
#         # v4
#         # count[char] = 1 unless count[char]
#         # 1 more slick trick: the ||= operator is analogous to any <operator>=
#         # ie my_var += 1 means my_var = my_var + 1
#         # so count[char] ||= 1 means count[char] = count[char] || 1
#         # so v5, final answer
#         count[char] ||= 1
#         count[char] += 1
#     }
#     return count
# end
# puts letter_count('Did this work?')
# def print_contacts(hash)
#     # only change is to use do/end over {} for multi-line blocks
#     hash.each{ |key, value| 
#         puts "#{key} has a phone number of #{value}"
#     }
# end
# # I think you're good on symbols based on this, but let me know if they still seem mysterious. they are cool in a vacuum and also have alternate syntaxes when used as hash keys.
# contacts = { 'Brian': '333-333-3333',
# 'Lenny': '444-444-4444',
# 'Daniel': '777-777-7777' }
# print_contacts(contacts)
# def multiply_by(numArr, n) #non mutating
#     newArr = []
#     numArr.each{ |num| newArr.push(num*n)}
#     # v1 would be to write this w/ map
#     # newArr = numArr.map { |num| num * n }
#     # note that in this block there's no return keyword (in contrast to a js map), see below
#     # note that map is non mutating, it returns a new array w/o changing the original. the mutating version is map!. mutating methods are usually named ending w/ !, as are any methods that you in general should think twice before using, ie send_some_email_to_all_users!
#     # in general, the only way to mutate an object is to call one of its own methods that causes it to mutate itself
#     # so if you wanted a mutating version of this method, it would be like
#     # def multiply_by!(numArr, n)
#     #     numArr.map! { |num| num * n }
#     # end
#     # the last evaluated expression in a method or block is automatically returned
#     # there are very different opinions as to whether this is more helpful or more confusing, mostly depending on what language one is coming from
#     # but for better or worse it's idiomatic to omit the return word
#     return newArr
# end
# nums = [1,2,3,4]
# # puts will call any object's own .to_s method on it and print the casted version, which is sometimes helpful and sometimes not
# # sometimes you just want p, which does not cast as string before printing
# puts multiply_by(nums, 5)
# puts nums
# def factorial_reduce(n)
#     # ruby linters will yell at this line over some spacings
#     return Array(2..n).reduce(1) {|product, num| product*num}
#     # instead
#     # return Array(2..n).reduce(1) { |product, num| product * num }
#     # for methods that take a block like reduce (especially reduce), if the block is real simple like this, you might see 
#     # Array(2..n).reduce(&:*)
#     # this is calling the to_proc method on the symbol :*. a proc is a block that you can assign to a variable and pass around (like a js function), which is not possible other than w/ a proc.
#     # some symbols can just magically be converted into blocks by calling .to_proc on them. this is both cool and horrifying imo
#     # but anyways try the version with the &:*, it's common in reduce w/ &:* and &:+
#     # the other place you'll see it is something like people.map(&:first_name). this will call the .first_name method on each element of the array
# end
#
# def factorial_loop(n)
#     # I think all my comments on this have already appeared somewhere above
#     # so give this one a retry w/ those in mind as an exercise
#     factorial = 1
#     for i in 2..n
#         factorial = factorial * i
#     end
#     return factorial
# end


# class Soup
#     TEMPERATURE_VALUES = [:hot, :cold]
#     # symbols make sense here because there's no need for every instance of the soup class to have its own private memory location for its temperature string. they can all share
#     def initialize(args)
#         # reminder to myself to address with_indifferent_access after these examples
#         @name = args[:name] # it is common to either specify a default in case the arg is empty, or to raise an error if it's empty but can't be omitted
#         @ingredients = args[:ingredients]
#         unless TEMPERATURE_VALUES.include? args[:temperature]
#             raise "Invalid temperature, allowed values are #{TEMPERATURE_VALUES}"
#             # you might also want to standardize user inputs in some ways, like downcasing
#             # you might also also want to .to_sym the user input, in case they put in a string
#             # on the other hand, it can be weird if I pass in a value of "Cold", and the instance has a different value than what I passed in of :cold. all a judgement call
#         end
#         @temperature = args[:temperature]
#         # super bonus note that will make more sense later: in the course of making rails apps, you'll be using a library called activerecord that's like sequelize, which provides hooks and validations that accomplish this more neatly. But it's still good to know this vanilla "validation" inside of initialize, because not every class you write will be attached to a db table, and those won't have the validations or hooks
#     end
#     # rest of class unchanged
# end
# borscht = Soup.new(
#   name: "Borscht",
#   temperature: :cold,
#   ingredients: ["Beets", "Sour Cream", "Dill", "Potatoes (optional)"]
# )
# p borscht
# # borscht = Soup.new(
# #   name: "Borscht",
# #   temperature: :Cold,
# #   ingredients: ["Beets", "Sour Cream", "Dill", "Potatoes (optional)"]
# # )
# # p borscht
# # borscht = Soup.new(
# #   name: "Borscht",
# #   temperature: 'cold',
# #   ingredients: ["Beets", "Sour Cream", "Dill", "Potatoes (optional)"]
# # )
# # p borscht














