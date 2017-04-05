from agent import Agent
import numpy as np


class HumanAgent(Agent):

    def __init__(self, playernumber):
        super(HumanAgent, self).__init__()
        self.player = playernumber


    def learn(self, prev_total_score, action_taken_by_this_agent, score_delta):
        # score is number
        pass

    def get_action(self, observation):
        # observation is number
        player_dict = {0: 'Heads', 1: 'Tails'}
        print "From the game: Score: {} \t Toss: {} ".format(observation[0],  player_dict[observation[1]])
        # player1 is bool
        # self.KEEP = 0
        # self.GIVE = 1
        # ####
        # self.HEADS = 0
        # self.TAILS = 1
        # self.FORFEIT = 2
        if self.player == 1:
            playeraction = raw_input("Keep - 0 or Give - 1 ? ")
        else:
            playeraction = raw_input("Heads - 0, Tails - 1, or Forfeit - 2")


        return int(playeraction)

