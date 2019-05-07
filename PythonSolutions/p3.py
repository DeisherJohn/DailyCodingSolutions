#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Serialize binary tree
#   Daily Problem #: 3
#   Author: John Deisher
#   Date Started: 4/25/19
#   Date Finished: 4/25/19
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

   Tree Structure

                root
            /             \
           left            right
        /       \
    left.left   null
"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        pass

def serialize(_tree):
    
    if _tree is None:
        return "null"
    else:
        return _tree.val + "," + serialize(_tree.left) + "," + serialize(_tree.right)

def reconstruct_tree(_splitString):
    if len(_splitString) is not 0:
        if _splitString[0] is 'null':
            return Node(_splitString.pop(0))

        branch = Node(_splitString.pop(0))

        if len(_splitString) is not 0:
            branch.left = reconstruct_tree(_splitString)
        if len(_splitString) is not 0:
            branch.right = reconstruct_tree(_splitString)

        return branch
    pass

def deserialize(_sstring):
    split_string = _sstring.split(',')

    if len(split_string) > 1:
        return reconstruct_tree(split_string)

def main():

    testTree = Node("root", Node("left", Node("left.left")), Node("right"))

    assert deserialize(serialize(testTree)).left.left.val == 'left.left'
    pass

if __name__ == '__main__':
    main()