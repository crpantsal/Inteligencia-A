# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        
        """La funcion de evaluacion funcianara de la siguiente forma, si la accion es stop 
        retornaremos un numero negativo, en caso contrario si pacaman esta cerca de fantasma y
        este no ha comido una caosula, devolveremos un  numero negativo para que se aleje, en 
        caso contrario devolveremos un numero positivo y la puntacion obetnida, y en caso de que estemos
        lejos del fanstasma devolveremos un numero positivo y la puntacion obetnida"""
        
        if (action != "Stop"):
            successorGameState = currentGameState.generatePacmanSuccessor(action)
            newPos = successorGameState.getPacmanPosition()
            newFood = successorGameState.getFood()
            newGhostStates = successorGameState.getGhostStates()
            newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    
            
            
           
            for ghost in successorGameState.getGhostPositions():
                for scared in newScaredTimes:                    
                    if (scared != 0):
                        if (util.manhattanDistance(newPos,ghost) < 1):
                            return -1000
                        elif (util.manhattanDistance(newPos,ghost) > 1):
                            return 1000 + successorGameState.getScore()
                    else:
                        return 1000 + (successorGameState.getScore())
        else:
            return -1000
            
        
def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
       

        def minimax(currentGameState, depth):
             
            if (depth == 0 or currentGameState.isWin() or currentGameState.isLose()):
                return self.evaluationFunction(currentGameState) ,None 
            
            agentIndice = depth % currentGameState.getNumAgents()
            indice = (currentGameState.getNumAgents() - agentIndice) % currentGameState.getNumAgents()
            
            if indice == 0: #Para el pacamnan maximizamos nuesto valor 
                value = -float("inf") # Generamos un diccionario donde la key sera el valor que tiene hacer un movimiento, y el value el movimiento
                lista = {minimax(currentGameState.generateSuccessor(indice,move),depth-1)[0] : move for move in currentGameState.getLegalActions()}
                
                max_value = max(lista.keys())
                value = max(max_value,value)
                return value,lista[value] #Retornamos el valor maximo,con el movimiento
            
            else:#Para los fantasmas minimizamos nuestro valor
                value = float("inf") # Generamos un diccionario donde la key sera el valor que tiene hacer un movimiento, y el value el movimiento
                lista = {minimax(currentGameState.generateSuccessor(indice,move),depth-1)[0] : move for move in currentGameState.getLegalActions(indice)}
                                 
                min_value = min(lista.keys())
                value = min(min_value,value)
                return value,lista[value]#Retornamos el valor minimos,con el movimiento
            
        min_max = minimax(gameState,self.depth * gameState.getNumAgents())
        return min_max[1]
        
    

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def poda_alfa_beta(currentGameState, depth, alfa, beta):
             
            if (depth == 0 or currentGameState.isWin() or currentGameState.isLose()):
                return self.evaluationFunction(currentGameState) ,None
            
            agentIndice = depth % currentGameState.getNumAgents()
            indice = (currentGameState.getNumAgents() - agentIndice) % currentGameState.getNumAgents()
            
            if indice == 0:
                value = -float("inf")
                lista = {}
                
                for move in currentGameState.getLegalActions():
                    score,action = (poda_alfa_beta(currentGameState.generateSuccessor(indice,move),depth-1,alfa,beta)[0],move)
                    lista[score] = action
                    value = max(lista.keys())                    
                    
                    alfa = max(alfa,value)
                    
                    if (value > beta):
                        return value,lista[value]
                    
                return value,lista[value]
            
            else:
                value = float("inf")
                lista = {}                
                
                for move in currentGameState.getLegalActions(indice):
                    score,action = (poda_alfa_beta(currentGameState.generateSuccessor(indice,move),depth-1,alfa,beta)[0],move)
                    lista[score] = action                    
                    value = min(lista.keys())                 
                    
                    beta = min(value,beta)
                    
                    if (value < alfa):
                        return value,lista[value]
                     
                return value,lista[value]
            
        al_bet = poda_alfa_beta(gameState,self.depth * gameState.getNumAgents(),-float("inf"),float("inf"))
        return al_bet[1]


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def Expectimax(currentGameState, depth):
             
            if (depth == 0 or currentGameState.isWin() or currentGameState.isLose()):
                return self.evaluationFunction(currentGameState) ,None
            
            agentIndice = depth % currentGameState.getNumAgents()
            indice = (currentGameState.getNumAgents() - agentIndice) % currentGameState.getNumAgents()
            
            if indice == 0:
                value = -float("inf")
                lista = {Expectimax(currentGameState.generateSuccessor(indice,move),depth-1)[0] : move for move in currentGameState.getLegalActions() }
                value = max(lista.keys()) 
                return value,lista[value]
            
            else:
                value = 0
                numAccions = 0
                lista = {}
                
                #El valor sera la suma de la puntuacion obtenido, entre el numero de acciones, y la accion la ultima realizada
                for move in currentGameState.getLegalActions(indice):
                    numAccions += 1 
                    score,action = (Expectimax(currentGameState.generateSuccessor(indice,move),depth-1)[0],move)
                    value += score
                    
                    lista[value] = action                    
           
                return value/numAccions,lista[value]
            
        exp = Expectimax(gameState,self.depth * gameState.getNumAgents())
        return exp[1]
    
    
