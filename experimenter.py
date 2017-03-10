import numpy as np
import matplotlib.pyplot as plt
import argparse
from game import Game
from simple_agent1 import Agent1
from simple_agent2 import Agent2

class Experimenter(object):

    def __init__(self, rounds = 10, graph = False):
        self.agent1 = Agent1()
        self.agent2 = Agent2()
        self.g = Game(self.agent1, self.agent2)
        self.rounds = rounds;
        self.graph = graph

    def run(self):
        scores = []
        rounds = []
        for i in range(self.rounds):
            score = self.g.play_round()
            scores.append(score)
            rounds.append(i + 1)
            print('Score: ' + str(score))
            
        if (self.graph):
            plt.plot(rounds, scores)
            plt.ylabel('Player 1 Score')
            plt.xlabel('Number of Rounds')
            plt.title('Coin Toss Game Results')
            plt.show()

def main():

    parser = argparse.ArgumentParser(description='Experimenter') 
    parser.add_argument('-R', '--rounds', required=False, type=int, help='Pass the number of rounds you would like to see played')
    parser.add_argument('-G', '--graph', required=False, action='store_true', help='If included, this flag will print a graph of the score after each round')
    args = parser.parse_args()
    rounds = 10
    if (args.rounds):
        rounds = args.rounds
    graph = False
    if (args.graph):
        graph = args.graph
    exp = Experimenter(rounds, graph)
    exp.run()

if __name__ == "__main__":
    main()
