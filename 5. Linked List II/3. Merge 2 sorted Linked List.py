from common import *

def merge_two_sorted_LL(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    finalHead = None
    finalTail = None

    while head1 is not None and head2 is not None:
        if(head1.data < head2.data):
            if(finalHead == None):
                finalHead = head1
                finalTail = head1
            else:
                finalTail.next = head1
                finalTail = head1
            head1 = head1.next
        else:
            if(finalHead == None):
                finalHead = head2
                finalTail = head2
            else:
                finalTail.next = head2
                finalTail = head2
            head2 = head2.next
    
    if head1 is not None:
        finalTail.next = head1
    
    if head2 is not None:
        finalTail.next = head2
    
    return finalHead


head1 = createLLFromList([2,5,9,10,17])
head2 = createLLFromList([3,6,7])

print_LL(head1)
print_LL(head2)

finalHead = merge_two_sorted_LL(None,None)

print_LL(finalHead)

# https://leetcode.com/problems/merge-two-sorted-lists/description/