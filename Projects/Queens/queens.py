# depth first search
# python terminal test:
# > python -i Projects/Queens/queens.py
# > f
# > dfs(f)
# > exit()

n = 5 # número de reinas en el tablero, tablero (n * n)
f = [[i+1] for i in range(n)] # [[1], [2], [3], ..., [n]]

# se recibe una lista que almacena las posibles configuraciones para las reinas
def dfs(frontier):
    if len(frontier) == 0:
        print("No hay solución para ", n, " reinas")
        return
    else:
        actual_state = frontier.pop(0)
        if goal_test(actual_state):
            print("Se encontró la solución para ", n, " reinas:\n")
            print(actual_state)
            return
        else:
            print("#actual_state: ", actual_state)
            offsprings = expand(actual_state)
            print("- offsprings: ", offsprings)
            if len(offsprings) > 0:
                if frontier:
                    frontier[:0] = offsprings # concatena al inicio toda la lista offsprings
                else:
                    frontier = offsprings[:] # clonar la lista offsprings en frontier
            print("* frontier: ", frontier, "\n")
            dfs(frontier)

def goal_test(test):
    return attacks(test) == 0 and len(test) == n

def expand(configuration):
    # obtener los hijos/descendientes del vector dado
    # se envía una lista con las siguientes configuraciones posibles (lista de listas)
    offsprings = []

    # si no es de las hojas del árbol
    if len(configuration) < n:
        # offsprings = [[1], [2], [3], ... [n]]
        offsprings = [[item] for item in range(1, n+1) if item not in configuration]

        for child in offsprings:
            child[:0] = configuration
        
    return offsprings

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
    dfs(f)


if __name__=="__main__": 
    main() 