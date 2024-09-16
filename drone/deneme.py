alisveris_listesi = []
urun_miktarlari = ()
benzersiz_urunler = set()
urun_miktar_dict = {}

print("Alışveriş listesi uygulamasına hoş geldiniz!")
print("Ürünleri eklemek için ürün adını yazın ve Enter'a basın.")
print("Ürün miktarını eklemek için miktarı yazın ve Enter'a basın.")
print("Ürün eklemeyi bitirmek için 'bitir' yazın ve Enter'a basın.")

while True:
    urun = input("Ürün: ")
    
    if urun.lower() == 'bitir':
        break
    
    miktar = input("Miktar: ")  
    alisveris_listesi.append((urun, miktar)) 
    benzersiz_urunler.add(urun)
    urun_miktar_dict[urun] = miktar

print("\nAlışveriş listeniz:")
print("Liste:")
for urun, miktar in alisveris_listesi:
    print(f"{urun}: {miktar}")

print("\nBenzersiz ürünler:")
print(benzersiz_urunler)

print("\nÜrün ve miktarları (Dictionary):")
for urun, miktar in urun_miktar_dict.items():
    print(f"{urun}: {miktar}")