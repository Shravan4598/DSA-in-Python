class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST_Better(node):
    if node is None:
        # Return True for BST, and set min to infinity and max to -infinity for empty nodes
        return True, float('inf'), float('-inf')
    
    # Recursively check the left subtree
    is_left_bst, left_min, left_max = checkBST_Better(node.left)
    
    # Recursively check the right subtree
    is_right_bst, right_min, right_max = checkBST_Better(node.right)
    
    # The current node is a valid BST if:
    # 1. Left subtree is a BST and right subtree is a BST.
    # 2. The current node's value is greater than the maximum value of the left subtree.
    # 3. The current node's value is less than the minimum value of the right subtree.
    if (is_left_bst and is_right_bst and left_max < node.data and node.data < right_min):
        # Return True (it is a BST), the new minimum (from the left or the current node),
        # and the new maximum (from the right or the current node)
        return True, min(left_min, node.data), max(right_max, node.data)
    else:
        # If any condition fails, it's not a BST
        return False, min(left_min, node.data), max(right_max, node.data)
