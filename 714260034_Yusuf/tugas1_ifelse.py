
#Tugas Mandiri if else

nilai = float(input("Masukkan nilai akhir (0-100): "))

if nilai >= 80 and nilai <= 100:
    huruf =("A")
elif nilai >= 70 and nilai < 80:
    huruf=("B")
elif nilai >= 60 and nilai < 70:
    huruf=("C")
elif nilai >= 50 and nilai < 60:
    huruf=("D")
else:
    huruf=("E")

print(f"Nilai {nilai} setara dengan huruf mutu {huruf}")

#Format komentar identitas
#==========================================
#Nama : Muhammad Yusuf Abdurrahman
#NIM  : 714260034
#Kelas: A D4TI 
#Kelompok : The Panturas