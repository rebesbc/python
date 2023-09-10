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