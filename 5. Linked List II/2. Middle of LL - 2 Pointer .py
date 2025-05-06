def middleOfLLUsingSlowAndFast(head):
    if(head is None or head.next is None):
        return head
    
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow=slow.next
        fast = fast.next.next
    
    return slow # When fast reaches end, slow will be at middle

