import numpy as np

# game only returns observation and reward. eg - observation is the what the player does, reward is the final outcome

# to do:
    # dense rewards

class Game(object):
    def __init__(self, agent1, agent2):

        # negative score means player 2 wins. Positive score means player 1 wins. A score of zero is either beginning
        # game or a tie
        self.player1 = agent1
        self.player2 = agent2
        self.score = 0
        self.keepScores = {0: 0.5, 1: -0.5}

    def play_round(self):
        toss = self.flip()
        action = self.player1.get_action(toss)
        if (action == self.player1.KEEP):
            self.player2.get_action(action)
            score_delta = self.keepScores[toss]
        else:
            response = self.player2.get_action(action)
            if (response == self.player2.FORFEIT):
                score_delta = -.5
            elif (response == toss):
                score_delta = -1
            else:
                score_delta = 1
        self.player1.learn(score_delta)
        self.player2.learn(score_delta)
        self.score += score_delta
        return self.score


    def flip(self):
        randToss = np.random.random()
        if randToss > .5:
            toss = 0
        else:
            toss = 1
        return toss

