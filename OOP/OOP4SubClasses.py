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

class Developer(Employee): # inherits attributes and methods from Employee
    raise_amt = 1.10

    # if we want to add an attribute that is specific to the developers subclass, such as a favourite 
    # programming language, we give them their own init method
    def __init__(self, first, last, pay, prog_lang):
        # instead of copying the entire block from the parent class, we use super() to use the parent's init method
        super().__init__(first, last, pay)
        # Employee.__init__(first, last, pay) would do the same
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None): # dont want to pass mutable objects here
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # add option to add or remove employees that the manager is supervising
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

print(mgr_1.email)

# Additional Python functions
print(isinstance(mgr_1, Manager))

print(issubclass(Developer, Employee))