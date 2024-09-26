# write a program that prients the multiplication table for a given number.

n =int(input("give n number"))
i=1
while i<=10:
    print(f"{n} * {i} ={n*i}")5
    i+=1


 # write a program to calculate the factorial of a number using a loop


    n =int(input("give n value"))
    factorial =1
    while n>0:
        factorial =factorial*n
        n-=1
        print(factroial) 


#write a program to print the number from 1 to 10
#For multiples of three ,print 'fizz' instead of the number and for multiple of five ,print 'buzz
                     
n=int(input("enter a number:"))
for i in range (1,n+1):
    print(i)

    for i in range(1,100+1):
        if(i%3==0):
            print("fizz")
        elif(i%5==0):
            print("buzz")
        else:
            print(i)  
 
 #For numbers which are multiples of both three and five ,print 'fizzbuzz"
    for i in range (1,100+1):
     if(i%3==0 and i%5==0):
         print("fizzbuzz")
    else:
         print(i)  

# write a program that check if a number is prime
num =int(input("enter a number: "))
if num==1:
    print("not a prime number")
if num>1:
  for n in range(2,num):
    if num%2==0:
        print(num, "is not a prime number ")
        break
    else:
         print(num, "num is a prime number")


# write a program to check if a string is a palindrome.
n="madam"
rev=""
temp=n 
for i in n:
    rev=i+rev
if temp==rev:
    print("palindrome")
else:
     print("not palindrome")

# write a program that generates a random number between 1 and 100and ask the user to guess it . the program should give hints('too low and too high) until the user guesses correctly
number = random.randint(1, 100)
guess = None

print("Welcome to the Guess the Number game!")
print("I've picked a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break 
    print("Thanks for playing!")
# write a program that takes a number as input and print the sum of its digits
n=int(input("enter a number:"))
digits = 0
digit_sum = 0
temp = n  
while temp > 0:
    digit = temp % 10  
    digit_sum += digit  
    digits += 1         
    temp //= 10         
    print(digits)
    print(digit_sum)


# write a program to find the largest of three number using if statement
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
if n1>n2 and n1>n3:
    print("return n1")
elif(n2>n1 and n2>n3):
    print("return n2")
else:
    print(n3)  

 # write a program to check if a number is an Armstrong number
n =int(input("enter a number:"))
num=n
s=0
while n>0:
    r=n%10
    s=s+r*r*r
    n=n//10
if s==num:
    print(num," Armstrong number")
else:
    print(num, "Not an Armstrong")

# write a program that counts the number of even and odd number in list
n = [22,55,77,99,100,11,33,55]
even_count = 0
even_number=[]
odd_count =0 
odd_number=[]
for i in n:
    if i % 2 == 0:
        even_number.append(i)
        even_count += 1  
    else:
        odd_number.append(i)
        odd_count += 1 
        print(even_count)
        print(even_number)
        print(odd_number)
        print(odd_count)
        
    



        