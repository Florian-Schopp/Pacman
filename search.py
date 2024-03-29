# search.py
# ---------
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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
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

def isVisited(node,problem,toVisit):
    """Checks if a node was already visited

        Method to check if the node was already visited. 

        Parameters
        ----------
        problem : Problem
            A description of the problem with Start,Goal and all walls.
        node : Node
            The node to be evaluated if it was already visited

        Returns
        -------
            Boolean if the node was already visited
        """
    print(len(problem._visitedlist))
    for visited in problem._visitedlist:
        if visited==node[0]:
            return True
    for visited in toVisit:
        if visited[0]==node[0]:
            return True
    return False

def aStarSearch(problem, heuristic=nullHeuristic):
    """Finds the shortest path to a given problem by using the A* algorithm

        If no heuristic isn't passed in, the Nullheuristic is used. The algorithm uses the passed in heuristic and the walked distance to estimate the next best step.

        Parameters
        ----------
        problem : Problem
            A description of the problem with Start,Goal and all walls.
        heuristic : heuristic, optional
            The heuristic to evaluate the goal distance (default is Nullheuristic)

        Returns
        -------
            A list of the steps to take from the start to the goal of the shortest path.
            
        Raises
        ------
        RuntimeError
            If no way for the given problem can be found to reach the goal.
        """
    
    initState = problem.getStartState()
    toVisit=[]
    toVisit.append((initState,) +('',0,tuple(),))
    while len(toVisit)>0:
        next = toVisit.pop(0)
        if problem.isGoalState(next[0]):
            return next[3]
        for successor in problem.getSuccessors(next[0]):
            if not isVisited(successor,problem,toVisit):
                toVisit.append(successor + (next[3]+(successor[1],),(heuristic(successor[0], problem)+len(next[3])+1)))
        toVisit = sorted(toVisit, key=lambda x: x[4])
    raise RuntimeError("No path was found!")
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
