# Python Object Oriented Programming Tutorial 2 by Corey Schafer

# An example for subclass use could be that there are different types of Employees
# such as developers and managers. Both would have names, salaries and email adresses
# so we can inherit these attributes from the partent class into our subclass

class Employee:
    
    raise_amt = 1.04     # Instance Variable - applies only to the respective instance

    # initialize - the init method runs each time a new instance of the class is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return ("{} {}" .format(self.first, self.last))

    def apply_raise(self):
        # (1) using self here in front of raise_amount because it should only apply to the instance
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    pass

dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'User', 60000)

# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)