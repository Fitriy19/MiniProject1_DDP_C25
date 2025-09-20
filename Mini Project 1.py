#MINI PROJECT 1

data_pelanggan = [
    ("amel", "potong rambut", 25000),
    ("aya", "creambath", 90000),
    ("sabilla", "hair coloring", 120000),
    ("dila", "smoothing", 170000)
]

#Read
def tampilkan_pelanggan():
    print("\n============== Data Pelanggan ================")
    if data_pelanggan:
        print(f"{"No.":<4}{"Nama":<15}{"Layanan":<20}{"Harga"}")
        print("----------------------------------------------")
        for i, (nama, layanan, harga) in enumerate(data_pelanggan, start=1):
            print(f"{i:<4}{nama:<15}{layanan:<20}{harga}")
    else:
        print("\n--Data pelanggan belum ada--")

#Create
def tambah_pelanggan():
    nama = input("\nMasukkan nama pelanggan: ")
    layanan = input("Masukkan layanan yang dipilih: ")
    while True:
        harga = input("Masukkan harga layanan: ")
        try:
            biaya = int(harga)
            break
        except ValueError:
            print("\n--Harga harus berupa angka!--")
    data_pelanggan.append((nama, layanan, biaya))
    print(f"\n---Data pelanggan berhasil ditambahkan---")
    tampilkan_pelanggan()

#Update
def ubah_pelanggan():
    nama = input("\nMasukkan nama pelanggan yang ingin diubah: ")
    for i, (n, l, b) in enumerate(data_pelanggan):
        if n == nama:
            layanan_baru = input("Masukkan layanan baru: ")
            while True:
                input_harga = input("Masukkan harga layanan: ")
                try:
                    harga = int(input_harga)
                    break
                except ValueError:
                    print("\n--Harga harus berupa angka!--")
            data_pelanggan[i] = (nama, layanan_baru, harga)
            print(f"\n---Data pelanggan berhasil diubah---")
            tampilkan_pelanggan()
            break
    else:
        print("\n--Nama pelanggan tidak ditemukan--")

#Delete
def hapus_pelanggan():
    nama = input("\nMasukkan nama pelanggan yang ingin dihapus: ")
    for i, (n, l, b) in enumerate(data_pelanggan):
        if n == nama:
            del data_pelanggan[i]
            print(f"\n---Data pelanggan berhasil dihapus.---")
            tampilkan_pelanggan()
            break
    else:
        print("\n--Nama pelanggan tidak ditemukan--")

#Menu Utama
while True:
    print("\n=============================================")
    print("|           MANAJEMEN SALON RAMBUT          |")
    print("=============================================")
    print("|  1. Lihat Data Pelanggan                  |")
    print("|  2. Tambah Data Pelanggan                 |")
    print("|  3. Ubah Data Pelanggan                   |")
    print("|  4. Hapus Data Pelanggan                  |")
    print("|  5. Keluar                                |")
    print("=============================================\n")
    pilihan = str(input("Masukkan pilihan Anda (1-5): "))

    if pilihan == "1":
        print("\n=== Anda memilih Lihat Data Pelanggan ===")
        tampilkan_pelanggan()
        input("\nTekan Enter untuk kembali ke menu awal..")
    elif pilihan == "2":
        print("\n=== Anda memilih Tambah Data Pelanggan ===")
        tambah_pelanggan()
        input("\nTekan Enter untuk kembali ke menu awal..")
    elif pilihan == "3":
        print("\n=== Anda memilih Ubah Data Pelanggan ===")
        tampilkan_pelanggan()
        ubah_pelanggan()
        input("\nTekan Enter untuk kembali ke menu awal..")
    elif pilihan == "4":
        print("\n=== Anda memilih Hapus Data Pelanggan ===")
        tampilkan_pelanggan()
        hapus_pelanggan()
        input("\nTekan Enter untuk kembali ke menu awal..")
    elif pilihan == "5":
        print("\n=== Anda memillih keluar. Terima kasih! ===")
        break
    else:
        print("\n--Pilihan tidak valid, hanya pilih diantara 1-5--")
        input("\nTekan Enter untuk kembali ke menu awal..")
