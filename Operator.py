# operaton
PPKN = 40
nilai = input ("Masukkan nilai anda: ")
alpa = 3
sakit = 8

#Aritmatika
nilai_akhir = PPKN + int(nilai)
print("Jumlah nilai akhir:", nilai_akhir)
jumlah_total = alpa + sakit
print("Jumlah total alpa dan sakit anda adalah",jumlah_total)

#lulus jika nilai akhir lebih besar dari 70 dan jumlah total alpa dan sakit lebih kecil dari 20
lulus = nilai_akhir >=70 and jumlah_total < 20 or nilai_akhir >=83 and jumlah_total < 30
print("Apakah anda lulus?", lulus)

