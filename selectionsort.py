def selectionsort(arr):
    length = len(arr)
    for i in range(length-1):
        imin = i
        for j in range(i+1,length):
            if(arr[j] < arr[imin]):
                imin = j
        temp = arr[imin]
        arr[imin] = arr[i]
        arr[i] = temp
        print("iteration ",i,"->",arr)

arr = [2,7,4,1,5,3,2,1]
selectionsort(arr)

print("final",arr)
