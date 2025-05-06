class QueueUsingList:
    def __init__(self):
        self.__queue = []

    def size(self):
        return len(self.__queue)
    
    def isEmpty(self):
        '''if(self.size()==0):
            return True
        else:
            return False
        '''
        return self.size() == 0
    
    def enqueue(self,data):
        self.__queue.append(data)
        return f"We have added {data} to the Queue"
    
    def front(self):
        if(self.size()==0):
            print("Queue is Empty, cannot show Front")
            return None
        return self.__queue[0]
    
    def dequeue(self):
        if(self.size()==0):
            print("Queue is Empty, cannot dequeue")
            return None
        
        '''
        elementToBeDequeue=self.front()
        self.__queue.pop(0)
        return elementToBeDequeue
        '''

        return self.__queue.pop(0)
    
Q = QueueUsingList()

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
