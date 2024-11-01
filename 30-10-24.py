# classmethod:-
#  The classmethod decorator in Python is used to defi ne a class method.
 
# decorator :- 
# Decorators in Python are a way to modify or enhance the behavior of functions or classes without directly modifying their source code.
 
# static variable :-
#  When we declare a variable inside a class but outside method is called static variable.

# Examples:-

# Write a program to deposit or withdraw money in a bank account?
class account:
    def __init__(self):
        self.balance = 0
        print("New Account Created.")
    def deposit(self):
        amount = float(input("Enter amount to Deposit : "))
        self.balance += amount
        print("New Balance : ", self.balance)
    def withdraw(self):
        amount = float(input("Enter amount to Withdraw : "))
        if amount > self.balance:
            print("insufficent balance")
        else:
            self.balance -= amount
            print("New Balance : ", self.balance)
    def Total_Balance(self):
        print("Total Balance : ", self.balance)
account = account()
account.deposit()
account.withdraw()
account.Total_Balance()


class collage:
    def __init__(self,name,branch,rollno,classno,blockno):
        self.name=name
        self.branch="ece"
        self.rollno=rollno
        self.classno=classno
        self.blockno=blockno 
    def display(self):
        print(self.branch)
        print(self.name)
        print(self.rollno)
        print(self.classno)
        print(self.blockno)
c=collage("faisal","ece",76,257,1900)
c.display()
c1=collage("karimulla","ece",77,203,170)
c1.display()


#static variable:
# declaration:
# in static variable is not changing object to object
# we can declare a static variable inside the class directly
# inside the constructor ,instance methode using classname
# outside of class using class name
# inside the class methose using class variable
#
# accessing :
# using class name we can access inside the constructor and instance method
# outside of a class using classname and ORV
# inside of the class method using class variable
#  
