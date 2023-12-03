from agent.Utilities import *
from agent.State import State

OO = 1e9
AI = '1'
PLAYER = '2'


def min_max_pruning(state: State, depth, turn, alpha, beta, maxDepth, values, adj, id, expandedNodes):
    if state.isLeafNode():
        val, col = state.checkFourAndBeyond(state.bitboard[0]) - state.checkFourAndBeyond(state.bitboard[1]), -1
        adj[id] = []
        values[id].append(int(val))
        return val, col
    if depth == maxDepth:
        ans = state.getScore(0) - state.getScore(1)
        adj[id] = []
        values[id].append(int(ans))
        return ans, -1

    expandedNodes[0] += 1
    if turn == AI:
        val = -OO
    else:
        val = OO

    # At each node need to make adj = <Key, List<Pair<id, val>>>

    bestMove = 0
    adj[id] = []
    for col in state.getPossibleMoves():
        state.makeMove(col)

        child_id = id * 7 + col + 1
        adj[id].append(child_id)
        values[child_id] = [col]

        nextTurn = PLAYER if turn == AI else AI
        (childValue, nextMove) = min_max_pruning(state, depth + 1, nextTurn, alpha, beta, maxDepth,
                                                 values, adj, child_id, expandedNodes)
        state.undoMove()

        if turn == AI:
            if childValue > val:
                val = childValue
                bestMove = col
            values[id].append(int(val))
            if val >= beta:
                return val, bestMove
            alpha = max(val, alpha)
        else:
            if childValue < val:
                val = childValue
                bestMove = col
            values[id].append(int(val))
            if alpha >= val:
                return val, bestMove
            beta = min(beta, val)

    return val, bestMove

