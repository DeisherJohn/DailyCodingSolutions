#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Count Unival Trees
#   Daily Problem #: 8
#   Author: John Deisher
#   Date Started: 5/7/19
#   Date Finished: 5/7/19
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class BinaryTreeNode(object):
	"""docstring for BinaryTreeNode"""
	def __init__(self, value):
		super(BinaryTreeNode, self).__init__()
		self.value = value
		self.left = None
		self.right = None

def check_for_unival(binaryNode):
	if binaryNode is None:
		return 0

	count = check_for_unival(binaryNode.left) + check_for_unival(binaryNode.right)

	if binaryNode.left == binaryNode.right == None:
		count += 1
	elif binaryNode.left is None or binaryNode.right is None:
		pass
	elif binaryNode.left.value == binaryNode.right.value:
		count += 1

	return count
	pass

def main():

	root = BinaryTreeNode(0)
	root.left = BinaryTreeNode(1)
	root.right = BinaryTreeNode(0)
	root.right.left = BinaryTreeNode(1)
	root.right.left.left = BinaryTreeNode(1)
	root.right.left.right = BinaryTreeNode(1)
	root.right.right = BinaryTreeNode(0)

	print("Number of unival nodes in tree: " + str(check_for_unival(root)))
	pass

if __name__ == '__main__':
	main()

"""
OUTPUT: 

Number of unival nodes in tree: 5
[Finished in 0.2s]
"""