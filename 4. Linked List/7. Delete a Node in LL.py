from common import Node,take_input_better,print_LL

head = take_input_better()

def delete_at_head(head):
    if(head is None): # My LL is Empty
        return None
    newHead = head.next
    return newHead


print_LL(head)

def is_tail_node(node):
    if(node==None):
        return True
    if(node.next == None):
        return True
    return False

def delete_at_tail(head):
    if(head is None or head.next is None):
        return None # if the list is empty or has one Node
    
    temp = head
    while(temp.next.next is not None):
        temp=temp.next
    print("Data of Node we have stopped", temp.data)
    temp.next = None
    return head
    

def delete_at_tail_recursive(head):
    if(head is None): # Base Case
        return None
    
    if(head.next is None):
        return None
    
    head.next = delete_at_tail_recursive(head.next)
    return head


def delete_at_index(head,index):
    if(head==None):
        print("LL is Empty")
        return head

    if(index==0):
        return head.next 
    
    temp = head
    count =0

    while(temp is not None and count<index-1):
        temp=temp.next
        count+=1

    if(temp is None or temp.next is None):
        print("Out of Bounds")
        return head
    
    nodeToBeDeleted = temp.next
    nodeAfterDeletedNode = nodeToBeDeleted.next
    
    temp.next = nodeAfterDeletedNode
    return head

def delete_at_index_recursion(head,index):
    if(head is None):
        print("Index is Out of Bounds")
        return None

    if(index ==0):
        return head.next

    head.next = delete_at_index_recursion(head.next,index-1)

    return head

def delete_a_node_by_value(head,value):
    if(head is None):
        print("List Empty")
        return None
    
    if(head.data == value):
        return head.next # Boundary case when head is value
    
    temp = head

    while temp.next is not None and temp.next.data !=value:
        temp = temp.next

    if(temp.next is None):
        print("value not present")
        return head

    nodeToBeDeleted = temp.next
    nodeAfterDeletedNode = nodeToBeDeleted.next
    temp.next = nodeAfterDeletedNode

    return head



head = delete_a_node_by_value(head,3)
print("After Deletion")
print_LL(head)