#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Valleys Full of Water
#   Daily Problem #: 30
#   Author: John Deisher
#   Date Started: 5/11/2019
#   Date Finished:  WIP
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map 
where each element is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, 
and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""

def compute_held_volume(topograph):

    added_set = set()
    current_max = topograph[0]
    current_max_index = 0
    current_sum = 0
    in_valley = False
    returnSum = 0

    for i, elevation in enumerate(topograph):
        if (elevation >= current_max) and in_valley is False:
            current_max = elevation
            current_max_index = i 

        if elevation < current_max:
            in_valley = True
            current_sum += elevation

        if elevation >= current_max and in_valley is True:
            if (min(current_max_index, i),max(current_max_index, i)) not in added_set:
                area = current_max * ((i-1)-current_max_index)
                returnSum += area - current_sum
                added_set.add((min(current_max_index, i),max(current_max_index, i)))
            current_max = elevation
            current_sum = 0
            current_max_index = i
            in_valley = False

    current_max = topograph[-1]
    current_max_index = len(topograph)
    current_sum = 0
    in_valley = False

    for i in range(len(topograph)-1,0,-1):
        i_elevation = topograph[i]
        if i_elevation >= current_max and in_valley is False:
            current_max = i_elevation
            current_max_index = i 

        if i_elevation < current_max:
            in_valley = True
            current_sum += i_elevation

        if i_elevation >= current_max and in_valley is True:
            if (min(current_max_index, i),max(current_max_index, i)) not in added_set:
                area = current_max * (current_max_index-1 - i)
                returnSum += area - current_sum
                added_set.add((min(current_max_index, i),max(current_max_index, i)))
            current_max = i_elevation
            current_sum = 0
            current_max_index = i
            in_valley = False

    print(returnSum)


    pass

# test = [3,6,3,3,0,3,6,5,4,5,4,6]
# test = [2, 1, 2]
test = [3, 0, 1, 3, 0, 5]

compute_held_volume(test)