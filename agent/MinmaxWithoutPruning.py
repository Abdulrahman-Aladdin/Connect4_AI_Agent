from Utilities import *

OO = 1e9
AI = '1'
PLAYER = '2'


def min_max_no_pruning(board, depth, turn, alpha, beta, maxDepth, values, adj, id):
    if isLeafNode(board):
        return evalLeafNode(board), board
    elif depth == maxDepth:
        ans = evalFunction(board)
        values[id] = ans
        return ans, board

    if turn == AI:  # current node is max
        val = -OO
    else:
        val = OO

    bestMove = 0

    # id = 0 -> 1 2 3 4 5 6 7
    # id = 1 ->
    for col in range(0, cols):
        adj[id].append(id+col+1)
        rowPlayed = playColumn(board, col, turn)
        if rowPlayed == -1:
            continue
        nextTurn = PLAYER if turn == AI else AI
        (childValue, nextMove) = min_max_no_pruning(board, depth + 1, nextTurn, alpha, beta, maxDepth,values, adj, id+col+1)
        board[rowPlayed][col] = '0'

        if turn == AI:
            if childValue > val:
                val = childValue
                bestMove = col
        else:
            if childValue < val:
                val = childValue
                bestMove = col


    values[id] = val

    return val, bestMove
