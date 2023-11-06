import pulp # Soal Latihan 2 (Slide 33)

# Membuat objek masalah optimasi
model = pulp.LpProblem(name="Pemecahan_Persamaan", sense=pulp.LpMinimize)

# Membuat variabel x dan y
x = pulp.LpVariable(name="x")
y = pulp.LpVariable(name="y")

# Menambahkan batasan
model += 2 * x + y == 21

# Menyelesaikan masalah
model.solve()

# Menampilkan hasil
print("Status: ", model.status)
print("Nilai x = ", x.varValue)
print("Nilai y = ", y.varValue)