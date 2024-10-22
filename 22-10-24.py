# FUNCTION TYPES:

# 1. Built-in Functions:
#  These are functions that are readily available in Python, such as print(), len(), sum(), and type().
 
 
# 2. User-Defined Functions:
#  Functions defined by the user using the def keyword. They can take parameters and return values.
 
def my_function(param1, param2):
    return param1 + param2
 
 
# 3. Lambda Functions:
#  Also known as anonymous functions, these are defined using the lambda keyword and can have any number of arguments but only one expression.
 
add = lambda x, y: x + y
 
 
# 4. Higher-Order Functions:
#  Functions that take other functions as arguments or return them as results. For example, map(), filter(), and reduce().
 
def apply_function(func, value):
    return func(value)
 
 
# 5. Recursive Functions:
#  Functions that call themselves to solve a problem. They must have a base case to prevent infinite recursion.
 
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
 
 
# 6. Generator Functions:
#  Functions that use the yield statement to return an iterator. They can produce a sequence of results lazily.
 
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
 
 
# 7. Coroutine Functions: 
# Similar to generators but used for cooperative multitasking. They are defined with async def and use await to pause execution.
 
("------------------------------------------------------------------------------------------------------------------------------")


# Recursive function examples:

# Fibonacci sequence:

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=5
print(fibonacci(n)) 

# sum of an array

def sum_array(arr):
    if len(arr) ==0:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])
arr = [2,3,5]
print(sum_array(arr))  

# lambda functions:

# addtion:
add=lambda x,y:x+y
print(add(3,5))

# even numbers:

numbers =[1,2,3,4,5,6,7]
even_numbers = list(filter((lambda x : x%2 == 0),numbers))
print(even_numbers)


# filter function:

numbers =[1,2,3,4,5,6,7]
odd_numbers = list(filter((lambda x : x % 2!= 0),numbers))
print(odd_numbers)

# filtering positive function example:

numbers = [1,2,4,-2,-6,6,-8,6]
positive_numbers = list(filter(lambda x:x>0,numbers))
print(positive_numbers)

# map function example:    
    
# squaring each numbers:

numbers = [1,2,3,4,5,6]
squared = list(map(lambda x:x**2,numbers))
print(squared)     


# doubling each value:

numbers = [1,2,3,4,5,6,7]
doubled = list(map(lambda x: x*2,numbers))
print(doubled)
 