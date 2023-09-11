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

    def search(self, key):
        # busca el primer nodo que contenga el dato que coincida con el parámetro 'key'
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        # inserta un nuevo nodo en un índice cualquiera deseado
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        # elimina el nodo que contenga la información deseada
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

