def find_closest(lst, k):
    lst.sort()
    closest_num = lst[0]
    for num in lst:
        if abs(num - k) < abs(closest_num - k):
            closest_num = num
        if num > k:
            break
    return closest_num

lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
k = 9.1
print(find_closest(lst, k))

lst = [2, 5, 5, 7, 8, 8, 9]
k = 6
print(find_closest(lst, k))