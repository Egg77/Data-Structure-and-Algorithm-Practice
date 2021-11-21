from typing import List

class Heap:

    def __init__ (self):
        self.heapList : List = [0]
        self.length :int = 0

    """This is usually implemented with an array, not a list. But, Python doesn't have arrays, so I'm going to use a List. 
       This may not perfectly represent the time complexity of a heap, but it has the handy by-product of making this thing dynamically sized. """

    # Here are a few helper methods that are going to be needed for this array implementation:

    def leftChild (self, i : int) -> int:
        return 2 * i + 1

    def rightChild (self, i : int) -> int:
        return self.leftChild(i) + 1
    
    def parent (self, i : int) -> int:
        return (i - 2) / 2

    def swap (self, a, b):
        temp = a
        a = b
        b = temp
    
    # And here's the main event:

    def insert (self, key: int):

        self.length += 1
        self.heapList.append = key
        self.fixUp(self.length - 1)


    def deleteMax(self):

        self.swap(self.heapList[0], self.heapList[self.length - 1])
        self.length -= 1
        self.fixDown(self.length, 0)
        return self.heapList[self.length]


    def fixUp(self, i : int):

        while (self.parent(i) is not None) and (self.heapList[self.parent(i)] < self.heapList[i]):
            self.swap(self.heapList[i], self.heapList[self.parent(i)])
            i = self.parent(i)


    def fixDown(self, length: int, i : int):

        while (self.heapList[self.rightChild(i)] is not None) and (self.heapList[self.leftChild(i)] is not None):
            j = self.leftChild(i)

            if (self.heapList[j] < self.heapList[j+1]) and (j != self.length - 1):
                j += 1
            if self.heapList[i] >= self.heapList[j]:
                break

            self.swap(self.heapList[i], self.heapList[j])
            i = j
