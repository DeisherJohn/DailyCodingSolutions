#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Estimate of Pi using Monte Carlo Method
#   Daily Problem #: 14
#   Author: John Deisher
#   Date Started: 5/8/2019
#   Date Finished: 5/8/2019
#   Note: review of Monte Carlo method https://en.wikipedia.org/wiki/Monte_Carlo_method
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

The area of a circle is defined as πr^2. 
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

from random import random, seed
from time import time

seed(time())

def main():
    #program parameters
    base_loops = 10

    for loop_exp in range(8):
        inside = 0
        print("Sample Size: " + str(base_loops**loop_exp))
        for i in range(base_loops**loop_exp):
            inside += 1 if 1 >= random()**2+random()**2 else 0
        pi = (inside/(base_loops**loop_exp))*4
        print('π: %.4f'%pi)
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT:

Sample Size: 1
π: 4.0000
Sample Size: 10
π: 3.2000
Sample Size: 100
π: 3.0800
Sample Size: 1000
π: 3.1400
Sample Size: 10000
π: 3.1508
Sample Size: 100000
π: 3.1375
Sample Size: 1000000
π: 3.1414
Sample Size: 10000000
π: 3.1416
[Finished in 12.4s]
"""