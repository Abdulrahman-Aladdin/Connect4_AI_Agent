import numpy as np
maxDepth = 5
MAXNUMBER = 1e9
rows = 6
cols = 7


def min_max_no_pruning(board, depth, turn):
    pass
#     if(depth == maxDepth or leafNode(board)):
#         return (evalFunction(board), board)
#
#     if(turn == 0): # current node is max
#         val = -MAXNUMBER
#     else:
#         val = MAXNUMBER
#     bestMove = board
#
#     for child in possibleMoves(board, turn+1):
#         (childValue, nextMove) = min_max_no_pruning(child, depth+1, 1 - turn)
#         if(turn == 0):
#             if val < childValue:
#                 val = childValue
#                 bestMove = child
#         else:
#             if(val > childValue):
#                 val = childValue
#                 bestMove = child
#
#     return (val, bestMove)


def min_max_pruning(board, depth, turn, alpha, beta):
    if depth == maxDepth or leafNode(board):
        return evalFunction(board), board

    if turn == 0:   # current node is max
        val = -MAXNUMBER
    else:
        val = MAXNUMBER
    bestMove = 0

    for col in range(0, cols):
        rowPlayed = playColumn(board, col, turn+1)
        if rowPlayed == -1:
            continue
        childValue, nextMove = min_max_pruning(board, depth+1, 1-turn, alpha, beta)
        board[rowPlayed][col] = 0

        if turn == 0:
            if val < childValue:
                val = childValue
                bestMove = col
            if val >= beta:
                return val, col
            alpha = max(alpha, val)
        else:
            if val > childValue:
                val = childValue
                bestMove = col
            if val <= alpha:
                return val, col
            beta = min(beta, val)

    return val, bestMove


def leafNode(board):
    return all(cell != 0 for row in board for cell in row)


def playColumn(board, col, turn):
    for i in range(rows - 1, -1, -1):
        if board[i][col] == 0:
            board[i][col] = turn
            return i
    return -1


def evalFunction(board):
    score = 0

    # Check rows for potential wins or threats
    for r in range(board.shape[0]):
        for c in range(board.shape[1] - 3):
            window = board[r, c:c+4]
            score += evaluate_window(window)

    # Check columns for potential wins or threats
    for c in range(board.shape[1]):
        for r in range(board.shape[0] - 3):
            window = board[r:r+4, c]
            score += evaluate_window(window)

    # Check diagonals (positive slope) for potential wins or threats
    for r in range(board.shape[0] - 3):
        for c in range(board.shape[1] - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window)

    # Check diagonals (negative slope) for potential wins or threats
    for r in range(board.shape[0] - 3):
        for c in range(board.shape[1] - 3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window)

    return score


def evaluate_window(window):
    score = 0
    player_count = np.count_nonzero(window == 1)
    agent_count = np.count_nonzero(window == 2)
    empty_count = np.count_nonzero(window == 0)

    if player_count == 4:
        score += 100
    elif player_count == 3 and empty_count == 1:
        score += 5
    elif player_count == 2 and empty_count == 2:
        score += 2
    elif agent_count == 4:
        score -= 100
    elif agent_count == 3 and empty_count == 1:
        score -= 5
    elif agent_count == 2 and empty_count == 2:
        score -= 2

    return score


def main():
    board = np.zeros((rows, cols), dtype=int)

    while True:
        move = input()
        playColumn(board, int(move), 1)
        (val, col) = min_max_pruning(board, 0, 1, -MAXNUMBER, MAXNUMBER)
        playColumn(board, col, 2)
        print(board)


if __name__ == "__main__":
    main()
