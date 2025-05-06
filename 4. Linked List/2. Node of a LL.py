# Create a Node of LL

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


first = Node(1)
second = Node(2)
third = Node(3)

# print(id(first), id(second),id(third))

first.next = second
second.next = third

head = first

print(head.data)
print(head.next.data)
print(head.next.next.data)


