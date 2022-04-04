# Python Object Oriented Programming Tutorial 6 by Corey Schafer

class Employee:
    
    # initialize - the init method runs each time a new instance of the class is created
    # the instance is passed as itself so that is why "self" is the 1st argument by convention
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    # property decorators "@property" let us define attributes as we would definde class methods
    # but call them as class attributes below without "()"
    # Getters

    @property
    def email(self):
        return ("{}.{}@company.com" .format(self.first, self.last))
    
    # the instance is passed to class methods as well
    @property
    def fullname(self):
        return ("{} {}" .format(self.first, self.last))

    # Setters
    # setter properties --> @xxx.setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    # Deleters
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)

emp_1.fullname = 'Corey Schafer'

print(emp_1.fullname)

# run the deleter
del emp_1.fullname