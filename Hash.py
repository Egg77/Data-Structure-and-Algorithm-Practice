from typing import List
from LinkedList import *

"""This is a practice implementation of a hash table using chaining to avoid collisions. The hash function will be super simple, but, you know... practice! The previously created (singly) LinkedList class will be used for the chaining."""

class Hash:

    def __init__ (self):
        # This is the "array" (it's a List - Python doesn't have arrays by default, but just go with it) that 
        # will act as the main container for each key-value pair. Each array index will contain its own linked 
        # list, (or "bucket") allowing hashing collisions to be avoided, and also allowing the hash to 
        # dynamically re-size after its initialization.

        self.array : List[LinkedList] = []
        # Since this is a list, and we can't initialize an empty array with a fixed size, need this for loop to 
        # fill each list index with a linkedList object:

        for _ in range (100):
            self.array.append(LinkedList())

    
    def hashFunction(self, key : int) -> int:

        return key % 100


    def insert (self, key : int, value):

        # This always has an O(1) time complexity, because finding both the correct array index and adding a 
        # new value to its bucket are both O(1) operations.

        index = self.hashFunction(key) # Index of array to place the new value
        self.array[index].add(value, key) # Adding the new value - prior LinkedList implementation should handle this already


    """
    The main disadvantage of using chaining is that as each index's linked list grows, the lookup and delete time complexity worsens.
    What begins as O(1) becomes O(1+m), where m is the bucket size of each index. 

    Note that in both of these methods, the bulk of the work is happening in pre-existing LinkedList class methods!
    """

    def delete (self, key : int):

        index = self.hashFunction(key)
        target = self.array[index] # Temporary LinkedList object to access the LinkedList associated with this array index

        result = target.removeAtKey(key)

        if result == -1:
            print("No such key found.")


    def lookup (self, key : int):

        index = self.hashFunction(key)
        result =  self.array[index].searchKey(key) # The searchKey() implementation is a LinkedList class method

        if result == -1:
            print("No such key found!")
            # TODO: "None" is being printed in addition to this, when the key isn't found. 
            # Figure out why that's happening.
        
        else:
            return result