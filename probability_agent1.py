from agent import Agent
import numpy as np

class Prob_Agent1(Agent):

    def __init__(self):
        super(Prob_Agent1, self).__init__()

    def learn(self, prev_total_score, action_taken_by_this_agent, score_delta):
        pass

    def get_action(self, observation):
        if (observation[1] == self.HEADS):
            k = .5
            g = .5
        else:
            k = .3
            g = .7
        return np.random.choice([self.KEEP, self.GIVE], p=[k, g])