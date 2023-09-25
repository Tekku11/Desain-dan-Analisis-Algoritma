def DnC_Max(arr, index, len):
    maximum = -1

    if(index >= len - 2):
        if(arr[index] > arr[index + 1]):
            return arr[index]
        else:
            return arr[index + 1]
        
    maximum = DnC_Max(arr, index + 1, len)

    if(arr[index] > maximum):
        return arr[index]
    else:
        return maximum

def DnC_Min(arr, idx, len):
    minimum = 0
    if(idx >= len - 2):
        if(arr[idx] < arr[idx + 1]):
            return arr[idx]
        else:
            return arr[idx + 1]
        
    minimum = DnC_Min(arr, idx + 1, len)

    if(arr[idx] < minimum):
        return arr[idx]
    else:
        return minimum
    
if __name__ == '__main__':

    minimum, maximum = 0, -1

    # Array initialization
    arr = [4, 12, 23, 9, 21, 1, 35, 2, 24]

    maximum = DnC_Max(arr, 0, 9)
    minimum = DnC_Min(arr, 0, 9)

    print("The minimum number in the array is: ", minimum)
    print("The minimum number in the array is: ", maximum)
