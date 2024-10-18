<<<<<<< HEAD
#probleam 1)

s=input("Enter a word or sentence: ")
l=list(s.split())
print(l, type(l))
print(l[::-1])

# probleam 2)

s1= input("Enter a word or sentence: ")
print(s1[::-1])

#probleam 3)

s2 =input("Enter a word or sentence: ")
print(s2.replace(" ",""))

#probleam 4)


str=input("Enter a word or sentence: ")
l=list(str)
#print(l)
freq=[l.count(ele) for ele in l]
#print(freq)
d= dict(zip(l,freq))
=======
#probleam 1)

s=input("Enter a word or sentence: ")
l=list(s.split())
print(l, type(l))
print(l[::-1])

# probleam 2)

s1= input("Enter a word or sentence: ")
print(s1[::-1])

#probleam 3)

s2 =input("Enter a word or sentence: ")
print(s2.replace(" ",""))

#probleam 4)


str=input("Enter a word or sentence: ")
l=list(str)
#print(l)
freq=[l.count(ele) for ele in l]
#print(freq)
d= dict(zip(l,freq))
>>>>>>> 6908afecf5b442c876789f33915223dc395f3a1d
print(d)