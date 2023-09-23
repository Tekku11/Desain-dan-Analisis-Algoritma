def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        next = list[i]
#Compare the current element with next one

        while(list[j] > next) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = next
    return list

#Masukka angka dengan urutan lainnya
list = [35, 31, 32, 34, 33, 37, 36]
print(list)
InsertionSort(list)
print("Setelah insertion sort:")
print(list)

#Latihan Insertion Sort
list2 = [89, 12, 57, 16, 25, 11, 75]
print("\nLatihan insertion sort:\n", list2)
InsertionSort(list2)
print("Setelah insertion sort:\n", list2)
