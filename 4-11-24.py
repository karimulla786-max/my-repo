
"""
static method:- 

static method does not require an instance of the class to be called and cannot access
or modify the class state. Static methods are used when some functionality relates to the class
but does not need any instance to perform the work
To define a static method, you can use the @staticmethod decorator
 
>we are not using instance and static variable
>we are not passing any paramter like self or cls
>we have to pass @staticmethod decorate
>we can access static method using class anem and cls variable
 
class method:-

To create a class method, we use the @classmethod decorator or the classmethod()
function. The method should take cls as its first parameter, which refers to the class itself.

>inside the class method have  to use only static variable
>while declaring class method have to pass @class method
>while declaring class method have to pass cls as first parameter
>using cls keyword we can declare and can access the data in side class method has context menu

 
instance method:

>we can declaring and accessing a instance variable inside a method
>while declaring instance method have to pass self as an first paramater
>we can acces thses instance method using orv or classname
 
"""

# static method Example:-

class fruits:
    @staticmethod
    def m():
        orange=2
        mango=1
        kiwi=5
        apple=6
        totaliteams=orange+mango+kiwi+apple
        return totaliteams
f=fruits()
print(f.m())



class add:
    @staticmethod 
    def m():
        a=9
        b=8
        print(a+b)
a1=add()
a1.m()



class bank:
    @staticmethod
    def m():
        name="karimulla"
        age=24
        acc_no=10139329
        moble=37363763828
        return name ,age,acc_no,moble

c=bank()
print(c.m())

# Class method Example:-

class collage:
    branch="ece"
    @classmethod
    def m(cls,name,rollno):
        cls.collagename="karimulla"
        print(name)
        print(rollno)
        print(cls.branch)
        print(cls.collagename)


class Animal:
    totalprice=10000
    @classmethod
    def m(cls,dog,cat,bird):
        cls.shopname="ANIMAL STORE"
        print(dog)
        print(cat)
        print(bird)
        print(Animal.totalprice)
        print(cls.shopname)

animals=Animal()
animals.m("plute","rocky","swift")


# Instance method Example:-


class Cart:  
    def __init__(self):
        self.items = {}
    def add_item(self, item_name,quantity):
        self.items[item_name] = quantity
    def display_items(self):  
        print(self.items)
 
a = Cart()
a.add_item("book", 3)
a.display_items()
 
#2nd ex
class Student:
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def show(self):
        print('Name:', self.name, 'Age:', self.age)


 