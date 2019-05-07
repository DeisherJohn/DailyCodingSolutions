#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Find sum in list
#   Daily Problem #: 1
#   Author: John Deisher
#   Date Started: 5/7/19
#   Date Finished: 5/7/19
#	Notes: complete in a single pass, 
#		   idea for solution comes from Google Mock Interview video on youtube
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from random import randint, seed
from time import time

seed(time())

def findSum(inputList, sumToFind):

	complementList = list()

	for item in inputList:
		if item in complementList:
			return True
		else:
			complementList.append(sumToFind - item)
	return False
	pass

def main():

	testCase1 = [10, 15, 3, 7]
	testCase2 = list()

	for _ in range(10):
		testCase2.append(randint(0,10))

	testItem1 = randint(5,15)
	testItem2 = randint(5,15)
	print("Is sum " + str(17) + " in " + str(testCase1) + " : " + str(findSum(testCase1, 17)))
	print("Is sum " + str(testItem1) + " in " + str(testCase2) + " : " + str(findSum(testCase2, testItem1)))
	print("Is sum " + str(testItem2) + " in " + str(testCase2) + " : " + str(findSum(testCase2, testItem2)))

	pass

if __name__ == '__main__':
	main()

"""
OUTPUT: 

Is sum 17 in [10, 15, 3, 7] : True
Is sum 3 in [1, 1, 8, 4, 9, 10, 1, 7, 2, 1] : True
Is sum 7 in [1, 1, 8, 4, 9, 10, 1, 7, 2, 1] : False
[Finished in 0.3s]
""