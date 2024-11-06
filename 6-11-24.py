"""
Inheritence:-
        it inherits the properties from parent class to the child class.
 
types of inheritence:-

1.sigle inheritence:-  
               a child class inherits properties and methods from a single parent class.
 
2.multiple inheritence:-
               a class to inherit attributes and methods from more than one parent class.
 
3.hierachical inheritence:- 
               inheriting properties and method from single class from multiple class at a same time.
 
4.hybrid inheritence:-
               using more then one type of inheritence.
5.multilevel:-
               inheriting properties and method from multrilevel classes to single class
"""


#single inheritence example:-

class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name ("makes a sound."))
 
class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
 
    def speak(self):
        print(self.name)
        print(self.breed,"bark")

dog = Dog("Buddy", "German Shepherd")
dog.speak()  

# multiple inheritance:-

class Worker:
    def do_work(self):
        print("Doing work")
 
class Manager:
    def manage(self):
        print("Managing the team")
 
class Employee(Worker, Manager):
    def perform(self):
        print("Performing employee duties")
 
employee = Employee()
employee.do_work()  
employee.manage()  
employee.perform()  

# multilevel inheritance:-

class Organization:
    def company_name(self):
        print("Company: skywaves software pvt")
 
class Department(Organization):
    def department_name(self):
        print("Department: Software Development")
 
class Worker(Department):
    def job_title(self):
        print("Job Title: Software Engineer")
 
worker = Worker()
worker.company_name()   
worker.department_name() 
worker.job_title()      


# hierachical inheritence:- 


class Shape:
    def draw(self):
        print("Drawing a shape")
 
class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius
 
class Rectangle(Shape):
    def area(self, length, width):
        return length * width
 
class Square(Rectangle):  
    def area(self, side):
        return side * side
 
circle = Circle()
rectangle = Rectangle()
square = Square()
circle.draw()  
print("Circle Area:", circle.area(5)) 
rectangle.draw()  
print("Rectangle Area:", rectangle.area(5, 10))   
square.draw()  
print("Square Area:", square.area(4))


# hybrid inheritance:-

class Device:
    def power_on(self):
        print("Device powered on")
 
class Phone(Device):
    def make_call(self):
        print("Making a call")
 
class SmartPhone(Phone):
    def browse_internet(self):
        print("Browsing the internet")
 
class Laptop(Device):
    def run_program(self):
        print("Running program")
 
class SmartLaptop(Laptop):
    def video_call(self):
        print("Making a video call")
 

smartphone = SmartPhone()
smartphone.power_on() 
smartphone.make_call()  
smartphone.browse_internet()  

smartlaptop = SmartLaptop()
smartlaptop.power_on()   
smartlaptop.run_program() 
smartlaptop.video_call()  