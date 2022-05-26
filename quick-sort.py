def quicksort(sequence):

    #length = len(sequence)
    length = len(sequence)
    if(length <= 1):
        return sequence
    else :
        pivot = sequence.pop()
        left = []
        right = []
        for item in sequence:
            if(item > pivot):
                right.append(item)
            else:
                left.append(item)

    return quicksort(left) + [pivot] + quicksort(right)





sequence = [10,20,5,21,12,6,9]
print(quicksort([10,20,5,21,12,6,9]))