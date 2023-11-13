class Agent:
    def __init__(self, k, pruning):
        self.k = k
        self.pruning = pruning

    def play(self, state):
        column = 5
        user_score = 2
        agent_score = 1
        state_value = 5
        return column, user_score, agent_score, state_value
