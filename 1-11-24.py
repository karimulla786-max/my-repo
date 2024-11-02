#1.Create a class Person that has instance variables name, age, and gender. Add methods to:
#Initialize these variables.
#Update the age.
#Display the person's information.
# Exercise:
# > Create multiple instances of the Person class.
# > Change the age of one person and display the updated information.


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def update_age(self, new_age):
        self.age = new_age
 
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
 
person1 = Person("karimulla", 24, "Male")
person2 = Person("ashok", 25, "Male")
person3 = Person("ram", 20, "Male")
 
print(person1.display_info())
print(person2.display_info())
print(person3.display_info())
 
person1.update_age(31)
print(person1.display_info())



# 2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
# Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
# Exercise:
# >Create multiple employee instances.
# >Print the total number of employees after adding each new employee.
# >Check whether changing the total_employees in one instance affects the others.


class company:
    employee_count = 0
    def __init__(self):
        self.ename = input("Enter Employee Name Here : ")
        self.edepartment = input("Enter Employee Deportment Here : ")
        company.employee_count += 1
    def display_count(self):
        print("Total Employees : ", company.employee_count)
    def display_details(self):
        print("Name of Employee : ", self.ename)
        print("Name of Employee Deportment : ", self.edepartment)
e1 = company()
print(e1)
e1.display_count()
e1.display_details()
e2 = company()
print(e2)
e2.display_count()
e2.display_details()
e3 = company()
print(e3)
e3.display_count()
e3.display_details()

# 3.Create a class Rectangle that has instance variables length and width. 
#  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
#  Exercise:
#    >Create instances of the Rectangle class with different lengths and widths.
#    >Calculate and print the area for each rectangle.


class Rectangle:
    def get_data(self):
        self.length = int(input("Enter The Length : "))
        self.width = int(input("Enter the Width : "))
    def show_data(self):
        print("Length : ", self.length)
        print("Width : ", self.width)
    def area(self):
        print("Area : ", self.length*self.width)
rect = Rectangle()
rect.get_data()
rect.show_data()
rect.area()

# 4.Create a class Employee where:
#  Each employee has an instance variable salary.
#  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
#  Write a method total_salary that calculates the total salary for an employee (including the bonus).
#  Exercise:
#   >Create several employee instances with different salaries.
#   >Change the bonus amount (static variable) and see how it affects all employees.
#   >Calculate and print the total salary for each employe


class Employee:
    def emp_details(self):
        self.ename = input("Enter Name Of Employee Here : ")
        self.esalary = int(input("Enter Employee Salary Here : "))
        print("Employee Name : ", self.ename)
        print("Employee Salary : ", self.esalary)
    def add_bouns(self):
        bouns = int(input("Enter Employee Bouns Here : "))
        self.esalary += bouns
    
    def total_salary(self):
        print("Total Salary : ", self.esalary)
e1 = Employee()
print(e1)
e1.emp_details()
e1.add_bouns()
e1.total_salary()