import numpy as np

class Agent:

    def __init__(self, player1):
        # player1 is bool
        self.KEEP = 0
        self.GIVE = 1
        ####
        self.HEADS = 0
        self.TAILS = 1
        self.FORFEIT = 2
        # Define for each player
        pass

    def learn(self, score, action):
        # score is number
        pass

    def get_action(self, observation):
        # observation is bool
        return # int
