import pandas as pd

df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]
    ])
df.columns = ['id', 'name', 'age', 'decision']

#Latihan Data Frame
data = {'No': [1,2,3],
    'Prodi': ['Informatika', 'Sistem Informasi', 'Teknik Sipil'],
    'Mahasiswa': [50,55,40],
    'Laki-Laki': [30,30,30],
    'Perempuan': [20,25,10]}

df = pd.DataFrame(data, index=[' ',' ',' '])
df.head()
