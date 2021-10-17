"""Egg's Various Stack and Queue Implementations"""

from Node import Node

"""This stack ADT data type uses a linked list with the head serving as the top of the stack, enabling push and pop to be both O(1) operations"""

class stack:

    def __init__ (self):
        self.head = None
        self.length : int = 0

    
    def push(self, value):
        
        newNode = Node(value)
        newNode.setNext(self.head)
        self.head = newNode
        self.length += 1


    def pop (self):

        # Check if the stack is empty
        if self.head == None:
            raise IndexError
        
        # Grab value from the head, change the head to the next node
        else:
            tempValue = self.head.getValue()
            self.head = self.head.getNext()
            self.length -= 1
            return tempValue
    
        # Let garbage collection tidy up the poor little orphaned node

    def peek (self):
    
        # Check if the stack is empty
        if self.head == None:
            raise IndexError
        
        else:
            return self.head.getValue()


    def size(self) -> int:

        return self.length


    def printStack(self):

        # This is a convenience method just to see what's in the stack. Since the entire stack needs to be traversed, it's an O(n) operation

        if self.head == None:
            print("The stack is empty")
        
        else:
            tempNode = self.head
            indexCount = 0

            while tempNode is not None:
                print ("{" + str(indexCount) + ", " + str(tempNode.getValue()) + "}")
                tempNode = tempNode.getNext()
                indexCount += 1



"""This queue ADT uses a linked list data structure with head and tail pointers to enable dynamic sizing and O(1) queue and enqueue opeartions"""

class queue:

    def __init__ (self):
        self.head = None
        self.tail = None
        self.length = 0


    def enqueue (self, value):

        newNode = Node(value)

        if self.head == None:
            self.head = newNode
        
        else:
            self.tail.setNext(newNode)
            
        self.tail = newNode
        self.length += 1


    def dequeue (self):

        if self.head == None:
            raise IndexError
        
        else:
            value = self.head.getValue()
            self.head = self.head.getNext()
            self.length -= 1
            return value


    def size (self) -> int:
        
        return self.length


    def printQueue(self):

        # This is a convenience method just to see what's in the queue. Since the entire stack needs to be traversed, it's an O(n) operation

        if self.head == None:
            print("The queue is empty")
        
        else:
            tempNode = self.head
            indexCount = 0

            while tempNode is not None:
                print ("{" + str(indexCount) + ", " + str(tempNode.getValue()) + "}")
                tempNode = tempNode.getNext()
                indexCount += 1
