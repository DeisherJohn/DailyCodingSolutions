#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Longest Sub String
#   Daily Problem #: 13
#   Author: John Deisher
#   Date Started: 5/8/2019
#   Date Finished: 5/8/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Amazon.

Given an integer k and a string s, 
find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
the longest substring with k distinct characters is "bcb".
"""

def get_longest_substring(s, k):
	#k is the number of distinct chars
	if k < 1:
		#base case where no distinct chars are wanted
		return ""

	best_substring = ""
	
	for ind, c in enumerate(s):
		char_list = set()
		current_substring = ""

		for letter in s[ind:]:
			if letter in char_list:
				current_substring = current_substring + letter
			elif letter not in char_list and len(char_list) < k:
				char_list.add(letter)
				current_substring = current_substring + letter
			else:
				break

		if len(current_substring) > len(best_substring):
			best_substring = current_substring
	return best_substring

	pass

def main():
	testStrings = list()

	testStrings.append("abcba")
	testStrings.append("aaAAAaaaa")
	testStrings.append("qqwqweqwerqwertqwerty")

	MAX_NUMBER_OF_CHARS = 6 #including 0
	for num_of_chars in range(MAX_NUMBER_OF_CHARS):
		for test in testStrings:
			print("\nTest string: " + test + " ; Number of chars to match: " + str(num_of_chars))
			print("Substring: " + get_longest_substring(test, num_of_chars))

	#test given in problem

	assert get_longest_substring(testStrings[0],2) == "bcb"
	pass

if __name__ == '__main__':
	main()

"""
OUTPUT:


Test string: abcba ; Number of chars to match: 0
Substring: 

Test string: aaAAAaaaa ; Number of chars to match: 0
Substring: 

Test string: qqwqweqwerqwertqwerty ; Number of chars to match: 0
Substring: 

Test string: abcba ; Number of chars to match: 1
Substring: a

Test string: aaAAAaaaa ; Number of chars to match: 1
Substring: aaaa

Test string: qqwqweqwerqwertqwerty ; Number of chars to match: 1
Substring: qq

Test string: abcba ; Number of chars to match: 2
Substring: bcb

Test string: aaAAAaaaa ; Number of chars to match: 2
Substring: aaAAAaaaa

Test string: qqwqweqwerqwertqwerty ; Number of chars to match: 2
Substring: qqwqw

Test string: abcba ; Number of chars to match: 3
Substring: abcba

Test string: aaAAAaaaa ; Number of chars to match: 3
Substring: aaAAAaaaa

Test string: qqwqweqwerqwertqwerty ; Number of chars to match: 3
Substring: qqwqweqwe

Test string: abcba ; Number of chars to match: 4
Substring: abcba

Test string: aaAAAaaaa ; Number of chars to match: 4
Substring: aaAAAaaaa

Test string: qqwqweqwerqwertqwerty ; Number of chars to match: 4
Substring: qqwqweqwerqwer

Test string: abcba ; Number of chars to match: 5
Substring: abcba

Test string: aaAAAaaaa ; Number of chars to match: 5
Substring: aaAAAaaaa

Test string: qqwqweqwerqwertqwerty ; Number of chars to match: 5
Substring: qqwqweqwerqwertqwert
[Finished in 0.1s]
"""