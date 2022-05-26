def merge_sort(unsorted):
    if len(unsorted) <=1:
        return unsorted
    mid = len(unsorted)//2
    print(mid)
    left = unsorted[:mid]
    right = unsorted[mid:]
    print(left)
    print(right)
    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left,right))

def merge(left,right):
    s = []
    while(len(left)!=0 and len(right)!=0):
        if(left[0]<right[0]):
            s.append(left[0])
            left.remove(left[0])
        else:
            s.append(right[0])
            right.remove(right[0])
    if(len(left)!=0):
        s = s + left
    else:
        s = s + right
    return s
unsorted = [34, 44, 22, 25, 18, 11]
print(merge_sort(unsorted))