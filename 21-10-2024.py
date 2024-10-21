# FUNCTION:
# Funtion are blocks of organised,reusable code that perform a specific task
# Declaration:-you defind a function using the def keyword ,followed by the function name,parentheses(),and a colon:
# syntax:-def function_name(parameters):
# function call:- To execute a function and run the code insid it,you call the function by using its name followed by parentheses()


# Function to add two numbers.

def add(a,b):
    return (a+b)
    
    
print(add(7,6))

# funtion to check even and old numbers.

def is_even(numbers):
    return numbers % 2 == 0
print(is_even(4))
print(is_even(7))

# function to calulate factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))


# function to find maximum of three numbers.

def max_of_three(x ,y ,z):
    return max(x ,y ,z )
print(max_of_three(10,20,5))

# function to reverse a string.

def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

