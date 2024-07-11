class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Inorder Traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Preorder Traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

# Postorder Traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

# Create a binary tree with three levels
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

print("Inorder traversal:")
inorder(root)  # Output: 4 2 5 1 6 3 7
print("\nPreorder traversal:")
preorder(root)  # Output: 1 2 4 5 3 6 7
print("\nPostorder traversal:")
postorder(root)  # Output: 4 5 2 6 7 3 1
