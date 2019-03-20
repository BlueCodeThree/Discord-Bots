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
    """

length_answer = """
    Getting the length of a string in ruby: 
    ```variableName.length```
    """

time_answer = """
    ```# gets the time right now
    time_now = Time.now ```
    """

gets_answer = """```# asks for user input. The "chomp" removes an enter key at the end of the input
    gets.chomp
    ```"""

function_answer = """ Function/ Method for ruby. 
Note that there is no ":" etc. 
```def functionName(thingies)
    # things for the function go here
end
    ```"""

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

cycling through numbers:
```(1..10).each do |i|
    puts " number #{i}"
end
```
    '''