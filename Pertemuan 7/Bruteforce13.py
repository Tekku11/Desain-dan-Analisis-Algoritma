# Algoritma Brute Force: Faktorial(Slide 74)
n = int(input('Masukkan nilai n: '))

def hitung_faktorial(n):
    if n>=2:
        n = n * hitung_faktorial(n-1)
    elif n == 0: # Ketentuan jika 0!
        n = 1
    return n

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')