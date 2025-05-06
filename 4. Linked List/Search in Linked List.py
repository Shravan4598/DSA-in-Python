from common import createLLFromList,print_LL,Node

head = createLLFromList([1,2,3,4,5])

print_LL(head)

def search_by_value(head,value):
    temp = head
    index = 0


    while temp != None :
        if(temp.data == value):
            return index
        temp =temp.next
        index+=1

    return "Not Found"

def search_by_value_recursive(head,value):
    pass

print("Searching ")
print(search_by_value(head,5))


        