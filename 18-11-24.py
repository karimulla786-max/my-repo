""" Encapuslation
While modeling real-life objects with object oriented programming, we ensure to bundle related information together to 
clearly separate information of different objects.
Bundling of related properties and actions together is called Encapsulation.
Classes can be used to bundle related properties and actions. """



class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera= camera
    def make_call(self,number):
        print("calling..{}".format(number))
mobile_obj = Mobile("iPhone 16 Pro max", "50 MP")
mobile_obj.make_call(85613795375)



class student:
    def __init__(self, name, rollno, dept):
        self.__name = name
        self.__rollno = rollno
        self.__dept = dept
 
    def get_student(self):
        print(self.__name)
        print(self.__rollno)
        print(self.__dept)
        
    def promot_nextsection(self, percentage):
        self.__dept *= (1 + percentage / 100)
 
std = student("karimulla", 24, 29)
print(std.get_student())  
std.promot_nextsection(10)
print(std.get_student())  


