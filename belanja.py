# a) list kosong
belanja = []

# memasukkan 5 nama barang (menggunakan loop)
print("Masukkan 5 nama barang:")
for i in range(5):
    barang = input(f"Barang ke-{i+1}: ")
    belanja.append(barang)

# Menampilkan daftar belanja bernomor
print("\n--- Daftar Belanja ---")
for i, barang in enumerate(belanja, start=1):
    print(f"{i}. {barang}")

# Menampilkan total item dan item ke-3 dalam daftar
print("\n--- Informasi Tambahan ---")
print(f"Total item dalam daftar: {len(belanja)}")
print(f"Item ke-3 dalam daftar: {belanja[2]}")