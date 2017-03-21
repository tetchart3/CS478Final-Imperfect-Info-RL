
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

    def learn(self, prev_total_score, action_taken_by_this_agent, score_delta):
        # score is number
        pass

    def get_action(self, observation):
        # observation is number
        return # int


# agent1: observation = [total_score, heads_or_tails]
# agent2: observation = [total_score, keep_or_give]

# experiment_replay = (observation, action_taken_by_this_agent, score_delta, next_observation)