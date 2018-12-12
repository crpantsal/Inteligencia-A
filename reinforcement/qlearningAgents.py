# -*- coding: utf-8 -*-
# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.elements = {}

        "*** YOUR CODE HERE ***"
        
        
        
class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.elements = {}

        "*** YOUR CODE HERE ***"
        
        
        

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        
        #Si no hem visitat el Qnode posem a 0 el seu valor y retornem el node
        #En cas contrari retornerm el Qnode
        if not self.elements.has_key((state,action)):
            self.elements[(state,action)] = 0.
        
        return self.elements[(state,action)]
        

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        
        #Generem tots el moviments que podem fer
        actions = self.getLegalActions(state)
        #En cas de que la accio no sigui legal (Exit) retornem 0
        if not actions:
            return 0.0
         #Obtenim els valors 
        _max = [self.getQValue(state, action) for action in actions]
        #Retornem el maxim
        return max(_max)
                

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        #1
       
       #Generem tots el moviments que podem fer
        actions = self.getLegalActions(state)
        #En cas de que la accio no sigui legal (Exit) retornem None
        if not actions:
            return None

        _max_action = util.Counter()
        for action in actions:
            _max_action[action] = self.getQValue(state, action)
         #Sino retornarem la millor accio
        return _max_action.argMax()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        
        if legalActions:
            if util.flipCoin(self.epsilon):#Si la epsilon es mayor que unvalor random farem una accio aleatoria
                action = random.choice(legalActions)
            else:
                action = self.computeActionFromQValues(state)
                #Si no agafarem la millor
        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        
        """Implementem la formula del q-learning"""
        
        sample = self.discount * self.computeValueFromQValues(nextState)  + reward
        self.elements[(state,action)] = (1-self.alpha) * self.getQValue(state,action) + self.alpha * sample
        

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action



class QLearningAgentPractica(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.elements = {}

        "*** YOUR CODE HERE ***"
        
        
###  EXAMEN  ###        
class QLearningAgentPractica(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.elements = {}
        
        "*** YOUR CODE HERE ***"
        
        
        

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        
        #Si no hem visitat el Qnode posem a 0 el seu valor y retornem el node
        #En cas contrari retornerm el Qnode
        times_est = 0
        est_vist = 0
        if not self.elements.has_key((state,action)):
            self.elements[(state,action)] = 0.
        
        return (self.elements[(state,action)],est_vist,times_est)
        

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        
        #Generem tots el moviments que podem fer
        actions = self.getLegalActions(state)
        #En cas de que la accio no sigui legal (Exit) retornem 0
        if not actions:
            return 0.0
         #Obtenim els valors 
        _max = [self.getQValue(state, action)[0] for action in actions]
        #Retornem el maxim
        return max(_max)
                

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        #1
       
       #Generem tots el moviments que podem fer
        actions = self.getLegalActions(state)
        #En cas de que la accio no sigui legal (Exit) retornem None
        if not actions:
            return None

        _max_action = util.Counter()
        for action in actions:
            _max_action[action] = self.getQValue(state, action)[0]
         #Sino retornarem la millor accio
        return _max_action.argMax()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        n = 0
        ns = 0
        "*** YOUR CODE HERE ***"
        for i in legalActions:
            value,n_veg,vist_est = self.getQValue(state, i)
            n+=vist_est
            ns += n_veg
        n+=1
        
        
            
        self.epsilon = (self.epsilon / (self.getQValue(state,action)+1)) * (ns/n)
        
        if legalActions:
            
            if util.flipCoin(self.epsilon):#Si la epsilon es mayor que unvalor random farem una accio aleatoria
                action = random.choice(legalActions)
            else:
                action = self.computeActionFromQValues(state)
                #Si no agafarem la millor
        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        
        """Implementem la formula del q-learning"""
        
        # p = (self.epsilon/(self.getQValue(state,action)+1)) * 
        sample = self.discount * self.computeValueFromQValues(nextState)  + reward
        value,n_veg,vist_est = self.getQValue(state,action)
        self.elements[(state,action)] = ((1-self.alpha) * self.getQValue(state,action) + self.alpha * sample,n_veg+1,1)
        

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)

