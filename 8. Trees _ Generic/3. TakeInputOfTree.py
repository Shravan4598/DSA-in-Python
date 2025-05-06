from commons import TreeNode,print_tree_detailed

def take_input():
    data = int(input("Enter the data for the Node: "))

    node = TreeNode(data)

    num_children = int(input(f"Enter the number of Children for {data}"))

    for _ in range(num_children):
        child = take_input()
        node.children.append(child)

    
    return node

root = take_input()
print_tree_detailed(root)




