#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Circular Buffer with thread locks
#   Daily Problem #: 16
#   Author: John Deisher
#   Date Started: 5/8/2019
#   Date Finished: 5/8/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. 
i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

from threading import Semaphore, Lock

class CircularBuffer(object):
    """docstring for CircularBuffer"""
    def __init__(self, _size):
        super(CircularBuffer, self).__init__()
        self.__size = _size
        self.buffer = [0]*_size
        self.lock = Lock()
        self.emptyBuffer = Semaphore(0)
        self.__lastEntry = -1
        self.__itemsAdded = 0


    def record(self, order_id):
        self.lock.acquire()
        if self.__lastEntry is (self.__size - 1):
            self.__lastEntry = 0
        else:
            self.__lastEntry += 1

        self.buffer[self.__lastEntry] = order_id

        if self.__itemsAdded < self.__size:
            self.__itemsAdded += 1
            self.emptyBuffer.release()

        self.lock.release()
        pass

    def get_last(self, i = 1):

        items = []

        for _ in range(i):
            self.emptyBuffer.acquire()
            self.lock.acquire()
            
            items.append(self.buffer[self.__lastEntry])
            self.buffer[self.__lastEntry] = 0

            if self.__lastEntry is 0:
                self.__lastEntry = self.__size - 1
            else:
                self.__lastEntry -= 1

            self.__itemsAdded -= 1
            self.lock.release()

        return items
        pass

def main():
    myBuffer = CircularBuffer(5)

    #[6,2,3,4,5]
    print(myBuffer.buffer)
    myBuffer.record(1)
    print(myBuffer.buffer)
    myBuffer.record(2)
    print(myBuffer.buffer)
    myBuffer.record(3)
    print(myBuffer.buffer)
    myBuffer.record(4)
    print(myBuffer.buffer)
    myBuffer.record(5)
    print(myBuffer.buffer)
    myBuffer.record(6)
    print(myBuffer.buffer)
    myBuffer.record(6)
    print(myBuffer.buffer)
    myBuffer.record(6)
    print(myBuffer.buffer)
    print("\nPULL LAST ENTRY: " + str(myBuffer.get_last()))
    print(myBuffer.buffer)
    myBuffer.record(3)
    print(myBuffer.buffer)
    myBuffer.record(3)
    print(myBuffer.buffer)
    print("\nPULL LAST 3 ITEMS: " + str(myBuffer.get_last(3)))
    print(myBuffer.buffer)
    myBuffer.record(9)
    print(myBuffer.buffer)
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT: 

[0, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[1, 2, 0, 0, 0]
[1, 2, 3, 0, 0]
[1, 2, 3, 4, 0]
[1, 2, 3, 4, 5]
[6, 2, 3, 4, 5]
[6, 6, 3, 4, 5]
[6, 6, 6, 4, 5]

PULL LAST ENTRY: [6]
[6, 6, 0, 4, 5]
[6, 6, 3, 4, 5]
[6, 6, 3, 3, 5]

PULL LAST 3 ITEMS: [3, 3, 6]
[6, 0, 0, 0, 5]
[6, 9, 0, 0, 5]
[Finished in 0.2s]
"""