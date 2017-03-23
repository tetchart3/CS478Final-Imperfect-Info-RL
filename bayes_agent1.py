from agent import Agent
import numpy as np

class Bayes_Agent1(Agent):

    def __init__(self):
        super(Bayes_Agent1, self).__init__()
        # Set the prior to be keep for heads and gives for tails
        self.prior_keep_heads = 1
        self.prior_keep_tails = 0

        # Init the observation
        self.prevObservation = 0

        # Init counts at 1 for laplacian smoothing
        self.total_rounds = 1
        self.guesses_heads = 1
        self.guesses_tails = 1
        self.gives = 1


    def learn(self, prev_total_score, action_taken_by_this_agent, score_delta):
        # Update the counts
        self.total_rounds += 1
        if action_taken_by_this_agent == self.GIVE:
            self.gives += 1
            if score_delta == -1:
                if self.prevObservation == self.HEADS:
                    self.guesses_heads += 1
                else:
                    self.guesses_tails += 1
            else:
                if self.prevObservation == self.HEADS:
                    self.guesses_tails += 1
                else:
                    self.guesses_heads += 1


    def get_action(self, observation):
        self.prevObservation = observation[1]

        if self.prevObservation == self.HEADS:
            expected_keep_score = .5
            expected_give_score = (self.guesses_tails / self.gives) - (self.guesses_heads / self.gives)
        else:
            expected_keep_score = -.5
            expected_give_score = (self.guesses_heads / self.gives) - (self.guesses_tails / self.gives)
        
        if np.max([expected_give_score, expected_keep_score]) == expected_give_score:
            return self.GIVE
        else:
            return self.KEEP


# agent1: observation = [total_score, heads_or_tails]
# agent2: observation = [total_score, keep_or_give]

# experiment_replay = (observation, action_taken_by_this_agent, score_delta, next_observation)