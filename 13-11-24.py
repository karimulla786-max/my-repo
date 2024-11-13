"""""

#2.Problem Statement: Create a base class Vehicle with attributes brand and model. Then, create two derived classes Car and Bike, both inheriting from Vehicle, and adding their own attributes and methods.

#Tasks:
#Define a base class Vehicle with attributes brand and model.
#Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
#Create another derived class Bike that inherits from Vehicle and adds an attribute type.
#Implement methods to display the details of the vehicles.
#Create instances of both Car and Bike and display their information.



# Base class Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand)
        print(self.model)
              


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)  
        self.num_doors = num_doors

    def display(self):
        super().display()  
        print(self.num_doors)

class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)  
        self.bike_type = bike_type

    def display(self):
        super().display()  
        print(self.bike_type)

car = Car("honda", "elevate", 4)

bike = Bike("royal enfield", "500cc", "Sport")

car.display()

bike.display()


#5. Hybrid Inheritance
#Problem Statement: Create a class structure to represent hybrid inheritance:

##Device: Base class with name attribute.
#Phone: Derived from Device with an additional phone_number attribute.
#Tablet: Derived from Device with an additional screen_size attribute.
#Smartphone: Derived from both Phone and Tablet with an additional attribute os.

#Tasks:
#Define a base class Device with an attribute name.
#Define a class Phone that inherits from Device and adds an attribute phone_number.
#Define a class Tablet that inherits from Device and adds an attribute screen_size.
#Define a class Smartphone that inherits from both Phone and Tablet, adding an attribute os.
#Implement methods to display all attributes of the Smartphone.
#Create an instance of Smartphone and display its information.


class Device:
    def __init__(self):
        self.name = input("Enter Device Name Here : ")
 
    def device_details(self):
        print("Device Name : ", self.name)
 
class Phone(Device):
    def __init__(self):
        Device.__init__(self)
        self.phone_number = int(input("Enter Phone Number Here : "))
 
    def phone_details(self):
        print("Phone Number : ", self.phone_number)
 
class Tablet(Device):
    def __init__(self):
        self.screen_size = float(input("Enter Screen Size Here : "))
 
    def tablet_details(self):
        print("Screen Size : ", self.screen_size)
   
class Smartphone(Phone,Tablet):
    def __init__(self):
        Phone.__init__(self)
        Tablet.__init__(self)
        self.os = input("Enter Os Here : ")
 
    def smartphone_details(self):
        print("OS : ", self.os)
   
 
s=Smartphone()
print('-----------')
s.device_details()
s.phone_details()
s.tablet_details()
s.smartphone_details()



#6.Basic Inheritance
#Problem Statement: Create a class Person with attributes: name and age. 
# Create another class Student that inherits from Person and has 
# an additional attribute grade. Define methods in both classes to display the attributes.

#Tasks:
##Define a Person class with an __init__ method to initialize name and age.
#Define a Student class that inherits from Person, with an additional attribute grade.
#Define a display_info method in both Person and Student classes to print all attributes.
#Create objects for both Person and Student and display their information.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self.name)
        print(self.age)


class Student(Person):
    def __init__(self, name, age, grade):
        
        super().__init__(name, age)  
        self.grade = grade

    def display_info(self):
        
        super().display_info()  
        print(self.grade)

person = Person("karimulla", 20)

student = Student("pandu", 25, "A+")


person.display()
student.display()




# Abstraction in Python is a concept that allows you to hide complex implementation details and show only the essential features of an object or function. It helps in reducing complexity by providing a clear interface and hiding unnecessary information.
 
 
#1. Abstract Classes: These are classes that cannot be instantiated directly and may contain abstract methods that must be implemented by subclasses. You can create abstract classes using the abc (Abstract Base Class) module.
 
 
#2. Abstract Methods: Methods in an abstract class that have no implementation. They must be overridden in any subclass.
 
 
 
#Example:
 
from abc import ABC, abstractmethod
 
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
 
class Dog(Animal):
    def make_sound(self):
        print("Bark")
 
dog = Dog()

"""

#Real time example of abstraction:-

from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def show_speed(self):
        pass
 

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."
    
    def stop_engine(self):
        return "Car engine stopped."
    
    def show_speed(self):
        return "Car speed: 120 km/h."
 
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started."
    
    def stop_engine(self):
        return "Bike engine stopped."
    
    def show_speed(self):
        return "Bike speed: 80 km/h."

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started."
    
    def stop_engine(self):
        return "Truck engine stopped."
    
    def show_speed(self):
        return "Truck speed: 60 km/h."
 
vehicles = [Car(), Bike(), Truck()]
 
for vehicle in vehicles:
    print(vehicle.start_engine())
    print(vehicle.show_speed())
    print(vehicle.stop_engine())
    print()

