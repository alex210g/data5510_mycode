# encapsulation example, anumber is hidden (private)
class Student:
    def __init__(self, anum, name):
        self.__anum = anum 
        self.__gpa = __gpa
        self.name = name 
        
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

class GradStudent(Student): 
    def __init__ (self, anum, name, gpa, ssn): 
        self.__anum = anum 
        self.__gpa = __gpa
        self.name = name 
        self.degree = degree
        
andy = Student("a000001", "andy", 3.9, 12345)

print(andy.get_name())
andy.set_anum("a00000001")

# print(andy.__anum)
print(andy.get_anum())

saige = GradStudent("a0234", "saige", 4.0, )

print(andy.get_anum())



