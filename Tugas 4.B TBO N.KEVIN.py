#. TUGAS 4.B - KULIAH TBO
#. DOSEN = Arnes Vandika, M.Kom
#. IF NESTED (IF BERSARANG)
print ('NAMA = Nikolas Kevin');
print ('NPM = 21421003'); 
#
#input data
var_umur = input("Berapa Umur Anda : ")

#Statement IF Bersarang
if(int(var_umur) < 25) :
  if (int(var_umur) < 20 ) :
    print("Anda Masih Sekolah")
  else :
    print("Anda Sudah Bekerja")
elif(int(var_umur) > 25) :
   if (int(var_umur) < 30) :
      print("Harusnya Sudah Anda Menikah")
   else :
     print("Anda Sudah Punya Anak 3")
else :
     print("Maaf, Jawaban Anda Salah")

