#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Find sum in list
#   Daily Problem #: 1
#   Author: John Deisher
#   Date Started: 5/7/19
#   Date Finished: 5/7/19
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Follower Answer: 

Use a doubly linked list of nodes that carry the product of the nodes before and after them. 
once it is built it only requires one pass to get the list back of all nodes with no division
"""
#node used for divisionless product finding
class productListNode(object):
	"""docstring for productListNode"""
	def __init__(self, value):
		super(productListNode, self).__init__()
		self.value = value
		self.next = None
		self.prev = None
		self.productOfPrev = 1
		self.productOfNext = 1

class productList(object):
	"""docstring for productList"""
	def __init__(self, startNode = None):
		super(productList, self).__init__()
		self.head = startNode
		self.end = None

	def build(self, listOfNumbers):
		for num in listOfNumbers:
			newNode = productListNode(num)

			if self.end is not None:
				newNode.prev = self.end
				self.end.next = newNode
				self.end = newNode
			else:
				self.head = newNode
				self.end = newNode

			if newNode.prev is not None:
				newNode.productOfPrev = newNode.prev.value * newNode.prev.productOfPrev
		
		currentNode = self.end
		while currentNode is not None:
			if currentNode.next is not None:
				currentNode.productOfNext = currentNode.next.value * currentNode.next.productOfNext

			currentNode = currentNode.prev
		pass
		
	def print_list_of_products(self):
		returnList = list()
		currentNode = self.head

		while currentNode is not None:
			returnList.append(currentNode.productOfPrev * currentNode.productOfNext)

			currentNode = currentNode.next

		return returnList
		pass

#if division can be used, this returns the product with 2 passes
def products_of_numbers_without_ith(listOfNumbers):
	product = 1
	zeros_in_list = 0
	productList = []

	for num in listOfNumbers:
		if num != 0:
			product *= num
		else:
			zeros_in_list += 1

	for num in listOfNumbers:
		if zeros_in_list > 1:
			productList.append(0)
			continue

		if num != 0 and zeros_in_list == 1:
			productList.append(0)
		elif num == 0:
			productList.append(product)
		else:
			productList.append(product//num)

	return productList
	pass

def main():
	testCase1 = [1, 2, 3, 4, 5]
	testCase2 = [3, 2, 1]
	zeroTestCase = [1, 2, 3, 4, 5, 0]
	doubleZeroTestCase = [1, 2, 0, 3, 4, 5, 0]

	print("Test case 1: " + str(testCase1))
	print("Output: " + str(products_of_numbers_without_ith(testCase1)))
	print()
	print("Test case 2: " + str(testCase2))
	print("Output: " + str(products_of_numbers_without_ith(testCase2)))
	print()
	print("Zero test Case: " + str(zeroTestCase))
	print("Output: " + str(products_of_numbers_without_ith(zeroTestCase)))
	print()
	print("Double zero test case: " + str(doubleZeroTestCase))
	print("Output: " + str(products_of_numbers_without_ith(doubleZeroTestCase)))

	testWithoutDivision1 = productList()
	testWithoutDivision1.build(testCase1)

	testWithoutDivision2 = productList()
	testWithoutDivision2.build(testCase2)

	testWithoutDivision3 = productList()
	testWithoutDivision3.build(zeroTestCase)

	testWithoutDivision4 = productList()
	testWithoutDivision4.build(doubleZeroTestCase)

	print()
	print("Test without division on testCase1: " + str(testCase1))
	print("Output: " + str(testWithoutDivision1.print_list_of_products()))
	print()
	print("Test without division on testCase2: " + str(testCase2))
	print("Output: " + str(testWithoutDivision2.print_list_of_products()))
	print()
	print("Test without division on zeroTestCase: " + str(zeroTestCase))
	print("Output: " + str(testWithoutDivision3.print_list_of_products()))
	print()
	print("Test without division on doubleZeroTestCase: " + str(doubleZeroTestCase))
	print("Output: " + str(testWithoutDivision4.print_list_of_products()))
	pass

if __name__ == '__main__':
	main()


"""
OUTPUT

Test case 1: [1, 2, 3, 4, 5]
Output: [120, 60, 40, 30, 24]

Test case 2: [3, 2, 1]
Output: [2, 3, 6]

Zero test Case: [1, 2, 3, 4, 5, 0]
Output: [0, 0, 0, 0, 0, 120]

Double zero test case: [1, 2, 0, 3, 4, 5, 0]
Output: [0, 0, 0, 0, 0, 0, 0]

Test without division on testCase1: [1, 2, 3, 4, 5]
Output: [120, 60, 40, 30, 24]

Test without division on testCase2: [3, 2, 1]
Output: [2, 3, 6]

Test without division on zeroTestCase: [1, 2, 3, 4, 5, 0]
Output: [0, 0, 0, 0, 0, 120]

Test without division on doubleZeroTestCase: [1, 2, 0, 3, 4, 5, 0]
Output: [0, 0, 0, 0, 0, 0, 0]
[Finished in 0.2s]
"""