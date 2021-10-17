from stack_queue import stack
from random import random

myStack : stack = stack()

for _ in range(128):
    myStack.push(random())

print(myStack.size())
myStack.printStack()

for _ in range(64):
    myStack.pop()

print(myStack.size())
myStack.printStack()
print(myStack.peek())
