## HANDLING EXCEPTIONS 
# we do this so the program can still run
# and not crash even when there are errors

try: 
    x = int(input("First Number: "))
    y = int(input("First Number: "))
    print(x / y)
except:
    print("General Error")

try: 
    x = int(input("First Number: "))
    y = int(input("First Number: "))
    print(x / y)
except ValueError:
    print("Please enter a valid number next time!")
except ZeroDivisionError:
    print("Cannot divide by 0")
finally:
    print("DONE!")

# finally is used for streams to close them, 
# because they are prone error

## RAISING EXCEPTIONS

# assertion error 
# if you need some condition to be a way in your program

x = 100 
y = 20
assert(x < y)


# raise exceptions to for self checking if things go wrong or not 

def some_function():
    if True:
        raise Exception("general exception")
some_function()

# stops from executing
# def some_function():
#    if True:
#        raise ValueError("combed exception")
# some_function()









    

