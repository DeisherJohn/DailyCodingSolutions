#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Locking Binary Tree
#   Daily Problem #: 24
#   Author: John Deisher
#   Date Started: 5/9/2019
#   Date Finished: 5/9/2019
#   Notes: I assume if any decendant or ancestor is locked that a node cannot be chagned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Implement locking in a binary tree. 
A binary tree node can be locked or unlocked only if all of its descendants or 
ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, 
then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. 
Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. 
You may assume the class is used in a single-threaded program, 
so there is no need for actual locks or mutexes. Each method should run in O(h), 
where h is the height of the tree.
"""


class LockingNode(object):
    """docstring for LockingNode"""
    def __init__(self, value, parent = None):
        super(LockingNode, self).__init__()
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.__lock = False

    def is_locked(self):
        return self.__lock
        pass

    def lock(self):
        if not self.check_decentants_for_lock() and not self.check_ancestor_for_lock() and not self.is_locked():
            self.__lock = True
            return True
        else:
            return False
        pass

    def unlock(self):
        if not self.check_decentants_for_lock() and not self.check_ancestor_for_lock() and self.is_locked():
            self.__lock = False
            return True
        else:
            return False
        pass

    def check_decentants_for_lock(self):
        if self is None: return False

        for node in [self.left, self.right]:
            if node is not None:
                if node.is_locked():
                    return True
                if node.check_decentants_for_lock():
                    return True
        return False
        pass

    def check_ancestor_for_lock(self):
        if self.parent is not None:
            if self.parent.is_locked():
                return True
            return self.parent.check_ancestor_for_lock()
        pass


def main():
    myTree = LockingNode("Root")

    myTree.left = LockingNode("Left", myTree)
    myTree.right = LockingNode("Right", myTree)
    myTree.left.left = LockingNode("Left.Left", myTree.left)

    for node in [myTree.left, myTree.left.left, myTree, myTree.right]:

        print("\nChecking lock on {} : {}".format(node.value, node.is_locked()))
        print("Locking {} : {}".format(node.value, node.lock()))
        print("Checking lock on {} : {}".format(node.value, node.is_locked()))
    pass

if __name__ == '__main__':
    main()


"""
OUTPUT: 

Checking lock on Left : False
Locking Left : True
Checking lock on Left : True

Checking lock on Left.Left : False
Locking Left.Left : False
Checking lock on Left.Left : False

Checking lock on Root : False
Locking Root : False
Checking lock on Root : False

Checking lock on Right : False
Locking Right : True
Checking lock on Right : True

[Finished in 0.1s]
"""