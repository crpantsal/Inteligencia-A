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
    
    nodo = problem.getStartState()
    frontera = util.Stack()
    frontera.push((nodo,[]))    
    cerrados = []
 
    while (not frontera.isEmpty()):
        
        nodo,list_position = frontera.pop()       
                
        if (problem.isGoalState(nodo)):            
            return list_position
        
        if (nodo not in cerrados):
            cerrados.append(nodo)            
            for success in problem.getSuccessors(nodo):
                if (success[0] not in cerrados):                       
                    frontera.push((success[0],list_position+[success[1]]))
  
            

    util.raiseNotDefined()
    
        
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    nodo = problem.getStartState()
    frontera = util.Queue()
    cerrados = []
    frontera.push((nodo,[]))
    
    while(not frontera.isEmpty()):
        
        nodo,list_position = frontera.pop()   
        
        if (problem.isGoalState(nodo)):            
            return list_position
    
        if (nodo not in cerrados):
            cerrados.append(nodo)        
            for success in problem.getSuccessors(nodo):
                if (success[0] not in cerrados):
                    frontera.push((success[0],list_position+[success[1]]))
                
    
    
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

    
    
    frontera = util.PriorityQueue()
    nodo = problem.getStartState()
    frontera.push((nodo,[],0),1)
    cerrados = []

    while(not frontera.isEmpty()):
        
        nodo,direccion,coste = frontera.pop()
       
        if(problem.isGoalState(nodo)):
            return direccion
        
        if (nodo not in cerrados):
            cerrados.append(nodo)
            
            for success in problem.getSuccessors(nodo):              
                
                actual = heuristic(success[0],problem)
                coste_a = coste+success[2]
                movimientos = direccion+[success[1]]
                cota = actual+coste_a    
                frontera.push((success[0],movimientos,coste_a),cota)


    util.raiseNotDefined()


def DFSLimited(problem, limit=70):
    
    nodo = problem.getStartState()
    frontera = util.Stack()
    frontera.push((nodo,[],0))    
    cerrados = []

    
    while (not frontera.isEmpty()):
        
        nodo,list_position, coste = frontera.pop()       
                
        if (problem.isGoalState(nodo)):     
            print (len(list_position))
            return list_position
        
        if (nodo not in cerrados and coste < 75):
            cerrados.append(nodo)            
            for success in problem.getSuccessors(nodo):
                if (success[0] not in cerrados):                       
                    frontera.push((success[0],list_position+[success[1]],coste+success[2]))
                    

        

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
