#contoh sederhana pembuatan list pada bahasa pemrograman python

list1=['kimia','fisika',1993,2021]
list2=[1,2,3,4,5]
list3=["a","b","c","d"]



print("list1:",list1[0])
print("list2:",list2[0:5])


list=['fisika','kimia',1993,2017]
print("nilai ada pada index 2 :",list[2])

list[2]=2001
print("nilai baru ada pada index 2:",list[2])

#contoh cara menghapus nilai pada python
list=['fisika','kimia',1993,2017]

print(list)
del list[2]
print("setelah di hapus nilai pada index 2 :",list)


aku=['hallo !']*4
print(aku)