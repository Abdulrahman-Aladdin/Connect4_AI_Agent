from agent.AgentClass import Agent


class Controller:

    def __init__(self):
        self.agent = None

    def initiate_agent(self, k, pruning):
        self.agent = Agent(k, pruning)

    def agent_turn(self, state):
        return self.agent.play(state)
