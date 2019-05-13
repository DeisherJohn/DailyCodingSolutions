#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Moving Median
#   Daily Problem #: 33
#   Author: John Deisher
#   Date Started: 5/14/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""
from collections import OrderedDict

testList = [2, 1, 5, 7, 2, 0, 5]
myOrdDict = OrderedDict()

for i, num in enumerate(testList):
    myOrdDict[i] = num



print(myOrdDict)