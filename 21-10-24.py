                              #  TUPLE:

# How do you create a empty tuple on python ?
tuple = ()
print(tuple)
print(type(tuple))

# Write a python program to unpack atuple into several variables ?

t = ("karimulla",24,30000)
(name,age,salary) = t
print(name)    #unpacking of tuple

# write a python program to add an item to the tuple ?

t = (1,2,3,4,5,6)
l = list(t)
l.append(7)
print(tuple(l))

# Write a python program to convert tuple into a string ?

t=("karimulla",1,2,3)
print(str(t))

# Write a python program to find most frequent element in tuple?

t=(1,2,3,4,5,6,2,3,4,3,6,4,4,4)
most_frequent=0
max_count=0
for i in t:
    count=t.count(i)
    if count > max_count:
        most_frequent=i
print(most_frequent) 

                              # DICTIONARY:


# Write a python program to  add a key to a dictionary ?

dict1={"Brand":"Ford","Model":"Mustang","Year":1964}
dict1["color"]="blue"
print(dict1)

# Write a python program to check weather the given value is present in the dictionary or not ?

dict1={"Brand":"Ford","Model":"Mustang","Year":1964}
if "Mustang" in dict1.values():
    print("Yes, exist")
else:
    print("No, Not exist")

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict3={}
for x in range(1,16):
    dict3[x]=x**2
print(dict3)
#Write a python program to merge two python dictionaries ?
dict6={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30}
dict6_1={"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict6.update(dict6_1)
print(dict6)

# Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
# Sample string : 'skywavessoftwares'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

dict7={}
s="skywavessoftwares"
for letter in s:
    dict7[letter]=dict7.get(letter,0)+1
print(dict7)
