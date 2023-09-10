'''
Algoritma:
1. Membuat fungsi penentu true atau false.
2. Deklarasi variabel.
3. Membuat perulangan pada fungsi.
4. Cetak hasil binary.

Pseudocode:
1. def searchBinary():
2. 0 <- first
3. len(list) - 1 <- last
4. foundFlag <- False
5. mid = (first + last) // 2
6. if list[mid] == item: -> foundFlag = True
7. return foundFlag
8. True/False <- print

'''
def searchBinary(list,item):
    first = 0
    last = len(list) - 1
    foundFlag = False
    while (first <= last and not foundFlag):
        mid = (first + last) //2
        if list[mid] == item :
            foundFlag = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag

#Pernyataan True
print("Search Binary=", searchBinary([8,9,10,100,1000,2000,3000], 10))
#Pernyataan False
print("Search Binary=", searchBinary([8,9,10,100,1000,2000,3000], 5))