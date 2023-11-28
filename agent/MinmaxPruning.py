from agent.Utilities import *
from agent.State import State
OO = 1e9
AI = '1'
PLAYER = '2'


def min_max_pruning(state: State, depth, turn, alpha, beta, maxDepth):
    # if state.isLeafNode():
    #     return evalLeafNode(state), state
    if depth == maxDepth:
        return getScore(state.checkFiveAndBeyond(state.bitboard[0]), 
                        state.checkFourAndBeyond(state.bitboard[0]), 
                        state.checkThreeAndBeyond(state.bitboard[0]), 
                        state.checkTwoAndBeyond(state.bitboard[0])) - getScore(state.checkFiveAndBeyond(state.bitboard[1]), 
                        state.checkFourAndBeyond(state.bitboard[1]), 
                        state.checkThreeAndBeyond(state.bitboard[1]), 
                        state.checkTwoAndBeyond(state.bitboard[1])), state
        # return state.checkFourAndBeyond(state.bitboard[0]) - state.checkFourAndBeyond(state.bitboard[1]), state

    if turn == AI:
        val = -OO
    else:
        val = OO

    #At each node need to make adj = <Key, List<Pair<id, val>>>


    bestMove = 0

    for col in state.getPossibleMoves():
        state.makeMove(col)
        # rowPlayed = playColumn(state, col, turn)
        # if rowPlayed == -1:
        #     continue

        nextTurn = PLAYER if turn == AI else AI
        (childValue, nextMove) = min_max_pruning(state, depth + 1, nextTurn, alpha, beta, maxDepth)
        # state[rowPlayed][col] = '0'
        state.undoMove()
        if turn == AI:
            if childValue > val:
                val = childValue
                bestMove = col

            if val >= beta:
                return val, bestMove
            alpha = max(val, alpha)
        else:
            if childValue < val:
                val = childValue
                bestMove = col

            if alpha >= val:
                return val, bestMove
            beta = min(beta, val)


    return val, bestMove

def getScore(fives, fours, threes, twos):
    return 