# es un objeto para almacenar un nodo perteneciente a una lista enlazada
class Node:
    # atributos
    data = None 
    next_node = None 

    # constructor
    def __init__(self, data):
        self.data = data

    # devuelve la representación del objeto en un String
    def __repr__(self):
        # %s se sustituye por lo que hay a continuación de %
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    Singly linked list
    python ya tiene por defecto un atributo de tipo 'head'
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        # devuelve una representación de la lista en String
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        # agrupa todas las cadenas de nodos en una sola cadena String
        return '-> '.join(nodes)

    def is_empty(self):
        return self.head == None
    
    def size(self):
        # devuelve el número de nodos que hay en la lista

        current = self.head
        count = 0

        # el último nodo de una lista enlazada, es el que no guarda referencia a otro nodo
        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def add (self, data):
        # añade un nuevo nodo al comienzo de la lista
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node