import threading

# so first the myfunction gets called and is waiting

event = threading.Event()

def myfunction():
    print("Waiting for event to trigger")
    event.wait()
    print("Performing action XYZ now...")

t1 = threading.Thread(target=myfunction)
t1.start()

# then based on input, the event is triggered (continutes myfunciton)

x = input("Do you want to trigger the event? (y/n)")

if x == 'y':
    event.set()