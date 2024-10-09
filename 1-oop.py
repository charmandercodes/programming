# Notes 
# We use object oriented programming to simulate objects from the real world into the programming world
# Objects such as car, book, building 
# A class is a the blueprint or schema that the object will have 
# The object is an instance of that class/schema


# Example 1 

class Person: 
    def __init__(self):
        print("Hello World!")

x = Person()

# What is happening above?
# 1. You have a class called Person
# 2. Inside the class, there is a special method called __init__ that is called initialisor
# 3. This method gets run automatically every time a new Person Object is called 
# 4. So in the last, calling the Person() will print Hello World!

class Person: 
    def __init__(self):
        self.name = "Mike"
        self.age = 25

person1 = Person()

print(person1.name)
print(person1.age)

# What is happening above?
# Like before, the init is being run automatically
# and it is assigning some attributes to the self (instance of object)
# which is then being printed 

class Person: 
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

person1 = Person("Mike", 30, 180)

print(person1.name)
print(person1.age)
print(person1.height)
person1.name = "Henry"
print(person1.name)

# What is happening above?
# Instead of hardcoding the attributes, we can make them
# parameters by adding parameters to self 
# in the init the parameters are referenced 
# and this way we can input diffrent values to different instances


# METHODS 
# Apart from attributes (.name .age)
# you can also define methods .method()

class Person: 
    # Special Constructor (initialiser)
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    # Constructor 

    def get_older(self, years):
        self.age + years
        print(self.age)

    # Special Destructor (removes object from memory)

    def __del__(self):
        print("Object deleted")

    # Special String Constructor (that returns a string of your choice when printing object)
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"
    
        
person1 = Person("Mike", 30, 180)

# helloWorld 

print(person1.get_older(2))

# __str__

print(person1) 

# __del__

print(person1.name)
del person1
# will not work
# print(person1.name) 


# CLASS VARIABLES 

class Person: 
    amount = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount = Person.amount + 1
    def __del__(self):
        Person.amount = Person.amount - 1

person1 = Person("Mike", 30, 180)
person2 = Person("Sarah", 340, 232)
print(Person.amount)
del person1
print(Person.amount)



    
