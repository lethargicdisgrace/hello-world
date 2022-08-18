def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr


li=[9,5,6,3,5,4,2,5,8,2]    
print(selectionSort(li))