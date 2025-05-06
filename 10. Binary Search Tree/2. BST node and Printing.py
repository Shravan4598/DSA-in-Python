from predefinedBSTs import create_predefined_bsts_manual

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_bst(root):
    if(root is None):
        return
    print_bst(root.left)
    print(root.data,end = " ") # Inorder Traversal of my BST
    print_bst(root.right)

root1, root2, root3 = create_predefined_bsts_manual()


def print_binary_tree(node):
    if node is None:
        return
    
    # Format: Node: L->LeftChild, R->RightChild
    print(f"{node.data}:", end=" ")
    
    if node.left:
        print(f"L->{node.left.data}", end=", ")
    else:
        print("L->None", end=", ")
    
    if node.right:
        print(f"R->{node.right.data}")
    else:
        print("R->None")
    
    # Recur for the left and right children
    print_binary_tree(node.left)
    print_binary_tree(node.right)

# Example usage to print the tree
print("Binary Tree Structure:")


print_binary_tree(root2)
