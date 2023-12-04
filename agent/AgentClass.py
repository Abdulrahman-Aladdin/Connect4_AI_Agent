# import numpy as np
from agent.MinmaxPruning import min_max_pruning
from agent.MinmaxWithoutPruning import *
from agent.State import State
from agent.Utilities import count_consecutive_ones


class Agent:
    def __init__(self, k, pruning):
        self.expandedNodes = [0]
        self.k = k
        self.method = None
        if pruning:
            self.method = min_max_pruning
        else:
            self.method = min_max_no_pruning
        board = [[0 for _ in range(7)] for _ in range(6)]
        self.state = State(board)

    def play(self, col):
        adj = {}
        values = {0: [-1]}
        self.state.makeMove(col)
        self.expandedNodes = [0]
        val, column = self.method(self.state, 0, AI, -OO, OO, self.k, values, adj, 0, self.expandedNodes)
        print("Expanded node -> " + str(self.expandedNodes[0]))
        self.state.makeMove(column)
        return (column, self.state.checkFourAndBeyond(self.state.bitboard[1]),
                self.state.checkFourAndBeyond(self.state.bitboard[0]), val, adj, values)

    def playYALABA2A(self, state):
        my_state = np.array(state)
        adj = {}
        values = {}
        val, column = self.method(my_state, 0, AI, -OO, OO, self.k, values, adj, 0)
        temp = my_state.copy()
        playColumn(temp, column, '1')
        user_score, agent_score = self.get_score(temp)
        return column, user_score, agent_score, val, adj, values

    @staticmethod
    def get_score(board):
        return count_consecutive_ones(board, '2'), count_consecutive_ones(board, '1')
