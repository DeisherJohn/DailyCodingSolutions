#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Graph Transversal
#   Daily Problem #: 9
#   Author: John Deisher
#   Date Started: 5/2/19
#   Date Finished: 5/2/19
#	Notes: Negatives and zero can be in the array
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
import random
import time

class weightedGraph(object):
	"""docstring for weightedGraph
		This is a class based approch, it has a O(n) run build time, O(1) for evaluating
		changes based on the addition of a new number, and has O(1) space. Numbers can only
		be added at the end of this, numbers needing to be added in the middle with require a 
		rebuild of the whole graph

		negative numbers and 0 are treated as unselected (or 0) since we are not required to
		select them and they will do nothing to increase the overall sum

		general structure is based off the viterby algorithm but without a backtract path, 
		by using nodes instead of numbers a backtrace path could be seleted"""
		
	def __init__(self):
		super(weightedGraph, self).__init__()
		self.end = 0
		self.second_to_last_node = 0
		self.third_to_last_node = 0
		
	def add_value(self, newValue):
		if newValue <= 0:
			newValue = max(self.end, self.second_to_last_node, self.third_to_last_node)
			self.third_to_last_node = newValue
			self.second_to_last_node = newValue
		else:
			newValue += max(self.second_to_last_node, self.third_to_last_node)
			self.third_to_last_node = self.second_to_last_node
			self.second_to_last_node = self.end
			
		self.end = newValue
		pass

	def get_largest_path(self):
		return max(self.end, self.second_to_last_node)
		pass

	def build_graph(self, items):
		self.end = self.second_to_last_node = self.third_to_last_node = 0
		for item in items:
			self.add_value(item)
		pass

fillInput = []
testCase1 =  [2, 4, 6, 2, 5]
testCase2 =  [5, 1, 1, 5]

myGraph = weightedGraph()

for x in range(10):
	fillInput.append(random.randrange(-2,10))
print(fillInput)

myGraph.build_graph(fillInput)

print(myGraph.get_largest_path())

myGraph.build_graph(testCase1)
print(myGraph.get_largest_path())
myGraph.build_graph(testCase2)
print(myGraph.get_largest_path())