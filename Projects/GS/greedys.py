from tree import Node

n = 3                   # tablero (n * n)
root = Node([2, 2, 1])  # Node([1] * n)    # [1, 1, 1, 1], n = 4
f = root.data           # frontier en estado inicial


# Greedy Search
def greedys(frontier):
    print("\n- actual_state: ", frontier)
    if not frontier:
        print("No hay solución")
        return False
    else:
        actual_state = frontier #.pop(0)
        if goal_test(actual_state):
            print("Se encontró la solución para ", n, " reinas: ")
            print(actual_state)
            return True
        else:
            offsprings = expand(actual_state)
            print("- offsprings: ", offsprings)
            offsprings_attacks = evaluate(offsprings)
            offsprings = bubble_sort(offsprings, offsprings_attacks)
            print("- sorted offsprings: ", offsprings)
        if offsprings:
            greedys(offsprings[0])
        else:
            greedys([])


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
            offsprings.append(child)

            father = root.get_node(configuration)
            father.add_child(Node(child))
                
    return offsprings


def evaluate(offsprings):
    number_attacks = []
    for child in offsprings:
        number_attacks.append(attacks(child))
    
    return number_attacks


# Bubble Sort
def bubble_sort(offsprings, attacks):
    swapped = False

    for n in range(len(attacks)-1, 0, -1):
        for i in range(n):
            if attacks[i] > attacks[i + 1]:
                swapped = True
                attacks[i], attacks[i + 1] = attacks[i + 1], attacks[i]
                offsprings[i], offsprings[i + 1] = offsprings[i + 1], offsprings[i]             
        if not swapped:
            break
        
    return offsprings


def attacks(configuration):
    # queens = len(configuration) # n
    attacks = 0
    
    for i in range(1, n): # for i = 1; i < n; i++
        for j in range(i+1, n+1): # for j = i+1; j <= n; j++
            if configuration[i-1] == configuration[j-1]:
                attacks += 2
            if abs(i - j) == abs(configuration[i-1] - configuration[j-1]):
                attacks += 2

    return attacks

###########
def main():
    print("# Calculemos el tablero para ", n, " reinas #")
    greedys(f)


if __name__=="__main__": 
    main() 