'''
Stack Implementation : Using In-Built Python List

'''

class StackUsingList:
    def __init__(self):
        self.__stack =[] # Very Important to make it private so that functionality is right
    
    def push(self,data):
        self.__stack.append(data)
        print(f"Pushed {data} into Stack")

    def size(self):
        return len(self.__stack)
    
    def is_empty(self):
        '''
        if(len(self.stack)==0):
            return True
        else:
            return False
        '''
        return len(self.__stack) == 0
    
    def top(self):
        if(self.is_empty()):
            print("Stack is Empty, No top element")
            return None
        # return self.stack[len(self.stack)-1]
        return self.__stack[-1]
    
    def pop(self):
        if(self.is_empty()):
            print("Stack is Empty, Cannot pop")
            return None
        return self.__stack.pop()
    

myStack = StackUsingList()

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




