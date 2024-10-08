# Strings are just like lists, they are a sequence of characters
# you can use list functions on strings as a result 

# Case manipulation functions
print('''
      
      CASE MANIPULATION
      
      ''')

text = "This is my text!"

text = text.upper()

print(text)

text = text.lower()

print(text)

text = text.title()

print(text)

text = text.swapcase()

print(text)

# counting

print('''
      
      COUNTING
      
      ''')

text = "I am Mike and Life is Life"

print(text.count("Life"))

print(len(text))

print('''
      
      SLICING
      
      ''')

print(text[2])

print(text[6:])

# Indexing 

print('''
      
      FINDING INDEX
      
      ''')

print(text.find("Mike"))

# Looping 

print('''
      
      LOOPING
      
      ''')

for letter in text:
    print(letter)


# Escape Characters

print('''
      
      ESCAPING CHARACTERS
      
      ''')

text = "Line 1 \nLine 2"

'''
Line 1 
Line 2
'''

print(text)

# Joining Strings

print('''
      
      JOINING
      
      ''')

separator = "."

mylist = ["I", "am", "Mike"]

print(separator.join(mylist))

# Separating into list

print('''
      
      SEPARATING
      
      ''')

text = "I love yellow bees"

words = text.split(' ')

print(words)

words = text.split('o')

print(words)

# Replacing

print('''
      
      REPLACING
      
      ''')

text = "I love yellow bees"

print(text.replace("Mike", "Sara"))

# String Formatting 

print('''
      
      STRING FORMATTING
      
      ''')

name = input()
age = int(input())

print(f"My name is {name} and I am {age} years old!")


