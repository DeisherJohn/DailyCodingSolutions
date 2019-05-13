#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: XOR Linked List
#   Daily Problem #: 6
#   Author: John Deisher
#   Date Started: 5/8/19
#   Date Finished: 5/8/19
#   Note: below is psudo code only since I do not have a pointers in python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, 
which is an XOR of the next node and the previous node. Implement an XOR linked list; 
it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer functions that 
converts between nodes and memory addresses.
"""

class XORNode(object):
    """docstring for XORNode"""
    def __init__(self, value):
        super(XORNode, self).__init__()
        self.value = value
        self.both = None

    def get_next(self, last = 0):
        #this functions can traverse the list in both directions
        last_prt = last  if last != 0 else 0
        #returns a memory address to either the next or prev link, depending on the last address given
        return self.both ^ last_prt


class XORLinkedList(object):
    """docstring for XORLinkedList"""
    def __init__(self):
        super(XORLinkedList, self).__init__()
        self.head = None
        self.tail = None
        self.last_prt = None

    def get_pointer(obj):
        return object_hex_address

    def dereference_pointer(ptr):
        return object_at_hex_address

    def add(self, element):
        newElem = XORNode(element)

        if self.head is None:
            self.head = get_pointer(newElem)
            self.tail = get_pointer(newElem)
        else:
            newElem.both = self.tail
            dereference_pointer(self.tail).both = dereference_pointer(self.tail).both ^ get_pointer(newElem)
            self.tail = get_pointer(newElem)
        pass
        
    def get(self, index):
        current_memory_address = self.head
        prev_memory_address = 0

        for _ in range(index):
            temp_holder = current_memory_index
            current_memory_address = dereference_pointer(current_memory_address).get_next(prev_memory_address)
            prev_memory_address = temp_holder
            pass

        return dereference_pointer(current_memory_address)
        pass




"""
Due to get_pointer and dereference_pointer being psudo functions this code is not compilable
however, this general process would work given working functions. 
"""