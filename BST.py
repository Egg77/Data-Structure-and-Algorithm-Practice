"""Egg's Binary Search Tree (BST) Implementation"""

from Node import Node

class BST:
    
    def __init__ (self):
        self.root : Node = None
        self.height : int = 0
    
    
    def bstInsert (self, value):
        self.root = self.insertNode(value, self.root)


    def insertNode (self, value, node : Node) -> Node:

        """ The worst case scenario time complexity for this - an unbalanced tree (ie. one side is way bigger than the other), is O(n).
        HOWEVER, if the tree is balanced - which is generally the aspiration here - most operations are O(log n). Why? The number of nodes increases
        very rapidly, while the height increases much more slowly. Since the height itself is what determines how many operations need to take place,
        we end up with an O(log n) time complexity, rather than O(n).
        """

        """ YAY recursion. It's pretzel brain time...
        The idea of this entire method is to insert a new node into the tree. In order to do that, the method needs to be called repeatedly, 
        each time comparing the desired input value to the value of each of the current node's left and right children. This needs to keep 
        running until the end is found. This could honestly be achieved with a loop as well, but why use loops when we can be fAnCy.
        
        Also, since this method is recursive, it needs to be called by a main "insert" method to get things going. See bstInsert() above.
        """

        if node == None:
            newNode = Node(value)
            node = newNode

        # Note that setLeft() or setRight() is necessary, since the ultimate goal here is to add a new node somewhere. At each recursive call of this method,
        # the left/right pointer is reset, ultimately being passed the same left/right pointer it already has. However, once an empty left/right pointer is found,
        # a new node is created, and this gets passed to the set left/right method, which allows the newly created node to be connected to the former leaf node preceding it.
        # This is is why in the search function below, the setLeft and setRight methods aren't needed - the tree is only being searched, no new node is created, meaning
        # it also never needs to be connected to the leaf node's left/right pointer. 

        elif (value < node.getValue()):
            node.setLeft(self.insertNode(value, node.getLeft()))
        
        elif (value > node.getValue()):
            node.setRight(self.insertNode(value, node.getRight()))

        return node


    def searchBST (self, value):

        self.search(value, self.root)


    def search (self, value, node : Node):

        if node is None or value == node.getValue():
            return node
        
        if value < node.getValue():
            return self.search(value, node.getLeft())
        
        else:
            return self.search(value, node.getRight())
            
    
    #def delete (self, value):

        # This is probably among the more complicated methods to implement. There's probably a reason the video didn't mention it yet lol
        # Think about this and how to implement... 
        # - Need Node prior to the node to be removed
        # - Also need to figure out how to connect the nodes where the gap has been created
