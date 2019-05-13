#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Edit Distance Between Two Strings
#   Daily Problem #: 31
#   Author: John Deisher
#   Date Started: 5/12/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character 
insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: 
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


def letters_in_order(shortString, longString):
    longString_index_matched = 0
    matched_letters = 0
    missing_letters = 0
    skipped_letters = 0
    changed_letters = 0
    returnChanged = 0
    found_first_match = False
    returnLetters = 0
    for i, letter in enumerate(shortString):
        found = False
        for j in range(longString_index_matched,len(longString)):
            if letter == longString[j]:
                found = True
                longString_index_matched = j+1
                matched_letters += 1
                found_first_match = True
                break
            else:
                skipped_letters += 1

        if not found:
            missing_letters += 1
            returnLetters, returnMissing, returnChanged = letters_in_order(shortString[i+1:], longString[longString_index_matched:])
            missing_letters += returnMissing
            matched_letters += returnLetters
            break

    changed_letters = skipped_letters - returnLetters - returnChanged

    return matched_letters, missing_letters, changed_letters
    pass


def get_edit_distance(s1, s2):

    shortString = ""
    longString = ""

    if len(s1) >= len(s2):
        longString = s1
        shortString = s2
    else:
        longString = s2
        shortString = s1

    matched, change, addSub = letters_in_order(shortString, longString)
    lengthDiff = len(longString)-len(shortString)
    midRemove = lengthDiff - addSub
    


    return change + addSub + midRemove

    pass

short =  "kitten"
myLong = "sitting"
matched, change, addSub = letters_in_order(short, myLong)
lengthDiff = len(myLong)-len(short)
midRemove = lengthDiff - addSub
print("MATCH: " + short)
print("TO: " + myLong)

print("TOTAL CHANGES: " + str(get_edit_distance(myLong, short)))

"""OUTPUT

MATCH: kitten
TO: sitting
TOTAL CHANGES: 3
[Finished in 0.2s]

"""