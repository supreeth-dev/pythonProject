def sort(numbers):
    for i in range(len(numbers)-1,0,-1):
    #for i in range( len(numbers) - 1):
        for j in range(i):
            if numbers[j]>numbers[j+1]:
               temp = numbers[j]
               numbers[j] = numbers[j+1]
               numbers[j+1] = temp
numbers = [6, 3, 7, 5, 8, 2]
sort(numbers)
print(numbers)