# Lets say we have the following two functions 
import threading 

def function1():
    for x in range(10):
        print("ONE")
def function2():
    for x in range(10):
        print("TWO")


# These functions will always print one after the other 
# To get them to work in parallel, we need to use threading

# function1()
# function2()

# What are threads?
# Threads are basically building blocks of processes
# This program itself is a thread, and we can spawn multiple threads as part of the same process
# to get them work in parallel, and communicate with each other very well

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)


t1.start()
t2.start()

# Here the OS is switching between the threads based on various factors like CPU loads, 
# thread priorities and interal timing mechanisms of the Python interpreter
# They are running in parallel but not truly,since some are being outputted more times
# To get pure parellism, we need to implement synchronisation 


