# Python Object Oriented Programming Tutorial 2 by Corey Schafer

class Employee:
    
    # Class Variable - applies to entire class
    num_of_emps = 0      
    # Instance Variable - applies only to the respective instance   
    raise_amt = 1.04     

    # initialize - the init method runs each time 
    # a new instance of the class is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # (2) Here it makes only sense to apply the number 
        # of employees counter to the class itself and not to an instance
        Employee.num_of_emps += 1
    
    def fullname(self):
        return ("{} {}" .format(self.first, self.last))

    def apply_raise(self):
        # (1) using self here in front of raise_amount because it 
        # should only apply to the instance
        return self.pay * self.raise_amount 
        
    @classmethod
    # automatically accept the class as first argument 
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod # also called "alternative constructors"
    # automatically accept the class as first argument
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # return the new Employee object
        return cls(first, last, pay)

    @staticmethod # also called "alternative constructors"
    # doesn't depend on any speficic instance or the class
    # static methods do not take the class or the instance as arguments
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# Employee.raise_amt = 1.05

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

emp_string_1 = 'John-Doe-70000'

new_emp_1 = Employee.from_string(emp_string_1)

print(new_emp_1.__dict__)

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))