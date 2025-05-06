class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_bst(root):
    if root is None:
        return
    print_bst(root.left)
    print(root.data, end=" ")
    print_bst(root.right)

# Function to create predefined binary search trees manually
def create_predefined_bsts_manual():
    # Tree 1: Simple BST, height = 2
    root1 = BinaryTreeNode(10)
    root1.left = BinaryTreeNode(5)
    root1.right = BinaryTreeNode(15)
    # Structure:
    #        10
    #       /  \
    #      5    15
    
    # Tree 2: Slightly complex BST, height = 3
    root2 = BinaryTreeNode(20)
    root2.left = BinaryTreeNode(10)
    root2.right = BinaryTreeNode(30)
    root2.left.left = BinaryTreeNode(5)
    root2.left.right = BinaryTreeNode(15)
    root2.right.left = BinaryTreeNode(25)
    root2.right.right = BinaryTreeNode(35)
    # Structure:
    #        20
    #      /    \
    #    10      30
    #   /  \    /  \
    #  5   15  25  35
    
    # Tree 3: More complex BST, height = 4
    root3 = BinaryTreeNode(40)
    root3.left = BinaryTreeNode(20)
    root3.right = BinaryTreeNode(60)
    
    root3.left.left = BinaryTreeNode(10)
    root3.left.right = BinaryTreeNode(30)
    
    root3.left.left.left = BinaryTreeNode(5)
    root3.left.left.right = BinaryTreeNode(15)
    
    root3.left.right.left = BinaryTreeNode(25)
    root3.left.right.right = BinaryTreeNode(35)
    
    root3.right.left = BinaryTreeNode(50)
    root3.right.right = BinaryTreeNode(70)
    
    root3.right.left.right = BinaryTreeNode(55)
    
    root3.right.right.left = BinaryTreeNode(65)
    root3.right.right.right = BinaryTreeNode(75)
    
    # Structure:
    #         40
    #       /    \
    #     20      60
    #    /  \    /  \
    #  10   30  50  70
    # / \   / \  \  / \
    # 5 15 25 35 55 65 75
    
    return root1, root2, root3

root1, root2, root3 = create_predefined_bsts_manual()

# # Visualizing the trees by printing them in sorted order
# print("BST 1 (Simple, Height = 2):")
# print_bst(root1)  # Output: 5 10 15
# print("\nBST 2 (Height = 3):")
# print_bst(root2)  # Output: 5 10 15 20 25 30 35
# print("\nBST 3 (Complex, Height = 4):")
# print_bst(root3)  # Output: 5 10 15 20 25 30 35 40 50 55 60 65 70 75
