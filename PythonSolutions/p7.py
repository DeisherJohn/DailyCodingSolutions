#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: decode numstring
#   Daily Problem #: 7
#   Author: John Deisher
#   Date Started: 5/7/19
#   Date Finished: 5/7/19
#	Note: Solution constructed by referencing 
#		https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""



def find_number_of_possible_messages(message):
	
	wordCounts = [0] * (len(message)+1)
	wordCounts[0] = 1
	wordCounts[1] = 1

	for i in range(2, len(message)+1):
		if message[i-1] is not '0':
			wordCounts[i] += wordCounts[i-1]

		if message[i-2] == '1' or (message[i-2] == '2' and message[i-1] < '8'):
			wordCounts[i] += wordCounts[i-2]

	return wordCounts[len(message)]

	pass

def main():
	testCase = list()
	testCase.append("111")
	testCase.append("101")
	testCase.append("101011101010")
	testCase.append("123321256134")


	for case in testCase:
		print("Possible # of decodings for: " + str(case))
		print("Output: " + str(find_number_of_possible_messages(case)))
		print()
	
	pass

if __name__ == '__main__':
	main()

"""
OUTPUT:

Possible # of decodings for: 111
Output: 3

Possible # of decodings for: 101
Output: 1

Possible # of decodings for: 101011101010
Output: 2

Possible # of decodings for: 123321256134
Output: 30

[Finished in 0.2s]
"""