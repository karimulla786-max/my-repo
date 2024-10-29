#OOPS CONCEPT:- object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.

"""FEATURES OF OOPs:-

1)class
2)objects
3)abstraction 
4)encapsulation 
5)inheritance and  
6)polymorphism

CLASS:-

clss is a blueprint, class can declare a only once. class is two types
1)Static variables(VS)
2)Non-static variables(NSV)
Static variables(VS):-
When we declare a variable inside a class, but outside the method, it is called a static or class variable.
Non-Static variables(NVS)
the variables which are declared by using the name self are known as non-static variables.
ex:-
self.x=10
OBJECT:-
an object is a class of instance, Object can be declarede no.of times.
ABSTRACTION:-
The concept if hiding the properties of one class to another class or out side  class is known as abstraction.
ENCAPSULATION:-
The process of grouping/binding related data along with methodes is called as encapsulation.
INHERITANCE:-
the process of acquiring the properties of one class to another class.
POLYMORPHISM:-
the concept of defining multiple finctionalities or logics to perform an operation is known as polymorphism.

ADVANTAGES OF OOPs CONCEPT:-

1)Offers Security
2)Improves Collaboration
3)Allows Reuse of Code
4)Makes Changes Seamlessly
5)Locates and Fixes Problems Effortlessly
6)Ensures Flexibility
7)Drives Productivity
8)Maintains Code Consistently
9)Encourages Scalability
10)Reduces Development Cost

APPLICATION OF OOPs:-

1)Real Time Systems.
2)Client Server System.
3)Hypertext and Hypermedia.
4)Object Oriented Database.
5)Neural Networks and Parallel Programming.
"""
#EX:-
class number:
    evens = []
    odds = []
    def __init__(self,num):
        self.num = num
        if num%2==0:
            number.evens.append(num)
        else:
            number.odds.append(num)
n1 = number(21)
n2 = number(32)
n3 = number(43)
n4 = number(54)
n5 = number(65)
print("Even Numbers are : ", number.evens)
print("Odd Numbers are : ", number.odds)
n6 = number(110)
n7 = number(125)
n8 = number(118)
n9 = number(140)
print("Even Numbers are : ", number.evens)
print("Odd Numbers are : ", number.odds)
print('---------------------------------')
class Employee:
    company="skywaves softwares"
    def getdetails(self):
        self.ename=input("enter employee name : ")
        self.eid = int(input("enter employee id : "))
        self.esalary = int(input("enter employee salary : "))
        self.desig = input("enter employee designation : ")
    def empdetails(self):
        print("Employee name : ", self.ename)
        print("Employee id : ", self.eid)
        print("Employee Salary : ", self.esalary)
        print("Employee designation : ", self.desig)
e1 = Employee()
print(e1)
e1.getdetails()
e1.empdetails()
e2 = Employee()
print(e2)
e2.getdetails()   
e2.empdetails()
