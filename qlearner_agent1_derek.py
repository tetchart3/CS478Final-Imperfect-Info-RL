from agent import Agent
import numpy as np


#Does this make sense because observations are kind of independent?
class QLearnerAgent1Derek(Agent):

    OBSERVATION_SPACE = 2
    ACTION_SPACE = 2 #keep or give

    learning_rate = .01
    gamma = .8
    step = 0
    guesses = {0: 0, 1: 0}

    last_observation = None
    observation = None

    def __init__(self):
        super(QLearnerAgent1Derek, self).__init__()
        
        #initialize table
        self.Q = np.zeros([self.OBSERVATION_SPACE,self.ACTION_SPACE])


    def learn(self, prev_total_score, action_taken_by_this_agent, score_delta):
        
        # print("0,0: " + str(self.Q[0,0]))
        # print("0,1: " + str(self.Q[0,1]))
        # print("1,0: " + str(self.Q[1,0]))
        # print("1,1: " + str(self.Q[1,1]))

        #update Q table

        #This is when last observation leads to this observation...but that isn't the case with this game. Independent
        # if (self.last_observation != None and self.observation != None):
        #    self.Q[self.last_observation, action_taken_by_this_agent] = self.Q[self.last_observation, action_taken_by_this_agent] + \
        #        self.learning_rate * (score_delta + (self.gamma * self.Q[self.observation,action_taken_by_this_agent]) - self.Q[self.last_observation,action_taken_by_this_agent])

        #indepedent observations, so just update table
        self.Q[self.observation, action_taken_by_this_agent] = self.Q[self.observation, action_taken_by_this_agent] + \
                self.learning_rate * (score_delta - self.Q[self.observation,action_taken_by_this_agent])

    def get_action(self, observation):
        
        self.last_observation = self.observation
        self.observation = observation[1]
        observation = observation[1]

        #Choose an action by greedily (with noise) picking from Q table
        a = np.argmax(self.Q[observation,:] + np.random.randn(1,self.ACTION_SPACE)*(1./(self.step+1)))
        
        self.step += 1
        self.guesses[a] += 1
        if self.step % 10 == 0:
            print(self.guesses)
        
        return a

