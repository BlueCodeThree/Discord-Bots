print_answer = """```
    puts "Hello World"

    # puts can print multiple things, each on a new line
    puts(1, 2, "dog", "cat")

    # don't have to use brackets
    puts 1, 2, "dog", "cat"

    # print will join these two strings together on same line
    print("a", "b")

    # also can use without brackets
    print "a", "b"
    
    # 'p' acts like .inspect```

You can put sums inside the string
`puts "Here is a string with math #{3 + 5}`
    """

length_answer = """
    Getting the length of a string in ruby: 
    ```variableName.length```
    """


time_answer = """
    ```# gets the time right now
time_now = Time.now 
Time.now.year # for example, returns 2019
        
reference: http://ruby-doc.org/core-2.2.0/Time.html```
    """

gets_answer = """```# asks for user input. The "chomp" removes an enter key at the end of the input
    gets.chomp
    ```"""

function_answer = """ Function/ Method for ruby. 
Note that there is no ":" etc. 
```def functionName(thingies)
    # things for the function go here
end
    ```
In order to see all the methods for something...
`9.methods.sort`    
"""

convert_answer = """ Converting strings, integers and floats etc
```variableName.to_s # to string
variableName.to_f # to float
variableName.to_i # to integer
```
    """

string_answer = """ stuff about strings in ruby
`variableName.to_s  # convert to string`

`"string here".length # get the length`

interpolated variable
`"This is a string with a #{variable}"`

and combining strings
`full_name = "#{first_name} #{middle_name} #{last_name}"`

```puts "Vowels: " + full_name.count("aeiou").to_s
puts "Consonants: " + full_name.count("^aeiou").to_s```

```full_name.include?("Justine") # will say either true or false
full_name.index("Justine").to_s # the number index where this text occurs```
    """
if_answer = """ if conditionals. Notice no ":" etc
```if true
    # output here
elsif condition
    # output here
else conditions
    # output here
end```

Another way to do if statements:
`puts "you're young" if age < 30`

If age is bigger than or equal to 30, it'll puts "Old", else puts "Young"
`puts (age >= 30) ? "Old" : "Young"`

'unless' is confusing and means the opposite of 'if', so it runs if the parameters are false.
```unless variable >= 50 # variable is NOT bigger than or equal to 50
    # output here
end```

**Case**
```fruit = "pear"
case fruit
when "pear"
    # do this
when "apple"
    # do this
else 
    # this ```
    """

array_answer = """
Create an array:
`array = Array.new`

Create an array with three items:
`array = Array.new(3, "Jason")`

Create an empty array with bracket notation:
`array = []`

Create an array using brackets with three items:
`array = ["milk", "eggs", "bread"]`

Create an array using the %w notation which contains three strings:
`array = %w(milk eggs bread)`

Create an array using the %W notation which contains three strings and one is interpolated:
```item = “milk”
array = %W(#{item} eggs bread)```

How to cycle through arrays - for loop
```numbers = [1, 2, 3, 4, 5]

for number in numbers 
    puts " there are #{number} bottles!"
end
```

Cycle through array each 
```groceries = ["bananas", "apples", "bread", "milk"]

groceries.each do |food|
    puts "Get some #{food}"
end
``` 

Items can be added to the end of an array by using either push or <<
```arr = [1, 2, 3, 4]
arr.push(5) #=> [1, 2, 3, 4, 5]
arr << 6    #=> [1, 2, 3, 4, 5, 6]```
    """

loop_answer = '''
**Loops/Conditionals for Ruby**
next goes back to the top of the loop
unless means "not"
break ends the loop.
```loop do 
    x += 1
    next unless (x % 2) == 0
    puts x
    break if x >= 10
end
```
So in the above example, the loop skips over the number if it is odd, and puts the number if it is not odd, and breaks if x is bigger than or equal to 10.

**While**
```while y <= 10
    y += 1
    puts y
end```

**Until**
```until a >= 0
    a+= 1
    next unless (a % 2) == 0
    puts a
end
```
How to cycle through arrays - for loop
```numbers = [1, 2, 3, 4, 5]

for number in numbers 
    puts " there are #{number} bottles!"
end
```

Cycle through array each 
```groceries = ["bananas", "apples", "bread", "milk"]

groceries.each do |food|
    puts "Get some #{food}"
end
``` 

cycling through numbers - a range:
```(1..10).each do |i|
    puts "number #{i}"
end

for year in 2000...2015
    puts year
end
```
    '''

exceptions_answer = '''```
begin
    # code goes here
rescue
    # code here what happens if there is an error
    puts "You can't do that!"
    exit
end
```

another way using "raise"
```def check_age(age)
    raise ArgumentError, "Enter Positive Number" unless age > 0
end

begin
    check_age(-1)
rescue ArgumentError
    puts "That is an impossible age"
end
```
'''