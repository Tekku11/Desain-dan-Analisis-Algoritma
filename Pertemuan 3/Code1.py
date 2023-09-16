import datetime

'''
Algoritma:
1. Mengimpor datetime
2. Deklarasi variabel
3. Membuat lists
4. Mendefinisikan suatu variabel pada datetime
5. Cetak data

----------------------------------------------------------------------------------------
Pseudocode:
1. import datetime
2. x <- datetime.datetime.now()
3. variabel <- aList, Mahasiswa, bin _colors
4. print <- aList, Mahasiswa, bin_colors[1], Mahasiswa[1], Mahasiswa[5], Mahasiswa [1:3]
'''


x = datetime.datetime.now() #Fungsi datetime.datetime.now() berfungsi untuk menampilkan tanggal pada komputer user.

aList = ["John", 33, "Toronto", True]
print(aList)
print()

#Data mahasiswa
Mahasiswa = ["Darrell", 2022071075, "Informatika", "Desain dan Analisis Algoritma", x.strftime("%x"), "Universitas Pembangunan Jaya"] 
print(Mahasiswa)
print()

#Warna-warna
bin_colors=["Red", "Green", "Blue", "Yellow"]
print(bin_colors[1])

#Cetak NIM dalam list Mahasiswa
print("NIM\t: {}".format(Mahasiswa[1]))

#Cetak nama universitas dalam list Mahasiswa
print("Nama Institusi\t:",Mahasiswa[5])

#Slicing NIM dan Prodi
print("\nMenampilkan data NIM dan program studi:")
print(Mahasiswa[1:3])