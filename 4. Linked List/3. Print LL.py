
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data)
        temp = temp.next
    
    temp = head
    while(temp!=None):
        print(temp.data)
        temp = temp.next

    return


first = Node(1)
second = Node(2)
third = Node(3)

# print(id(first), id(second),id(third))

first.next = second
second.next = third

first.next


head = first

print_LL(head)


#####

# Always avoid accessing any property on None

####
# print(third.next.data) # AttributeError: 'NoneType' object has no attribute 'data'


