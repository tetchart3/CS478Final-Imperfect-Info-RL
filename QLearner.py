import numpy as np
import agent as Agent


class QLearner(Agent):
    LR = 0.1
    GAMMA = 0.99
    OBSERVATION_SPACE = 2 # H or T
    ACTION_SPACE = 2 # G or K

    def __init__(self):
        super(QLearner,self ).__init__()
        self.Q = np.zeros(shape = [self.OBSERVATION_SPACE, self.ACTION_SPACE])

    def learn(self, prev_total_score, action_taken_by_this_agent, score_delta):
        self.Q[?, action_taken_by_this_agent] = self.Q[?, action_taken_by_this_agent] \
        + LR*((GAMMA* ?)- self.Q[?, action_taken_by_this_agent])

    def get_action(self, observation):
        observation = observation[1]
        a = np.argmin(self.Q[observation,:])+np.random.randn(1, self.ACTION_SPACE)
        return a
