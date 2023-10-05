# breadth first search
# python terminal test:
# > python -i bfs.py
# > root.print_tree()
# > bfs(f)
from tree import Node

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)
node15 = Node(15)
node16 = Node(16)
node17 = Node(17)
node18 = Node(18)

root.add_child(node2)
root.add_child(node3)
node2.add_child(node5)
node2.add_child(node6)
node3.add_child(node7)
node3.add_child(node8)
node5.add_child(node9)
node5.add_child(node10)
node6.add_child(node11)
node6.add_child(node12)
node7.add_child(node13)
node7.add_child(node14)
node8.add_child(node15)
node8.add_child(node16)
node12.add_child(node17)
node14.add_child(node18)

f = [root.data]

# se recibe una lista que almacena los valores de los nodos, no los nodos en sí mismos
def bfs(frontier):
    if len(frontier) == 0:
        print("No hay solución")
        return
    else:
        actual_state = frontier.pop(0)
        if goal_test(actual_state):
            print("Se encontró la solución para ", actual_state)
            return actual_state
        else:
            offsprings = expand(actual_state)
            print("actual state: ", actual_state, ", offsprings: ", offsprings)
            if len(offsprings) > 0:
                # extend funciona como append:
                # concatena al final toda la lista enviada por parámetro
                frontier.extend(offsprings)
            print("* frontier: ", frontier, "\n")
            bfs(frontier)

def goal_test(test):
    goal = 17
    return test == goal

def expand(data):
    # obtener el objeto Node a través de su data
    node = root.get_node(data)
    offsprings = []

    for child in node.children:
        offsprings.append(child.data)

    return offsprings