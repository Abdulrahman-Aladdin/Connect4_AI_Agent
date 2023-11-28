import numpy as np

rows = 6
cols = 7
AI = '1'
PLAYER = '2'


def isLeafNode(board):
    return all(cell != '0' for row in board for cell in row)


def evalLeafNode(board):
    Aiscore = count_consecutive_ones(board, AI)
    playerScore = count_consecutive_ones(board, PLAYER)
    return Aiscore - playerScore


def count_consecutive_ones(array, val):
    rows, cols = array.shape
    consecutive_ones_diagonals = [0] * 24
    consecutive_ones_rows = [0] * rows
    consecutive_ones_cols = [0] * cols

    # Function to count consecutive ones in a 1D array
    def count_consecutive_ones_1d(arr):
        count = 0
        max_count = 0
        for elem in arr:
            if elem == val:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max(max_count - 3, 0)

    # Iterate through main diagonals
    i = 0
    for d in range(-rows + 1, cols):
        diagonal = np.diagonal(array, offset=d)
        consecutive_ones_diagonals[i] = count_consecutive_ones_1d(diagonal)
        i += 1

    # Iterate through anti-diagonals
    for d in range(-rows + 1, cols):
        diagonal = np.diagonal(np.fliplr(array), offset=d)
        consecutive_ones_diagonals[i] = count_consecutive_ones_1d(diagonal)
        i += 1

    # Count consecutive ones in rows
    for i in range(rows):
        consecutive_ones_rows[i] = count_consecutive_ones_1d(array[i, :])

    # Count consecutive ones in columns
    for j in range(cols):
        consecutive_ones_cols[j] = count_consecutive_ones_1d(array[:, j])

    score = sum(consecutive_ones_cols) + sum(consecutive_ones_rows) + sum(consecutive_ones_diagonals)
    return score


def playColumn(board, col, turn):
    for i in range(rows - 1, -1, -1):
        if board[i][col] == '0':
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
    AI_count = np.count_nonzero(window == AI)
    PLAYER_count = np.count_nonzero(window == PLAYER)
    empty_count = np.count_nonzero(window == '0')

    if PLAYER_count == 4:
        score -= 50
    elif PLAYER_count == 3 and empty_count == 1:
        score -= 25
    elif PLAYER_count == 2 and empty_count == 2:
        score -= 15
    elif PLAYER_count == 1 and empty_count == 3:
        score -= 5

    if AI_count == 4:
        score += 50
    elif AI_count == 3 and empty_count == 1:
        score += 25
    elif AI_count == 2 and empty_count == 2:
        score += 15
    elif AI_count == 1 and empty_count == 3:
        score -= 5

    return score
