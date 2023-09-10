'''
A. Algoritma Penjumlahan Berulang:
1. Deklarasi sum = 0
2. Fungsi untuk penjumlahan
3. Cetak hasil penjumlahan

B. Pseudocode Penjumlahan Berulang:
1. 0 <- sum
2. for -> in -> : -> sum = sum + item -> return sum
3. print jumlah(([]))

---------------------------------------------------------------------------

A. Algoritma Perkalian Berulang:
1. Deklarasi sum = 1        (sum = 1 untuk nilai awal pada proses perkalian. Jika sum = 0 maka hasil perkalian akan menjadi 0)
2. Fungsi untuk perkalian
3. Cetak hasil perkalian

B. Pseudocode Perkalian Berulang:
1. 1 <- sum
2. for -> in -> : -> sum = sum * item -> return sum
3. print jumlah(([]))

---------------------------------------------------------------------------

A. Algoritma Pembagian Berulang:
1. Deklarasi sum = 1        (sum = 1 untuk nilai awal pada proses pembagian. Jika sum = 0 maka hasil pembagian tidak dapat ditemukan)
2. Fungsi untuk pembagian
3. Cetak hasil pembagian

B. Pseudocode Pembagian Berulang:
1. 1 <- sum
2. for -> in -> : -> sum = sum / item -> return sum
3. print jumlah(([]))

--------------------------------------------------------------------------------
'''

#Penjumlahan berulang
def jumlah(tambah):
    sum=0
    for item in tambah:
        sum = sum + item
    return sum

print(jumlah([1,2,3,5,7,1,3]))

#Perkalian berulang
def jumlah(tambah):
    sum=1
    for item in tambah:
        sum = sum * item
    return sum

print(jumlah([5,15,20]))


#Pembagian berulang
def jumlah(tambah):
    sum=1
    for item in tambah:
        sum = sum / item
    return sum

print(jumlah([3,2,4,5]))