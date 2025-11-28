from typing import List
from src.library_item import LibraryItem

class LibraryMember: # Merepresentasikan anggota perpustakaan yang dapat meminjam item.
    def __init__(self, member_id: int, name: str):
        self.member_id: int = member_id
        self.name: str = name
        # Atribut: + borrowed_items: LibraryItem[]
        self.borrowed_items: List[LibraryItem] = []

    def borrow_item(self, item: LibraryItem) -> None: # Menambahkan item ke daftar pinjaman anggota.
        if item not in self.borrowed_items:
            self.borrowed_items.append(item)
            print(f"✅ {self.name} berhasil meminjam item: {item.title}")
        else:
            print(f"❌ {self.name} sudah meminjam item: {item.title}")

    def return_item(self, item: LibraryItem) -> None: #  Menghapus item dari daftar pinjaman anggota (mengembalikan item).
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"✅ {self.name} berhasil mengembalikan item: {item.title}")
        else:
            print(f"❌ {self.name} tidak meminjam item: {item.title}")

    def list_borrowed_items(self) -> None: # Menampilkan daftar item yang sedang dipinjam oleh anggota.
        print(f"\n--- Pinjaman {self.name} (ID: {self.member_id}) ---")
        if not self.borrowed_items:
            print("Saat ini tidak ada item yang dipinjam.")
            return

        for item in self.borrowed_items:
            print(f"- [ID {item.item_id}] {item.title}")
