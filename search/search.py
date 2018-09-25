# -*- coding: utf-8 -*-
#
# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "\n\nStart:", problem.getStartState()
    print "\n\nIs the start a goal?", problem.isGoalState(problem.getStartState())
    print "\n\nStart's successors\n\n:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    

    #return ['West','West','West','West','South','South',"East",'South','South','West']
    
    frontera = util.Stack()
    frontera.push(((problem.getStartState(),"",0),[]))
    nodo = problem.getStartState()
    cerrados = []
    list_f = []
    
    i = 0
    j = 0
    salir = True

    y = []
    #print "Succesores:" , problem.getSuccessors((25,16))
    #MIRAR DE SOLO IR AL POR EL PRIMERO
    print "\n\nStart:", problem.getStartState()
    while (salir):
        #print (j)
        elemento = frontera.pop()
        
        nodo = elemento[0][0]
        posicion = elemento[0][1]
        coste = elemento[0][2]
        list_position = elemento[1]
        x = list_position[:]
        
        
        #print "len: \t", nodo,"\n"
        #Pensar como se guardan
        #print j, "list:", list_position, nodo
        for i in range(len(problem.getSuccessors(nodo))):
            if (problem.getSuccessors(nodo)[i][0] not in cerrados):
                #print j,  elemento[1]
                #if(nodo == problem.getStartState()):
                    
                list_position.append(problem.getSuccessors(nodo)[i][1])                
                frontera.push((problem.getSuccessors(nodo)[i],list_position))
                #
                print j, elemento[1] , nodo
                list_position = x

       
        #El motivo es el retrocezo como estos ya estan listos en cerrados solo añade y en cambio cuando encuetra otro camino reinicia la lista.
        #print "y:", y
        if (problem.isGoalState(nodo)):
            salir = False
            list_f = list_position
        
        print j, elemento[1] , nodo
        cerrados.append(nodo)
        #list_position = []
       
        j+=1  
    
     
    
    return list_f#['South','South','West','South','West','West','South']#,'West']
    #return ['West','West','West','West','West','West','West','West','West']
    #return ['South','South','West','South','West','West','South','West']   
    util.raiseNotDefined()
    
        
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
