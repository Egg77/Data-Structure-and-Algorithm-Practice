from LinkedList import LinkedList

myList : LinkedList = LinkedList()
myList.add("hello")
myList.add(34)
myList.add("huh")
myList.add(12347812)
myList.printList()

myList.removeBack()
myList.printList()

myList.insertFront(785349)
myList.printList()

print(myList.getValueAt(0))
print(str(myList.search("huh")))

myList.updateAt(33333, 2)
myList.printList()

myList.removeFront()
myList.printList()

myList.addAt(4444, 1)
myList.printList()

myList.removeAt(2)
myList.printList()