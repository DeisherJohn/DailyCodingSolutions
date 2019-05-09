#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: RegEx Parser
#   Daily Problem #: 25
#   Author: John Deisher
#   Date Started: 5/10/2019
#   Date Finished: 5/10/2019 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression 
and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", 
your function should return true. 
The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", 
your function should return true. 
The same regular expression on the string "chats" should return false.
"""


def is_match(regEx, testString, can_fail = False):
    originalTestString = testString
    matchedString = ""
    lastChar = ""
    checkForStar = True

    if regEx == testString:
        return True

    if regEx == ".*":
        return True

    for i,c in enumerate(regEx):
        #get the next letter to test and remove it from the input
        if len(testString) > 0:
            test_char = testString[0]
            testString = testString[1:]
        else:
            test_char = ''
            testString = ''

        
        #check if the char matches
        if c == "*":
            #repeat the last letter 
            while True:
                if test_char == lastChar:
                    #if the test letter is th elast letter add it
                    if len(testString) > 0:
                        #check if there are more letters
                        test_char = testString[0]
                        testString = testString[1:]
                    else:
                        break

                    matchedString += lastChar
                elif lastChar == '.':
                    if i == len(regEx)-1: return True

                    for ind in range(len(regEx)):
                        if regEx[-1] != "*" and len(testString) == 0:
                            return False

                        gotMatch = is_match(regEx[i+1:], testString[ind:])
                        if gotMatch:
                            return True

                    return False
                else:
                    #add the letter back into the string since * does not mean a letter has to be used
                    testString = test_char + testString
                    break
            #used to ensure that a letter can be removed from regEx if it is stared
            checkForStar = True
        if c == "." or c == test_char:
            if c is "." and test_char is '':
                if i == len(regEx)-1:
                    return False
            
            matchedString += test_char
        else:
            testString = test_char + testString
            if checkForStar:
                checkForStar = False 
                continue
            else:
                return False

        lastChar = c

    if checkForStar is False:
        return False
    return matchedString == originalTestString

    pass

def main():
    #print(is_match(".*at", "chat"))
    print("Checking '{}' using regEx: {} : {}".format("ray", "ra.", is_match("ra.", "ray")))
    print("Checking '{}' using regEx: {} : {}".format("raymond", "ra.", is_match("ra.", "raymond")))
    print("Checking '{}' using regEx: {} : {}".format("chat", ".*at", is_match(".*at", "chat")))
    print("Checking '{}' using regEx: {} : {}".format("chats", ".*at", is_match(".*at", "chats")))
    print("Checking '{}' using regEx: {} : {}".format("qwerty", "qw.*", is_match("qw.*", "qwerty")))
    print("Checking '{}' using regEx: {} : {}".format("qwerty", "qw.*y", is_match("qw.*y", "qwerty")))
    print("Checking '{}' using regEx: {} : {}".format("qwerty", "qw.*wy", is_match("qw.*wy", "qwerty")))
    print("Checking '{}' using regEx: {} : {}".format("qwerty", "qwy", is_match("qwy", "qwerty")))
    print("Checking '{}' using regEx: {} : {}".format("qwerty", "qw.*.y", is_match("qw.*.y", "qwerty")))
    print("Checking '{}' using regEx: {} : {}".format("qwerty", "......", is_match("......", "qwerty")))
    print("Checking '{}' using regEx: {} : {}".format("cat", "......", is_match("......", "cat")))
    print("Checking '{}' using regEx: {} : {}".format("qwerty", "...", is_match("...", "qwerty")))
    print("Checking '{}' using regEx: {} : {}".format("qwerty", ".*", is_match(".*", "qwerty")))
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT: 

Checking 'ray' using regEx: ra. : True
Checking 'raymond' using regEx: ra. : False
Checking 'chat' using regEx: .*at : True
Checking 'chats' using regEx: .*at : False
Checking 'qwerty' using regEx: qw.* : True
Checking 'qwerty' using regEx: qw.*y : True
Checking 'qwerty' using regEx: qw.*wy : False
Checking 'qwerty' using regEx: qwy : False
Checking 'qwerty' using regEx: qw.*.y : True
Checking 'qwerty' using regEx: ...... : True
Checking 'cat' using regEx: ...... : False
Checking 'qwerty' using regEx: ... : False
Checking 'qwerty' using regEx: .* : True
[Finished in 0.1s]
"""