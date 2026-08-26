# contoh: kategori nilai
nilai = int(input("Masukkan nilai (0-100: "))

if nilai >= 90:
    kategori = "A (Sangat Baik)"
elif nilai >= 80:
    kategori = "B (Baik)"
elif nilai >= 70:
    kategori = "C (Cukup)"
elif nilai >= 60:
    kategori = "D (Kurang)"
else:
    kategori = "E (Sangat Kurang)"

print("Nilai :", nilai)
print("Kategori:", kategori)