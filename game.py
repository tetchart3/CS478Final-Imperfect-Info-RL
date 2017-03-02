import numpy

# game only returns observation and reward. eg - observation is the what the player does, reward is the final outcome

# to do:
    # dense rewards

class Game(object):
    def __init__(self):

        # negative score means player 2 wins. Positive score means player 1 wins. A score of zero is either beginning
        # game or a tie
        self.score = 0
        self.keepScores = {'h': 0.5, 't': -0.5}

    def start_game(self):
        self.flip()
        return self.toss

    def flip(self):
        randToss = np.random.random()
        if randToss > .5:
            self.toss = 'h'
        else:
            self.toss = 't'


    def game_action(self, agent):
        # start action depending on state
        if agent.number == 1:
            return self.agent1_action_response(agent)
        else:
            return self.agent2_action_response(agent)

    def agent1_action_response(self, agent):
        # do action for player 1
        if agent.action == 1:  # keep
            self.score += self.keepScores[self.toss]
        return agent.action, self.score


    def agent2_action_response(self, agent):
        # do action for player 2
        if agent.action == 1:  # keep
            if agent.guess == self.toss:
                self.score -= 1
            else:
                self.score += 1
        else:
            self.score += 0.5
