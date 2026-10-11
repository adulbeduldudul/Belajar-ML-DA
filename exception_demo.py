"""
Demo Exception Handling (try-except) - Python
"""

print("=" * 55)
print("0. MASALAH: tanpa try-except, program LANGSUNG CRASH")
print("=" * 55)
# Baris ini bakal bikin program berhenti total (ZeroDivisionError)
# print(10 / 0)   # <- dicomment biar demo bisa lanjut

print()
print("=" * 55)
print("1. STRUKTUR DASAR try-except")
print("=" * 55)
try:
    hasil = 10 / 0
    print("hasil:", hasil)
except:
    print("Waduh, ada error pas bagi nol!")

print("Program tetap jalan walau ada error di atas.\n")

print("=" * 55)
print("2. MENANGKAP ERROR SPESIFIK (bagus & disarankan)")
print("=" * 55)
try:
    angka = int("abc")  # gagal: 'abc' bukan angka
except ValueError:
    print("Gagal! Yang lo masukin bukan angka valid.\n")

print("=" * 55)
print("3. 'as e' -> ambil detail pesan error-nya")
print("=" * 55)
try:
    angka = int("abc")
except ValueError as e:
    print("Pesan asli dari Python:", e, "\n")

print("=" * 55)
print("4. BANYAK except (beda error, beda penanganan)")
print("=" * 55)
data = {"nama": "Budi"}


def akses(dict_data, key):
    try:
        return dict_data[key]
    except KeyError:
        return f"Key '{key}' gak ada di dictionary"
    except TypeError:
        return "Key-nya salah tipe"


print(akses(data, "nama"))   # normal
print(akses(data, "umur"))   # KeyError
print(akses(data, [1, 2]))   # TypeError
print()

print("=" * 55)
print("5. else & finally")
print("=" * 55)
print("- else: jalan KALAU TIDAK ada error")
print("- finally: jalan APAPUN, error atau enggak\n")


def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("  -> Error: gak bisa bagi nol")
        return None
    else:
        print("  -> else: aman, gak ada error")
        return hasil
    finally:
        print("  -> finally: ini SELALU dieksekusi")


print("bagi(10, 2):")
bagi(10, 2)
print("\nbagi(10, 0):")
bagi(10, 0)
print()

print("=" * 55)
print("6. raise -> lempar error sendiri")
print("=" * 55)


def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur gak boleh negatif!")
    return f"Umur {umur} valid"


try:
    print(cek_umur(25))
    print(cek_umur(-5))  # ini bakal lempar ValueError
except ValueError as e:
    print("Ke-catch:", e)
print()

print("=" * 55)
print("7. CONTOH REAL-WORLD: input user yang aman")
print("=" * 55)


def input_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Itu bukan angka, coba lagi!")


print("(fungsi input_angka siap dipakai, loop sampe user masukin angka valid)")

print()
print("=" * 55)
print("8. JANGAN pakai 'except:' kosong (nangkep SEMUA error)")
print("=" * 55)
# KURANG BAIK: nangkep semua termasuk bug logika & Ctrl+C
# try:
#     ...
# except:
#     pass   # <- bahaya, nyembunyiin semua masalah

# BAIK: spesifik
try:
    x = int("xyz")
except ValueError:
    print("Ini bagus, cuma nangkep ValueError doang")

print("\nSelesai! Semua contoh udah valid & kejalan.")
