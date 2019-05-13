#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: A* algorithm
#   Daily Problem #: 23
#   Author: John Deisher
#   Date Started: 5/9/2019
#   Date Finished: 5/9/2019
#   Notes: review of A* found here: https://www.geeksforgeeks.org/a-search-algorithm/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall 
everywhere else on the second row.
"""

class A_star_node(object):
    """docstring for A_star_node"""
    def __init__(self, pos, h = 0, parent = None):
        super(A_star_node, self).__init__()
        self.pos = pos
        self.g = 0
        self.h = h
        self.parent = parent

        if self.parent is not None:
            self.g = self.parent.g + 1

        self.f = self.g + self.h

def get_h_between(nodeA, nodeB):
    return ((nodeA[0]-nodeB[0])**2 + (nodeA[1]-nodeB[1])**2)**0.5
    pass

def A_star(maze, start, end):
    if start == end:
        return 0

    open_list = list()
    closed_list = list()

    maze_y = len(maze) #y
    maze_x = len(maze[0]) #x

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    open_list.append(A_star_node(start, get_h_between(start, end)))

    while len(open_list) > 0:

        ind = 0
        currentLow = open_list[0]
        for i, node in enumerate(open_list):
            if currentLow.f > node.f:
                ind = i

        tempNode = open_list.pop(ind)
        closed_list.append(tempNode.pos)

        for neighbor in neighbors:
            newPos = (tempNode.pos[0] + neighbor[0] ,tempNode.pos[1] + neighbor[1])
            if newPos[0] >= 0 and newPos[0] < maze_y and newPos[1] >= 0 and newPos[1] < maze_x:
                if newPos == end:
                    return int(tempNode.f)

                if newPos in closed_list or maze[newPos[0]][newPos[1]] == 1:
                    #position has already been checked or is out of the maze
                    continue
                #add a new node to the open list to check
                newNode = A_star_node(newPos, get_h_between(newPos, end), tempNode)
                open_list.append(newNode)

    return None
    pass


def main():
    myMaze = [[0, 0, 0, 0],[1, 1, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
    myStart = (3, 0)
    myEnd = (0, 0)

    steps = A_star(myMaze, myStart, myEnd)

    if steps is None:
        print("No Path")
    else:
        print("Steps needed: " + str(steps))
    pass

if __name__ == '__main__':
    main()

"""
OUTPUT:

Steps needed: 7
[Finished in 0.1s]
"""