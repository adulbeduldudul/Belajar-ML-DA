"""
Demo konversi nilai: for-loop if/elif/else  ->  List Comprehension
"""

b = [10, 80, 95, 70]

print("=" * 55)
print("VERSI 1: For loop biasa (kode asli)")
print("=" * 55)
n_loop = []
for x in b:
    if x >= 90:
        c = "A"
    elif x > 75:
        c = "B"
    else:
        c = "C"
    n_loop.append((x, c))
print(n_loop)

print()
print("=" * 55)
print("VERSI 2: List Comprehension (nested ternary)")
print("=" * 55)
# elif di LC -> dirantai pakai 'else'
# if c1: A  elif c2: B  else: C
#  ->  "A" if c1 else ("B" if c2 else "C")
n_lc = [(x, "A" if x >= 90 else "B" if x > 75 else "C") for x in b]
print(n_lc)

print()
print("Hasil identik? ->", n_loop == n_lc)

print()
print("=" * 55)
print("VERSI 3: BEST PRACTICE - function helper + LC")
print("=" * 55)
def konversi_nilai(x):
    if x >= 90:
        return "A"
    elif x > 75:
        return "B"
    return "C"

n_helper = [(x, konversi_nilai(x)) for x in b]
print(n_helper)
print("Hasil identik? ->", n_loop == n_helper)
