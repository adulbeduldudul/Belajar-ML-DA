try:
    angka=int(input("Masukkan angka: "))
    hasil=10/angka
    print(hasil)
except ValueError:
    print("Error: input bukan angka")
except ZeroDivisionError:
    print("Error: gak bisa bagi nol")
