from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic
from algorithms.utils import Queue
from algorithms.utils import PriorityQueue


def tinyDiagnosticSearch(problem: SearchProblem):
    """
    Returns a hard-coded sequence of moves for the tinyDiagnostic layout.
    For any other station layout, the sequence of moves will be incorrect.
    """
    s = Directions.SOUTH
    e = Directions.EAST
    return [s, e, s, e, e, e, e, s, e, e, s, s, e, s, s, e, s, e, e, e, e, e, e, e]


def depthFirstSearch(problem: SearchProblem):
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
    # TODO: Add your code here
    visitados = set()
    pila = utils.Stack()
    estadoInicial = problem.getStartState()
    pila.push((estadoInicial, []))
    while not pila.isEmpty():
        nodo, camino = pila.pop()

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if problem.isGoalState(nodo):
            return camino

        for sucesor, accion, costo in problem.getSuccessors(nodo):
            if sucesor not in visitados:
                nuevoCamino = camino + [accion]
                pila.push((sucesor, nuevoCamino))

    return []
    utils.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    inicio = problem.getStartState()
    cola  = Queue()
    visitados = set()
    visitados.add(inicio)
    cola.push((inicio,[]))
    
    while not cola.isEmpty():
        estado, camino = cola.pop()
        
        if problem.isGoalState(estado):
            return camino
        
        vecinos = problem.getSuccessors(estado)
        
        for succesor, accion, costo in vecinos:
            if succesor not in visitados:
                visitados.add(succesor)
                nuevoCamino = camino + [accion]
                cola.push((succesor, nuevoCamino))
        
    return []


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """
    # TODO: Add your code here
    inicio = problem.getStartState()
    cola = PriorityQueue()
    mejorCosto = {}
    mejorCosto[inicio] = 0
    cola.push((inicio, [], 0), 0)

    while not cola.isEmpty():
        estado, camino, costo = cola.pop()

        if costo > mejorCosto[estado]:
            continue

        if problem.isGoalState(estado):
            return camino

        vecinos = problem.getSuccessors(estado)

        for sucesor, accion, costoPaso in vecinos:
            nuevoCosto = costo + costoPaso

            if sucesor not in mejorCosto or nuevoCosto < mejorCosto[sucesor]:
                mejorCosto[sucesor] = nuevoCosto
                nuevoCamino = camino + [accion]
                cola.push((sucesor, nuevoCamino, nuevoCosto),nuevoCosto)

    return []


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    inicio = problem.getStartState() #iniciamos 
    cola = PriorityQueue()
    
    mejorCosto = {}  
    mejorCosto[inicio] = 0
    
    costoInicial = 0
    prioridad = costoInicial + heuristic(inicio, problem) # f(n)=g+h
    
    cola.push((inicio, [], 0), heuristic(inicio, problem))
    
    while not cola.isEmpty():
        estado, camino, costo = cola.pop()
        
        if problem.isGoalState(estado):
            return camino
        
        vecinos = problem.getSuccessors(estado)
        
        for sucesor, accion, costoPaso in vecinos:
            
            nuevoCosto = costo + costoPaso
            
            if sucesor not in mejorCosto or nuevoCosto < mejorCosto[sucesor]:
                
                mejorCosto[sucesor] = nuevoCosto
                
                nuevoCamino = camino + [accion]
                
                prioridad = nuevoCosto + heuristic(sucesor, problem)
                
                cola.push((sucesor, nuevoCamino, nuevoCosto), prioridad)
    return []


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
