def bubble_sort(arr):
    n = len(arr)

    for passes in range(0,n):
        for j in range(0,n-1-passes):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr


unsorted_list = [120,25,11,34,90,22]
sorted_list = bubble_sort(unsorted_list)
print("Sorted Elements :", sorted_list)