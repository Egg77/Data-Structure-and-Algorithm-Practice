""" Egg's Singly Linked List Implementation """

"""  
    @TODO:
    - Swap two nodes
    - Reverse
    - Sort using some method I haven't learned yet!
    - Sort using some other sorting method I haven't learned yet!

"""

from Node import *

class LinkedList:

    def __init__ (self):
        self.head: Node = None
        self.tail: Node = None
        self.length : int = 0

    def length(self) -> int:
        # Since we're tracking the length of the list in the LinkedList class, this is super easy and becomes an O(1) operation

        return self.length


    def add (self, value, key : int = 0):
        # Since we're using a tail Node in the Linked List class, this is super easy and becomes an O(1) operation

        # Make a shiny new Node and pass it the desired value
        newNode = Node(value, key)

        # Check if the list is empty and assign the value to the head, which will also be the tail in this case
        if self.length == 0:
            # Point the class-level head pointer to the newly created Node
            self.head = newNode
            # Point the class-level tail pointer to the newly created Node
            self.tail = newNode

        else:
            self.tail.setNext(newNode)
            self.tail = newNode

        self.length += 1


    def removeBack (self):
        # Since we're using a tail Node in the Linked List class, this is super easy and becomes an O(1) operation

        # Check to see if the list is empty
        if self.length == 0:
            raise IndexError

        else:
            current = self.head

            # Traverse through the list until the second last Node is found
            while current.getNext().getNext() is not None:
                current = current.getNext()

            # Set the second last Node's next pointer to None, making it the new tail
            current.setNext(None)
            # Set the tail Node to the former second last Node
            self.tail = current
            # Let Python's garbage collection deal with the severed Node, scary as that may be
            self.length -= 1


    def insertFront (self, value):
        # This is an O(1) operation, since we always keep track of the head

        newNode = Node(value)        

        # Check if the list is empty and assign the value to the head, which will also be the tail in this case
        if self.length == 0:
            # Point the class-level head pointer to the newly created Node
            self.head = newNode
            # Point the class-level tail pointer to the newly created Node
            self.tail = newNode

        else:
            newNode.setNext(self.head)
            self.head = newNode

        self.length += 1


    def removeFront (self):
        # This is an O(1) operation, since we always keep track of the head

        # Check if the list is empty
        if self.length == 0:
            # Nothing to do here
            raise IndexError

        else:
            self.head = self.head.getNext()
            self.length -= 1


    def getValueAt (self, index : int):
        # Since the list needs to be traversed to get the specified index, this is an O(n) operation

        # Raise an error if the list is empty or if the specified index is out of bounds
        if (self.length == 0) or (index > (self.length - 1)):
            raise IndexError

        else:
            current  = self.head
            counter  = 0

            while counter != index:
                current = current.getNext()
                counter += 1

            return current.getValue()   


    def updateAt (self, value, index : int):
        # Since the list needs to be traversed to get the specified index, this is an O(n) operation

        # If the list is empty or the provided index doesn't exist, raise an error
        if (index > (self.length - 1)) or (self.length == 0):
            raise IndexError

        else:
            current  = self.head
            counter = 0

            while counter != index:
                current = current.getNext()
                counter += 1

            current.setValue(value)


    def search (self, value) -> bool:
        # Returns True if at least one instance of the specified value is found
        # Could also make a version of this method that returns an integer that counts all matched values...
        
        # Since the list needs to be traversed to get the specified index, this is an O(n) operation
        
        if self.length == 0:
            return False

        else:
            current = self.head

            while current is not None:
                if current.getValue() == value:
                    return True
                else:
                    current = current.getNext()
            
            # If we've made it here and still haven't found the value, it's not there
            return False


    def searchKey (self, key : int):
        # Searches each node for a specified key, returns the value associated with that node.
        # Made specifically for the Hash practice implementation.

        if self.length == 0:
            return -1
        
        else:
            current = self.head

            while current is not None:
                if current.getKey() == key:
                    return current.getValue()
                else:
                    current = current.getNext()
        
        return -1


    def printList (self):
        # This is an O(n) operation, because it's literally printing the entire list

        if self.length == 0:
            print("The list is empty :3")
            return
        
        else:
            current = self.head
            indexCount = 0
            print("List length: " + str(self.length))

            while current is not None:
                print ("{" + str(indexCount) + ", " + str(current.getValue()) + "}")
                current = current.getNext()
                indexCount += 1


    def addAt (self, value, index : int):
        # This is an O(n) operation, because the list up to the insertion index needs to be traversed

        if index > (self.length - 1):
            raise IndexError

        # Make a shiny new Node
        newNode = Node(value)

        # Check if the list is empty
        if (self.length == 0) and (index == 0):
            self.head = newNode
            self.tail = newNode

        else:
            current = self.head
            prev = None
            counter = 0

            while counter != index:
                prev = current
                current = current.getNext()
                counter +=1
            
            prev.setNext(newNode)
            newNode.setNext(current)
        
        self.length += 1


    def removeAt (self, index : int):
        # This is an O(n) operation, because the list up to the removal index needs to be traversed

        if (index > (self.length -1)) or (self.length == 0):
            raise IndexError
        
        else:
            current = self.head
            prev = None
            counter = 0

            while counter != index:
                prev = current
                current = current.getNext()
                counter += 1
            
            prev.setNext(current.getNext())
            self.length -= 1

            # And current is set adrift to await garbage collection...


    def removeAtKey (self, key : int):
        # This is an O(n) operation, because the list up to the removal key needs to be traversed

        if self.searchKey(key) == -1:
            return -1
        
        else:
            current = self.head

            if current.getKey() == key:
                self.removeFront()
            
            else:
                prev = None

                print(current.getKey())
                print(key)

                while current.getKey() != key:
                    prev = current
                    current = current.getNext()
                
                prev.setNext(current.getNext())

            self.length -= 1

        # And current is set adrift to await garbage collection...