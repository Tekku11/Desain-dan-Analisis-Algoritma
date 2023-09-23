def LinearSearch(list, item):
    index = 0
    found = False

    #Match the value with each data element
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1
    return found

list1 = [12, 33, 11, 99, 22, 55, 90]
print(LinearSearch(list1, 12))
print(LinearSearch(list1, 91), "\n")

#Latihan Linear Search
list2 = ['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p']
print("Latihan linear search:\n", list2)
print("Mencari huruf 'a':")
print(LinearSearch(list2, 'a'))