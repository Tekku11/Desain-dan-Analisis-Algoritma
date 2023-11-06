import pulp # Soal Cerita 1(Slide 20)

# Membuat objek masalah optimasi
model = pulp.LpProblem(name="Pemecahan_Persamaan", sense=pulp.LpMinimize)

# Membuat variabel x dan y
x = pulp.LpVariable(name="x")
y = pulp.LpVariable(name="y")

# Menambahkan batasan
model += 3 * x + 4 * y == 11000
model += 1 * x + 7 * y == 15000

# Menyelesaikan masalah
model.solve()

# x.varValue += 500

# Menampilkan hasil
print("Status: ", model.status)
print("Nilai x = ", x.varValue)
print("Nilai y = ", y.varValue)