'''
Search and Insertion:

Binary Search Tree is a node based binary tree data structure
which has the following properties:
- The left subtree of a node contains only nodes with keys
lesser than the node's key.
- The right subtree of a node contains only nodes with keys
greater than the node's key
- The left and right subtree each must also be a binary search
tree. There must be no duplicate nodes.
'''
import pprint

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def search(root, key):
    '''
    Searching a key
    To search a given key in BST, we first compare it with root, if
    the key is present at root, we return root. If key is greater
    than root's key, we recur for right subtree of root node. Otherwise
    we recur for left subtree
    '''
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


def insert(root, node):
    '''
    Insertion of a key
    A new key is always inserted at leaf. We start searching a key
    from root till we hit a leaf node. Once a leaf node is found,
    the new node is added as a child of the leaf node.
    '''
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
    return root

def inorder(root):

    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def minValueNode(node):
    '''
    Given a non-empty binary search tree, return the node with minimum
    key value found in that tree. Note that the entire tree does not need
    to be searched.
    '''
    current = node
    while (current.left is not None):
        current = current.left
    return current


def deleteNode(root, key):
    '''
    given a binary search tree and a key, this function delete the key
    and returns the new root.
    '''

    #Base Case
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's key
    # then it lies in left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)
    # If the key to be delete is greater than the root's key
    # then it lies in right subtree
    elif(key > root.val):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root

root = Node(15)
root = insert(root, Node(37))
root = insert(root, Node(17))
root = insert(root, Node(40))
root = insert(root, Node(12))
root = insert(root, Node(13))
root = insert(root, Node(10))
root = insert(root, Node(8))
root = insert(root, Node(14))
root = insert(root, Node(11))
ro
res = deleteNode(root, 8)
a = 1