#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Find single in list with triplets
#   Daily Problem #: 40
#   Author: John Deisher
#   Date Started: 7/5/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

def get_single(data):

    ones = 0
    twos = 0

    for num in data:
        #gets the bits that have already showed up before
        #and adds them to the twos, meaning its the second time
        twos = twos | (ones & num)

        #adds bits that are new to the ones
        ones = ones ^ num
       
        common_bits = ~(ones & twos)
        print("PRE-ONES: {}, PRE-TWOS: {}, COMMON BITS: {}".format(ones, twos, common_bits))

        ones &= common_bits
        twos &= common_bits
        print("POST-ONES: {}, POST-TWOS: {}".format(ones, twos))

    return ones
    pass


def main():
    testData = [5,1,6,7,1,7,5,1,5,7]
    print(get_single(testData))
    pass

if __name__ == '__main__':
    main()