class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.level = None
        self.children = []

    def __init__(self, data, level):
        self.data = data
        self.level = level
        self.children = []

    # toString
    def __repr__(self):
        # %s se sustituye por lo que hay a continuación de %
        return "<Node: %s>" % self.data

    def add_child(self, child):
        self.children.append(child)

    def get_node(self, data):
        if self.data == data:
            return self
        
        # buscar recursivamente en sus hijos
        for child in self.children:
            found = child.get_node(data)
            if found:
                return found
        
        return None

    def print_tree(self, level=1):
        if self is not None:
            print("    |" * level, "Node: ", self.data)

        for child in self.children:
            child.print_tree(level+1)
