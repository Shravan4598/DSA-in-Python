from genericTreesInput import predefined_generic_tree_inputs

# Properties (Examples)
# root1: Contains 5 nodes, Height = 3
# Structure: 
#       1
#     /   \
#    2     3
#   / \
#  4   5
#
# root2: Contains 6 nodes, Height = 3
# Structure:
#       10
#    /   |   \
#  20    30   40
#        / \
#      50   60
#
# root3: Contains 5 nodes, Height = 3
# Structure:
#       100
#      /   \
#    200   300
#   / \
# 400 500


def preorder_traversal(root):
    if(root is None): # Edge Case
        return

    print(root.data,end=" ")
    for eachChild in root.children:
        preorder_traversal(eachChild)


def postOrder_traversal(root):
    if(root is None): # Edge Case
        return
    
    for eachChild in root.children:
        postOrder_traversal(eachChild)
    
    print(root.data,end=" ")

root1, root2, root3 = predefined_generic_tree_inputs()
print ("Preorder Traversal:")
preorder_traversal(root1)


print ("PostOrder Traversal:")
postOrder_traversal(root1)