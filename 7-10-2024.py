<<<<<<< HEAD
#1. Python Program to count occurrence of a given characters in string. 

str=input("Enter a word or sentence: ")
l=list(str)
#print(l)
freq=[l.count(ele) for ele in l]
#print(freq)
d= dict(zip(l,freq))
print(d)


#2. Python Program to check if two Strings are Anagram. 


str1=input("Enter a string1: ")
str2=input("Enter a string2: ")
if len(str1)!=len(str2):
    print("Not Anagram")
else:
    if sorted(str1) == sorted(str2):
        print("strings are Anagram")
    else:
        print("Not Anagram")


#3. Python program to check a String is palindrome or not. 

sp=input("Enter a string: ")
revstr=(sp[::-1])
if revstr==sp:
    print("string is palindrome")
else:
    print("string is not palindrome")

#4. Python program to replace the string space with a given character. 
s="python"
c= "open source program"
s1=" "
for i in s:
    if i==" ":
        s1+=c
    else:
        s1 += i
print("string: ",s1)

#5. Python program to replace the string space with a given character using replace() method.

 
str5="Replace space in this string"
replacement_char = "-"
output_string = str5.replace(' ', replacement_char)

print("original string: ", str5)
print("modified string: ",output_string)


#6. Python program to convert lowercase char to uppercase of string. 

s=input("Enter a string: ")
print(s.upper())

#7. Python program to check given character is digit or not using isdigit() method. 

sd=input("Enter a string: ")
print(sd.isdigit())


#8. Python program to separate characters in a given string. 
ss=input("Enter a string: ")
print(ss.split())

#9. Python program to remove blank space from string. 
ss1=input("Enter a string: ")
print(len(ss1))
ss2=(ss1.strip())
print(len(ss2))
print(ss2)

#10. Python program to concatenate two strings using join() method. 

sj1=input("Enter a string1: ")
sj2=input("Enter a string2: ")
js=" ".join([sj1,sj2])
print(js)

#11. Python program to concatenate two strings without using join() method. 

sc1=input("Enter a string1: ")
sc2=input("Enter a string2: ")
sc3=sc1+" "+sc2
print(sc3)

#12. Python program to remove repeated character from string. 
sr=input("Enter a string: ")
str=''
for ch in sr:
    if ch not in str:
        str=str+ch
print(str)

#13. Python program to count alphabets, digits and special characters. 
str13=input("Enter a string: ")
alphabets=0
digits=0
specialc=0
for ch in str13:
    if ch.isalpha():
        alphabets=alphabets+1
    elif ch.isdigit():
        digits=digits+1
    else:
        specialc=specialc+1
print("alphabets count: ",alphabets)
print("digits count: ",digits)
print("special chara count: ",specialc)

#14. Python program to check given character is digit or not. 
str14=input("Enter a string: ")
print(str14.isdigit())

#15. Python program to print all non repeating character in string. 
str15= input("Enter a string: ")
for i in str15:
    if str15.count(i)==1:
        print(i)


#16. Python program to copy one string to another string.  
str16=input("Enter a string: ")
p=(str16[:])
print(p)

#17. Python program to print the highest frequency character in a String. 
str17= "hello world"
max_char= max(set(str17),key = str.count)
print({f'highet frequenct char: {max_char}'})
print(f'frequency: {str.count,{max_char}}')

#18. Python program to calculate sum of integers in string.
str18="123456789"
total_sum=0
for i in str18:
    total_sum+=int(i)
=======
#1. Python Program to count occurrence of a given characters in string. 

str=input("Enter a word or sentence: ")
l=list(str)
#print(l)
freq=[l.count(ele) for ele in l]
#print(freq)
d= dict(zip(l,freq))
print(d)


#2. Python Program to check if two Strings are Anagram. 


str1=input("Enter a string1: ")
str2=input("Enter a string2: ")
if len(str1)!=len(str2):
    print("Not Anagram")
else:
    if sorted(str1) == sorted(str2):
        print("strings are Anagram")
    else:
        print("Not Anagram")


#3. Python program to check a String is palindrome or not. 

sp=input("Enter a string: ")
revstr=(sp[::-1])
if revstr==sp:
    print("string is palindrome")
else:
    print("string is not palindrome")

#4. Python program to replace the string space with a given character. 
s="python"
c= "open source program"
s1=" "
for i in s:
    if i==" ":
        s1+=c
    else:
        s1 += i
print("string: ",s1)

#5. Python program to replace the string space with a given character using replace() method.

 
str5="Replace space in this string"
replacement_char = "-"
output_string = str5.replace(' ', replacement_char)

print("original string: ", str5)
print("modified string: ",output_string)


#6. Python program to convert lowercase char to uppercase of string. 

s=input("Enter a string: ")
print(s.upper())

#7. Python program to check given character is digit or not using isdigit() method. 

sd=input("Enter a string: ")
print(sd.isdigit())


#8. Python program to separate characters in a given string. 
ss=input("Enter a string: ")
print(ss.split())

#9. Python program to remove blank space from string. 
ss1=input("Enter a string: ")
print(len(ss1))
ss2=(ss1.strip())
print(len(ss2))
print(ss2)

#10. Python program to concatenate two strings using join() method. 

sj1=input("Enter a string1: ")
sj2=input("Enter a string2: ")
js=" ".join([sj1,sj2])
print(js)

#11. Python program to concatenate two strings without using join() method. 

sc1=input("Enter a string1: ")
sc2=input("Enter a string2: ")
sc3=sc1+" "+sc2
print(sc3)

#12. Python program to remove repeated character from string. 
sr=input("Enter a string: ")
str=''
for ch in sr:
    if ch not in str:
        str=str+ch
print(str)

#13. Python program to count alphabets, digits and special characters. 
str13=input("Enter a string: ")
alphabets=0
digits=0
specialc=0
for ch in str13:
    if ch.isalpha():
        alphabets=alphabets+1
    elif ch.isdigit():
        digits=digits+1
    else:
        specialc=specialc+1
print("alphabets count: ",alphabets)
print("digits count: ",digits)
print("special chara count: ",specialc)

#14. Python program to check given character is digit or not. 
str14=input("Enter a string: ")
print(str14.isdigit())

#15. Python program to print all non repeating character in string. 
str15= input("Enter a string: ")
for i in str15:
    if str15.count(i)==1:
        print(i)


#16. Python program to copy one string to another string.  
str16=input("Enter a string: ")
p=(str16[:])
print(p)

#17. Python program to print the highest frequency character in a String. 
str17= "hello world"
max_char= max(set(str17),key = str.count)
print({f'highet frequenct char: {max_char}'})
print(f'frequency: {str.count,{max_char}}')

#18. Python program to calculate sum of integers in string.
str18="123456789"
total_sum=0
for i in str18:
    total_sum+=int(i)
>>>>>>> 6908afecf5b442c876789f33915223dc395f3a1d
print(total_sum)