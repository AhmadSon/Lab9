from model.daftar_nilai import *
from view.view_nilai import *

print("PROGRAM DATA MAHASISWA")
while True:
    print("\n")
    print("[ (L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar ]")
    pilih = input("Masukkan pilihan: ")
    if pilih.lower() == 't':
        tambah()

    elif pilih.lower() == 'l':
        lihat()

    elif pilih.lower() == 'u':
        ubah()

    elif pilih.lower() == 'h':
        hapus()

    elif pilih.lower() == 'c':
        mencari()

    elif pilih.lower() == 'k':
        break

    else:
        print("pilihan salah")

