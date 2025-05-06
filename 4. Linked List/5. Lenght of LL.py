from common import Node,take_input_better,print_LL

def lenthOfLL(head):
    temp = head
    ans = 0

    while(temp!=None):
        temp = temp.next
        ans = ans + 1

    return ans


headOfLL = take_input_better()

length = lenthOfLL(headOfLL)
print(length)


def lengthOfLinkedListRecursive(head):
    if(head==None): # Base Case
        return 0
    
    recursionAnswer = lengthOfLinkedListRecursive(head.next)

    return 1 + recursionAnswer

length = lengthOfLinkedListRecursive(headOfLL)
print(length)