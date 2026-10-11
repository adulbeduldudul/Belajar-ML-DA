"""
Demo List Comprehension di Python
"""

print("=" * 60)
print("1. FORMAT DASAR")
print("=" * 60)
# Syntax: [ekspresi for item in iterable if kondisi]
# Looping biasa
angka = [1, 2, 3, 4, 5]
kuadrat_loop = []
for x in angka:
    kuadrat_loop.append(x ** 2)

# Pakai List Comprehension (1 baris, lebih cepat & pythonic)
kuadrat_lc = [x ** 2 for x in angka]

print("Angka        :", angka)
print("Kuadrat loop :", kuadrat_loop)
print("Kuadrat LC   :", kuadrat_lc)

print()
print("=" * 60)
print("2. DENGAN KONDISI (FILTER)")
print("=" * 60)
# Ambil hanya angka genap
genap = [x for x in angka if x % 2 == 0]
print("Angka genap  :", genap)

# Ambil hanya yang ganjil sekaligus dikuadratkan
ganjil_kuadrat = [x ** 2 for x in angka if x % 2 != 0]
print("Ganjil^2     :", ganjil_kuadrat)

print()
print("=" * 60)
print("3. IF-ELSE (TRANSFORMASI NILAI)")
print("=" * 60)
# Kalau genap -> 'genap', kalau ganjil -> 'ganjil'
label = ["genap" if x % 2 == 0 else "ganjil" for x in angka]
print("Label        :", label)

# Note: posisi if-else BERBEDA dengan filter (if doang)
# Filter:  [x for x in data if kondisi]
# If-else: [nilai_a if kondisi else nilai_b for x in data]

print()
print("=" * 60)
print("4. STRING MANIPULATION")
print("=" * 60)
nama = ["budi", "siti", "agus", "dewi"]
nama_kapital = [n.title() for n in nama]
print("Asli         :", nama)
print("Title case   :", nama_kapital)

# Ambil huruf vokal dari sebuah kata
kata = "list comprehension"
vokal = [huruf for huruf in kata if huruf in "aiueo "]
print("Vokal+spasi  :", vokal)

# Panjang setiap nama
panjang = [len(n) for n in nama]
print("Panjang nama :", panjang)

print()
print("=" * 60)
print("5. NESTED LIST (2 DIMENSI)")
print("=" * 60)
# Flatten: gabungin list 2D jadi 1D
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [num for row in matrix for num in row]
print("Matrix 2D    :", matrix)
print("Flatten 1D   :", flatten)

# Bikin tabel perkalian
perkalian = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Tabel kali   :", perkalian)

print()
print("=" * 60)
print("6. CONTOH REAL-WORLD")
print("=" * 60)
# a. Ambil data dari list of dict
siswa = [
    {"nama": "Budi", "nilai": 85},
    {"nama": "Siti", "nilai": 92},
    {"nama": "Agus", "nilai": 78},
    {"nama": "Dewi", "nilai": 88},
]

siswa_lulus = [s["nama"] for s in siswa if s["nilai"] >= 80]
print("Siswa lulus  :", siswa_lulus)

# b. Normalisasi teks (lowercase + hapus spasi)
raw_data = ["  Hello ", " WORLD", "Python ", "  ROCKS"]
bersih = [t.strip().lower() for t in raw_data]
print("Data bersih  :", bersih)

# c. Konversi tipe data
str_angka = ["10", "20", "30", "40"]
int_angka = [int(x) for x in str_angka]
print("List int     :", int_angka, "(total:", sum(int_angka), ")")

# d. Cari file dengan ekstensi tertentu
files = ["data.csv", "script.py", "image.png", "notes.txt", "app.py"]
py_files = [f for f in files if f.endswith(".py")]
print("File .py     :", py_files)

print()
print("=" * 60)
print("7. BUKAN LIST COMPREHENSION (Set & Dict)")
print("=" * 60)
# Set comprehension -> { }
unik = {x % 3 for x in range(10)}
print("Set sisa bagi 3:", unik)

# Dict comprehension -> {key: value}
kuadrat_dict = {x: x ** 2 for x in range(1, 6)}
print("Dict kuadrat :", kuadrat_dict)

print()
print("=" * 60)
print("8. KAPAN JANGAN PAKAI LIST COMPREHENSION?")
print("=" * 60)
# Kalau logicnya kompleks/banyak kondisi, bacaannya jadi susah
# Misal INI KURANG BAGUS (terlalu dalam):
# hasil = [f(x) for x in data if c1(x) if c2(x) for y in x if c3(y)]
# -> mending pakai for loop biasa biar kebaca orang lain

print("Selesai! Semua contoh di atas udah kejalan & valid.")
