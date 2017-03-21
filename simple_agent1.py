from agent import Agent

class Agent1(Agent):

    def __init__(self):
        super(Agent1, self).__init__()

    def learn(self, prev_total_score, action_taken_by_this_agent, score_delta):
        pass

    def get_action(self, observation):
        if (observation[1] == self.HEADS):
            return self.KEEP
        else:
            return self.GIVE
