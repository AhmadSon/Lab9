from view.input_nilai import *

mahasiswa = {}

# Menambahkan data mahasiswa
def tambah():
    global mahasiswa
    ulangi = "y" or "Y"
    while ulangi == "y" or "Y":
        nim = input_nim()
        nama = input_nama()
        tugas = input_tugas()
        uts = input_uts()
        uas = input_uas()
        akhir = input_akhir()
        mahasiswa[nim] = [nim, nama, tugas, uts, uas, akhir]
        ulangi = (input("Ingin Menambah Data ? (y/t): "))
        if ulangi == "t" or "T":
            return mahasiswa

# Mengubah Data Mahasiswa
def ubah():
    nim = input("Masukkan NIM untuk mengubah: ")
    if nim in mahasiswa.keys():
        print("="*68)
        print("Mengubah data {}.".format(nim))
        print("="*68)
        mahasiswa[nim][1] = input("Masukan Nama yang benar: ")
        mahasiswa[nim][2] = int(input("Masukan Nilai Tugas yang benar: "))
        mahasiswa[nim][3] = int(input("Masukan Nilai UTS yang benar: "))
        mahasiswa[nim][4] = int(input("Masukan Nilai UAS yang benar: "))
        mahasiswa[nim][5] = mahasiswa[nim][2] *.3 + mahasiswa[nim][3] *.35 + mahasiswa[nim][4] *.35
    else:
        print("'{}' Tidak ditemukan.".format(nim))

# Menghapus Data Mahasiswa
def hapus():
    nim = input("Masukan NIM untuk menghapus data: ")
    if nim in mahasiswa.keys():
        del mahasiswa[nim]
        print("\nData '{}' berhasil dihapus.".format(nim))
    else:
        print("'{}' Tidak ditemukan.".format(nim))

# Mencari Data Mahasiswa
def mencari():
    print("Mencari Data Mahasiswa")
    print("="*40)
    nim = input("Masukan NIM untuk mencari: ")
    print("\nHasil")
    print("="*68)
    print("|    NIM    |      Nama      | Tugas |  UTS  |  UAS  | Akhir |")
    print("="*68)
    if nim in mahasiswa.keys():
        print("| {0:9} | {1:14} | {2:5} | {3:5} | {4:5} | {5:5}".format(nim, mahasiswa[nim][1], mahasiswa[nim][2], mahasiswa[nim][3], mahasiswa[nim][4], mahasiswa[nim][5]))
        print("-"*68)
    else:
        print("'{}' Tidak ditemukan.".format(nim))