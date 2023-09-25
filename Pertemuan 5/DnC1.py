# Hitung Inversi
'''
def countInversion(array):
    result = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                result = result + 1
    return result

arr1 = [21, 70, 36, 14, 25]
print(countInversion(arr1))
'''
#Slide 13
#Hitung inversi dengan divide dan conquer

def countInversion(arr):
    icount = 0
    if len(arr) <= 1:
        return icount
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    icount = icount + countInversion(left)
    icount = icount + countInversion(right)
    i = j = k = 0

    #print(left)
    #print(right)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            #print(Left[i], right[j])
            arr[k] = right[j]
            j = j + 1
            icount = icount + (mid-i)
        k = k + 1

    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1
    return icount
arr = [1, 20, 6, 4, 5]
result = countInversion(arr)
print(result)