from predefinedBT import BinaryTreeNode,predefined_binary_tree_inputs,print_level_wise

def construct_tree_from_inorder_and_preorder(inorder,preorder,inS,inE,prS,prE):
    if(inS>inE or prS>prE): # Base Condition
        return None
    
    root_data =  preorder[prS]  # preorder[0] # To avoid using 0
    root = BinaryTreeNode(root_data)

    rootIndexInInorder = -1
    for i in range(inS,inE+1):
        if(inorder[i] == root_data):
            rootIndexInInorder = i
            break
    
    if(rootIndexInInorder==-1):
        print ("Root not found in Inorder,please check logic")
        return None
    
    linS = inS
    linE = rootIndexInInorder -1
    lprS = prS + 1
    lprE =  lprS + (linE - linS) 


    rinE = inE
    rprS = lprE + 1
    rprE = prE
    # rprE - rprS = rinE - rinS
    rinS = rootIndexInInorder +1

    root.left = construct_tree_from_inorder_and_preorder(inorder,preorder,linS,linE,lprS,lprE)
    root.right = construct_tree_from_inorder_and_preorder(inorder,preorder,rinS,rinE,rprS,rprE)

    return root


preorder = [1,2,4,5,3,6]
inorder=  [4, 2, 5, 1, 3, 6]
n = len(inorder)
root = construct_tree_from_inorder_and_preorder(inorder,preorder,0,n-1,0,n-1)
print_level_wise(root)
