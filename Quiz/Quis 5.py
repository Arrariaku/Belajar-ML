#1
panjang = int(input("Masukan jumlah angka: "))
list = []

for i in range(panjang):
    isilist = int(input("Masukan angka: "))
    list.append(isilist)

print(f"Hasil penjumlahan: {sum(list)}")

# atau
list2 = input("masukan angka: ")

pisah = map(int, str(list2))

print(f"Hasil penjumlahan: {sum(pisah)}")

#2
warna = int(input("Masukan jumlah warna: "))
list_warna = []

for i in range(warna):
    isiwarna = input("Masukan warna: ")
    list_warna.append(list(isiwarna))
    
print(list_warna)

#3
list3 = [6, 5, 3, 9]
list4 = [0, 1, 7, 7]

zipped = zip(list3, list4)

jumlah = [x + y for (x, y) in zipped]
print(jumlah)

#4
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Original List: {list5}")

print(f"Bilangan Genap: \n {list(filter(lambda x: x%2 ==  0, list5))}")
print(f"Bilangan Genap: \n {list(filter(lambda x: x%2 !=  0, list5))}")
