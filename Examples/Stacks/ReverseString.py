''' The purpose of this example is to show how to use a Stack to reverse a string in Python
    Note that while a Stack can be implemented using a Python list, this performs append() and pop() operations at O(n) time complexity.

    Instead, this example will use collections.deque - a proper Stack implementation, that performs the aforementioned operations at O(1) time complexity.

    It's also worth noting that Python has a built in way to reverse a String, but this can be used if specifically required to use a Stack.
'''

from collections import deque

def ReverseString (input_string):

    reversedString = ""
    stack = deque()

    if not input_string: #str is falsy
        return ""
    
    else:

        for c in input_string:
            stack.append(c)
        
        while stack: #deque is also falsy
            reversedString += stack.pop()
    
    return reversedString


testString = "No, this is PATRICK!"
print(testString)
print(ReverseString(testString))
