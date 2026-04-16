# Kendi değerlerini buraya gir (Mevcut İrtifa, Hedef İrtifa, Hız, Kalan Mesafe)
tod, vsi, durum = descent_calculator(7500, 1500, 110, 25)

print(f"Alçalmaya Başlama Mesafesi (TOD): {tod} NM")
print(f"Gereken Alçalma Varyosu: {vsi} fpm")
print(f"Mevcut Durum: {durum}")
