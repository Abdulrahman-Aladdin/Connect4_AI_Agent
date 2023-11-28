# import numpy as np
from agent.MinmaxWithoutPruning import *
from agent.Utilities import count_consecutive_ones


class Agent:
    def __init__(self, k, pruning):
        self.k = k
        self.pruning = pruning
        self.method = min_max_no_pruning

    def play(self, state):
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
