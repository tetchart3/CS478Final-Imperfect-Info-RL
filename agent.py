
class Agent(object):

    def __init__(self):
        # player1 is bool
        self.KEEP = 0
        self.GIVE = 1
        ####
        self.HEADS = 0
        self.TAILS = 1
        self.FORFEIT = 2
        # Define for each player
        pass

    def learn(self, score_delta):
        # score is number
        pass

    def get_action(self, observation):
        # observation is number
        return # int
