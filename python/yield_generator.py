# Iterators - can be used many times
mylist = [x for x in range(3)]
for i in mylist: print(i)  # 0 1 2
for i in mylist: print(i)  # 0 1 2

# Generators - can only be used once
mygenerator = (x for x in range(3))
for i in mygenerator: print(i)  # 0 1 2
for i in mygenerator: print(i)  #

# Yield - return generator
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i

mygenerator = createGenerator()
print(mygenerator)  # <generator object createGenerator at 0xb7555c34>
for i in mygenerator: print(i)  # 0 1 2
for i in mygenerator: print(i)  #
