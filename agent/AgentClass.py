from agent.minmax import *
import numpy as np


class Agent:
    def __init__(self, k, pruning):
        self.k = k
        self.pruning = pruning

    def play(self, state):
        my_state = np.array(state)
        adjacency_list = {}
        for i in range(400):
            adjacency_list[i] = []
        for i in range(57):
            for j in range(1, 8):
                adjacency_list[i].append(i * 7 + j)
        for i in range(57, 400):
            adjacency_list[i] = []
        values = []
        for i in range(400):
            values.append(i)
        val, column = 0, 0
        if self.pruning:
            val, column = self.min_max_pruning(my_state, 0, 2, -MAXNUMBER, MAXNUMBER)
        else:
            val, column = min_max_no_pruning(my_state, 0, 2)
        user_score = 2
        agent_score = 1
        state_value = 5
        return column, user_score, agent_score, state_value, adjacency_list, values

    def min_max_pruning(self, board, depth, turn, alpha, beta):
        if depth == self.k or self.leafNode(board):
            return self.evalFunction(board), board

        if turn == 0:  # current node is max
            val = -MAXNUMBER
        else:
            val = MAXNUMBER
        bestMove = 0

        for col in range(0, cols):
            rowPlayed = self.playColumn(board, col, turn + 1)
            if rowPlayed == -1:
                continue
            childValue, nextMove = self.min_max_pruning(board, depth + 1, 1 - turn, alpha, beta)
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

    @staticmethod
    def leafNode(board):
        return all(cell != 0 for row in board for cell in row)

    @staticmethod
    def playColumn(board, col, turn):
        for i in range(rows - 1, -1, -1):
            if board[i][col] == 0:
                board[i][col] = turn
                return i
        return -1

    @staticmethod
    def evalFunction(board):
        score = 0

        # Check rows for potential wins or threats
        for r in range(board.shape[0]):
            for c in range(board.shape[1] - 3):
                window = board[r, c:c + 4]
                score += evaluate_window(window)

        # Check columns for potential wins or threats
        for c in range(board.shape[1]):
            for r in range(board.shape[0] - 3):
                window = board[r:r + 4, c]
                score += evaluate_window(window)

        # Check diagonals (positive slope) for potential wins or threats
        for r in range(board.shape[0] - 3):
            for c in range(board.shape[1] - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += evaluate_window(window)

        # Check diagonals (negative slope) for potential wins or threats
        for r in range(board.shape[0] - 3):
            for c in range(board.shape[1] - 3):
                window = [board[r + 3 - i][c + i] for i in range(4)]
                score += evaluate_window(window)

        return score

    @staticmethod
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

