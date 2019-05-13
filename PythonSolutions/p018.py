#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Find Largest int in Sub-Array of Size(k)
#   Daily Problem #: 18
#   Author: John Deisher
#   Date Started: 5/8/2019
#   Date Finished: 5/8/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, 
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store the results. 
You can simply print them out as you compute them.
"""

class SlidingWindowNode(object):
    """docstring for SlidingWindowNode"""
    def __init__(self, value, index):
        super(SlidingWindowNode, self).__init__()
        self.value = value
        self.index = index
        self.next = None
        self.prev = None

    def __del__(self):
        #decon operator
        self.value = None
        self.index = None
        self.next = None
        self.prev = None
        pass

#using this class meets the requirement of O(n) time complexity
class SlidingWindow(object):
    """docstring for SlidingWindow
        Custom deque implementation for a sliding window
    """
    def __init__(self, size):
        super(SlidingWindow, self).__init__()
        self.size = size
        self.head = None
        self.tail = None

    def build_list(self, values):
        for i,value in enumerate(values):
            self.add_node(SlidingWindowNode(value, i))
            if i >= self.size-1:
                print("Max of window: [" + str(i-self.size+1) + "," + str(i) + "] is: " + str(self.get_max(i)))
        pass

    def add_node(self, node):
        currentNode = self.tail

        if currentNode is None:
            #start of the list
            self.head = node
            self.tail = node
        else:

            while node.value > currentNode.value:
                if currentNode.prev is None:
                    #start of the list
                    self.head = node
                    self.tail = node
                    currentNode = node
                    break
                else:
                    currentNode = currentNode.prev
                    self.remove_node(currentNode.next)

            if currentNode is not node:
                currentNode.next = node
                node.prev = currentNode
                self.tail = node
        pass

    def remove_node(self, node):
        if node is not self.head:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node is not self.tail:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        del node
        pass

    def get_max(self, pos):
        currentNode = self.head
        if currentNode is None:
            return []
        else:
            while currentNode.index <= (pos-self.size):
                currentNode = currentNode.next
                self.remove_node(currentNode.prev)
            return currentNode.value
        pass
        
def get_max_value_of_sub_array(dataInput, k):
    #Time Complexity O(n*k)
    if k == len(dataInput):
         print('Max of {} is : {}'.format(str(dataInput), str(max(dataInput))))

    for i in range(k, len(dataInput)+1):
        print('Max of {} is : {}'.format(str(dataInput[i-k:i]), str(max(dataInput[i-k:i]))))
    pass

def main():
    testCase = [1,5,8,7,6,5,4,3,1,4,9,6,3,5,3,4,2,1,3]
    WINDOW_SIZE = 5

    print("Test Array: " + str(testCase))

    print("\nUsing time complexity of O(n*k)")
    get_max_value_of_sub_array(testCase, WINDOW_SIZE)

    
    print("\nUsing time complexity of O(n)")
    myWindow = SlidingWindow(WINDOW_SIZE)
    myWindow.build_list(testCase)

    pass

if __name__ == '__main__':
    main()

"""
Test Array: [1, 5, 8, 7, 6, 5, 4, 3, 1, 4, 9, 6, 3, 5, 3, 4, 2, 1, 3]

Using time complexity of O(n*k)
Max of [1, 5, 8, 7, 6] is : 8
Max of [5, 8, 7, 6, 5] is : 8
Max of [8, 7, 6, 5, 4] is : 8
Max of [7, 6, 5, 4, 3] is : 7
Max of [6, 5, 4, 3, 1] is : 6
Max of [5, 4, 3, 1, 4] is : 5
Max of [4, 3, 1, 4, 9] is : 9
Max of [3, 1, 4, 9, 6] is : 9
Max of [1, 4, 9, 6, 3] is : 9
Max of [4, 9, 6, 3, 5] is : 9
Max of [9, 6, 3, 5, 3] is : 9
Max of [6, 3, 5, 3, 4] is : 6
Max of [3, 5, 3, 4, 2] is : 5
Max of [5, 3, 4, 2, 1] is : 5
Max of [3, 4, 2, 1, 3] is : 4

Using time complexity of O(n)
Max of window: [0,4] is: 8
Max of window: [1,5] is: 8
Max of window: [2,6] is: 8
Max of window: [3,7] is: 7
Max of window: [4,8] is: 6
Max of window: [5,9] is: 5
Max of window: [6,10] is: 9
Max of window: [7,11] is: 9
Max of window: [8,12] is: 9
Max of window: [9,13] is: 9
Max of window: [10,14] is: 9
Max of window: [11,15] is: 6
Max of window: [12,16] is: 5
Max of window: [13,17] is: 5
Max of window: [14,18] is: 4
[Finished in 0.1s]
"""