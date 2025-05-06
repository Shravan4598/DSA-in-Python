class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

def print_tree(root):
    if(root==None): # Edge Case
        return
    print(root.data)
    for eachChild in root.children:
        print_tree(eachChild)


def print_tree_detailed(root):
    if(root==None): # Edge Case
        return
    
    print(f"{root.data}:",end = "")

    for eachChild in root.children:
        print(eachChild.data,end = ",")

    print()

    for eachChild in root.children:
        print_tree_detailed(eachChild)