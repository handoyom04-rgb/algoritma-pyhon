# Contoh Syarat Kelulusan ddengan 2 kondisi
nilai = int(input("Nilai ujian  : "))
absen = int(input("Jumlah absen : "))

if nilai >= 75:
    if absen <= 5:
        print("LULUS - SELAMAT!")
    else:
        print("TIDAK LULUS - absen terlalu banyak")
else:
    print("TIDAK LULUS - Nilai di bawah KKM ")