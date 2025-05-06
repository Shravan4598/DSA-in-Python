class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to return complex binary trees
def predefined_binary_tree_inputs():
    # Tree 1: Basic Tree with height 3
    root1 = BinaryTreeNode(1)
    root1.left = BinaryTreeNode(2)
    root1.right = BinaryTreeNode(3)
    root1.left.left = BinaryTreeNode(4)
    root1.left.right = BinaryTreeNode(5)
    root1.right.right = BinaryTreeNode(6)
    
    # Tree 2: Slightly complex tree with height 4
    root2 = BinaryTreeNode(10)
    root2.left = BinaryTreeNode(20)
    root2.right = BinaryTreeNode(30)
    root2.left.left = BinaryTreeNode(40)
    root2.left.right = BinaryTreeNode(50)
    root2.right.left = BinaryTreeNode(60)
    root2.right.right = BinaryTreeNode(70)
    root2.left.left.left = BinaryTreeNode(80)
    
    # Tree 3: More complex tree with height 5
    root3 = BinaryTreeNode(100)
    root3.left = BinaryTreeNode(200)
    root3.right = BinaryTreeNode(300)
    root3.left.left = BinaryTreeNode(400)
    root3.left.right = BinaryTreeNode(500)
    root3.right.left = BinaryTreeNode(600)
    root3.right.right = BinaryTreeNode(700)
    root3.left.left.left = BinaryTreeNode(800)
    root3.left.left.right = BinaryTreeNode(900)
    root3.right.right.left = BinaryTreeNode(1000)
    root3.right.right.right = BinaryTreeNode(1100)

    return root1, root2, root3

# Getting predefined binary trees
root1, root2, root3 = predefined_binary_tree_inputs()

# Properties and Visualization
# root1: Contains 6 nodes, Height = 3
# Structure:
#       1
#     /   \
#    2     3
#   / \     \
#  4   5     6
#
# Preorder = 1 2 4 5 3 6 
# Post Order = 4 5 2 6 3 1 
# Inorder Traversal = 4 2 5 1 3 6
# 
# root2: Contains 8 nodes, Height = 4
# Structure:
#       10
#     /    \
#   20      30
#  /  \    /  \
# 40   50 60  70
# /
# 80
#
# root3: Contains 12 nodes, Height = 5
# Structure:
#        100
#      /     \
#    200     300
#   /  \     /  \
# 400  500  600  700
# / \        /  \
# 800 900   1000 1100


class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


from collections import deque

def print_level_wise(root):
    if root is None:
        return
    
    queue = deque([root])  # Initialize the queue with the root node
    
    while queue:
        current_node = queue.popleft()  # Dequeue the front node
        print(f"{current_node.data}: ", end=" ")
        
        if current_node.left:
            print(f"L->{current_node.left.data}", end=", ")
            queue.append(current_node.left)  # Enqueue the left child
        else:
            print("L->None", end=", ")
        
        if current_node.right:
            print(f"R->{current_node.right.data}")
            queue.append(current_node.right)  # Enqueue the right child
        else:
            print("R->None")

# # Example usage to print the binary tree level-wise
# print("Level-Wise Printing of Binary Tree:")
# root1,root2,root3 = predefined_binary_tree_inputs()
# print_level_wise(root1)
