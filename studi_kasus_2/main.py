# main.py adalah entry point untuk mendemonstrasikan kelas-kelas yang telah dibuat
from datetime import date
from src.author import Author
from src.library_item import Book, LibraryItem
from src.library_member import LibraryMember

def main():
# Fungsi utama untuk mendemonstrasikan fungsionalitas sistem perpustakaan berdasarkan class diagram.
    print("=========================================")
    print("   DEMONSTRASI SISTEM PERPUSTAKAAN (UML)   ")
    print("=========================================")

    # 1. Membuat objek Author
    print("\n[1] Membuat Penulis (Author)")
    author1 = Author("Andrea Hirata", 1967)
    author2 = Author("J.K. Rowling", 1965)
    
    current_year = date.today().year
    print(f"Usia {author1.name} di tahun {current_year}: {author1.get_age(current_year)} tahun")
    
    # 2. Membuat objek Book
    print("\n[2] Membuat Item Perpustakaan (Book)")
    book1 = Book(item_id=101, isbn="978-9791227181", title="Laskar Pelangi", author=author1)
    book2 = Book(item_id=102, isbn="978-0747532743", title="Harry Potter and the Sorcerer's Stone", author=author2)
    
    # Memanggil method display_info()
    book1.display_info()
    book2.display_info()
    
    # Memanggil method calculate_late_fee(days_late: int) -> float
    days_late = 5
    fee1 = book1.calculate_late_fee(days_late)
    fee2 = book2.calculate_late_fee(days_late)
    print(f"\nDenda keterlambatan untuk '{book1.title}' selama {days_late} hari: ${fee1:.2f}")
    print(f"Denda keterlambatan untuk '{book2.title}' selama {days_late} hari: ${fee2:.2f}")

    # 3. Membuat objek LibraryMember
    print("\n[3] Membuat Anggota Perpustakaan (LibraryMember)")
    member1 = LibraryMember(member_id=2001, name="Budi Santoso")
    member2 = LibraryMember(member_id=2002, name="Dewi Lestari")

    # 4. Melakukan peminjaman dan pengembalian
    print("\n[4] Proses Peminjaman dan Pengembalian")
    
    # Anggota 1 meminjam book1 dan book2
    member1.borrow_item(book1)
    member1.borrow_item(book2)
    member1.list_borrowed_items()
    
    # Anggota 1 mengembalikan book1
    member1.return_item(book1)
    member1.list_borrowed_items()
    
    # Anggota 2 meminjam book1 (yang sudah dikembalikan)
    member2.borrow_item(book1)
    
    # Anggota 2 mencoba mengembalikan book2 (yang tidak dia pinjam)
    member2.return_item(book2) 
    
    member2.list_borrowed_items()


if __name__ == "__main__":
    main()
