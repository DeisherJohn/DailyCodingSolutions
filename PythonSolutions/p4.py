#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Find Lowest Missing Int
#   Daily Problem #: 4
#   Author: John Deisher
#   Date Started: 4/25/19
#   Date Finished:	4/25/19
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
import random
import time

random.seed(time.time())

limit = 10
def find_missing_int(_list):
	_list = set(_list)

	for i in range(1,len(_list)):
		if i not in _list:
			return i 

	return len(_list)
	pass

def main():

	testList = []
	testCase1 = [3, 4, -1, 1]
	testCase2 = [1, 2, 0]

	for _ in range(20):
		testList.append(random.randint(0,limit))

	print("List to find missing int: " + str(testCase1))
	print()
	print("First missing number is: " + str(find_missing_int(testCase1)))
	print()
	

	print("List to find missing int: " + str(testCase2))
	print()
	print("First missing number is: " + str(find_missing_int(testCase2)))
	print()

	print("List to find missing int: " + str(testList))
	print()
	print("First missing number is: " + str(find_missing_int(testList)))
	print()
	testList.sort()
	print(testList)

if __name__ == '__main__':
	main()


"""
Output

List to find missing int: [3, 4, -1, 1]

First missing number is: 2

List to find missing int: [1, 2, 0]

First missing number is: 3

List to find missing int: [7, 0, 3, 3, 9, 7, 6, 8, 4, 6, 0, 1, 4, 9, 0, 9, 5, 10, 6, 3]

First missing number is: 2

[0, 0, 0, 1, 3, 3, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8, 9, 9, 9, 10]
[Finished in 0.2s]
"""