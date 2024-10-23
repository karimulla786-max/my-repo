# TYPES OF ARGUMENTS:
''''
 1.Positional argument
 2.Keywoard argument
 3.Variable length argument
 4.Default argument
'''

# 1.Positional argument:
# A positional argument is an argument in a function or method that is assigned based on its position in the function call. In programming, the order of the arguments matters; they are matched to the parameters in the function definition based on their position.
 
# Example in Python:
 
def add(a, b):
    return a + b
 
result = add(3, 5)
print(result)  

# keywoard argument:

# A keyword argument is an argument passed to a function using the parameter name, allowing you to specify which parameter you are providing a value for. This improves code readability and allows you to pass arguments in a different order.
     

def calculate_area(length, width):
    return length * width
 
area = calculate_area(width=5, length=10)
print(area)  

# Default argument:
# A default argument is a parameter in a function that has a predefined value. If a value is not provided for that parameter when the function is called, the default value is used.

 
def greet(name, message="Hello"):
    return f"{message}, {name}"
greeting1 = greet("Alice")
greeting2 = greet("Bob", "Welcome")
 
print(greeting1)  
print(greeting2)   

# Variable length argument:

#Variable-length arguments allow a function to accept a flexible number of arguments, enabling it to handle more inputs than specified in the function definition. In Python, this is done using *args for positional arguments and **kwargs for keyword arguments.
 
# Example with *args:
 
def sum_numbers(*args):
    return sum(args)
 
result1 = sum_numbers(1, 2, 3)
result2 = sum_numbers(4, 5, 6, 7, 8)
 
print(result1) 
print(result2)  
 
# In this example, sum_numbers can accept any number of positional arguments, which are accessible as a tuple within the function.
 
# Example with **kwargs:
 
def display_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
 
display_details(name="Alice", age=30, city="New York")