def SelectionSort(list):
    for i in range(len(list) - 1, 0, -1):
        max_idx = 0
        for location in range(1, i + 1):
            if list[location] > list[max_idx]:
                max_idx = location
        list[i], list[max_idx] = list[max_idx], list[i]
    return list


list = [70, 15, 25, 19, 34, 44]
print(list)
SelectionSort(list)
print("Setelah selection sort:")
print(list)

#Latihan Selection Sort
list2 = [89, 12, 57, 16, 25]
print("Latihan selection sort:\n", list2)

SelectionSort(list2)
print("Setelah selection sort:\n", list2)