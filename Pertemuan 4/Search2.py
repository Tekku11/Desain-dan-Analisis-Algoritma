def BinarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

list1 = [12, 33, 11, 99, 22, 55, 90]
print(BinarySearch(list1, 12))
print(BinarySearch(list1, 91), "\n")

#Latihan Binary Search
list2 = ['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p', 'z'] #Saya menambahkan 1 data di list yaitu'z' agar data tersebut dapat dibagi 2 karena jika tidak, maka data tersebut akan bernilai indeks ganjil yaitu 9 dan akan menjadi false ketika dicari
print("Latihan binary search:\n", list2)
print("Mencari huruf 'a':")
print(BinarySearch(list2, 'a'))