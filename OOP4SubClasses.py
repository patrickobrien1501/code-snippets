# Python Object Oriented Programming Tutorial 2 by Corey Schafer

# An example for subclass use could be that there are different types of Employees
# such as developers and managers. Both would have names, salaries and email adresses
# so we can inherit these attributes from the partent class into our subclass

class Employee:
    
    raise_amount = 1.04     # Instance Variable - applies only to the respective instance

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
        return self.pay * self.raise_amount 
        
