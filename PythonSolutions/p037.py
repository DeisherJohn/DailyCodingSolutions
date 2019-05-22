#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Palindrome Maker
#   Daily Problem #: 34
#   Author: John Deisher
#   Date Started: 5/22/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

def get_power_set(s):
    power_list = list(set())
    base_set = set()

    for item in s:
        base_set.add(item)
        power_list.append({item})

    for s1 in base_set:
        len_of_set = len(power_list)
        for i, s2 in enumerate(power_list):
            newset = {s1} | s2
            if newset not in power_list:
                power_list.append(newset)

            if i > len_of_set: break

    print(power_list)
    pass

def main():
    get_power_set({1})
    get_power_set({1,2})
    get_power_set({1,2,3})
    get_power_set({1,2,3,4})
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT:

[{None}, {1}]
[{None}, {1}, {2}, {1, 2}]
[{None}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
[{None}, {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {1, 2, 3}, {1, 2, 4}, {3, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}]
[Finished in 0.2s]
"""