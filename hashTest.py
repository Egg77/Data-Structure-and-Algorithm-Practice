from Hash import Hash

myHash = Hash()

for x in range(10):
    myHash.insert(x, int(x+2))

for y in range (10):
    print(myHash.lookup(y))

for z in range (1, 2):
    myHash.delete(z)

for a in range (11):
    print(myHash.lookup(a))