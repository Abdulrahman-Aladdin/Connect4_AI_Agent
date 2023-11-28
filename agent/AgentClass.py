# import numpy as np
from agent.MinmaxPruning import min_max_pruning
from agent.MinmaxWithoutPruning import *
from agent.State import State
from agent.Utilities import count_consecutive_ones


class Agent:
    def __init__(self, k, pruning):
        self.k = k
        self.pruning = pruning
        self.method = min_max_no_pruning
        board = [[0 for _ in range(7)] for _ in range(6)]
        self.state = State(board)

    def play(self, col):
        # my_state = np.array(state)
        # my_state = State(state)
        adj = {}
        values = {}
        self.state.makeMove(col)
        val, column = self.method(self.state, 0, AI, -OO, OO, self.k, values, adj, 0)
        self.state.makeMove(column)
        # my_state.makeMove(column)
        # temp = my_state.copy()
        # playColumn(temp, column, '1')
        # user_score, agent_score = self.get_score(temp)
        return column, self.state.checkFourAndBeyond(self.state.bitboard[1]), self.state.checkFourAndBeyond(self.state.bitboard[0]), val, adj, values

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
