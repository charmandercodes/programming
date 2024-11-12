import threading 

# In the following code, "Another text" will be outputting before the t1 thread, 
# even though it is after, this is because "Another Text" is part of the main thread 
# Like before with the t2 thread, its execution is based on multiple factors
def hello():
    for x in range(50):
        print("Hello!")

t1 = threading.Thread(target=hello)
t1.start()

# To ensure t1 gets executed before the print statement, use .join

t1.join()

print("Another Text")

