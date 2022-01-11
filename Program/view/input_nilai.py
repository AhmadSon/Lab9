# Mencari Data Mahasiswa
def mencari():
    print("Mencari Data Mahasiswa")
    print("="*40)
    nim = input("Masukan NIM untuk mencari")
    print("\nHasil")
    print("="*68)
    print("|    NIM    |      Nama      | Tugas |  UTS  |  UAS  | Akhir |")
    print("="*68)
    if nim in mahasiswa.keys():
        print("| {0:9} | {1:14} | {2:5} | {3:5} | {4:5} | {5:5}".format(nim, mahasiswa[nim][1], mahasiswa[nim][2], mahasiswa[nim][3], mahasiswa[nim][4], mahasiswa[nim][5]))
        print("-"*68)
    else:
        print("'{}' Tidak ditemukan.".format(nim))


# Input Data
def input_nim():
    print("\nMasukan data mahasiswa")
    global nim
    nim = input("\nNIM: ")
    return nim

def input_nama():
    global nama
    nama = input("\nNama: ")
    return nama

def input_tugas():
    global tugas
    tugas = int(input("Masukan nilai tugas: "))
    return tugas

def input_uts():
    global uts
    uts = int(input("Masukan nilai UTS: "))
    return uts

def input_uas():
    global uas
    uas = int(input("Masukan nilai UAS: "))
    return uas

def input_akhir():
    global akhir
    akhir = (tugas *.3 + uts *.35 + uas * .35)
    return akhir