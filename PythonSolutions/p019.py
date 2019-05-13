#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Minimum Cost of Painting Houses
#   Daily Problem #: 19
#   Author: John Deisher
#   Date Started: 5/11/2019
#   Date Finished: 5/11/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
return the minimum cost which achieves this goal.
"""

from random import randint, seed
from time import time

seed(time())


class HouseNode(object):
    """docstring for HouseNode"""
    def __init__(self, color_cost, parent = None):
        super(HouseNode, self).__init__()
        self.color_backptr_cost = color_cost.copy()
        self.parent = parent

        if parent is not None:
            self.fill_backptr()

    def get_min_not_at_index(self, i = -1):
        #if i == -1 will get the min
        min_cost = max(self.color_backptr_cost)
        min_ind = 0
        for ind,cost in enumerate(self.color_backptr_cost):
            if i == ind:
                continue
            if min_cost >= cost:
                min_cost = cost
                min_ind = ind       
        return min_cost
        pass
        
    def fill_backptr(self):
        for i in range(len(self.color_backptr_cost)):
            self.color_backptr_cost[i] += self.parent.get_min_not_at_index(i)
        pass

    def print_house(self):
        if self.parent is None:
            print("Parent is None")
        print("Color Cost: {}".format(str(self.color_backptr_cost)))
        pass
        
def matrix_maker(n,k):
    #n is rows, k is columns
    newHouse = list()
    for _ in range(n):
        newRow = list()
        for _ in range(k):
            newRow.append(randint(1,10))
        newHouse.append(newRow)
    return newHouse
    pass

def main():
    #3 houses, 4 colors
    
    testMatrix = list()
    costMatrix = [[3,4,5,6],[7,5,3,1],[8,7,4,3]]
    
    testMatrix.append(costMatrix)
    testMatrix.append(matrix_maker(5,5))
    testMatrix.append(matrix_maker(10,5))
    testMatrix.append(matrix_maker(10,3))


    for test in testMatrix:

        root = None
        currentNode = None

        for k in test:
            if root == None:
                root = HouseNode(k)
                currentNode = root
            else:
                newNode = HouseNode(k,currentNode)
                currentNode = newNode

        print("Minimum cost for matrix: {} is : {}".format(str(test),str(currentNode.get_min_not_at_index())))

    pass

if __name__ == '__main__':
    main()

"""
Minimum cost for matrix: [  [3, 4, 5, 6], 
                            [7, 5, 3, 1], 
                            [8, 7, 4, 3]] is : 8

Minimum cost for matrix: [  [1, 9, 7, 7, 2], 
                            [4, 9, 6, 7, 4], 
                            [10, 3, 1, 2, 4], 
                            [2, 3, 10, 2, 5], 
                            [9, 10, 10, 6, 2]] is : 10 

Minimum cost for matrix: [  [7, 9, 2, 1, 10],
                            [10, 1, 3, 1, 4], 
                            [2, 3, 9, 7, 5], 
                            [8, 10, 5, 6, 6], 
                            [7, 9, 3, 10, 6], 
                            [1, 9, 2, 6, 2], 
                            [2, 3, 3, 5, 10], 
                            [10, 6, 5, 6, 8], 
                            [9, 9, 1, 10, 3], 
                            [10, 4, 7, 5, 4]] is : 28

Minimum cost for matrix: [  [2, 7, 4], 
                            [8, 7, 9], 
                            [7, 8, 1], 
                            [4, 9, 5], 
                            [1, 4, 1], 
                            [9, 6, 8], 
                            [6, 8, 7], 
                            [1, 8, 6], 
                            [3, 3, 10], 
                            [8, 9, 6]] is : 38
[Finished in 0.1s]
"""