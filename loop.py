#didalam bahasa pemrograman python pengulangan di bagi menjadi 3 bagian,yaitu:
#while Loop
#for Loop
#nested Loop

#contoh pengulangan while loop
#catatan penentuan ruang lingkup di python bisa menggunakan tab alih alih mengunakan tanda kurang

count=0
while(count<9):
    print("the count is  :",count)
    count=count+1
print("good bay!")

#conton pengulangan for sederhana
angka=[1,2,3,4,5]
for x in angka:
    print(x)

#contoh pengulangan for
buah=["nanas","apel","jeruk"]
for makanan in buah:
    print("saya suka makan",makanan)

#contoh pengulangan nesped loop
# catatan:penggunaanmodulo pada kondisional  mengasumsikan nilai senilai nol sebagai true(benar) dan nol sebagai fals(salah)
i=0
while(i<100):
    j=2
    while(j<=(i/j)):
        if not (i%j):break
        j=j+1
    if(j>i/j):print(i,"is prime")
    i=i+1
print("good bye !")