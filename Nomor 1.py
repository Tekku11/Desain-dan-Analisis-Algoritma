'''
Algoritma:
1. Menyiapkan parameter fungsi
2. Mengisi parameter fungsi dengan fungsi kpk
3. Deklarasi variabel
4. Pencetakan nilai setiap variabel operan dan hasilnya

Pseudocode:
1. fungsi KPK
2. deklarasi
3. x <- 3 
4. y <- 4
5. print variabel x, y dan kpk(x,y)
'''
def kpk(x, y):
    z = x
    while x % y != 0:
        x = x + z
    return x

x = 3
y = 4
z = x
print('KPK dari ', x, 'dan ', y, 'adalah ', kpk(x,y))