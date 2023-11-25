print("Kök Bulma Uygulaması")
print("Lütfen Denklemdeki Değerleri Giriniz")

a = int(input("İlk Değer:"))
b = int(input("İkinci Değer:"))
c = int(input("üçüncü Değer:"))

delta =(b ** 2- 4*a * c

kok1 = (-b - delta ** 0.5) / (2 * a)
kok2 = (-b + delta ** 0.5) / (2 * a)

print("Denklemin birinci kökü {}\nDenklemin ikinci kökü {}".format(kok1,kok2))