#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Placing Queens
#   Daily Problem #: 38
#   Author: John Deisher
#   Date Started: 5/22/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, 
returns the number of possible arrangements of the board where N queens 
can be placed on the board without threatening each other, 
i.e. no two queens share the same row, column, or diagonal.
"""
import time

def n_queens(N, col = 0, dead_y = None, dead_maj = None, dead_min = None):
    if col is 0:
        dead_y = set()
        dead_maj = set()
        dead_min = set()

    if col == N: return 1

    placement_nums = 0

    for y in range(N):
        if (y in dead_y) or ((y+col) in dead_maj) or ((y-col) in dead_min):
                continue
        if col == 0:
            placement_nums += n_queens(N, 1,{y}, {y+col}, {y-col})
        else:
            dead_y.add(y)
            dead_maj.add(y+col)
            dead_min.add(y-col)
            placement_nums += n_queens(N, col + 1, dead_y, dead_maj, dead_min)
            dead_y.remove(y)
            dead_maj.remove(y+col)
            dead_min.remove(y-col)
            
    return placement_nums
    pass

def main():
    for i in range(1,15):
        start = time.time()
        num = n_queens(i)
        end = time.time()

        print("N={}, Solutions: {} : time={} [in sec]".format(i,num,end-start))
    
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT:
N=01, Solutions: 1          : time=0.0 [in sec]
N=02, Solutions: 0          : time=0.0 [in sec]
N=03, Solutions: 0          : time=0.0 [in sec]
N=04, Solutions: 2          : time=0.0 [in sec]
N=05, Solutions: 10         : time=0.0 [in sec]
N=06, Solutions: 4          : time=0.0009982585906982422 [in sec]
N=07, Solutions: 40         : time=0.001993417739868164 [in sec]
N=08, Solutions: 92         : time=0.004987001419067383 [in sec]
N=09, Solutions: 352        : time=0.02892279624938965 [in sec]
N=10, Solutions: 724        : time=0.08477210998535156 [in sec]
N=11, Solutions: 2680       : time=0.4269258975982666 [in sec]
N=12, Solutions: 14200      : time=2.2425920963287354 [in sec]
N=13, Solutions: 73712      : time=12.73914122581482 [in sec]
N=14, Solutions: 365596     : time=75.06831359863281 [in sec]
[Finished in 90.7s]
"""