class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, node=Node):
        self.root = None
        self.node = Node

    def insert(self, val):
        if self.root is None:
            self.root = self.node(val)
        if val < self.root.