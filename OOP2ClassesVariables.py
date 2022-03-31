# Python Object Oriented Programming Tutorial 2 by Corey Schafer

class Employee:
    
    num_of_emps = 0         # Class Variable - applies to entire class
    raise_amount = 1.04     # Instance Variable - applies only to the respective instance

    # initialize - the init method runs each time a new instance of the class is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # (2) Here it makes only sense to apply the number of employees counter to the class itself
        # and not to an instance
        Employee.num_of_emps += 1
    
    def fullname(self):
        return ("{} {}" .format(self.first, self.last))

    def apply_raise(self):
        # (1) using self here in front of raise_amount because it should only apply to the instance
        return self.pay * self.raise_amount 
        
print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
emp_3 = Employee('Chris', 'Dean', 40000)

print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.apply_raise())

print(emp_1.__dict__)

print(Employee.num_of_emps)