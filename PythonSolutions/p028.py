#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Text Justification
#   Daily Problem #: 27
#   Author: John Deisher
#   Date Started: 5/11/2019
#   Date Finished:  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, 
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. 
There should be at least one space between each word. 
Pad extra spaces when necessary so that each line has exactly length k. 
Spaces should be distributed as equally as possible, with the extra spaces, 
if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words 

["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 

and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def justify_text(s, k):

    line_char_count = 0
    lines = list()
    charsOnLine = list()
    for word in s:
        if line_char_count is 0 or (line_char_count + len(word) + 1) > k:
            lines.append([word])
            if line_char_count is not 0:
                charsOnLine.append(line_char_count)
            line_char_count = len(word)
        else:
            line_char_count += len(word) + 1
            lines[-1].append(" " + word )

    charsOnLine.append(line_char_count)

    returnList = list()
    for i , line in enumerate(lines):  
        spaced = ""
        ind = 0
        while charsOnLine[i] < k:
            line[ind] += " "
            charsOnLine[i] += 1
            ind = (ind + 1) % (len(line) - 1) if len(line) != 1 else 0
            pass

        spaced = ''.join(line)
        returnList.append(spaced)

    return returnList
    pass

# test = ["this", "hello", "world"]
test = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 

print(justify_text(test, 16))

"""
OUTPUT

['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
[Finished in 0.2s]
"""