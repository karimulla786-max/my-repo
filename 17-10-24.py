# Finding the union of two sets?

set_a = {1, 2, 3}
set_b = {3, 4, 5}
 
union = set_a | set_b
print("Union:", union)


# Finding the intersection of two sets?

intersection = set_a & set_b
print("Intersection:", intersection)
 
# Using sets to remove duplicates from a list of tuples

data = [(1, 'a'), (2, 'b'), (1, 'a'), (3, 'c')]
unique_data = list(set(data))
print(unique_data)

# set operation morn than two sets
 
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {5, 6, 7}
 
# Union
union_all = set_a | set_b | set_c
print("Union of all sets:", union_all)
 
# Intersection
intersection_all = set_a & set_b & set_c
print("Intersection of all sets:", intersection_all)
 
# Difference
difference_ab = set_a - set_b
print("Difference (set_a - set_b):", difference_ab)
 
difference_all = set_a.difference(set_b).difference(set_c)
print("Difference (set_a - set_b - set_c):", difference_all)

# creating a set of unique names from a list

names = ["karimulla","nikil","kowshik","chinna"]
unique_names = set(names)
print(unique_names)


# Analyzing interests of two users to find common interests

interests_user1 = {"reading", "gaming", "music"}
interests_user2 = {"music", "sports", "travel"}
 
common_interests = interests_user1 & interests_user2
print("Common interests:",common_interests)
 



