# What is recursion?

# Recursion is where a functions calls itself to solve smaller instances of the 
# the same problem. It has two parts, the base case and recursive part 

# Factorials

# Iterative Approach

n = 7

fact = 1

while n > 0:
    fact = fact * n
    n = n - 1
    print(f"factorial: {fact}")
    print(f"n: {n}")

# Recursive Approach
# the best way I can explain recursion, is that the function will keep calling 
# other smaller versions of its call, until it hits the base, which thereafter
# everything unravels

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(7))

# Recursive method is not always efficient, sometimes iterative method can be more efficient 

# Fibonacci

def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b 
    return a 

print(fibonacci(1000))

def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return (fibonacci2(n-1) + fibonacci2(n-2))

print(fibonacci2(1000))

# recursion error will happen which is stack overflow