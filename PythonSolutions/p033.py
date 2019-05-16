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

class SortedList(object):
    """docstring for SortedList"""
    def __init__(self):
        super(SortedList, self).__init__()
        self.data = list()
        self.length = 0

    def add_item(self, item):
        self.data.insert(0,item)
        self.data.sort()
        self.length += 1
        pass
    
    def get_median(self):
        mid = self.length//2
        if self.length % 2 == 0:
            #even
            lower = (self.data[mid-1]) 
            higher = self.data[mid]

            return (higher + lower)/2
        else:
            #odd
            return self.data[mid]



testList = [2, 1, 5, 7, 2, 0, 5]
sortList = SortedList()

for i, num in enumerate(testList):
    sortList.add_item(num)
    print("\ndata: " + str(sortList.data))
    print("Median is: " +str(sortList.get_median()))


"""
OUTPUT 


data: [2]
Median is: 2

data: [1, 2]
Median is: 1.5

data: [1, 2, 5]
Median is: 2

data: [1, 2, 5, 7]
Median is: 3.5

data: [1, 2, 2, 5, 7]
Median is: 2

data: [0, 1, 2, 2, 5, 7]
Median is: 2.0

data: [0, 1, 2, 2, 5, 5, 7]
Median is: 2
[Finished in 0.1s]

"""