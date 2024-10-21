                                  # LIST:

# Write a python program to merge two list?

list1 = [1,2,3,4]
list2 = [5,6,7,8]

merged_list = [list1 + list2]
print(merged_list)

# Write a python program to delete element of given index in list ?

list = [1,2,3,4,5,6,7,8,9]
del list[5]
del list[6]
print(list)

# Write a python program to delete given element from the list?

list = [1,2,3,4,5,6]
list.remove(4)
print(list)

# Write a python programe to check if the two list are having atleast one common element?

l=[1,2,3,4]
l1=[87,22,4,20]
common_element = set(l)&set(l1)
if common_element:
    print("having common elements")
else:
    print("not present elements")

# Write a python program to remove  specified column from the nestedlist?

l= [[1, 2, 3], [1, 3, 6], [5,5,5]]
del l[1][0:2+1]
del l[2][0:2+1]
print(l)

# Write python program to convert a list of integers into single integer?
list = [1,2,3,4,5,6,7]
s=""
for i in list:
   s+=str(i)
print(s)

# Write  a python programe to remove duplicates from the list?
list = [1,2,3,6,8,7,6,5,6]
s=set(list)
print(s)
l=list(s)
print(l)
                   
                  # SET:

# Write a program to create a set?

my_set = {1,2,3,4,5,6}
print(my_set)

# Write program to iterate over sets?

s = set("karimulla")
for char in s:
    print(char)

#Write a Python program to add member to a set?
s={1,2,3,4,5}
s.add(56)
print(s)
#output
#{1, 2, 3, 4, 5, 56}
#Write a Python program to remove item from a given set?
s={1,2,3,4,5,6}
s.remove(4)
print(s)
#output
#{1, 2, 3, 5, 6}
#Write a python program to create a intersection of set?
s={1,2,3,4,3,2}
s1={5,6,7,8,2,4,3}
print(s.intersection(s1))
#output
#{2, 3, 4}
#Write a python program to createa unionof set?
s={1,2,3,4,5}
s1={6,7,8,9,2,4}
print(s.union(s1))
#output
#{1, 2, 3, 4, 5, 6, 7, 8, 9}
#Write a python program to create set differance?
s={1,2,3,4,5}
s1={6,7,8,9,2,5}
print(s.difference(s1))
#output
#{1, 3, 4}
#Write a python program to create a symmetric defferance?
s={1,4,5,6,7}
s1={2,7,9,10,2,5}
print(s.symmetric_difference(s1))
#output
#{1, 2, 4, 6, 9, 10}
#write a python program to find max and min values in a set?
s={0,1,2,3,4,5,6}
max_v=0
min_v=0
for i in s:
    if i>max_v:
        max_v=i
    if i<min_v:
        min_v=i    
print(max_v)
print(min_v)
#output
#6
#0 
  
#Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set?
s={1,2,3,4,5}
s1={6,7,8,9,1,2,3,4}
s.difference_update(s1)
s.add(10)
print(s)
#output
#{10, 5}
#Write a Python program to remove items 10, 20, 30 from the following set at once?
s={1,2,10,20,30}
s1={10,20,30}
print(s.difference(s1))
#output
#{1, 2}
#Check if two sets have any elements in common. If yes, display the common elements?
s={1,2,3,4}
s1={1,2,3,4}
s2=s.intersection(s1)
if (s==s1):
    print("yes",s2)
#output
#yes {1, 2, 3, 4}
#Update set1 by adding items from set2, except common items?
s={1,2,3,4,5}
s2={6,7,8,9,2,3}
print(s.symmetric_difference(s2))
#output
#{1, 4, 5, 6, 7, 8, 9}
#Remove items from set1 that are not common to both set1 and set2?
s={1,2,3,4}
s1={3,4,5,6,7}
print(s.difference(s1))
#output
#{1, 2}
#How do you create a empty tuple on python?
t=()
print(t)
print(type(t))
#output
#<class 'tuple'>
#Write a python program to unpack atuple into several variables?
ft=("apple","orange","mango","banana","pineapple","custedapple")
a,b,c,d,e,f=ft
print(a,c)
print(b,d)
print(c,e)
print(f,e)
#output
#apple mango
#orange banana
#mango pineapple
#custedapple pineapple
 