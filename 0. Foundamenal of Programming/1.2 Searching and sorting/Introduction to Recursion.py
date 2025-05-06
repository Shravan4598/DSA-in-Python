'''
def printFive(n):
    print(n)
    printFour(4)

def printFour(n):
    print(n)
    printThree(3)

def printThree(n):
    print(n)
    printTwo(2)

def printTwo(n):
    print(n)
    printOne(1)

def printOne(n):
    print(n)
'''

def printNum(n):
    print(n)
    if(n==1):
        return
    printNum(n-1)

printNum(5)



# We have to print from 5 to 1, but we can not change anything
#  in above code, just can define more function with same 
# structure as printFive