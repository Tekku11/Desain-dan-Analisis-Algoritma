import pulp # Soal Cerita 1(Slide 20)

# Membuat objek masalah optimasi
model = pulp.LpProblem(name="Pemecahan_Persamaan", sense=pulp.LpMinimize)

# Membuat variabel x dan y
x = pulp.LpVariable(name="x")
y = pulp.LpVariable(name="y")

# Menambahkan batasan
model += 2 * x + 2 * y == 44    # Rumus keliling persegi panjang
model += x - y == 6             # Ketentuan lebar lebih pendek 6 cm dari panjangnya

# Menyelesaikan masalah
model.solve()

# Menampilkan hasil
print("Status: ", model.status)
print("Nilai x = ", x.varValue)
print("Nilai y = ", y.varValue)