#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Can sum be made from list of numbers
#   Daily Problem #: 42
#   Author: John Deisher
#   Date Started: 7/5/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. 
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

def check_for_subsum(numbers, target_sum):
    if len(numbers) == 0:
        return False

    for i,num in enumerate(numbers):
        if num == target_sum:
            return [num]
        elif num > target_sum:
            continue
        else:
            target_nums = check_for_subsum(numbers[:i] + numbers[i+1:], target_sum - num)

            if target_nums != False:
                target_nums.append(num)
                return target_nums

    return False
    pass

def main():
    S = list()
    k = list()

    S.append([12, 1, 61, 5, 9, 2])
    k.append(24)

    print(check_for_subsum(S[0], k[0]))
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT:
[2, 9, 1, 12]
[Finished in 0.1s]
"""