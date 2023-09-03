'''Fungsi untuk menukar posisi dua variabel x dan y, dengan kasus :
Disediakan 3 wadah. 2 dari 3 wadah tersebut diisi oleh air dan jus

Algoritma:
1. Menyiapkan fungsi main dan penukaran posisi wadah
2. Deklarasi variabel
3. Cetak posisi awal wadah
4. Mengubah posisi wadah
5. Cetak posisi setelah pertukaran

Pseudocode:
1. def tukar_posisi
2. Variabel = air, jus, kosong
3. air, jus, kosong = tukar_posisi(air, jus, kosong)
'''

def tukar_posisi(air, jus, kosong):
    kosong = air  
    air = jus  
    jus = kosong
    return air, jus, kosong

def main():
    air = "air mineral"
    jus = "jus jeruk"
    kosong = "angin"

    print("Posisi Awal:")
    print("Wadah 1:", air)
    print("Wadah 2:", jus)
    print("Wadah 3:", kosong)
    print("")

    air, jus, kosong = tukar_posisi(air, jus, kosong)

    kosong = "angin"

    print("Posisi Setelah Pertukaran:")
    print("Piring 1:", air)
    print("Piring 2:", jus)
    print("Piring 3:", kosong)

if __name__ == "__main__":
    main()