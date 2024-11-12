import threading 
import time

x = 8192

# The following TRIVIAL program is intended to show how locking works 
# As it is, the program will double if its less than 16.. and half if its more than 1 
# so it will continue like this forever 

################ AS IT IS ##############
# def halve():
#     global x
#     while x > 1:
#         x = x /2
#         print(x)
#         time.sleep(1)
#     print("Reached the minimum ")

# def double():
#     global x
#     while x < 16384:
#         x = x * 2
#         print(x)
#         time.sleep(1)
#     print("Reached the maximum!")

# t1 = threading.Thread(target=halve)
# t2 = threading.Thread(target=double)

# t1.start()
# t2.start()

################ WITH LOCKS ##############

lock = threading.Lock()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x = x /2
        print(x)
        time.sleep(1)
    print("Reached the minimum ")
    lock.release()

def double():
    global x, lock 
    lock.acquire()
    while x < 16384:
        x = x * 2
        print(x)
        time.sleep(1)
    print("Reached the maximum!")
    lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()