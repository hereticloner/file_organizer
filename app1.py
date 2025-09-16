import os
import shutil
ana_dizin = input("duzenlemek istediginiz yolu girin: ")
tum_oge = os.listdir(ana_dizin)
uzanti_gore = {}
print(f"{ana_dizin}")

print("bu klasordeki hersey")
for oge in tum_oge:
    tam_yol = os.path.join(ana_dizin, oge)
    print(f"klasordeki tum ogeler{oge}")

    if os.path.isfile(tam_yol):
        ad, uzanti = os.path.splitext(oge)
        print(f"ad '{oge}',uzanti{uzanti}")
        uzanti = uzanti.lower()
        if uzanti in uzanti_gore:
            uzanti_gore[uzanti].append(oge)
        else:
            uzanti_gore[uzanti] = [oge]

for uzanti, dosyalar in uzanti_gore.items():
    klasor = uzanti[1:]
    yeni_klasor = os.path.join(ana_dizin, klasor)
    if not os.path.exists(yeni_klasor):
        os.makedirs(yeni_klasor)
    for ad in dosyalar:
        kaynak_yolu = os.path.join(ana_dizin, ad)
        hedef_yolu = os.path.join(yeni_klasor, ad)
        shutil.move(kaynak_yolu, hedef_yolu)
print("Klasordeki tum dosyalar duzenlendi.")
