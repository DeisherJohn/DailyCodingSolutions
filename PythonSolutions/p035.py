#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Palindrome Maker
#   Daily Problem #: 34
#   Author: John Deisher
#   Date Started: 5/22/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array so that all the Rs come first, 
the Gs come second, and the Bs come last. 

You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array 
['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become 
['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def sort_char_to_index(s, sort_c_list = ["R", "G"] , start_i = 0):
    if len(sort_c_list) == 0:
        return

    index = start_i
    char = sort_c_list[0]

    for i in range(index, len(s)):
        if s[i] is char:
            temp_char = s[index]
            s[index] = s[i]
            s[i] = temp_char

            index += 1
            pass
        pass

    sort_char_to_index(s,sort_c_list[1:],index)
    pass

def main():
    rgb_list = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    sort_char_to_index(rgb_list)
    print(rgb_list)
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT: 

['R', 'R', 'R', 'G', 'G', 'B', 'B']
[Finished in 0.2s]
"""