# Algoritma Brute Force: Pangkat(Slide 73)
bilangan = int(input('Masukkan bilangan: '))
pangkat = int(input('Masukkan pangkat: '))

def hitung_pangkat(bilangan, pangkat):
    if pangkat > 1:
        bilangan = bilangan * hitung_pangkat(bilangan, pangkat - 1)
    elif pangkat == 0: # Ketentuan jika user menginput pangkat = 0
        bilangan = 1
    return bilangan

hasil = hitung_pangkat(bilangan, pangkat)
print(f'Hasil = {hasil}')