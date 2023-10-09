def faktorial(n):
    if(n == 1):
        return n
    return faktorial(n-1) * n

n = int(input("Masukkan nilai n: ")) #input nilai
print(f"Hasil dari {n}! = ", faktorial(n)) #output nilai
