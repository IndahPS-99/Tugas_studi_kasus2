from abc import ABC, abstractmethod
from typing import Optional
from src.author import Author

# Menggunakan ABC (Abstract Base Class) untuk kelas yang memiliki metode abstrak
class LibraryItem(ABC):
    def __init__(self, item_id: int, title: str):
        self.item_id: int = item_id
        self.title: str = title

    @abstractmethod # Menampilkan detail informasi spesifik item.
    def display_info(self) -> None:
        pass

    @abstractmethod # Menghitung denda keterlambatan berdasarkan jumlah hari terlambat.
    def calculate_late_fee(self, days_late: int) -> float:
        pass

class Book(LibraryItem): # Merepresentasikan sebuah Buku, merupakan subkelas dari LibraryItem.
    def __init__(self, item_id: int, isbn: str, title: str, author: Author):
        super().__init__(item_id, title)
        # Atribut private: - isbn: str
        self._isbn: str = isbn
        # Atribut public: + author: Author
        self.author: Author = author

    def display_info(self) -> None: # Menampilkan detail informasi Buku, termasuk ISBN dan penulis.
        print("--- Detail Buku ---")
        print(f"ID Item: {self.item_id}")
        print(f"Judul: {self.title}")
        print(f"ISBN: {self._isbn}")
        print(f"Penulis: {self.author.name} (Lahir: {self.author.birth_year})")

    def calculate_late_fee(self, days_late: int) -> float:
        if days_late <= 0:
            return 0.0
        # Denda 0.50 per hari
        return days_late * 0.50
    