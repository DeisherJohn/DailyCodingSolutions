#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Checking for Well-Formed Brackets
#   Daily Problem #: 27
#   Author: John Deisher
#   Date Started: 5/10/2019
#   Date Finished: 5/10/2019 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def are_brackets_well_formed(input_brackets):
    openSet = {'(', '[', '{'}
    closedSet = {')',']','}'}
    bracketPairs = {'(':')', '[':']', '{':'}'}
    brackets = list()

    for b in input_brackets:
        if b in openSet:
            brackets.append(b)
        elif b in closedSet:
            if bracketPairs[brackets[-1]] is not b:
                return False
            brackets.pop(-1)

    if len(brackets) is 0:
        return True
    else:
        return False
    pass

def main():
    testCases = list()

    testCases.append("([])[]({})")
    testCases.append("([)]")
    testCases.append("((()")
    testCases.append("({[]}())")

    for case in testCases:
        print("Testing: " + case + " for balance : " + str(are_brackets_well_formed(case)))
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT: 

Testing: ([])[]({}) for balance : True
Testing: ([)] for balance : False
Testing: ((() for balance : False
Testing: ({[]}()) for balance : True
[Finished in 0.1s]

"""