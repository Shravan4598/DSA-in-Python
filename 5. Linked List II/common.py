class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data,end="->")
        temp = temp.next

    print()
    return




def take_input_better():
    value = int(input("Enter the value of Node :- "))
    head = None
    tail = None
    
    while(value != -1):
        newNode = Node(value)
        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        
        value = int(input("Enter the value of Node :- "))
    
    return head


def createLLFromList(l1):
    # value = int(input("Enter the value of Node :- "))
    head = None
    tail = None
    for value in l1:
        newNode = Node(value)
        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
            
    return head


def lenthOfLL(head):
    temp = head
    ans = 0

    while(temp!=None):
        temp = temp.next
        ans = ans + 1

    return ans