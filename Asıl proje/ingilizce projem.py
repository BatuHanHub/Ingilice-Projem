"""Ingilizce Projem, version 1.0 -release (x86_x64)
Licence GPLv3+ : GNU GPL version 3 <https://www.gnu.org/licenses/gpl-3.0.html>
copyright (C) 2022 BatuHanHub Software 

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law."""

#8.sınıf ıngılızce projem 2021-2022
# yorum satırlarıdır kod ile alakası yoktur. program # leri çalıştırmaz.

import time #zamanlayıcı ekler
import random #ürünleri rasgele dağıtmasına yarayan temel

#takımları isimleri bölümü

print("ilk harfini BÜYÜK diğerlerini küçük harflere yazınız\n") #uyarı notu

x = input("1.takımın adını giriniz \n$") #1.takımın ad girmesini istiyor
y = input("2. takımın adını giriniz \n$") #2.takımın ad girmesini istiyor

########################################################################################################################################

#ürünlerin listesi (değişken = "ürün1 \n","ürün2 \n") 

Meyve = "Grapes \n","Watermelon \n","Strawberry \n","Cherry \n"
Sebze = "Bell Pepper \n","Cabbage \n","Carrot \n","Cucumber \n","Eggplant \n","Onion \n","Pepper \n","popcorn \n","Tomato \n","Potato \n"
Etler = "Fish \n","Chicken \n","Mince \n","Beef \n","Lamb \n","Steak \n"
Yesillik = "Basil \n","Mint \n","Parsley \n"
Paketli_urun = "Flour \n","Sugar \n","Baking Powder \n","Milk \n","Rice \n","Lentin \n","Cummin \n","Yeast \n","Salt \n","Pasta \n","Chili Pepper \n","Black Pepper \n"
Digerleri = "Butter \n","Oil \n","Cheese \n","Walnut \n","Olive \n","Olive Oil \n","Bread \n","Garlic \n","Ginger \n"

#NOT: \n yeni satıra geçer.

##########################################################################################################################################

#ürünleri rasgele dağıtmaya yarıyor

string = Meyve  + Sebze + Etler + Yesillik + Paketli_urun + Digerleri #değişkenlerden hangisini kullanacağı yazıyor
length = 8 #burada kaç tane ürün listeleyeceğini söylüyor 10 yaparsanız 10 tane ürün listeler
Liste1 = "".join(random.sample(string,length))
Liste2 = "".join(random.sample(string,length))
print("\n List of "+x+" team \n"+Liste1)
print("\n List of "+y+" team \n"+Liste2)

###########################################################################################################################################

#zamanlayıcı kod

zaman = int(input("oyun kaç dakika sürecek(60 saniye = 1 dakika) \n$"))

while zaman:
    dakika = zaman // 60
    saniye = zaman % 60
    zamanlayıcı = "{:02d}:{:02d}".format(dakika, saniye)
    print(zamanlayıcı, end="\r")
    time.sleep(1)
    zaman -= 1
print("Süre bitti!")

#############################################################################################################################################

#takımların doğru ve yanlışlarını yazarak durumu "x team won!" olarak ekrana yazdırır

takım1 = int(input(x + " takımının doğru sayısını yazınız: "))
takım2 = int(input(y + " takımının doğru sayısını yazınız: "))

if takım1 > takım2:
	print(x + " team won!")
	
elif takım2 > takım1:
	print(y + " team won!")

else:
    print("Friendship won!") #eğer skor eşit ise "Friendship won!" yazısı gelir

##############################################################################################################################################

input("Oyun bitti! Çıkmak için enter tuşuna basınız...") 

#çıkmak için bir tuşa basınız diyor (ben orayı yanlış yazmışım ("çıkmak için bir tuşa basın olacaktı" ama orjinalliğini koruması açısından düzeltmedim))
