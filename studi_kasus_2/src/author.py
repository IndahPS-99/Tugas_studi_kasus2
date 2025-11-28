from datetime import date

class Author:   # Merepresentasikan seorang penulis dalam sistem perpustakaan.
    def __init__(self, name: str, birth_year: int):
        self.name: str = name
        self.birth_year: int = birth_year

    def get_age(self, current_year: int) -> int:
        if current_year < self.birth_year:
            # Menghindari usia negatif jika tahun saat ini lebih kecil dari tahun lahir
            return 0
        return current_year - self.birth_year
    