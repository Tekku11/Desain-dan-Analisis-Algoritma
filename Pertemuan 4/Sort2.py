#list1 = [25,21,22,24,23,27,26]

#Proses penukaran bubble sort
'''
lastElementIndex = len(list1)-1
print(0,list1)
for idx in range(lastElementIndex):
    if list1[idx] > list1[idx+1]:
        list1[idx], list1[idx+1] = list1[idx+1], list1[idx]
    print(idx+1, list1)
print("")
'''

def BubbleSort(list):
    #Exchange the elements to arrange in order
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
    return list

#Masukkan angka dengan urutan lainnya
list1 = [25, 21, 22, 24, 23, 27, 26]
print(BubbleSort(list1))

#Latihan Bubble Sort
list2 = [100, 20, 60, 90, 40, 30]
print("\nLatihan Bubble Sort:")
print(BubbleSort(list2))

