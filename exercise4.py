# Christina Andrea Putri - Universitas Kristen Duta Wacana

# Alana datang ke sebuah toko yang menjual barang-barang K-Pop. Toko tersebut menjual berbagai macam album
# dan pernak-pernik K-Pop. Jika membeli 2 album akan mendapatkan diskon 5% ; jika membeli 3 atau lebih dari itu
# akan mendapat diskon 20% ; pembelian pernak-pernik lebih dari 2 juga akan mendapat diskon 10%.
# Jika Alana membeli 2 album dan 3 pernak-pernik, berapa total yang harus Alana bayar?
# (Album = Rp300.000,00 ; Pernak-pernik = Rp40.000,00)

#Input : jenis barang, jumlah barang
#Proses : operasi hitung total yang harus dibayar
#Output : jumlah yang harus dibayar

print("=============================")
print(" Selamat Datang ! \n Silahkan memilih barang yang Anda beli : ")
print("1. Album \n 2. Merchandise \n 3.Album+Merchandise \n ")

albm=int(input("Masukkan pilihan anda: "))
if albm==1:
    inp_1=int(input("Jumlah album yang dibeli: "))
elif albm==2 : 
    inp_2 = int(input("Jumlah merchandise yang dibeli : "))
elif albm==3:
    inp_1=int(input("Jumlah album yang dibeli: "))
    inp_2 = int(input("Jumlah merchandise yang dibeli : "))

alb_harga = 300000
merch_harga = 40000

def album(x,diskon=0):
    alb_total = x*alb_harga
    print("Total pembelian album : Rp", alb_total)
    if inp_1 == 2 : 
        diskon=0.05*alb_total
        print("Selamat Anda mendapat diskon album sebesar Rp", diskon)
        total = alb_total-diskon
        return total
    elif inp_1 >= 3 : 
        diskon=0.2*alb_total
        print("Selamat Anda mendapat diskon album sebesar Rp", diskon)
        total = alb_total-diskon
        return total

def merch(y,diskon=0):
    merch_total=y*merch_harga
    print("Total pembelian merchandise: Rp", merch_total)
    if inp_2 > 2 : 
        diskon2=0.1*merch_total
        print("Selamat Anda mendapat diskon merchandise sebesar Rp", diskon2)
        total2 = merch_total-diskon2
        return total2


if albm==1:
    print("Total yang harus dibayar adalah Rp", album(inp_1))
elif albm==2 : 
    print("Total yang harus dibayar adalah Rp",merch(inp_2))
elif albm==3:
    print("Total yang harus dibayar adalah Rp",album(inp_1)+merch(inp_2))





