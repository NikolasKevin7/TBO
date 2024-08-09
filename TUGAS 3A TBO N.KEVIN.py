#. TUGAS 3A - KULIAH TBO
#. DOSEN = Arnes Vandika, M.Kom
#. MATRIX PYTHON (PENJUMLAHAN)
print ('NAMA = Nikolas Kevin')
print ('NPM = 21421003')

mat1 = [
    [5,0],
    [2,6],
]

mat2 = [
    [1,0],
    [4,2],
]

for x in range(0, len(mat1)):
    for y in range(0, len(mat1[0])):
        print (mat1[x][y] + mat2[x][y], end=''),
    print
