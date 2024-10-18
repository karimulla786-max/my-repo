# Dictionary:-

#  A python dictionary is a built-in data type that stores key-value pairs.
#  key is unique and value is duplicates
#  it is a mutable
#  using curly braces {} or the dict() constructor

# Dictionary methods:

# 1. dict.get(key, default=None):
 
# Returns the value for the specified key. If the key does not exist, it returns the default value (or None if not specified).

dict = {'a':1,'b':2,'c':3,}
print(dict.get('a'))
 
# 2. dict.keys():
 
# Returns a view object that displays a list of all the keys in the dictionary.

my_dict = {'a':1,'b':2,'c':3,'d':4}
print(my_dict.keys())

# 3. dict.values():
 
# Returns a view object that displays a list of all the values in the dictionary.

d = {'a':1,'b':2}
print(d.values())

# 4. dict.items():
 
# Returns a view object that displays a list of all the key-value pairs as tuples.

my_dict = {'a':1,'b':2,'c':3}
print(my_dict.items())


# 5. dict.update(other_dict):
 
# Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.

my_dict = {'a':1,'b':2,'c':3}
my_dict.update({'d':4,'e':5,'f':6})
print(my_dict)

# 6. dict.pop(key, default=None):
 
# Removes the specified key and returns its value. If the key does not exist, it returns the default value (or raises a KeyError if not specified).


my_dict = {'a':1,'b':2,'c':3}
print(my_dict.pop('b'))


# 7. dict.popitem():
 
# Removes and returns the last inserted key-value pair as a tuple. Raises a KeyError if the dictionary is empty.

my_dict = {'a':1,'b':2,'c':3}
last_item = my_dict.popitem()
print(last_item)

# 8. dict.clear():
 
# Removes all items from the dictionary.

my_dict = {'a':1,'b':2,'c':3}
my_dict.clear()
print(my_dict)

# 9. dict.copy():
 
# Returns a shallow copy of the dictionary.

my_dict = {'a':1,'b':2,'c':3}
new_dict = my_dict.copy()
print(new_dict)

