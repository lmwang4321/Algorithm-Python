class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Traversal:
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res

r = Node(5)
r.left = Node(4)
r.right = Node(7)
r.left.left = Node(8)
r.left.right = Node(9)

t = Traversal()
print(t.inorderTraversal(r))

