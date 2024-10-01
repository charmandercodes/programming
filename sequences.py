## LISTS 

mylist = [1,2,3,"string",5]

print(mylist)

## Accessing parts of list via index

print(mylist[3]) 

## Reassigning parts of list 

mylist[2] = "another string"

print(mylist)

## Slicing the list 

print(mylist[:2])

print(mylist[2:5])

print(mylist[-3])

## For looping the list

mylist = [1,2,3,4,5]

for x in mylist:
    print(2 ** x)

## LIST OPERATIONS

x = [1,2,3]
y = [4,5,"string"]

# adding lists together
print(x + y)

# multiplying by scaler to increase size of list
print(y * 4)

## LIST FUNCTIONS 

x = [1,2,3,4,5]

# note: if you add boolean or string, this will only work with len
# x = [1,2,3,True,"string"]

print(len(x))
print(max(x))
print(min(x))

# LIST METHODS 

x = [1,2,3,True,"string"]

# Appending 

x.append("new value")

print(x)

# Inserting 

x.insert(2, "inserted value")

print(x)

# Removing 

# HAS to be in the list, otherwise error 
# x.remove("not in list")

x.remove("new value")

print(x)

# Popping 

# removes by index, not by value 

x.pop(0)
print(x)

# Print Index 

print(x.index(3))
print(x.index('inserted value'))

# Cool thing you can do: pop a value you do not know index of

x.pop(x.index("inserted value"))

print(x)

# Sort: only works with numbers

x = [5,4,3,2,1]

# Changes the list 
x.sort()
print(x)

# Just prints sorted version of list
print(sorted(x))


# TUPLES
# are just lists that cannot have values changed 
# defined with () instead of []

y = (1,2,3)
# Cannot do this
# y[2] = 10 
print(y[2])

# How to work with tuples freely 
# type cast them into lists and them back into tuples

y = list(y)

y[2] = 10 

y = tuple(y)

print(y)


# DICTIONARIES 
# Key value pairs 
person = {
    'name': 'Mark',
    'age': 24,
    'gender': 'male',
    True:88
}
# Getting stuff from dictionary has to be done by unique key
print(person['name'])
print(person[True])
# Adding a new key 

person['newkey'] = 67 

print(person)

# Dictionary Methods

print(person.items())

print(person.keys())

print(person.values())

# MEMBERSHIP OPERATORS

x = [1,2,3]

print(2 in x)
print(2 not in x)
print(7 in x)
print(7 not in x)

x = 10 

if type(x) is int:
    print("x is int")
else:
    print("x is not int")