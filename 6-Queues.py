# Why do we need queues?
# Let's say we have the following list:

# numbers = [10, 20, 30, 40, 50]

# We also have some number of threads accessing each element in the list,
# performing some operation (e.g., multiplying by 2).
# We use a variable called 'count' to track the next element to be accessed.

# Example scenario:
# Thread 1 accesses 'numbers[0]' (value 10), then increments 'count' to 1.
# Thread 2 accesses 'numbers[1]' (value 20), then increments 'count' to 2.
# Thread 3 accesses 'numbers[2]' (value 30), then increments 'count' to 3.

# If Thread 1 and Thread 2 finish at the exact same time,
# they might both increment the 'count' variable simultaneously,
# resulting in 'count' being set to 4 (or higher) instead of 3.
# This would cause 'numbers[3]' (value 40) to be skipped.

# This is where queues come in:
# Like a real-life queue, when an element is accessed, it is removed (popped)
# from the queue. The next element is then automatically available for any
# thread that is ready to process it. This ensures that each element is processed
# exactly once, without any being missed.

import queue

# by default it is first in first out 

q = queue.Queue()

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    q.put(number)

print(q.get())
print(q.get())

# You can also do Last In First Out

q = queue.LifoQueue()

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    q.put(number)

print(q.get())
print(q.get())

# You can also set your own priority of assingment in a queue 

q = queue.PriorityQueue()

q.put((2, "Hello World!"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get())

# You can also access each value in tuple 

q = queue.PriorityQueue()

q.put((2, "Hello World!"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))


while not q.empty():
    print(q.get()[1])


