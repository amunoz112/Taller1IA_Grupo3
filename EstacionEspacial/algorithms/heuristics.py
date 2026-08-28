from typing import Tuple
from algorithms import utils
from algorithms.problems import SystemRepairProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.

    Baseline rule for this workshop: estimate the direct distance to the next
    mandatory target:
    - K if the robot does not have the kit yet.
    - the nearest pending T if the robot has the kit and systems remain.
    - C if all systems have been repaired.
    """
    # TODO: Add your code here
    position, hasKit, pendingSystems = state
    
    if not hasKit:
        objetivo = problem.kitPosition
        
    if hasKit and len(pendingSystems) > 0:
        menorDistancia = float('inf')
        
        for sistema in pendingSystems:
            distancia = abs(position[0]-sistema[0]+abs(position[1]-sistema[1]))
            
            if distancia < menorDistancia:
                menorDistancia = distancia
                objetivo = sistema
    
    if hasKit and len(pendingSystems) == 0:
        objetivo = problem.controlPosition

    return abs(position[0] - objetivo[0]) + abs(position[1] - objetivo[1])
            

def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.

    Baseline rule for this workshop: estimate the direct distance to the next
    mandatory target:
    - K if the robot does not have the kit yet.
    - the nearest pending T if the robot has the kit and systems remain.
    - C if all systems have been repaired.
    """
    # TODO: Add your code here
    position, hasKit, pendingSystems = state
    
    if not hasKit:
        objetivo= problem.kitPosition
        
    if hasKit and len(pendingSystems) >0:
        menorDistancia = float('inf')
        
        for sistema in pendingSystems:
            disntacia = ((position[0] - sistema[0])**2 + (position[1] - sistema[1])**2)**0.5
                
            if disntacia < menorDistancia:
                menorDistancia = disntacia
                objetivo = sistema
                
    if hasKit and len(pendingSystems) == 0:
        objetivo = problem.controlPosition
        
    disntacia = ((position[0] - objetivo[0])**2 + (position[1] - objetivo[1])**2)**0.5
    
    return disntacia

def systemRepairHeuristic(state: Tuple[Tuple, bool, Tuple], problem: SystemRepairProblem):
    """
    Your heuristic for the SystemRepairProblem.

    state: (position, hasKit, pendingSystems)
    problem: SystemRepairProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider the kit, pending systems, and the final return to control center
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    position, hasKit, pendingSystems = state

    def distancia(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    if hasKit and len(pendingSystems) == 0:
        return distancia(position, problem.controlPosition)

    if not hasKit:
        distanciaKit = distancia(position, problem.kitPosition)
        menorSistema = float('inf')

        for sistema in pendingSystems:
            d = distancia(problem.kitPosition, sistema)

            if d < menorSistema:
                menorSistema = d

        return distanciaKit + menorSistema

    if hasKit and len(pendingSystems) > 0:
        menorSistema = float('inf')

        for sistema in pendingSystems:
            d = distancia(position, sistema)

            if d < menorSistema:
                menorSistema = d

        return menorSistema