nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

#Cek jika ketentuan nilai valid
if nterms <= 0:
    print("Masukkan bilangan bulat positif")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count = count + 1

#------------------------------------------------------------------------------------------------------------------------
#Fibonacci dengan rekursi
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 100
#Cek apakah nilai nterms valid
if nterms<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
