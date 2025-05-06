class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def size(self):
        return self.len
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self,data):
        newNode = Node(data)
        self.len +=1
        if(self.head is None): # My Queue is Empty
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        return f"Added {data} to the Queue"

    def front(self):
        if(self.isEmpty()):
            print ("Queue is Empty, cannot show Front")
            return

        return self.head.data

    def dequeue(self):
        if(self.isEmpty()):
            print ("Queue is Empty, cannot Dequeue")
            return
        self.len-=1
        dataToBeReturned = self.head.data
        self.head = self.head.next
        if(self.head == None): # Very Very Important to handle the Right Form of Queue 
            self.tail = None
        
        return dataToBeReturned


Q = QueueUsingLinkedList()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
print(Q.size())
print(Q.isEmpty())
print(Q.front())
print(Q.dequeue())
print(Q.dequeue())
print(Q.front())
print(Q.size())

# Visualization for the process
# https://www.cs.usfca.edu/~galles/visualization/QueueLL.html