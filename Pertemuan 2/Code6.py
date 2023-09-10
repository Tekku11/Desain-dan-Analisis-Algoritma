'''
Algoritma:
1. Membuat fungsi untuk memanggil array dalam suatu variabel pada indeks pertama, kedua dan terakhir.
2. Deklarasi variabel.
3. Cetak data array pertama, kedua dan terakhir.

Pseudocode:
1. def getFirst, getSecond, dan get Last
2. return f[0], return f[1], dan return[panjang indeks(f)-1]
3. [3, 7, 6, 5, 11] <- f
4. getFirst, getSecond, dan get Last <- print

'''

def getFirst(f):
    return f[0]

def getSecond(f):
    return f[1]

def getLast(f):
    return f[len(f)-1]

f = [3,7,6,5,11]

print("Array pertama:\n", getFirst(f))
print("Array kedua:\n", getSecond(f))
print("Array terakhir:\n", getLast(f))

