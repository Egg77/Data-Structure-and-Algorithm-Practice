"""This is the most generic, reusable Node possible. Lots of different names for the same thing - references to different Nodes. Arguably not the most space-efficient, but whatever. This is to facilitate frictionless learning and keep my other modules less cluttered with extra classes."""

class Node:
    def __init__ (self, value, key : int = 0):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
        self.left = None
        self.right = None

    def getValue (self):
        return self.value

    def setValue (self, value):
        self.value = value

    def getKey (self) -> int:
        return self.key
    
    def setKey (self, key):
        self.key = key
    
    def getNext (self):
        return self.next
    
    def setNext (self, newNext):
        self.next = newNext
    
    def getLeft (self):
        return self.left
    
    def setLeft (self, newLeft):
        self.Left = newLeft
    
    def getRight (self):
        return self.right

    def setRight (self, newRight):
        self.Right = newRight