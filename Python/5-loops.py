# Standard Loops

x = 0

while x < 5:
    x = x + 1
    print("are we there yet?")

y = 0 

for y in range(1,6):
    print("are we there yet!")


# Control Statments

# break - breaks the iterations 

z = 0 

while z < 10:
    z = z + 1
    if z == 5:
        break
    print(z)

# continue - skips an iteration

z = 0 

while z < 10:
    z = z + 1
    if z == 5:
        continue
    print(z)

# pass - skips 

for i in range(5):
    pass

# trickier to do in while loops 