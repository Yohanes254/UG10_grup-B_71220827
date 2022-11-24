
print :("~~~~~~~~~~~~~~~ /('v')/ ~~~~~~~~~~~~~~~~~")
print :("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print :("~~~~~~~~~~~~~~~ /('v')/~~~~~~~~~~~~~~~~~~")
print()
print :("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya")
print ("1.Limas")
print ("2.Bola")
print ("3.Prisma")
print ("4.Kerucut")
print()
pilihan =int( input( "Masukan Pilihan Anda " ))
if pilihan ==1 :
        panjang = int (input("Masukan panjang sisi alas limas :"))
        tinggi  = int (input ("Masukan tinggi limas ;" ))
        rumuslimas = (panjang*panjang*tinggi/3)
        print:("volume limas tersebut adalah ", rumuslimas)

if pilihan ==2 :
         jari = int (input("Masukan panjang jari-jari bola:"))
         rumusbola=((4/3)*3,14*jari**3)
         print:("volume bola tersebut adalah ", rumusbola)
    
