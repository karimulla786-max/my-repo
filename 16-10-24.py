<<<<<<< HEAD
# Set:-  a set is a collection of distinct objects, considered as an object in its own right. Sets are defined by their elements, which can be anything—numbers, characters, or even other sets.
 
# Key Characteristics of Sets:
 
# 1. Uniqueness: Each element in a set is unique; duplicates are not allowed.
 
# 2. Unordered: The elements in a set do not have a specific order.
 
# 3. Membership: You can check if an element is a member of a set.
 
# Notation:
 
# A set is usually denoted using curly braces.
# The empty set is denoted as  or.
 
# Creating a set:

my_set = {1,2,3,4,5,6,7}
print(my_set)


# Adding an element:

my_set = {1,2,3,4,5,6}
my_set.add(7)
print(my_set)


# Removing an element:

my_set.remove(3)
print(my_set)

# Set operations:
 
set_a = {1, 2, 3}
set_b = {3, 4, 5}
 
# Union
union = set_a | set_b
print("Union:", union)
 
# Intersection
intersection = set_a & set_b
print("Intersection:", intersection)
 
# Difference
difference = set_a - set_b
print("Difference:", difference)
 
# Symmetric Difference
symmetric_difference = set_a ^ set_b
print("Symmetric Difference:", symmetric_difference)


# Removing duplicates from list:

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)


# clearing a set:

my_set = {1,2,3,4}
my_set.clear()
print(my_set)


# Finding unique characters in a string:

my_string = "hello world"
unique_chars = set(my_string)
print(unique_chars)
=======
# Set:-  a set is a collection of distinct objects, considered as an object in its own right. Sets are defined by their elements, which can be anything—numbers, characters, or even other sets.
 
# Key Characteristics of Sets:
 
# 1. Uniqueness: Each element in a set is unique; duplicates are not allowed.
 
# 2. Unordered: The elements in a set do not have a specific order.
 
# 3. Membership: You can check if an element is a member of a set.
 
# Notation:
 
# A set is usually denoted using curly braces.
# The empty set is denoted as  or.
 
# Creating a set:

my_set = {1,2,3,4,5,6,7}
print(my_set)


# Adding an element:

my_set = {1,2,3,4,5,6}
my_set.add(7)
print(my_set)


# Removing an element:

my_set.remove(3)
print(my_set)

# Set operations:
 
set_a = {1, 2, 3}
set_b = {3, 4, 5}
 
# Union
union = set_a | set_b
print("Union:", union)
 
# Intersection
intersection = set_a & set_b
print("Intersection:", intersection)
 
# Difference
difference = set_a - set_b
print("Difference:", difference)
 
# Symmetric Difference
symmetric_difference = set_a ^ set_b
print("Symmetric Difference:", symmetric_difference)


# Removing duplicates from list:

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)


# clearing a set:

my_set = {1,2,3,4}
my_set.clear()
print(my_set)


# Finding unique characters in a string:

my_string = "hello world"
unique_chars = set(my_string)
print(unique_chars)
>>>>>>> 6908afecf5b442c876789f33915223dc395f3a1d
