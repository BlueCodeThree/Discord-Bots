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
    """