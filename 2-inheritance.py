# Inheritance, as the name suggests is to make new classes that are 
# specialised classes of a class that already exists
# Dog might inherit from the class animal 
# Worker might inherit from the class Person

class Person: 

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"
    

class Worker(Person):
    
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary
    
    def __str__(self):
        text = super(Worker, self).__str__()
        text = text + f", Salary {self.salary}"
        return text 
    
    def yearly_salary(self):
        return self.salary * 12 

worker1 = Worker("Henry", 40, 176, 3000)
print(worker1)
print(worker1.yearly_salary())

# By writing super(Worker, self) you are saying 
# "I want to use the parent class of worker, and I want to use
# it in the current instance"
# .__whatever__ is then a method of the parent class which you are accessing

# Operator Overloading 

# is when you redefine the stock standard operators builtin for python + - * 
# for your own behaviour for your classes

# in the following code __add__ replaces +
# and it adds the x components, y components, and returns the new vector 

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __add__(self, object2):
        return Vector(self.x + object2.x, self.y + object2.y)
    
    def __sub__(self, object2):
               return Vector(self.x - object2.x, self.y - object2.y)

    def __str__(self):
         return f"X: {self.x}, Y: {self.y}"

v1 = Vector(2,2)
v2 = Vector(2,2)

print(v1)
print(v2)

v3 = v1 - v2

print(v3)

v3 = v1 + v2

print(v3)
