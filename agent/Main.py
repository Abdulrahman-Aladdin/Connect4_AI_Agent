import numpy as np
from MinmaxPruning import *
from MinmaxWithoutPruning import *
from Utilities import *
import time


OO = 1e9
rows = 6
cols = 7
AI = '1'
PLAYER = '2'


def getGameFunction(algorithm):
    if algorithm == "pruning" or algorithm == '1':
        return min_max_pruning
    return min_max_no_pruning


def main(algorithm, maxDepth):
    temp = [['0' for _ in range(cols)] for _ in range(rows)]
    board = np.array(temp)
    function = getGameFunction(algorithm)

    while True:
        start_time = time.time()
        val, col = function(board, 0, AI, -OO, OO, maxDepth)
        end_time = time.time()

        print("Time Take: ", end_time - start_time)
        playColumn(board, col, AI)
        print(board)
        playerMove = int(input("Enter move: "))
        playColumn(board, playerMove, PLAYER)


if __name__ == "__main__":
    # For testing
    algorithm = input("Enter Algorithm: ")
    maxDepth = int(input("Enter Max Depth: "))
    ##########
    main(algorithm, maxDepth)
