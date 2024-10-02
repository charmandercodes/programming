# Functions help you from copy pasting code by calling upon the same lines instead

def add(a, b):
    return a + b 

print(add(2,4))

# You can also have default param values

def add(a=2, b=2):
    return a + b 

print(add(3,4))
print(add(3,4))

# You can also define functions with a variable amount of parameters

def mysum(*numbers):
    result = 0 
    for number in numbers:
        result = result + number
    return result

print(mysum(10,20,30))
