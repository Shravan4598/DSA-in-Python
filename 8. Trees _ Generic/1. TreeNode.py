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
