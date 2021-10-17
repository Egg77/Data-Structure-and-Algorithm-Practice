from stack_queue import queue

from random import random

myqueue : queue = queue()

for _ in range(10):
    myqueue.enqueue(random())

print(myqueue.size())
myqueue.printQueue()

for _ in range(3):
    myqueue.dequeue()

print(myqueue.size())
myqueue.printQueue()
