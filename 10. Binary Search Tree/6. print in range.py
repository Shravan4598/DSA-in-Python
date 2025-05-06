from predefinedBSTs import create_predefined_bsts_manual

def print_bst_in_range(root,low,high):
    if(root is None):
        return
    
    if(low < root.data):
        print_bst_in_range(root.left,low,high)

    if(low<=root.data<=high):
        print(root.data,end = ' ')

    if(high > root.data):
        print_bst_in_range(root.right,low,high)


root1, root2, root3 = create_predefined_bsts_manual()
print_bst_in_range(root3,525,150)