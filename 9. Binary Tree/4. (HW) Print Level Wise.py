class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


from collections import deque
from predefinedBT import predefined_binary_tree_inputs

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

# Example usage to print the binary tree level-wise
print("Level-Wise Printing of Binary Tree:")
root1,root2,root3 = predefined_binary_tree_inputs()
print_level_wise(root1)
