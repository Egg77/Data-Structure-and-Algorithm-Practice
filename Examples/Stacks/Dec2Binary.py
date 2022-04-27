"""
This program converts an integer (base 10) to binary (base 2).

The purpose of this exercise is to specifically perform this conversion using a Stack data structure. 
"""

from collections import deque

def Dec2Binary (input_int):

    stack = deque()
    temp = input_int
    output = ''

    if input_int == 0:
        return 0

    while temp != 0:
        stack.append(temp % 2)
        temp = temp // 2 # The // floors the division
    
    while stack:
        output += str(stack.pop())

    return output

testInt = 16
print(testInt)
print(Dec2Binary(testInt))