print ("hello world")

#more on object oriennted programming 

#3 pillars of OOP

# 1. encapsulation, which is adding controls around your data
# 2. inheritance: extending functionality to a child class
# 3. polymorphism: ability to extend functionality from multiple classes
# encapsulation example, anumber is hidden (private)
class Student:
    def __init__(self, anum, ssn, gpa, name):
        self.__anum = anum #the __ makes it private
        self.__ssn = ssn 
        slef.__gpa = gpa
        self.name = name

        #getters and setters, help you get the private data
    def get_anum(self):
        return self.__anum
        
    def set_anum(self, anum):
        self.__anum = anum
        
    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name
        
    def set_anum(self, anum):
        self.__anum = anum
        
    def get_gpa(self):
        return self.__gpa 
    
    def set_gpa(self, gpa): ## does not need __ becasue it is public 
        self.__gpa = gpa




andy = Student("a000001", 124, 3.8, "andy")
print(andy.get_name())

# print(andy.__anum)

andy.set_anum("a00000001")

print(andy.get_anum())



