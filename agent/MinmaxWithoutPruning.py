from agent.State import State
from agent.Utilities import *

OO = 1e9
AI = '1'
PLAYER = '2'


def min_max_no_pruning(state, depth, turn, alpha, beta, maxDepth, values, adj, id, expandedNodes):
    if state.isLeafNode():
        val, col = state.checkFourAndBeyond(state.bitboard[0]) - state.checkFourAndBeyond(state.bitboard[1]), -1
        adj[id] = []
        values[id].append(int(val))
        return val, col
    elif depth == maxDepth:
        ans = state.getScore(0) - state.getScore(1)
        adj[id] = []
        values[id].append(int(ans))
        return ans, -1

    expandedNodes[0] += 1
    if turn == AI:  # current node is max
        val = -OO
    else:
        val = OO

    best_move = 0

    # id = 0 -> 1 2 3 4 5 6 7
    # id = 1 ->
    adj[id] = []
    for col in state.getPossibleMoves():
        state.makeMove(col)

        child_id = id * 7 + col + 1
        adj[id].append(child_id)
        values[child_id] = [col]
        next_turn = PLAYER if turn == AI else AI
        child_value, next_move = min_max_no_pruning(state, depth + 1, next_turn, alpha, beta,
                                                    maxDepth, values, adj, child_id, expandedNodes)
        state.undoMove()

        if turn == AI:
            if child_value > val:
                val = child_value
                best_move = col
        else:
            if child_value < val:
                val = child_value
                best_move = col

    values[id].append(int(val))
    return val, best_move
