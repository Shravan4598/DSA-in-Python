
from common import *

headOdd = createLLFromList([1,2,3,4,5])
headEven = createLLFromList([1,2,3,4,5,6])

print_LL(headOdd)
print_LL(headEven)

def middleOfLL(head):
    if(head is None or head.next is None):
        return head
    
    length = lenthOfLL(head)
    middle = length//2

    temp = head
    count = 0

    while(count<middle):
        temp = temp.next
        count+=1
    
    return temp


def middleOfLLUsingSlowAndFast(head):
    if(head is None or head.next is None):
        return head
    
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow=slow.next
        fast = fast.next.next
    
    return slow # When fast reaches end, slow will be at middle


headOddMid = middleOfLLUsingSlowAndFast(headOdd)
headEvenMid = middleOfLLUsingSlowAndFast(headEven)

print(headOddMid.data)
print(headEvenMid.data)