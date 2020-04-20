class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

class Node:
    def __init__(self):
        self.predecessor = None
        self.d = None

class Graph:
    def __init__(self):
        self.G = []

    def addNodes(self, n):
        self.G.append(n)

    def addEdges(self, e):
        self.