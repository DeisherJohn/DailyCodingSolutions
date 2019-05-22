#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Palindrome Maker
#   Daily Problem #: 34
#   Author: John Deisher
#   Date Started: 5/22/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""
from random import randint, seed
from time import time

seed(time())

class Binary_Node(object):
    """docstring for Binary_Node"""
    def __init__(self, value):
        super(Binary_Node, self).__init__()
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def add_node(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Binary_Node(value)
                self.left.parent = self
            else:
                self.left.add_node(value)
        else:
            if self.right is None:
                self.right = Binary_Node(value)
                self.right.parent = self
            else:
                self.right.add_node(value)
        pass
        
class Binary_search_tree(object):
    """docstring for Binary_search_tree"""
    def __init__(self):
        super(Binary_search_tree, self).__init__()
        self.root = None

    def add_node(self, value):
        if self.root is None:
            self.root = Binary_Node(value)
        else: 
            self.root.add_node(value)
        pass

    def find_second_highest(self):

        iter_node = self.root

        while iter_node is not None:
            if iter_node.right is None:
                break
            iter_node = iter_node.right

        if iter_node.left is not None:
            iter_node = iter_node.left

            while iter_node is not None:
                if iter_node.right is None:
                    break
                iter_node = iter_node.right
        else:
            iter_node = iter_node.parent

        return iter_node.value
        pass


def main():
    testCases = list(list())
    
    for _ in range(5):
        testList = list()
        for _ in range(20):
            testList.append(randint(0,100))
        testCases.append(testList)

    for test in testCases:
        myTree = Binary_search_tree()
        for num in test:
            myTree.add_node(num)
        
        print("\nSecond highest number in tree is: {}".format(myTree.find_second_highest()))
        print("Tested on list: {}".format(test))
        test.sort()
        print("Sorted list: {}".format(test))
        
    pass
        
if __name__ == '__main__':
    main()

"""
OUTPUT:

Second highest number in tree is: 98
Tested on list: [50, 19, 2, 36, 60, 71, 30, 0, 94, 56, 81, 29, 57, 73, 100, 55, 45, 66, 98, 54]
Sorted list: [0, 2, 19, 29, 30, 36, 45, 50, 54, 55, 56, 57, 60, 66, 71, 73, 81, 94, 98, 100]

Second highest number in tree is: 96
Tested on list: [96, 3, 31, 16, 64, 1, 57, 52, 25, 43, 23, 27, 46, 33, 61, 9, 59, 90, 98, 61]
Sorted list: [1, 3, 9, 16, 23, 25, 27, 31, 33, 43, 46, 52, 57, 59, 61, 61, 64, 90, 96, 98]

Second highest number in tree is: 90
Tested on list: [17, 81, 87, 29, 50, 27, 80, 30, 87, 79, 73, 89, 65, 15, 91, 46, 24, 49, 90, 88]
Sorted list: [15, 17, 24, 27, 29, 30, 46, 49, 50, 65, 73, 79, 80, 81, 87, 87, 88, 89, 90, 91]

Second highest number in tree is: 79
Tested on list: [97, 79, 29, 31, 53, 29, 76, 17, 64, 70, 3, 32, 21, 31, 3, 25, 24, 49, 15, 48]
Sorted list: [3, 3, 15, 17, 21, 24, 25, 29, 29, 31, 31, 32, 48, 49, 53, 64, 70, 76, 79, 97]

Second highest number in tree is: 96
Tested on list: [86, 60, 87, 33, 44, 5, 41, 93, 48, 30, 54, 93, 4, 25, 45, 76, 100, 82, 96, 65]
Sorted list: [4, 5, 25, 30, 33, 41, 44, 45, 48, 54, 60, 65, 76, 82, 86, 87, 93, 93, 96, 100]
[Finished in 0.2s]
"""