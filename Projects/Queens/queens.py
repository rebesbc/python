# depth first search
# python terminal test:
# > python -i Projects/Queens/queens.py
# > f
# > dfs(f)
# > exit()

# greedy, voraz o A*
from tree import Node

n = 4 # número de reinas en el tablero, tablero (n * n)
root = Node([1] * n) # [1, 1, 1, 1], n = 4
root.level = 0
f = [root.data] # [i+1] for i in range(n) [[1], [2], [3], ..., [n]]


# se recibe una lista que almacena las posibles configuraciones para las reinas
def limited_dfs(frontier, limit):
    if len(frontier) == 0:
        print("No hay solución")
        return False
    else:
        actual_state = frontier.pop(0)
        node = root.get_node(actual_state)
        actual_states_level = node.level
        if goal_test(actual_state):
            print("Se encontró la solución para ", n, " reinas:\n")
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
                        frontier[:0] = offsprings # concatena al inicio toda la lista offsprings
                    else:
                        frontier = offsprings[:] # clonar la lista offsprings en frontier
                print("- frontier: ", frontier, "\n")
                limited_dfs(frontier, limit)
            


def iterative_dfs():
    limit = 2
    ok = True

    while ok:
        frontier = [root.data]
        ok = limited_dfs(frontier, limit)
        limit += 2


def goal_test(test):
    return attacks(test) == 0 and len(test) == n


def expand(configuration):
    # obtener los hijos/descendientes del vector dado
    # se envía una lista con las siguientes configuraciones posibles (lista de listas)
    # máx. -n- hijos
    offsprings = []

    for i in range(n):
        child = list(configuration)
        element = child[i]
        if (element <= n - 1):
            element += 1
            child[i] = element
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
    
    if queens > 1: # si hay más de 1 reina en la configuración, comprobar ataques
        for i in range(1, queens): # for i = 1; i < n; i++
            for j in range(i+1, queens+1): # for j = i+1; j <= n; j++
                if configuration[i-1] == configuration[j-1]:
                    attacks += 2
                if abs(i - j) == abs(configuration[i-1] - configuration[j-1]):
                    attacks += 2

    return attacks

#######################
def main():
    print("Calculemos el tablero para ", n, " reinas:")
    limited_dfs(f, 5)


if __name__=="__main__": 
    main() 