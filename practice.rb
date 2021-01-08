def p_times(str, n)
    for i in 1..n # rnages are inclusive on both ends, 0...n prints n+1 times
        puts str
    end 
end 

p_times('Learning Ruby', 3)

def letter_count(str)
    count = {}
    str.each_char{ |char|
        if !count[char] then 
            count[char] = 1
        else 
            count[char] += 1
        end
    }
    return count
end

puts letter_count('Did this work?')

def print_contacts(hash)
    hash.each{ |key, value| 
        puts "#{key} has a phone number of #{value}"
    }
end

contacts = { 'Brian': '333-333-3333',
'Lenny': '444-444-4444',
'Daniel': '777-777-7777' }

print_contacts(contacts)

def multiply_by(numArr, n) #non mutating
    newArr = []
    numArr.each{ |num| newArr.push(num*n)}
    return newArr
end

nums = [1,2,3,4]
puts multiply_by(nums, 5)
puts nums

def factorial_reduce(n)
    return Array(2..n).reduce(1) {|product, num| product*num}   
end

def factorial_loop(n)
    factorial = 1
    for i in 2..n
        factorial = factorial * i
    end
    return factorial
end

puts factorial_reduce(5)
puts factorial_loop(5)

# Class example in Ruby

class Soup #camel case classnames
    def initialize(name, temp, ingredients)
        @name = name
        @temperature = temp # hot or cold
        @ingredients = ingredients
    end

    def get_shopping_list
        return "- " + @ingredients.join("\n- ")
    end

    def get_opinion
        opinions = ["ok...", "no.", "Gross", "But why though"]
        ind = rand(opinions.length())
        if @temperature == 'Cold' then return opinions[ind] end
    end

end

borscht = Soup.new("Borscht", "Cold", ["Beets", "Sour Cream", "Dill", "Potatoes (optional)"])

puts borscht.get_shopping_list
puts borscht.get_opinion