#. TUGAS 5.B - KULIAH TBO
#. DOSEN = Arnes Vandika, M.Kom
#. FOR...ELSE

print ('NAMA = Nikolas Kevin');
print ('NPM = 21421003');
#

listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
   'Jogjakarta', 'Semarang', 'Makassar' 
]

kotaYangDicari = input('Ketik nama kota yang kamu cari: ')

for i, kota in enumerate(listKota):
  # kita ubah katanya ke lowercase agar
  # menjadi case insensitive
  if kota.lower() == kotaYangDicari.lower():
    print('Kota yang anda cari berada pada indeks', i)
    break
else:
  print('Maaf, kota yang anda cari tidak ada, coba lagi ya')