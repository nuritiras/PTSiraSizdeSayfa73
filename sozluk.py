#
#  PROGRAMLAMA TEMELLERİ DERSİ (PYTHON)
#  ÖĞRENME BİRİMİ 3 VERİ YAPILARI
#  Dictionary (Sözlük) Veri Tipi
#  SIRA SİZDE, SAYFA 73
#  Created by Nuri TIRAŞ on 25.011.2024.
#

sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }

# a) sozluk isimli sözlüğü meslekler isimli başka bir sözlüğe kopyalayınız ve ekrana yazdırınız.
yeni_sozluk=sozluk.copy()
print(yeni_sozluk)

# b) sozluk isimli sözlüğün değerlerini ekrana yazdırınız.
print(sozluk.values())

# c) sozluk isimli sözlüğü içi boş bir sözlük hâline getiriniz.
sozluk.clear()

# ç) sozluk isimli sözlüğe Matematikçi: Cahit Arf ikilisini ekleyiniz.
sozluk["Matematikçi"]="Cahit Arf"