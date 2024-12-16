# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def mesaj():
    for i in range(8):
        print("Görev tamamlandı")

mesaj()


# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def dikdörtgeninAlani(uzun_kenar, kisa_kenar):
    alan=float(uzun_kenar)*float(kisa_kenar)
    print("Alan: " , alan)
    return alan
uzun_kenar=input("uzun_kenar: ")

kisa_kenar=input("kisa_kenar: ")
dikdörtgeninAlani(uzun_kenar,kisa_kenar)


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
import random
durumlar=["Yazı","Tura"]
sonuc=random.choice(durumlar)
print("Sonuç: " , sonuc)


# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
sayi1=int(input("Sayı 1: "))
sayi2=int(input("Sayı 2: "))
 
print(sayi1,"ile",sayi2,"arasındaki asal sayılar:")
 
for sayi in range(sayi1,sayi2 + 1):
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi %i) == 0:
               break
       else:
           print(sayi)
    

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def tamBolenler (sayi):
    tamBolenlerListe=list()
    for item in range(1, sayi+ 1):
        if(sayi%item==0):
            tamBolenlerListe.append(item)
    return tamBolenlerListe

while True:
    sayi=input("Sayımız: ")
    if(sayi=="q") :
        print("Sona Erdi ")
        break
    else:
        sayi=int(sayi)
        print((tamBolenler(sayi)))
print("Bitirmek için q'ya basınız. ")
