import datetime

'''
Algoritma:
1. Deklarasi variabel
2. Perulangan indeks dalam variabel
3. Cetak variabel dalam perulangan
'''

x = datetime.datetime.now() #Fungsi datetime.datetime.now() berfungsi untuk menampilkan tanggal pada komputer user.

Mahasiswa = ["Darrell", "2022071075", "Informatika", "Desain dan Analisis Algoritma", x.strftime("%x"), "Universitas Pembangunan Jaya"] #Tipe data harus sama agar dapat dioperasikan
#plus = "UPJ"
for index in Mahasiswa:
    print("UPJ " + index)