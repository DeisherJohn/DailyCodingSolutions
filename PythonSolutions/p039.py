#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Placing Queens
#   Daily Problem #: 38
#   Author: John Deisher
#   Date Started: 5/22/2019
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. 
Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbors dies.
Any live cell with two or three live neighbors remains living.
Any live cell with more than three live neighbors dies.
Any dead cell with exactly three live neighbors becomes a live cell.
A cell neighbors another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. 
It should be able to be initialized with a starting list of live cell coordinates 
and the number of steps it should run for. Once initialized, it should print out the 
board state at each step. Since it's an infinite board, print out only the relevant coordinates, 
i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

class ConwayGame(object):
    """docstring for ConwayGame"""
    def __init__(self):
        super(ConwayGame, self).__init__()
        self.turn = 0
        self.even_board = None
        self.odd_board = None

    def update_square(self, pos):
        board_to_update_from = self.even_board if self.turn % 2 is 0 else self.odd_board
        board_to_update_to = self.even_board if self.turn % 2 is 1 else self.odd_board

        live_count = 0

        for x in range(-1, 1):
            for y in range(-1, 1):

                if x is 0 and y is 0:
                    continue

                if board_to_update_from[pos[0] + x][pos[1] + y] == "*":
                    #Live cell
                    live_count += 1



                pass
            pass

        if (live_count < 2 or live_count > 3) and board_to_update_from[pos[0]][pos[1]] == "*":
            board_to_update_to[pos[0]][pos[1]] = "."
        elif board_to_update_from[pos[0]][pos[1]] == "." and live_count == 3:
            board_to_update_to[pos[0]][pos[1]] = "*"
        else: 
            board_to_update_to[pos[0]][pos[1]] = board_to_update_from[pos[0]][pos[1]]

        pass
