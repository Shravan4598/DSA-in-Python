# Binary Tree Node

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)


def print_binary_tree(root):
    if(root is None):  # Base Case
        return

    # Format : Node : L->LeftChildData , R->RightChild Data
    print(root.data, end=": ")

    if(root.left is not None):
        print(f"L->{root.left.data}",end = ", ")
    else:
        print("L->None",end=",")

    if(root.right is not None):
        print(f"R->{root.right.data}")
    else:
        print("R->None")
 
    # Recur for the left and right children
    print_binary_tree(root.left)
    print_binary_tree(root.right)

# print_binary_tree(root)

from predefinedBT import predefined_binary_tree_inputs
root1, root2, root3 = predefined_binary_tree_inputs()

print_binary_tree(root1)
