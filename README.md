# MINI PROJECT 1
FITRI YANTI | 2309116016 | SISTEM INFORMASI

## MANAJEMEN SALON RAMBUT
### A. Deskripsi Program
Manajemen Salon Rambut adalah aplikasi Python sederhana untuk membantu pemilik salon atau admin mengelola data pelanggan dengan mudah dan efisien. Menerapkan konsep CRUD (Create, Read, Update, Delete) dengan menggunakan Conditional Statements, List & Tuple dan Looping.

### B. Flowchart
<img width="1534" height="1436" alt="Mini Project 1" src="https://github.com/user-attachments/assets/d9f0e0e4-e50a-435a-8b07-4b8d9552ff00" />

### C. Fitur Program
- Lihat Data Pelanggan (Read):
Menampilkan seluruh data pelanggan yang tersimpan.
- Tambah Data Pelanggan (Create):
Menambahkan pelanggan baru dengan nama, layanan, dan harga layanan.
- Ubah Data Pelanggan (Update):
Mengubah layanan dan harga pelanggan berdasarkan nama.
- Hapus Data Pelanggan (Delete):
Menghapus data pelanggan berdasarkan nama.
- Keluar:
Menghentikan program.

### D. Struktur Code
- data_pelanggan: list yang menyimpan data pelanggan. Disimpan menggunakan list of tuple.
- tampilkan_pelanggan(): menampilkan daftar pelanggan.
- tambah_pelanggan(): menambahkan pelanggan baru.
- ubah_pelanggan(): mengubah data pelanggan.
- hapus_pelanggan(): menghapus data pelanggan.
- Menu utama: menggunakan perulangan while True agar program terus berjalan sampai user memilih keluar.

### E. Penjelasan Output
#### 1. Read
Saat user memilih pilihan 1, program akan langsung menampilkan tabel data pelanggan.
<img width="890" height="542" alt="Screenshot 2025-09-20 192949" src="https://github.com/user-attachments/assets/c40be551-e94d-4d77-aee3-2dbdc56f1419" />

Jika tabelnya kosong,  maka program akan menampilkan output “data pelanggan belum ada”.
<img width="931" height="477" alt="Screenshot 2025-09-20 193153" src="https://github.com/user-attachments/assets/14c85e4a-a371-416f-9773-bc14ae24166f" />

#### 2. Create
Saat user memilih pilihan 2, program akan meminta input nama pelanggan, layanan, dan harga yang ingin ditambah. Jika input berhasil maka program akan langsung menampilkan tabel data pelanggan terbaru.
<img width="924" height="678" alt="Screenshot 2025-09-20 193925" src="https://github.com/user-attachments/assets/2da2b9c9-51b8-4586-ab80-734a1ea3c1e7" />

Jika harga yang dimasukkan user bukan angka, program akan menampilkan output “harga harus berupa angka!” dan meminta input ulang, sampai harga yang dimasukkan user berupa angka, baru kemudian program akan menampilkan tabel data pelanggan yang terbaru.
<img width="916" height="539" alt="Screenshot 2025-09-20 194149" src="https://github.com/user-attachments/assets/2a413f98-6062-4ee0-8f59-a0cd0eccff83" />

#### 3. Update
Saat user memilih pilihan 3, program akan menampilkan tabel data pelanggan kemudian meminta input nama pelanggan, layanan, dan harga yg ingin diubah. Jika input berhasil maka program akan langsung menampilkan tabel data pelanggan terbaru.
<img width="765" height="759" alt="Screenshot 2025-09-20 194700" src="https://github.com/user-attachments/assets/d0632d7b-0311-423d-abe9-c0f18079a664" />

Jika user mengetik nama pelanggan yang tidak ada dalam data, program akan menampilkan output “nama pelanggan tidak ditemukan”.
<img width="763" height="315" alt="Screenshot 2025-09-20 194840" src="https://github.com/user-attachments/assets/c692a9d6-6251-4d3a-88dc-5141d3157f27" />

Jika harga yang dimasukkan user bukan angka, program akan menampilkan output “harga harus berupa angka!” dan meminta input ulang, sampai harga yang dimasukkan user berupa angka, baru kemudian program akan menampilkan tabel data pelanggan yang terbaru.
<img width="767" height="804" alt="Screenshot 2025-09-20 195302" src="https://github.com/user-attachments/assets/b031aea9-74a1-4858-8b6d-f1b9861bf39e" />

#### 4. Delete
Saat user memilih pilihan 4, program akan menampilkan tabel data pelanggan kemudian meminta input nama pelanggan yg ingin dihapus. Jika input berhasil maka program akan langsung menampilkan tabel data pelanggan terbaru.
<img width="764" height="697" alt="Screenshot 2025-09-20 195547" src="https://github.com/user-attachments/assets/277e01b3-111f-4456-813f-f58d6c188561" />

Jika user mengetik nama pelanggan yang tidak ada dalam data, program akan menampilkan output “nama pelanggan tidak ditemukan”.
<img width="756" height="515" alt="Screenshot 2025-09-20 195755" src="https://github.com/user-attachments/assets/a83af76f-ac95-42a4-8273-7006b6f901e4" />

#### 5. Keluar
Saat user memilih pilihan 5, program akan menampilkan output “Anda memilih keluar. Terima Kasih” dan program akan langsung berhenti.
<img width="759" height="274" alt="Screenshot 2025-09-20 200000" src="https://github.com/user-attachments/assets/502b2842-c3e9-4b42-b3aa-2ca215518cff" />

Jika user memasukkan pilihan jawaban bukan diantara (1-5), program akan menampilkan output “pilihan tidak valid, hanya pilih diantara 1-5”.
<img width="767" height="293" alt="Screenshot 2025-09-20 200144" src="https://github.com/user-attachments/assets/e8cdf5d1-d574-4cc7-abb0-dfd4f27188fa" />

#### Tambahan:
Setelah setiap proses, program akan meminta pengguna menekan Enter agar hasil output bisa dibaca dengan jelas sebelum kembali ke menu utama.

<img width="761" height="254" alt="Screenshot 2025-09-20 200243" src="https://github.com/user-attachments/assets/3d96208c-aa77-4296-a91e-3a0ead5dcbe2" />
