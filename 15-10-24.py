# Tuple:- A tuple is an ordered,immutable collection of element in python.once a tuple is created,you cannoy add,remove,ormodify its element


# Basic tuple creation

my_tuple= (1,2,3,4,5,6)
print(my_tuple)


# Accessing tuple elements

my_tuple =("apple","mango","orange","pine apple")
print(my_tuple[2])

# Tuple unpacking

my_tuple = (10, 20, 30, 40, 50)
a, b, c, d, e =my_tuple
print(a, b, c, d, e)

# Concatenating tuples

tuples1 = (1,2,3)
tuples2 = (4,5,6,7,8)
combined = tuples1 + tuples2
print(combined)

# Tuple length

my_tuple = (1,2,3,4,5,6,7,8,9)
length = len(my_tuple)
print(length)

# Counting occurrences in a tuple

my_tuple =(1,2,3,1,4,2,3,1,1)
count_ones = my_tuple.count(1)
print(count_ones)

# Finding index of element

my_tuple = ("apple","kiwi","orange","mango","cheery")
index_a= my_tuple.index("mango")
print(index_a)

# Nested tuples

nested_tuple = ((1,2),(3,4),(5,6),(7,8))
print(nested_tuple[1][0])

# Tuple slicing

my_tuple = (10,20,30,40,50)
sliced = my_tuple[1:4]
print(sliced)
sliced = my_tuple[0:4]
print(sliced)
sliced = my_tuple[::]
print(sliced)
sliced = my_tuple[:3]
print(sliced)

# Conveting a list to tuple

my_list = [1,2,3,4,5,6,7,8]
my_tuple = tuple(my_list)
print(my_tuple)


# Sorting a tuple

my_tuple = (6,7,3,2,8,9,1,3)
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)


# Tuple comparison

tuple1 =(1,2,3,4,5)
tuple2 =(1,2,3,4,6)
print(tuple1<tuple2)


