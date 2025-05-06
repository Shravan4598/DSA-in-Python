from common import *

def reverse_LL(head):
    # Base Case
    print_LL(head)
    if( head == None or head.next == None ): # First always head is None
        return head
    
    smallLinkedListHead = reverse_LL(head.next)

    temp = smallLinkedListHead
    while(temp.next is not None):
        temp = temp.next

    temp.next = head
    head.next = None

    return smallLinkedListHead

def reverse_LL_with_tail_returned(head):
    # Base Case

    ## Please complete this code
    print_LL(head)
    if( head == None or head.next == None ): # First always head is None
        tail = head
        return head,tail
    
    smallLinkedListHead,tail = reverse_LL_with_tail_returned(head.next)
    
    pass


def reverse_LL_Better(head):
    # Base Case
    # print_LL(head)
    if( head == None or head.next == None ): # First always head is None
        return head
    
    smallLinkedListHead = reverse_LL_Better(head.next)

    tailOfReversedList = head.next
    tailOfReversedList.next = head
    head.next = None

    return smallLinkedListHead


head = createLLFromList([1,2,3,4,5,6,7,8,9,10])
print_LL(head)
head = reverse_LL_Better(head)
print_LL(head)