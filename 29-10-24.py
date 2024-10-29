#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"

def wish():
    greet="hello"
    name= input("Enter a name here : ")
    print(greet +' '+ name)
wish()
 
#2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
 
def add():
    num_1 = int(input("Enter The Number_1 Here : "))
    num_2 = int(input("Enter The Number_2 Here : "))
    total = num_1+num_2
    print("sum = ", total)
add()
 
 
#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
 
def is_even(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number : "))
result = is_even(num)
print(f"the number {num} is {result}.")
 
 
#4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
 
def factorial(c):
    if c==1 or c==0:
        return 1
    else:
        return (c*factorial(c-1))
c = int(input("entr the value : "))
result= factorial(c)
print("factorial of ", c,"is : ", result)

 
#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
 
def max_of_three(a,b,c):
    return max(a,b,c)
a=22
b=45
c=39
operation = max_of_three
print(max_of_three(a,b,c))

# 6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    
    for char in input_string:
        if char in vowels:
            count += 1
    
    return count

result = count_vowels("Hello, World!")
print(result)  
 
# 7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
print(is_prime(7))  
print(is_prime(10)) 


# 8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).

def recursive_sum(n):
    
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

result = recursive_sum(5)
print(result)  

# 9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))

#10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.

def find_common_elements(list1, list2):
    return [element for element in list1 if element in list2]
print(find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.

def reverse_string(s):
    return s[::-1]
print(reverse_string("karimulla"))

#12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.##

def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])
print(sort_dict_by_value({"a":7,"b":9,"c":3}))