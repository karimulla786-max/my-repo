#nested class:- it is nothing but a class in a class
 
#example:-
class employee:
    def __init__(self,name,age,skill):
        self.name = name
        self.age = age
        self.skill = skill
   
    def display(self):
        print(self.name)
        print(self.age)
        print(self.skill)
   
    class employement:
        def __init__(self,companyname,salary,domain):
            self.companyname = companyname
            self.salary = salary
            self.domain = domain
        def display(self):
            print(self.companyname)
            print(self.salary)
            print(self.domain)
   
    m = employement("skywaves",25000,"python")
    m.display()
 
p = employee("karimulla",24,"c,ece,")
p.display()