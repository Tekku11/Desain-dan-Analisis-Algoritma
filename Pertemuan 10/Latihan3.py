import pulp # Soal Cerita 1(Slide 20)

# Membuat objek masalah optimasi
model = pulp.LpProblem(name="Pemecahan_Persamaan", sense=pulp.LpMinimize)

# Membuat variabel x dan y
x = pulp.LpVariable(name="x")
y = pulp.LpVariable(name="y")

# Menambahkan batasan
model += 3 * x + 4 * y == 55
model += x + y == 16

# Menyelesaikan masalah
model.solve()

# Menampilkan hasil
print("Status: ", model.status)
print("Nilai x = ", x.varValue) # Lisa = 9 jam
print("Nilai y = ", y.varValue) # Muri = 6 jam

print("\nJam kerja masing-masing:\nLisa =", x.varValue, "jam")
print("Muri =", y.varValue, "jam")