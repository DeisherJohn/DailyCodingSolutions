#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Auto-complete
#   Daily Problem #: 11
#   Author: John Deisher
#   Date Started: 5/7/19
#   Date Finished: 5/7/19
#	Note: This is run in linear time and without custom data stuctures, to speed it up a new strucure for the dict would be needed
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""



def return_possible_words(dictSet, testWord):
	wordsToKeepTesting = []

	for word in dictSet:
		if testWord == word[:len(testWord)]:
			wordsToKeepTesting.append(word)

	return wordsToKeepTesting

def main():

	wordSet = {"dog", "deer", "debug", "hello", "world", "math", "maths", "halo", "howdy"}
	testWords = list()
	testWords.append("de")
	testWords.append("d")
	testWords.append("maths")
	testWords.append("h")

	for testWord in testWords:
		print("Matching words for: " + testWord + " is: " + str(return_possible_words(wordSet, testWord)) )
	pass

if __name__ == '__main__':
	main()

"""
OUTPUT: 
Matching words for: de is: ['debug', 'deer']
Matching words for: d is: ['debug', 'deer', 'dog']
Matching words for: maths is: ['maths']
Matching words for: h is: ['halo', 'howdy', 'hello']
[Finished in 0.2s]
"""