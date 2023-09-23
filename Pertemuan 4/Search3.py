def interpolationS(list, x):
    index0 = 0
    indexn = len(list) - 1
    found = False
    while index0 <= indexn and x >= list[index0] and x <= list[indexn]:
        
        #Find the mid point
        mid = index0 + int(((float(indexn - index0) / (list[indexn] - list[index0])) * (x - list[index0])))

        #Compare the value at mid point with search value
        if list[mid] == x:
            found = True
            return found
        
        if list[mid] < x:
            index0 = mid + 1
    return found

list1 = [12, 33, 11, 99, 22, 55, 90]
print(interpolationS(list1, 12))
print(interpolationS(list1, 91), "\n")


#Latihan Interpolation Search
list2 = ['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p']
print("Latihan interpolation search:\n", list2)
print("Mencari huruf 'u':")
print(interpolationS(list2, 'u'))
#Hasil pencarian 'u' = false, saya belum mendapatkan solusinya.