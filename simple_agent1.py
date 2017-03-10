from agent import Agent

class Agent1(Agent):

    def __init__(self):
        super(Agent1, self).__init__()

    def learn(self, score_delta):
        pass

    def get_action(self, observation):
        return self.GIVE
