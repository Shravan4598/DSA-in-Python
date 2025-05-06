class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []


root = TreeNode(1)

child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

def print_tree(root):
    if(root==None): # Edge Case
        return
    print(root.data)
    for eachChild in root.children:
        print_tree(eachChild)


print_tree(None)

def print_tree_detailed(root):
    if(root==None): # Edge Case
        return
    
    print(f"{root.data}:",end = "")

    for eachChild in root.children:
        print(eachChild.data,end = ",")

    print()

    for eachChild in root.children:
        print_tree_detailed(eachChild)

print_tree_detailed(root)




root = TreeNode(1)

child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children.append(child1)
child1.children.append(child2)
root.children.append(child3)

print_tree_detailed(root)