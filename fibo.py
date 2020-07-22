num1 = int(input("sayı giriniz: "))
b = 1
a = 1
toplam = 0
sayac = 0
print(toplam,a,b, sep = "\n")
while sayac <= (num1 - 3):
    toplam = a + b
    a = b
    b = toplam
    sayac = sayac +1
    print(toplam)
    