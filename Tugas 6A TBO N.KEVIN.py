#. TUGAS 6.A - KULIAH TBO
#. DOSEN = Arnes Vandika, M.Kom
#. IF FUNCTION

print ('NAMA = Nikolas Kevin');
print ('NPM = 21421003');
#
belanja = int(input('Total belanja Rp.'))
if belanja > 50000 :
 print('selamat anda mendapat diskon 5%')

 diskon = belanja * 5/100
 bayar = belanja - diskon
 print('total belanja anda, Rp. ', belanja)
 print('Potongan harga, Rp. ', diskon)
 print('Anda cukup bayar, Rp. ', bayar)

 print('terimakasih sudah belanja...')