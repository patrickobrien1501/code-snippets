# Python Object Oriented Programming Tutorial 1 by Corey Schafer

class Employee:
    
    # initialize - the init method runs each time a new instance of the class is created
    # the instance is passed as itself so that is why "self" is the 1st argument by convention
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    # the instance is passed to class methods as well
    def fullname(self):
        return ("{} {}" .format(self.first, self.last))

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))