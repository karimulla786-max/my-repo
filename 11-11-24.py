# Polymorphism:- It refers to the use of a single type entity (method, operator or object) 
#                to represent different types in different scenarios.
# Method overloding:- Two or more methods have the same name but different numbers of parameters or different types of parameters.
#method overriding:-  when you have two methods with the same name that each perform different tasks
# Ex:-

class bus:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive!")
class bike:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("ride!")
class lorry:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("ridder!")
bus1 = bus("mahindra", "Mustang")     
bike1 = bike("royal enfiled", " 500cc") 
lorry1 = lorry("ashok", "hcv")    
for x in (bus1, bike1, lorry1):
  x.move()