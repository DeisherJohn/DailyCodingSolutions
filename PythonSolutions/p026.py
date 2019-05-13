#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Remove kth to last item from a singly linked list
#   Daily Problem #: 26
#   Author: John Deisher
#   Date Started: 5/10/2019
#   Date Finished: 5/10/2019 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class Node(object):
    """docstring for Node
        Singly Linked List Node
    """
    def __init__(self, value = None):
        super(Node, self).__init__()
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    """docstring for SinglyLinkedList"""
    def __init__(self, head = None):
        super(SinglyLinkedList, self).__init__()
        self.head = head

    def addItem(self, item):
        #used to build the SLL
        iterItem = self.head

        if iterItem is None:
            self.head = item
            return

        while iterItem.next != None:
            iterItem = iterItem.next

        iterItem.next = item
        pass

    def popNextItem(self, item):
        #gets the node next to the given item
        popedItem = item.next
        item.next = item.next.next
        return popedItem
        pass

    def printList(self):
        #debugging and printing method
        printList = list()
        iterItem = self.head
        while iterItem is not None:
            printList.append(iterItem.value)
            iterItem = iterItem.next

        print(printList)
        pass

    def removeIthItem(self, ith_to_last_place):
        ith_minus_one = self.head
        iterItem = self.head

        for _ in range(ith_to_last_place):
            iterItem = iterItem.next
            if iterItem is None:
                return False

        while iterItem.next is not None:
            iterItem = iterItem.next
            ith_minus_one = ith_minus_one.next

        itemToRemove = self.popNextItem(ith_minus_one)

        return itemToRemove
        pass
        
def main():
    testList = SinglyLinkedList()

    for i in range(10):
        testList.addItem(Node(i))

    testList.printList()
    removedItem = testList.removeIthItem(5)

    if removedItem is not False:
        print("Item removed: " + str(removedItem.value))
    else:
        print("INDEX TO LARGE")
    testList.printList()
    pass


if __name__ == '__main__':
    main()