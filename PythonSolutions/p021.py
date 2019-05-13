#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Room scheduler
#   Daily Problem #: 21
#   Author: John Deisher
#   Date Started: 5/9/2019
#   Date Finished: 5/9/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
from random import randint, seed
from time import time

seed(time())

def times_overlap(timeA, timeB):
    if timeA[0] < timeB[0] and timeA[1] > timeB[0]:
        return True
    elif timeA[0] < timeB[1] and timeA[1] > timeB[1]:
        return True
    else:
        return False
    pass

def time_overlaps_in_room(room, newTime):
    for time in room:
        if times_overlap(time, newTime):
            return True
    return False
    pass

def schedule_rooms(list_of_times):
    rooms = list(list())

    for time in list_of_times:
        added = False
        for room in rooms:
            if not time_overlaps_in_room(room, time):
                room.append(time)
                added = True
                break
        else:
            newRoom = [time]
            rooms.append(newRoom)

    return len(rooms)
    pass

def make_room_schedule(num_of_times = 10):
    times = list()

    for _ in range(num_of_times):
        a = randint(0,300)
        b = randint(a,a+100)
        times.append((min(a,b), max(a,b)))

    return times
    pass


def main():
    testSchedule = make_room_schedule(100)
    print("Times a rooms is needed (size==100): ")
    print(testSchedule)

    print("\nNumber of rooms required: " + str(schedule_rooms(testSchedule)))
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT: 

Times a rooms is needed (size==100): 
[(174, 263), (87, 151), (105, 105), (185, 277), (65, 76), (162, 242), (99, 160), 
(5, 64), (6, 63), (124, 150), (102, 200), (87, 143), (145, 208), (136, 153), (24, 98), 
(153, 229), (61, 70), (67, 126), (36, 127), (195, 290), (43, 125), (165, 230), (23, 95), 
(285, 290), (116, 178), (154, 211), (235, 288), (87, 141), (76, 148), (147, 200), 
(261, 341), (54, 145), (50, 58), (284, 345), (163, 187), (64, 90), (130, 183), 
(234, 331), (221, 288), (68, 72), (200, 286), (201, 268), (49, 74), (237, 326), (27, 49), 
(87, 138), (185, 283), (123, 139), (127, 129), (39, 69), (35, 109), (212, 311), (24, 79), 
(37, 56), (161, 191), (244, 284), (126, 172), (253, 255), (181, 214), (220, 283), 
(168, 223), (36, 93), (193, 259), (179, 212), (286, 371), (123, 154), (39, 133), 
(87, 127), (197, 242), (52, 68), (193, 284), (71, 111), (65, 94), (167, 211), (293, 391), 
(147, 201), (210, 286), (230, 279), (223, 226), (114, 116), (106, 200), (108, 137), 
(299, 300), (129, 226), (277, 326), (272, 341), (51, 77), (196, 262), (206, 215), 
(239, 328), (158, 173), (105, 193), (36, 86), (251, 280), (1, 73), (14, 36), (288, 292), 
(277, 342), (119, 148), (281, 311)]

Number of rooms required: 18
[Finished in 0.1s]
"""