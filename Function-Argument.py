'''Function Arguments'''

""" What we learned ?"""
# The arguments that are passed based on their position are known as positional arguments.

# If we give names to arguments, they are keyword arguments. The order of argument doesn't matter for keyword arguments.

# We can also provide default values to arguments. These default values are used if we do not pass arguments during a function call.


''' Python Local '''
def add_numbers(num1, num2):
    result = num1 + num2
    return result

output = add_numbers(2,5)
print(output)

''' Global Variables '''
def add_numbers(num3, num4):
    result = num3 + num4
    return result

output = add_numbers(5,4)
print(output)

''' Global Variables '''
message = "How you doing?"

def greet():
    print(message)
greet() 

message = " OUTSIDE: Who are you?"  # --->>> Global variable

def ask():
    global message  # --->>>> By doing this we can change the global message
    message = " INSIDE :Why are U happy?"  #--->>> Local variable
    print(message)

ask()
print(message)


""" Never use Global Variable """


"""What we learned?"""

# A variable defined inside a function is local to it. When the function ends, this variable is destroyed.
# Variables defined outside a function are called global variables in Python.
# Inside functions, the global keyword can be used to change the value of a variable in the global scope.
# Using the local keyword is a bad practice and you should try to avoid it whenever possible.