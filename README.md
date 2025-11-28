# Tugas_studi_kasus2
# Sistem Perpustakaan Berbasis UML Class Diagram (Pure Python)


Proyek ini mengimplementasikan sebuah sistem perpustakaan sederhana berdasarkan Class Diagram UML yang disediakan. Implementasi dilakukan menggunakan Python murni tanpa *framework* eksternal.


## Struktur Proyek
library-system/ 
* ├── src/ 
* │   ├── author.py # Class Author 
* │   ├── library_item.py # Class abstrak LibraryItem dan subkelas Book 
* │   └── library_member.py # Class LibraryMember 
* └── main.py # Entry point untuk demonstrasi 

## Proses Berpikir (Design Implementation)


1.  **Analisis Diagram UML:** Diagram menunjukkan empat kelas: `Author`, `LibraryItem`, `Book`, dan `LibraryMember`, serta hubungan antar kelas:
    * **Pewarisan (Inheritance):** `Book` mewarisi dari `LibraryItem`. `LibraryMember` tampaknya memiliki keterkaitan yang lebih longgar (asosiasi/komposisi) namun panah menunjukkan pewarisan dari `Author` ke `LibraryMember` di diagram, yang secara *logika domain* (perpustakaan) tidak tepat. Saya menginterpretasikan panah dari `LibraryMember` ke `Author` sebagai kesalahan gambar, dan menganggap `LibraryMember` adalah entitas independen. **Implementasi ini memperlakukan `LibraryMember` sebagai kelas independen.**
    * **Abstraksi:** `LibraryItem` memiliki metode abstrak (`display_info`, `calculate_late_fee`), sehingga diimplementasikan sebagai **Abstract Base Class (ABC)** menggunakan modul `abc` di Python.
    * **Asosiasi:** `Book` memiliki atribut `author: Author` (asosiasi) dan `LibraryMember` memiliki `borrowed_items: LibraryItem[]` (asosiasi banyak-ke-banyak/komposisi).
    * **Akses Atribut:** Atribut `- isbn: str` diimplementasikan dengan konvensi *private* Python (`self._isbn`). Atribut lain bersifat *public* (`+`).


2.  **Modularisasi Kode:** Setiap entitas utama (`Author`, `LibraryItem`/`Book`, `LibraryMember`) ditempatkan dalam *file* Python-nya sendiri di direktori `src/` untuk menjaga kode tetap rapi.


3.  **Docstrings:** Setiap kelas dan metode diwajibkan memiliki dokumentasi. Saya menggunakan **docstrings** (standar PEP 257) untuk mendokumentasikan fungsionalitas, argumen (`Args`), dan nilai kembali (`Returns`).


4.  **Entry Point:** `main.py` diatur sebagai *entry point* untuk mengimpor dan mendemonstrasikan interaksi antar kelas (misalnya, membuat anggota, membuat buku, meminjam, mengembalikan).


## ⚙️ Cara Menjalankan Program


1.  **Kloning Repositori:**
    ```bash
    git clone [LINK_REPOSITORY]
    cd library-system
    ```


2.  **Jalankan Program:**
    Pastikan berada di direktori utama (`library-system/`) dan jalankan `main.py`.


    ```bash
    python main.py
    ```


3.  **Hasil Output:**
    Program akan mencetak langkah-langkah demonstrasi pembuatan objek, perhitungan usia penulis, denda keterlambatan, serta proses peminjaman dan pengembalian item perpustakaan.
