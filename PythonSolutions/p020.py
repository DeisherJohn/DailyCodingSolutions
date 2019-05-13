#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Detecting intersection of single linked list
#   Daily Problem #: 20
#   Author: John Deisher
#   Date Started: 5/9/2019
#   Date Finished: 5/9/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
from random import randint, seed
from time import time
seed(time())

class SLLNode(object):
    """docstring for SLLNode"""
    def __init__(self, value):
        super(SLLNode, self).__init__()
        self.value = value
        self.next = None

class SLL(object):
    """docstring for SLL"""
    def __init__(self, head):
        super(SLL, self).__init__()
        self.head = head

    def add_node(self, node):
        currentNode = self.head

        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = node
        pass

    """
    All class methods can be moved out, they are for utility of printing and 
    retreving length, they can be accomplished outside of the class just as easily. 
    """
    def print_list(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
        pass

    def get_list(self, node):

        if node is None:
            return ''

        return str(node.value) + ',' + self.get_list(node.next) 
        pass

    def get_len(self):
        current = self.head
        length = 0

        while current is not None:
            length += 1
            current = current.next
        return length

def return_intersection_node(sllA, sllB):
    current_A_node = sllA.head
    len_A = sllA.get_len()

    current_B_node = sllB.head
    len_B = sllB.get_len()

    if len_A > len_B:
        for _ in range(len_A - len_B):
            current_A_node = current_A_node.next
    elif len_A < len_B:
        for _ in range(len_B - len_A):
            current_B_node = current_B_node.next

    while current_A_node is not current_B_node:
        current_A_node = current_A_node.next
        current_B_node = current_B_node.next

    if current_A_node is None:
        return None
    else:
        return current_A_node
    pass

def testListIntersection():
    SLLA = SLL(SLLNode(1))

    for _ in range(randint(5,10)):
        SLLA.add_node(SLLNode(randint(0,20)))
    

    SLLB = SLL(SLLNode(2))

    for _ in range(randint(5,10)):
        SLLB.add_node(SLLNode(randint(0,20)))


    SLLCommon = SLL(SLLNode(randint(0,20)))
    for _ in range(randint(5,10)):
        SLLCommon.add_node(SLLNode(randint(0,20)))

    SLLA.add_node(SLLCommon.head)
    SLLB.add_node(SLLCommon.head)
    print("\n---- START OF TEST ----")
    print("Values of list A")
    print(SLLA.get_list(SLLA.head))
    print("\nValues of list B")
    print(SLLB.get_list(SLLB.head))
    print("\nValues of list common List")
    print(SLLCommon.get_list(SLLCommon.head))

    commonNode = return_intersection_node(SLLA, SLLB)

    if commonNode is not None:
        print("\nValue at start of common list: " + str(commonNode.value))
    else:
        print("\nThere was no intersection")
    pass

def main():
    for _ in range(5):
        testListIntersection()
    
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT:

---- START OF TEST ----
Values of list A
1,6,1,14,13,2,20,2,4,15,12,16,20,1,8,9,

Values of list B
2,6,9,1,2,6,0,3,15,12,3,4,15,12,16,20,1,8,9,

Values of list common List
4,15,12,16,20,1,8,9,

Value at start of common list: 4

---- START OF TEST ----
Values of list A
1,10,19,18,8,8,17,3,0,18,9,17,8,1,8,

Values of list B
2,3,14,0,4,10,10,18,9,17,8,1,8,

Values of list common List
18,9,17,8,1,8,

Value at start of common list: 18

---- START OF TEST ----
Values of list A
1,14,1,20,8,16,14,13,1,2,7,12,

Values of list B
2,4,15,11,20,14,19,14,13,1,2,7,12,

Values of list common List
14,13,1,2,7,12,

Value at start of common list: 14

---- START OF TEST ----
Values of list A
1,7,17,11,14,11,1,19,6,1,2,18,14,13,17,13,

Values of list B
2,11,5,7,10,3,3,2,18,14,13,17,13,

Values of list common List
2,18,14,13,17,13,

Value at start of common list: 2

---- START OF TEST ----
Values of list A
1,7,20,7,3,12,11,12,16,20,0,19,0,3,18,19,19,16,16,15,

Values of list B
2,7,1,20,18,3,12,0,19,0,3,18,19,19,16,16,15,

Values of list common List
0,19,0,3,18,19,19,16,16,15,

Value at start of common list: 0
[Finished in 0.1s]
"""