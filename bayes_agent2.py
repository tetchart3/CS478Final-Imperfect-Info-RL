from agent import Agent
import numpy as np

class Bayes_Agent2(Agent):

    def __init__(self):
        super(Bayes_Agent2, self).__init__()
        # We won't let it forfeit and set the
        # prior to be 50/50
        self.prior_heads = .5

        # Init counts at 1 for laplacian smoothing
        self.total_rounds = 1
        self.gives = 1
        self.heads_given_gives = 1

        # Assume that the probability if
        # player 1 keeps is 50/50
        self.gives_given_heads = .5


    def learn(self, prev_total_score, action_taken_by_this_agent, score_delta):
        # Update the counts
        self.total_rounds += 1
        if action_taken_by_this_agent != self.FORFEIT:
            self.gives += 1
        if action_taken_by_this_agent == self.HEADS:
            if score_delta == -1.0:
                self.heads_given_gives += 1
        if action_taken_by_this_agent == self.TAILS:
            if score_delta == 1.0:
                self.heads_given_gives += 1

        print("Gives", self.gives)
        print("H|G", self.heads_given_gives)

        # Update prior
        self.prior_heads = self.heads_given_gives / (1.0 * self.gives)


    def get_action(self, observation):
        print(self.prior_heads)
        if (observation[1] == self.KEEP):
            return self.FORFEIT
        elif (observation[1] == self.GIVE):
            return np.random.choice([self.HEADS, self.TAILS], p=[self.prior_heads, 1 - self.prior_heads])


# agent1: observation = [total_score, heads_or_tails]
# agent2: observation = [total_score, keep_or_give]

# experiment_replay = (observation, action_taken_by_this_agent, score_delta, next_observation)