"""EXAMEN"""    
class expectimaxMinimaxAgent2(MultiAgentSearchAgent):
    
    def getAction(self, gameState):
    
        def expectimax_MinimaxAgent2(currentGameState, depth):
    
            if (depth == 0 or currentGameState.isWin() or currentGameState.isLose()):
                return self.evaluationFunction(currentGameState) ,None
        
            agentIndice = depth % currentGameState.getNumAgents()
            indice = (currentGameState.getNumAgents() - agentIndice) % currentGameState.getNumAgents()
            
            """Pacaman siempre maximizara el valor"""
            if indice == 0: 
                
                value = -float("inf") # Generamos un diccionario donde la key sera el valor que tiene hacer un movimiento, y el value el movimiento
                lista = {expectimax_MinimaxAgent2(currentGameState.generateSuccessor(indice,move),depth-1)[0] : move for move in currentGameState.getLegalActions()}
                
                max_value = max(lista.keys())
                value = max(max_value,value)
                return value,lista[value] #Retornamos el valor maximo,con el movimiento
                
                
                
            #Si es par usara expectimax
            elif indice % 2 == 0: 
                value = 0
                numAccions = 0
                lista = {}
                
                #El valor sera la suma de la puntuacion obtenido, entre el numero de acciones, y la accion la ultima realizada
                for move in currentGameState.getLegalActions(indice):
                    numAccions += 1 
                    score,action = (expectimax_MinimaxAgent2(currentGameState.generateSuccessor(indice,move),depth-1)[0],move)
                    value += score
                    
                    lista[value] = action                    
           
                return value/numAccions,lista[value]
            
            #Si es impar usara minimax
            elif indice % 2 != 0: 
                
                value = float("inf") # Generamos un diccionario donde la key sera el valor que tiene hacer un movimiento, y el value el movimiento
                lista = {expectimax_MinimaxAgent2(currentGameState.generateSuccessor(indice,move),depth-1)[0] : move for move in currentGameState.getLegalActions(indice)}
                                 
                min_value = min(lista.keys())
                value = min(min_value,value)
                return value,lista[value]#Retornamos el valor minimos,con el movimiento
    
    
        exp_min_max = expectimax_MinimaxAgent2(gameState,self.depth * gameState.getNumAgents())
        return exp_min_max[1]

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    
    """Nuestra funcion de evaluacion sera la distancia de manhathan entre la comida y el pacaman     + 
     LA distancia entre las capsulas y el pacman, menos la distancia entre los fantasmas y el pacman"""
    
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    
    dist_food = 0
    
    for food in newFood.asList():
        dist_food=max(dist_food,util.manhattanDistance(newPos,food) ** -1 )
    
    dist_ghost = 0
    
    for ghost in currentGameState.getGhostStates():
        dist_ghost = max(dist_ghost,util.manhattanDistance(currentGameState.getPacmanPosition(),ghost.getPosition()))
    
    dist_caps = 0
    for Cap in currentGameState.getCapsules():
        dist_caps=max(dist_caps,util.manhattanDistance(Cap,currentGameState.getPacmanPosition()) **-1)
    
    return currentGameState.getScore() + dist_food - dist_ghost + dist_caps
    
  
    
    

# Abbreviation
better = betterEvaluationFunction

