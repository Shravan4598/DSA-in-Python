class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class StackUsingLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        newNode = Node(data)
        self.size+=1 # Very Important to maintain Size
        if(self.head==None):
            self.head=newNode
            return f"Added {data} to the stack"
        
        newNode.next = self.head
        self.head = newNode
        return f"Added {data} to the stack"

    def top(self):
        if(self.head is None or self.size == 0):
            return "Stack is Empty, no Top element"

        return self.head.data
    
    def pop(self):
        if(self.head is None or self.size == 0):
            return "Stack is Empty, Cannot Pop element"
    
        dataAtTop = self.head.data
        self.head = self.head.next
        self.size -=1
        return dataAtTop
    
    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size ==0

myStack = StackUsingLinkedList()

print(myStack.is_empty())
print(myStack.push(10))
print(myStack.push(20))
print(myStack.push(30))
print(myStack.push(40))
print(myStack.is_empty())
print(myStack.pop())
print(myStack.pop())
print(myStack.size())
print(myStack.top())