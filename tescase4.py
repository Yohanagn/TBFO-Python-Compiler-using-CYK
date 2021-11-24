# input
waktu = 1000

# waktu
Hari = waktu // (24 * 3600) # 24 jam dikonversi menjadi detik
print("Hari =", Hari)
waktu %= 24 * 3600
Jam = waktu // 3600
print("Jam =", Jam)
waktu %= 3600
Menit = waktu // 60
print("Menit =", Menit)
waktu %= 60
Detik = waktu
print("Detik =", Detik)
