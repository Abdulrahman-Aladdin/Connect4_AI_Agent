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
            val, column = min_max_pruning(my_state, self.k, 2, -MAXNUMBER, MAXNUMBER)
        else:
            val, column = min_max_no_pruning(my_state, self.k, 2)
        user_score = 2
        agent_score = 1
        state_value = 5
        return column, user_score, agent_score, state_value, adjacency_list, values
