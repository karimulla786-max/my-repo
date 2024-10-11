
#Basic List Operations:

#1.Write a Python program to create a list of 5 integers and print the sum of all elements in the list."""l1 = [1,3,6,7,9]
sum = 0
for i in l1:
    sum += int(i)
print(sum)
  
# 2.Create a list of strings containing the names of 5 fruits. Access and print the second and fourth elements using indexing.

list_1 = ["mango","grapes","pine apple","orange","gova"]

print(list_1[2])
print(list_1[4])


# 3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, the last three numbers, and every second number in the list."""

l1 = [1,2,3,4,5,6,7,8,9,10]
output = l1[0:3]
print(output)
result = l1[-3:]
print(result)
stp = l1[1:11:2]
print(stp)
 
# Adding and Removing Elements:

#1.Write a Python program that initializes a list with some numbers and:
#2.Adds a new number to the list using the append() method.
#3.Inserts a number at the second position using insert().
#4.Extends the list with another list of numbers.
#5.Remove all occurrences of the number 3 from a list of integers.
#6.Write a Python program to remove the last element of a list using pop() and print the updated list.


l1=[1,2,3,7,9,10]
l1.append(8)
print(l1)

print("---------------------")

l1.insert(3,9)
print(l1)

print("---------------------")

l2=[5,6,7,11,9,10]
l1.extend(l2)
print(l1)

print("------------------------")

l1.remove(3)
print(l1)

print("------------------------------")

l1.pop()
print(l1)

# Sorting and Reversing Lists: 

# 1.Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().

list_1 = [1,10,3,7,2,0,8,9,6,5]

list_1.sort(reverse=True)
print(list_1)

list_1.sort()
print(list_1)

print("---------------------------")

list_1.reverse()
print(list_1)

# 2.Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.

l1 = ["ram","sai","seetha","ravi","mani kanta"]
l1.reverse()
print(l1)

print("-----------------------------")

result = l1[::-1]
print(result)

print(l1 == result)

# Aliasing and Cloning:

# 1.Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.

l1 = [1,2,3,4,5,6,7,8,9]
x = l1
print(x)

l1.pop()
print(l1)

print(x)

result = l1.copy()
print("-------------")

l1.pop()
print(l1)
print(result)
 
#2.Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.

l1 = [1,"c",2,"d"]
x = l1

l1.remove(2)
print(l1)
print(x)
print(id(x))
print(id(l1))

print("--------------------------------")

list = l1.copy()
print(list)

print(id(list))
print(id(l1)) 

# Mathematical Operations:
 
#1.Create two lists of numbers, and use the + operator to concatenate them. Then, use the * operator to repeat the elements of one list 3 times.

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

list = l1 + l2
print(list)

result_1 = list * 3
print(result_1)

#2.Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each element is multiplied by 2).

l1 = ["1",4,5,6,7,10,3,"9","5"]
print(l1)
l2 = []
for i in l1:
   result = int(i) * 2
   l2.append(result)

print(l2)

# Membership Operators:

#1.Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."

list = ["six","seven",0.5,1,2,3]
if "six" in list:
    result = list.index("six")
    print(result)
else:
    print("Element not found")


# Given a list of student names, check if "John" and "Sara" are in the list using the in operator.

list = ["john","ravi","sai","mani","sara"]


if "john" and "sara" in list:
    print("yes, both are There")    


# Nested Lists:

#1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.
nl=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(nl)):
    print(nl[i])
element=nl[1][2]
print(element)
 
#2.Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.
nl2=[["karimulla","A+"],["ramesh","A"],["hari","B+"],["venkatesh","B"],["sai","C"]]
 
for p,q in nl2:
    print("Name: ",p)
    print("Grade: ",q)


# Advanced Challenges:

#1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#One containing only the even numbers.
#Another containing only the odd numbers.
 
lac=list(range(1,21))
print(lac)
even_i=[]
odd_i=[]
for i in lac:
    if i%2==0:
        even_i.append(i)
    else:
        odd_i.append(i)
print(even_i)
print(odd_i)
 
 
#2.Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).
 
la=[1,2,3,4,5,5,6,3,2,1,7,3,4,5]
la2=[]
for i in la:
    if i not in la2:
        la2.append(i)
print(la2)
 
#Given a list of tuples representing (name, age), sort the list by age in ascending order.
list_1=[("ram",15),("ramesh",10),("krishna",25),("suma",40)]
print(type(list_1))
sorted_list_1=sorted(list_1, key=lambda x:x[1])
print(sorted_list_1)
