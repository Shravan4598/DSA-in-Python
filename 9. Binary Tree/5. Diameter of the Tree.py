
from predefinedBT import predefined_binary_tree_inputs

def height(root):
    if(root is None):
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    heightOfTree = 1 + max(left_height,right_height)

    return heightOfTree

def diameter_of_a_tree(root):
    if(root is None):
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    left_diameter = diameter_of_a_tree(root.left)
    right_diameter = diameter_of_a_tree(root.right)

    ans = max(left_diameter,right_diameter,leftHeight+rightHeight)

    return ans


def diameter_of_tree_optimized(root):
    if(root is None):
        return 0,0 # height, diameter

    left_height,left_diameter = diameter_of_tree_optimized(root.left)
    right_height,right_diamter = diameter_of_tree_optimized(root.right)

    diameter_through_root = left_height+right_height # Option 1
    # left_diamter - Option 2
    # right_diamter - option 3

    ans_diameter = max(diameter_through_root,left_diameter,right_diamter)

    current_tree_height = 1 + max(left_height,right_height)

    return current_tree_height,ans_diameter

root1, root2, root3 = predefined_binary_tree_inputs()

treeHeight,treeDiameter = diameter_of_tree_optimized(root1)
print(treeHeight,treeDiameter)