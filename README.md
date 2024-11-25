PENEJELASAN KODE PROGRAM PRAKTIKUM 7

Program ini dirancang untuk membantu mengelola data nilai mahasiswa dengan cara yang sederhana dan efektif. Inti dari program ini adalah sebuah dictionary Python yang berfungsi sebagai "database" sederhana, di mana nama mahasiswa berperan sebagai kunci (key) dan nilai mereka sebagai nilai (value) dalam dictionary tersebut. Ketika program dijalankan, pengguna akan dihadapkan dengan menu interaktif yang menawarkan lima pilihan utama: menambah data, menampilkan data, menghapus data, mengubah data, atau keluar dari program.

Saat pengguna memilih untuk menambah data baru, program akan meminta dua input: nama mahasiswa dan nilainya. Fungsi tambah() akan memproses input ini dan menyimpannya ke dalam dictionary. Program secara otomatis akan menangani proses penyimpanan dan memberikan konfirmasi bahwa data telah berhasil ditambahkan. Untuk melihat data yang telah tersimpan, pengguna dapat menggunakan fungsi tampilkan() yang akan menampilkan seluruh data dalam format yang mudah dibaca. Jika belum ada data yang tersimpan, fungsi ini akan memberitahu pengguna bahwa database masih kosong.

Ketika perlu mengubah nilai mahasiswa, fungsi ubah() memungkinkan pengguna untuk memperbarui nilai dengan mencari berdasarkan nama mahasiswa. Program akan memeriksa apakah nama tersebut ada dalam database, dan jika ditemukan, pengguna dapat memasukkan nilai baru yang akan menggantikan nilai lama. Serupa dengan itu, fungsi hapus() memungkinkan pengguna untuk menghapus data mahasiswa berdasarkan nama. Kedua fungsi ini dilengkapi dengan sistem pengecekan untuk memastikan bahwa nama mahasiswa yang dicari memang ada dalam database, mencegah kesalahan yang mungkin terjadi.

Program ini menggunakan loop while True untuk tetap berjalan sampai pengguna memilih untuk keluar, memungkinkan penggunaan yang berkelanjutan. Setiap kali pengguna melakukan operasi, program akan kembali ke menu utama, siap untuk operasi berikutnya. Semua input pengguna divalidasi untuk mencegah crash program, dan pesan error yang informatif akan ditampilkan jika terjadi kesalahan. Meskipun program ini menyimpan data hanya selama program berjalan (tidak permanen), strukturnya yang sederhana membuatnya mudah digunakan untuk mengelola data nilai mahasiswa dalam satu sesi.

Keunggulan program ini terletak pada antarmukanya yang sederhana namun fungsional, serta kemampuannya untuk menangani operasi dasar manajemen data (Create, Read, Update, Delete atau CRUD) dengan efisien. Program ini cocok digunakan untuk mengelola data kelas kecil hingga menengah, di mana dosen atau guru perlu mencatat dan mengelola nilai mahasiswa secara cepat dan mudah. Meskipun tidak memiliki penyimpanan permanen, program ini dapat dengan mudah dimodifikasi untuk menambahkan fitur penyimpanan ke file jika diperlukan di masa mendatang.

Setiap fungsi dalam program dirancang dengan mempertimbangkan kemudahan penggunaan dan pencegahan kesalahan. Misalnya, saat memasukkan nilai, program akan memastikan bahwa input yang diterima adalah angka yang valid. Begitu juga saat menghapus atau mengubah data, program akan memverifikasi keberadaan data terlebih dahulu sebelum melakukan operasi, mencegah kesalahan yang mungkin timbul dari mencoba memanipulasi data yang tidak ada.

1.)Struktur Data Program

pythonCopymahasiswa = {}  # Dictionary kosong untuk menyimpan data mahasiswa

Program menggunakan dictionary Python untuk menyimpan data
Format: {"nama_mahasiswa": nilai}
Contoh: {"John": 85.5, "Maria": 90.0}


2.)Fungsi-fungsi Utama

a) Fungsi tambah()
pythonCopydef tambah():
    nama = input("Masukkan nama mahasiswa: ")     # Meminta input nama
    nilai = float(input("Masukkan nilai: "))      # Meminta input nilai
    mahasiswa[nama] = nilai                       # Menyimpan ke dictionary
    print(f"Data {nama} berhasil ditambahkan!")   # Konfirmasi

Meminta input nama dan nilai dari pengguna
Mengkonversi nilai ke float (bilangan desimal)
Menyimpan data ke dictionary dengan nama sebagai key dan nilai sebagai value

b) Fungsi tampilkan()
pythonCopydef tampilkan():
    if not mahasiswa:    # Cek apakah dictionary kosong
        print("Belum ada data mahasiswa.")
        return
    
    print("\nDaftar Nilai Mahasiswa:")
    print("----------------------")
    for nama, nilai in mahasiswa.items():    # Loop untuk setiap data
        print(f"Nama: {nama} | Nilai: {nilai}")
    print("----------------------")

Mengecek apakah ada data dalam dictionary
Jika kosong, tampilkan pesan "Belum ada data"
Jika ada data, tampilkan semua data dalam format tabel sederhana

c) Fungsi hapus(nama)
pythonCopydef hapus(nama):
    if nama in mahasiswa:    # Cek apakah nama ada dalam dictionary
        del mahasiswa[nama]   # Hapus data dengan key nama
        print(f"Data {nama} berhasil dihapus!")
    else:
        print(f"Data {nama} tidak ditemukan!")

Menerima parameter nama mahasiswa
Mengecek apakah nama ada dalam dictionary
Jika ada, hapus data menggunakan del
Jika tidak ada, tampilkan pesan error

d) Fungsi ubah(nama)
pythonCopydef ubah(nama):
    if nama in mahasiswa:    # Cek apakah nama ada dalam dictionary
        nilai_baru = float(input("Masukkan nilai baru: "))
        mahasiswa[nama] = nilai_baru    # Update nilai
        print(f"Data {nama} berhasil diubah!")
    else:
        print(f"Data {nama} tidak ditemukan!")

Menerima parameter nama mahasiswa
Mengecek apakah nama ada dalam dictionary
Jika ada, minta input nilai baru dan update data
Jika tidak ada, tampilkan pesan error


3.)Menu Utama Program (Fungsi main())

pythonCopydef main():
    while True:    # Loop terus sampai user memilih keluar
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        
        pilihan = input("\nPilih menu (1-5): ")
        
        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
            hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang akan diubah: ")
            ubah(nama)
        elif pilihan == "5":
            print("Program selesai!")
            break
        else:
            print("Pilihan tidak valid!")

Menampilkan menu dalam loop while True
Memproses input pengguna sesuai pilihan menu
Loop akan terus berjalan sampai pengguna memilih menu 5 (Keluar)


4.)Cara Kerja Program

Program dimulai dengan dictionary kosong
Pengguna dapat memilih menu 1-5
Setiap operasi (tambah/hapus/ubah) akan langsung mempengaruhi dictionary
Data tersimpan selama program berjalan (tidak permanen)

5.)Keamanan Program

Program menggunakan try-except untuk konversi nilai ke float
Validasi menu menggunakan if-elif
Pengecekan keberadaan data sebelum operasi hapus/ubah
