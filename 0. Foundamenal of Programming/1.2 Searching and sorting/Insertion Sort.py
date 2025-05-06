

def insertion_sort(arr):
    n = len(arr)

    for current in range(1,n):
        currentCard = arr[current]
        correctPosition = current-1 # It will go from i-1 to 0
        while correctPosition >=0:
            if(arr[correctPosition] < currentCard):
                break
            else:
                arr[correctPosition +1 ] = arr[correctPosition]
                correctPosition-=1
            arr[correctPosition + 1] = currentCard

    return arr


unsorted_list = [12,25,11,34,90,22]
sorted_list = insertion_sort(unsorted_list)
print("Sorted Elements :", sorted_list)