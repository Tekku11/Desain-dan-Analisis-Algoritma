#Inisiasi Set
set_01 = {4,5,6,2}
print(set_01) #Set juga mengurutkan angka dari terkecil hingga terbesar

#inisiasi mengubah list menjadi set
set_02 = set()
set_03 = set([2,1,4,3])
print(type(set_02))
print(set_03)

#Union Set (Penggunaan antara simbol dan kata operator berbeda operasi) | != .union()
set_A = {1,2,3,4}
set_B = {3,4,5,6}
print(set_A|set_B)
print(set_A.union(set_B))
print()

#Intersection Set (& != .intersection())
print(set_A & set_B)
print()

#Difference Set (- != .difference())
print(set_A - set_B)
print(set_B - set_A)
print()

#Symmetric Difference Set (^ != .symmetric_difference())
print(set_A.symmetric_difference(set_B))

#Latihan Union dan Intersection Set
yellow = {'Dandelions', 'Leaves', 'Fire Hydrant'}
red = ('Leaves', 'Fire Hydrant', 'Rose', 'Blood')
print(yellow.union(red))
print(yellow.intersection(red))