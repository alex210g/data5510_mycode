class Employee:
    def __init__ (self, name, salary):
        self.name = name 
        self.salary = salary
    #Calculate the increase and pass in the employee and raise
    def salary_increase(self, percent):
        return self.salary + (percent * self.salary)
    
#Instantiate the employee John as an object. 
employee_john = Employee("John", 5000)
#Print the new employee salary by passing in .10 as the percentage increase
print("Employees new salary", employee_john.salary_increase(.10))