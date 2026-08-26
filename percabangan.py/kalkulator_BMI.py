berat = int(input("Masukkan berat badan anda (kg): "))
tinggi = int(input("Masukkan tinggi badan anda (m) "))
bmi = berat / tinggi

print("Berat badan :", berat,"kg")
print("Tinggi badan :", tinggi,"m")

if bmi <18.5:
    print("Keterangan : Berat badan kurang")
elif bmi <25:
    print("Keterangan : berat badan normal")
elif bmi <30:
    print("Keterangan : berat badan berlebih")
else:
    print("Keterangan : obesitas")