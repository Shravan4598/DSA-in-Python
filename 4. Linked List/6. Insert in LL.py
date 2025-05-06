from common import Node,take_input_better,print_LL

head = take_input_better()

print_LL(head)

def insert_at_head(head,data): # O(1)
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head


# head = insert_at_head(head,100)
# print("After Inserting at Head")
# print_LL(head)

def insert_at_tail(head,data):
    newNode = Node(data)
    if(head is None):
        return newNode # If the list is empty,then newNode becomes the head
    
    temp = head
    while(temp.next != None):
        temp = temp.next

    temp.next = newNode

    return head

def insert_at_tail_recursively(head,data):
    if(head is None): # base
      newNode = Node(data)
      return newNode
      
    head.next = insert_at_tail_recursively(head.next,data)

    return head





def insert_at_index(head,data,index):
    if(index ==0):
        return insert_at_head(head,data)
    
    newNode = Node(data)
    temp = head
    count = 0

    while temp is not None and count < index - 1:
        temp = temp.next
        count+=1

    if(temp is None):
        print("Index out of bounds, please check index")
        return head
    
    newNode.next = temp.next
    temp.next = newNode
    return head


def insert_at_index_recursively(head,data,index):
    if(index ==0):
        return insert_at_head(head,data)
    if(head == None):
        print("Index is out of bounds")
        return head
    
    head.next = insert_at_index_recursively(head.next,data,index-1)

    return head

head = insert_at_index_recursively(head,35,3)
print("After Inserting at Index")
print_LL(head)


    

    







