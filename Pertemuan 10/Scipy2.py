# Slide 32
# 1. Impor modul yang diperlukan dari Scipy:

from scipy.optimize import linprog

# 2. Tentukan koefisien fungsi tujuan dan matriks batasan:
# Koefisien fungsi tujuan (Z = 5x1 + 7x2)

c = [-5, -7] # Karena kita ingin "maksimalkan" -5x1 - 7x2, maka perlu diubah menjadi "-5" dan "-7".

# Koefisien matriks batasan
A = [
    [1,0], # 1x1 + 0x2 <= 16
    [2,3], # 2x1 + 3x2 <= 19
    [1,1]  # 1x1 + 1x2 <= 8
]
# Batasan kanan (rhs) dari masing-masing batasan
b = [16, 19, 8]

# 3. Tentukan batasan variabel x1 dan x2 sebagai variabel non-negatif:
x1_bounds = (0, None) # x1 >= 0
x2_bounds = (0, None) # x2 >= 0

# 4. Gunakan linprog untuk menyelesaikan masalah pemrograman linier:
result = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method="highs")

# 5. Tampilkan hasilnya
# Hasil optimasi
print("Optimal Solution:")
print("x1 =", result.x[0])
print("x2 =", result.x[1])
print("Max Z =", -result.fun) # Karena tujuannya adalah memaksimalkan -Z