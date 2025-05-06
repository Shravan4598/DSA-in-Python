from commons import TreeNode,print_tree_detailed
from collections import deque

def take_input_level_wise():
    data = int(input("Enter the root data: "))
    root = TreeNode(data)

    queue = deque([root])

    while (len(queue)) != 0 :
        current_node = queue.popleft()

        num_children = int(input("Enter the number of Children for " + str(current_node.data)))

        for i in range(num_children):
            child_data = int(input(f"Enter the data for  child {i+1} of Node {current_node.data} : "))
            child_node = TreeNode(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)
    
    return root

root = take_input_level_wise()
print_tree_detailed(root)

