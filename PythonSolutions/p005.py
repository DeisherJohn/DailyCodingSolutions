#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Functional Programming
#   Daily Problem #: 5
#   Author: John Deisher
#   Date Started: 5/8/19
#   Date Finished: 5/8/19
#	Note: Help understanding how function object work in python was found below
#	https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
	def get_first(a,b):
		return a
	return pair(get_first)
	pass

def cdr(pair):
	def get_second(a,b):
		return b
	return pair(get_second)
	pass


def main():
	myPair = cons(3, 4)

	#Values of the function pair
	print("Direct Access of first: " + str(myPair.__closure__[0].cell_contents))
	print("Function Access of first: " + str(car(myPair)))
	print("Direct Access of second: " + str(myPair.__closure__[1].cell_contents))
	print("Function Access of second: " + str(cdr(myPair)))

	print("("+str(car(myPair))+","+str(cdr(myPair))+")")	
	pass

if __name__ == '__main__':
	main()

"""
OUTPUT:

Direct Access of first: 3
Function Access of first: 3
Direct Access of second: 4
Function Access of second: 4
(3,4)
[Finished in 0.1s]

"""