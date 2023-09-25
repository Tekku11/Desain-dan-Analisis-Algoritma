# Function to find the partition position
def partition(array, low, high):
        
        # Choose the rightmost element as pivot
        pivot = array[high]

        # Pointer for greater element
        i = low - 1

        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                  
                  # If element smaller than pivot is found
                  # Swap it with the greater element pointed by i
                  i = i + 1

                  # Swapping element at i with element at j
                  (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        #Return the position from where partition is done
        return i + 1

# Function to perform quicksort
def quickSort(array, low, high):
      if low < high:
            
            # Find pivot element such that
            # element smaller than pivot on the left
            # element greater than pivot on the right
            pi = partition(array, low, high)

            # Recursive call on the left of pivot
            quickSort(array, low, pi - 1)

            # Recursive call on the right of pivot
            quickSort(array, pi + 1, high)

data = [4, 12, 23, 9, 21, 1, 35, 2, 24]
print("Unsorted Array:")
print(data,"\n")

size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)