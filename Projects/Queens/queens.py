n = 50                  # tablero (n * n)
f = [0] * n             # [0, 0, 0, 0], n = 4
blacklist = []          # configuraciones visitadas

# Greedy Search
def greedys(frontier):
    print("\n- state: ", frontier)
    if not frontier:
        print("No hay solución")
        return False
    else:
        actual_state = frontier
        if goal_test(actual_state):
            print("Se encontró la solución para ", n, " reinas: ")
            print(actual_state)
            return True
        else:
            offsprings = expand(actual_state)
            order = evaluate(offsprings)
            offsprings = bubble_sort(offsprings, order)
        if offsprings:
            greedys(offsprings[0])
        else:
            greedys([])


def goal_test(test):
    return attacks(test) == 0


def expand(configuration):
    copy = configuration.copy()
    offspring_states = []
    blacklist.append(configuration)

    for row in range(0, n):
        for column in range(0, n):
            # Mueve la reina en la columna actual
            new_value = (configuration[column] + row) % n
            configuration[column] = new_value

            if configuration not in blacklist:
                offspring_states.append(configuration)

            configuration = copy.copy()

    return offspring_states


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