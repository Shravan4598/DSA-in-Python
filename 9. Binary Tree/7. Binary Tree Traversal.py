from predefinedBT import predefined_binary_tree_inputs

root1, root2, root3 = predefined_binary_tree_inputs()


def preorder_traversal(root):
    if(root is None):
        return
    
    print(root.data,end =" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if(root is None):
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data,end =" ")

def inorder_traversal(root):
    if(root is None):
        return
    inorder_traversal(root.left)
    print(root.data,end = " ")
    inorder_traversal(root.right)

inorder_traversal(root1)