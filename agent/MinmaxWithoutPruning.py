from Utilities import *

OO = 1e9
AI = '1'
PLAYER = '2'


def min_max_no_pruning(board, depth, turn, alpha, beta, maxDepth):
    if isLeafNode(board):
        return evalLeafNode(board), board
    elif depth == maxDepth:
        return evalFunction(board), board

    if turn == AI:  # current node is max
        val = -OO
    else:
        val = OO

    bestMove = 0

    for col in range(0, cols):
        rowPlayed = playColumn(board, col, turn)
        if rowPlayed == -1:
            continue
        nextTurn = PLAYER if turn == AI else AI
        (childValue, nextMove) = min_max_no_pruning(board, depth + 1, nextTurn, alpha, beta, maxDepth)
        board[rowPlayed][col] = '0'

        if (turn == AI):
            if childValue > val:
                val = childValue
                bestMove = col
        else:
            if childValue < val:
                val = childValue
                bestMove = col

    return val, bestMove
