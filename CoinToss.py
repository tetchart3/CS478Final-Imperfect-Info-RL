import numpy as np

class CoinToss:

    def __init__(self):
        self.keepScores = {'h':0.5, 't':-0.5}


    def playHumanGame(self, rounds):
        # Score of Player 1
        self.score = 0

        # Run through rounds
        for r in xrange(rounds):
            # User Interface
            print "\n=== Round {} ===".format(r+1)

            # Flip coin
            self.flip()
            print "Toss:", self.toss

            # Player 1 action
            player1 = raw_input("Player 1: Keep? (y/n): ")
            
            # Keep
            if player1 == 'y':
                self.score += self.keepScores[self.toss]

            # Give to Player 2
            else:
                player2 = raw_input("Player 2: Guess? (h/t/f): ")
                if player2 == self.toss:
                    self.score -= 1.0
                else:
                    self.score += 1.0

        print self.score

#####################################################################
# Game Mechanics

    def flip(self):
        randToss = np.random.random()
        if randToss > .5:
            self.toss = 'h'
        else:
            self.toss = 't'