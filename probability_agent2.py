from agent import Agent
import numpy as np

class Prob_Agent2(Agent):

    def __init__(self):
        super(Prob_Agent2, self).__init__()

    def learn(self, score_delta):
        pass

    def get_action(self, observation):
        if (observation[1] == self.KEEP):
            return self.FORFEIT
        elif (observation[1] == self.GIVE):
            h = .3
            t = .6
            f = .1
            return np.random.choice([self.HEADS, self.TAILS, self.FORFEIT], p=[h, t, f])