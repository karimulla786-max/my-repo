"""""
1. Single Inheritance

Problem Statement: Create a base class Animal with an attribute name and a method speak(). Then, create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
 
Tasks:

Define a base class Animal with an __init__ method that takes name as a parameter.

Define a method speak() in Animal that prints "Animal sound".

Create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".

Create an instance of Dog and call the speak() method.
""""" 


class Animal:
    def __init__(self, name):
        self.name = name  
    
    def speak(self):
        print("Animal sound") 
 
class Dog(Animal):
    def speak(self):
        print("Bark")  
    
dog = Dog("Buddy")
dog.speak()


""""
2. Multiple Inheritance

1.Problem Statement: Create a class Teacher with an attribute subject. Then, create a class Researcher with an attribute field. Finally, create a class TeachingResearcher that inherits from both Teacher and Researcher, and has an additional method to display both attributes.

Tasks:
Define a Teacher class with an __init__ method to initialize subject.
Define a Researcher class with an __init__ method to initialize field.
Define a TeachingResearcher class that inherits from both Teacher and Researcher, and has an __init__ method to initialize both subject and field. Add a method to display both.
Create an object of TeachingResearcher and display its attributes.

""" 


class Teacher:
    def __init__(self):
        self.subject = input("subject name: ")

class Researcher:
    def __init__(self):
        self.field = input("enter the field: ")
class TeacherResearcher(Teacher, Researcher):
    def __init__(self):
        Teacher.__init__(self)
        Researcher.__init__(self)
        
    def display(self):
        print(f"Subject: {self.subject}")
        print(f"Field: {self.field}")
teacher = TeacherResearcher()
teacher.display()
"""
Problem Statement: Create two base classes: Bird and Flyable. Bird should have an attribute species, and Flyable should have a method fly().
 Then, create a derived class Eagle that inherits from both Bird and Flyable.
Tasks:
Define a class Bird with an attribute species.
Define a class Flyable with a method fly() that prints "Flying".
Create a class Eagle that inherits from both Bird and Flyable, and has a method to display species and flying capability.
Create an instance of Eagle and call its methods.
"""
class Bird:
    def __init__(self):
        self.species = input("enter the species: ")
class flyover:
    def flyable(self):
        self.flyable = input("enter the flyable: ")
class Eagle(Bird,flyover):
    def __init__(self):
        Bird.__init__(self)
        flyover.flyable(self)
    def display(self):
        print(self.species)
        print(self.flyable)
Birds=Eagle()
Birds.display()


""""
3. Multilevel Inheritance
Problem Statement: Create a class hierarchy where Person is the base class, Employee is derived from Person, and Manager is derived from Employee. Each class should add an additional attribute, and a method to display all attributes from the hierarchy.

Tasks:
Define a base class Person with attributes name and age.
Define a derived class Employee with an additional attribute salary.
Define another derived class Manager that inherits from Employee and adds an attribute department.
Implement methods to display the information in each class.
Create an instance of Manager and display its information.

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
 
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)  
        self.salary = salary
 
    def display_employee(self):
        self.display_person()  
        print(f"Salary: {self.salary}")
 
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)  
        self.department = department
 
    def display_manager(self):
        self.display_employee()  
        print(f"Department: {self.department}")
 

manager = Manager("karimulla", 25, 100000, "IT Enigneer")
manager.display_manager()


""""

4. Hierarchical Inheritance
 
1.Problem Statement: Design a class hierarchy for an employee management system with the following structure:
 
Employee: Base class with name and salary.
Developer: Inherits from Employee with an additional attribute programming_language.
Manager: Inherits from Employee with an additional attribute team_size.
Intern: Inherits from Developer and has an additional attribute internship_duration.
Implement a method to display the details of each employee.


"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
 
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
 
    def display_developer(self):
        self.display_employee()
        print(f"Programming Language: {self.programming_language}")
 
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
 
    def display_manager(self):
        self.display_employee()
        print(f"Team Size: {self.team_size}")
 
class Intern(Developer):
    def __init__(self, name, salary, programming_language, internship_duration):
        super().__init__(name, salary, programming_language)
        self.internship_duration = internship_duration
 
    def display_intern(self):
        self.display_developer()
        print(f"Internship Duration: {self.internship_duration} months")
 
    developer = Developer("karimulla", 80000, "Python")
    developer.display_developer()


    manager = Manager("nikhil", 120000, 12)
    manager.display_manager()
    
intern = Intern("kowshik", 40000, "Java", 7)
intern.display_intern()



