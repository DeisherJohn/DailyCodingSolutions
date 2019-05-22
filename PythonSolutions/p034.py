#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Palindrome Maker
#   Daily Problem #: 34
#   Author: John Deisher
#   Date Started: 5/22/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Quora.
Given a string, find the palindrome that can be made by inserting the fewest
number of characters as possible anywhere in the word. If there is more than
one palindrome of minimum length that can be made, return the lexicographically
earliest one (the first one alphabetically).
For example, given the string "race", you should return "ecarace", since we can
add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three
letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".
"""
def is_palindrome(s):
    for i in range(len(s)):
        if i > (len(s) / 2):
            return True
        if s[i] != s[-(i+1)]:
            return False
    pass

def get_lexical_first(s1, s2):
    if len(s1) < len(s2):
        return s1
    if len(s2) < len(s1):
        return s2

    for i in range(len(s1)):
        if s1[i] < s2[i]:
            return s1
        if s1[i] > s2[i]:
            return s2

    return s1
    pass

def find_shortest_palindrome(s):
    r_s = s[::-1]
    
    current_match = s + r_s[1:]
    foundMatch = False

    for i in range(len(s)):
        testCase1 = s[:i] + r_s
        testCase2 = r_s[:i] + s
        #print("Test Cases: {} and {}".format(testCase1, testCase2))
        if len(testCase1) < len(current_match) and is_palindrome(testCase1):
            current_match = testCase1
            foundMatch = True

        if len(current_match) >= len(testCase2) and testCase2 == get_lexical_first(current_match, testCase2) and is_palindrome(testCase2):
            current_match = testCase2
            foundMatch = True

        if foundMatch:
            break

    return current_match
        
    pass

def main():

    testCases = list()

    testCases.append("race")
    testCases.append("google")
    testCases.append("aabzz")
    testCases.append("aaaab")
    testCases.append("zyxwz")
    testCases.append("zyxw")

    for test in testCases:
        print("Testing {} found {} as shortest palindrome".format(test, find_shortest_palindrome(test)))

    #print(find_shortest_palindrome("google"))
    #print(is_palindrome("ababa"))
    pass

if __name__ == '__main__':
    main()

"""
Testing race found ecarace as shortest palindrome
Testing google found elgoogle as shortest palindrome
Testing aabzz found aabzzbaa as shortest palindrome
Testing aaaab found baaaab as shortest palindrome
Testing zyxwz found zwxyzyxwz as shortest palindrome
Testing zyxw found wxyzyxw as shortest palindrome
[Finished in 0.2s]
"""