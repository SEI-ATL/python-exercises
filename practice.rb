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