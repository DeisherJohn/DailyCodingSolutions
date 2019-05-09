#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Sentence parse based on given dictionary
#   Daily Problem #: 22
#   Author: John Deisher
#   Date Started: 5/9/2019
#   Date Finished: 5/9/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', 
and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', 
and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or 
['bedbath', 'and', 'beyond'].
"""

class SentenceParser(object):
    """docstring for SentenceParser"""
    def __init__(self, word_set):
        super(SentenceParser, self).__init__()
        self.word_set = set()
        self.len_longest_word = 0
        self.len_shortest_word = None

        self.add_words_to_set(word_set)
            

    def add_words_to_set(self, word_list):
        for word in word_list:
            if word not in self.word_set:
                self.word_set.add(word)

                if self.len_shortest_word is None:
                    self.len_shortest_word = len(word)

                if len(word) > self.len_longest_word:
                    self.len_longest_word = len(word) 

                if len(word) < self.len_shortest_word:
                    self.len_shortest_word = len(word) 
        pass

    def empty_word_set(self):
        self.wordString = set()
        self.len_shortest_word = 100
        self.len_longest_word = 0
        pass

    def parse_sentence(self, wordString):
        found, returnList = self.__recursive_parse_sentence(wordString)

        return returnList if found else None
        pass

    def __recursive_parse_sentence(self, wordString):
        #wordString = list(wordString)

        if len(wordString) == 0:
            return True, []

        workingString = wordString

        if len(workingString) > self.len_shortest_word:
            word = workingString[:self.len_shortest_word-1]
            workingString = workingString[self.len_shortest_word-1:]
        else: 
            return False, wordString

        while len(word) <= self.len_longest_word and len(workingString) > 0:
            word += workingString[0]
            workingString = workingString[1:]

            if word in self.word_set:
                match,rstring = self.__recursive_parse_sentence(workingString)

                if not match:
                    workingString = rstring
                else:
                    rstring.insert(0,word)
                    return True, rstring

        return False, wordString
        pass

testSet = ["quick", "brown", "fox", "the", "he", "head", "a", "asd"]
testString1 = "thequickheadbrownfoxheadheadheadheadheadaheadheheheadasdasdasdasd"
testString2 = "thequickheadbrownfoxheadheadheadheadheadahasdzzzadheheheadasdasdasd"


myParser = SentenceParser(testSet)

print("TEST PASS: " + str(myParser.parse_sentence(testString1)))
print("\nTEST FAIL: " + str(myParser.parse_sentence(testString2)))

"""
OUTPUT: 
TEST PASS: ['the', 'quick', 'head', 'brown', 'fox', 'head', 'head', 'head', 'head', 'head', 'a', 'head', 'he', 'he', 'head', 'asd', 'asd', 'asd', 'asd']

TEST FAIL: None
[Finished in 0.1s]

"""