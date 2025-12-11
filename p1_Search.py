# p1_Search.py
# ---------
# Based on search.py from the UC Berkeley Pacman AI Projects.
# Original authors: John DeNero, Dan Klein, Brad Miller, Nick Hay, Pieter Abbeel.
# Original project link: http://ai.berkeley.edu
#
# Modifications for UCI EECS 118 by Mahmoud Elfar, 2025.
# This version includes changes to <TBD>.
#
# Licensing: You may use or extend this file for educational purposes
# provided that (1) solutions are not distributed or published,
# (2) this notice is retained, and (3) clear attribution to UC Berkeley is kept.


"""
In p1_Search.py, you will implement generic search algorithms which are called by
Pacman agents (in p1_SearchAgents.py).
"""

import util
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    stack = util.Stack()
    #Explored Set
    visited = set()

    #Get Initial State
    start = problem.getStartState()
    stack.push((start, []))

    while not stack.isEmpty():
        state, action = stack.pop()

        if problem.isGoalState(state):
            return action
        
        #Expansion
        if state not in visited:
            visited.add(state)
            for successor, actions, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    new_action = action + [actions]
                    stack.push((successor, new_action))
    return []
    

    
                    

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    #Explored Set
    visited = set()

    start = problem.getStartState()
    queue.push((start, []))

    while not queue.isEmpty():
        state, action = queue.pop()

        if problem.isGoalState(state):
            return action
        
        #Expansion
        if state not in visited:
            visited.add(state)
            for successor, actions, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    new_action = action + [actions]
                    queue.push((successor, new_action))
    return []
    

    util.raiseNotDefined()
    

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    visited = {}

    start = problem.getStartState()
    pq.push((start, [], 0), 0)
    while not pq.isEmpty():
        state, path, cost = pq.pop()

        if state in visited and visited[state] <= cost:
            continue
        
        visited[state] = cost
        if problem.isGoalState(state):
            return path
        #Expansion
        for successor, action, stepCost in problem.getSuccessors(state):
            new_cost = cost + stepCost
            pq.push((successor, path + [action], new_cost), new_cost)
    return []
    util.raiseNotDefined()


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    start = problem.getStartState()

    #best path
    best_g = {start: 0}
    #f(n) = g(n) + h(n)
    #f(n): priority of queue
    #g(n): path cost
    #h(n): heurisitic(state)
    pq.push((start, [], 0), heuristic(start, problem))

    while not pq.isEmpty():
        state, actions, gcost = pq.pop()
        if problem.isGoalState(state):
            return actions
        
        if gcost > best_g.get(state, float("inf")):
            continue

        #expand neighboring nodes
        for successor, action, stepCost in problem.getSuccessors(state):
            newG = gcost + stepCost
            #only consider this sucessor if path is the best path
            if newG < best_g.get(successor, float("inf")):
                best_g[successor] = newG
                newActions = actions + [action]
                fCost = newG + heuristic(successor, problem)
                pq.push((successor, newActions, newG), fCost)
    return []

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
