from game import Game
from simple_agent1 import Agent1
from simple_agent2 import Agent2

class Experimenter(object):

    def __init__(self, rounds = 10):
        self.agent1 = Agent1()
        self.agent2 = Agent2()
        self.g = Game(self.agent1, self.agent2)
        self.rounds = rounds;

    def run(self):
        for i in range(self.rounds):
            score = self.g.play_round()
            print('Score: ' + str(score))
