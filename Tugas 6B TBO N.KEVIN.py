#. TUGAS 6.B - KULIAH TBO
#. DOSEN = Arnes Vandika, M.Kom
#. IF...ELIF...bersarang [BAHAN UAS]

print ('NAMA = Nikolas Kevin');
print ('NPM = 21421003');
#
nilai = int(input("Masukkan nilai")) 
if nilai >= 90:
    print('Kategori beasiswa penuh')
elif nilai >= 80:
    print('Kategori beasiswa I')
elif nilai >= 70:
    print('Kategori beasiswa II')
else:
    print('Tidak mendapatkan beasiswa')
