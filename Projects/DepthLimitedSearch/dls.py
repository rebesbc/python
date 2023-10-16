# Depth Limited Search && Iterative Deepening Depth First Search
# Búsquedas aplicadas al problema de las reinas
# python terminal test:
# > python -i Projects/DLS/dls.py
# > dls(f, max_tries)
# > exit()

from tree import Node

n = 5                   # tablero (n * n)
max_tries = 30          # límite de iteraciones a probar
root = Node([1] * n)    # [1, 1, 1, 1], n = 4
root.level = 0
f = [root.data]         # frontier en estado inicial
visited = []            # nodos visitados


# Depth Limited Search
def dls(frontier, limit):
    if len(frontier) == 0:
        print("No hay solución")
        return False
    else:
        actual_state = frontier.pop(0)
        node = root.get_node(actual_state)
        actual_states_level = node.level
        visited.append(actual_state)
        if goal_test(actual_state):
            print("Se encontró la solución para ", n, " reinas: ")
            print(actual_state)
            return True
        else:
            if limit > actual_states_level:
                print("- actual_state: ", actual_state)
                offsprings = expand(actual_state)
                print("- offsprings: ", offsprings)
                assign_level(offsprings, actual_states_level + 1)
                if len(offsprings) > 0:
                    if frontier:
                        frontier[:0] = offsprings
                    else:
                        frontier = offsprings[:]
                print("- frontier: ", frontier, "\n")
                dls(frontier, limit)
            else:
                print("No se halló solución para ", n, " reinas en ", limit, " iteraciones")
                return False
            

# Iterative Deepening Depth First Search
def iddfs():
    limit = 2
    visited.clear()
    ok = False

    while not ok:
        frontier = [root.data]
        print("## Probando con un límite de ", limit, " ##")
        ok = dls(frontier, limit)
        limit += 2


def goal_test(test):
    return attacks(test) == 0


def expand(configuration):
    offsprings = []

    for i in range(n):
        child = list(configuration)
        element = child[i]
        if (element <= n - 1):
            element += 1
            child[i] = element
            if child not in visited:
                offsprings.append(child)

                # agregar al árbol cada hijo-offspring
                father = root.get_node(configuration)
                father.add_child(Node(child))

    return offsprings


def assign_level(children, level):
    for child in children:

        node = root.get_node(child)
        node.level = level


def attacks(configuration):
    queens = len(configuration) # n
    attacks = 0
    
    for i in range(1, queens): # for i = 1; i < n; i++
        for j in range(i+1, queens+1): # for j = i+1; j <= n; j++
            if configuration[i-1] == configuration[j-1]:
                attacks += 2
            if abs(i - j) == abs(configuration[i-1] - configuration[j-1]):
                attacks += 2

    return attacks

###########
def main():
    print("# Calculemos el tablero para ", n, " reinas #")
    dls(f, max_tries)


if __name__=="__main__": 
    main() 