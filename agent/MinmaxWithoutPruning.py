from agent.Utilities import *

OO = 1e9
AI = '1'
PLAYER = '2'


def min_max_no_pruning(board, depth, turn, alpha, beta, maxDepth, values, adj, id):
    if isLeafNode(board):
        val, col = evalLeafNode(board), -1
        adj[id] = []
        values[id] = val
        return val, col
    elif depth == maxDepth:
        ans = evalFunction(board)
        adj[id] = []
        values[id] = ans
        return ans, -1

    if turn == AI:  # current node is max
        val = -OO
    else:
        val = OO

    best_move = 0

    # id = 0 -> 1 2 3 4 5 6 7
    # id = 1 ->
    for col in range(0, cols):
        row_played = playColumn(board, col, turn)
        if row_played == -1:
            continue
        child_id = id * 7 + col + 1
        adj[id].append(child_id)
        next_turn = PLAYER if turn == AI else AI
        child_value, next_move = min_max_no_pruning(board, depth + 1, next_turn, alpha, beta,
                                                    maxDepth, values, adj, child_id)
        board[row_played][col] = '0'

        if turn == AI:
            if child_value > val:
                val = child_value
                best_move = col
        else:
            if child_value < val:
                val = child_value
                best_move = col

    values[id] = val
    return val, best_move
