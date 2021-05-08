#kondisi if adalah kondisi yang akan di exsekusioleh program jika bernilai benar atau  salah

nilai = 9
#jk kondisi benar/true maka program akan mengeksekusi program di bawahnya
if(nilai > 7):
    print("sembilan lebih besar dari  angka  tujuh") #kondisi benar di eksejusi

#jika kondisi salah /fals maka program tidak akan  mengeksekusi printah di bawahnya
if(nilai > 1):
    print("sembilan lebih besar dari angka  sepuluh") #kondisi salah maka tidak akan di eksekusi
#kondisi if else
nilai=4
#jk pernyataan pada if bernilai true maka if akan di eksekusi,tetapi jk false kode pada else yang akan di eksekusi
if(nilai>7):
    print("slamat anda lulus")
else:
    print("maaf  anda tidak lulus")


#contoh penggunaan kondisi elif
hari_ini="minggu"
if(hari_ini=="senin"):
    print("saya akan kuliah")
elif(hari_ini=="selasa"):
    print("saya  akan kuliah")
elif(hari_ini=="rabu"):
    print("saya  akan kuliah")
elif(hari_ini=="kamis"):
    print("saya  akan kuliah")
elif(hari_ini=="jumat"):
    print("saya  akan kuliah")
elif(hari_ini=="sabtu"):
    print("saya  akan kuliah")
elif(hari_ini=="minggu"):
    print("saya  tidak kuliah")