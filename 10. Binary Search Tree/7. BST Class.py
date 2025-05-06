def print_binary_tree(node):
    if node is None:
        return
    
    # Format: Node: L->LeftChild, R->RightChild
    print(f"{node.data}:", end=" ")
    
    if node.left:
        print(f"L->{node.left.data}", end=", ")
    else:
        print("L->None", end=", ")
    
    if node.right:
        print(f"R->{node.right.data}")
    else:
        print("R->None")
    
    # Recur for the left and right children
    print_binary_tree(node.left)
    print_binary_tree(node.right)

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.insert_helper(data,self.root)

    def insert_helper(self,data,node):
        if(node==None):
            newNode = BSTNode(data)
            return newNode
        
        if(data <  node.data):
            node.left = self.insert_helper(data,node.left)
        else:
            node.right = self.insert_helper(data,node.right)

        return node           

    def get_min_node(self,node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def delete_helper(self,data,root):
        if(root is None):
            return None
        
        if(data<root.data):
            root.left = self.delete_helper(data,root.left)
        elif(data>root.data):
            root.right = self.delete_helper(data,root.right)
        else:
            if(root.left is None):
                return root.right
            elif root.right is None:
                return root.left
            
            min_larger_node = self.get_min_node(root.right)
            root.data = min_larger_node.data

            root.right=self.delete_helper(min_larger_node.data,root.right)

        return root



    def delete(self,data):
        self.root = self.delete_helper(data,self.root)


    def search(self,data):
        return self.searchHelper(data,self.root)

    def searchHelper(self,data,root):
        if(root is None):
            return False
        if(root.data == data):
            return True
        
        if(data < root.data):
            return self.searchHelper(data,root.left)
        else:
            return self.searchHelper(data,root.right)



bstObject = BST()

bstObject.insert(20)
bstObject.insert(25)
bstObject.insert(10)
bstObject.insert(15)
print(bstObject.search(17))
bstObject.delete(20)
print_binary_tree(bstObject.root)
