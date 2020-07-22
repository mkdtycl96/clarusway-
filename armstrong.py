num1 = (input("bir sayı giriniz: "))
num_set = set(num1)
allnum = set("0123456789")
str_ = set("qwertyuıopğüişlkjhgfdsazxcvbnmöç")
if (num_set) - (allnum) == {"-"}:
    print("pozitif sayı giriniz")
elif (num_set) - (allnum) == {"."}:
    print("lütfen tam sayı giriniz")
elif len((num_set) & (str_)) > 0:
    print("lütfen harf girmeyiniz sadece sayı")

if (num_set - allnum != {"-"}) and (num_set - allnum != {"."} ) and len(num_set & str_) == 0:
    basamak = num1
    toplam = 0
    for x in basamak:
        rakam = int(x) ** len(basamak) 
        toplam += rakam
    if int(num1) == toplam :
        print("bu bir arstrong sayısıdır ") 
    else:
        print("armstrong sayısı değildir ")   
        



   
    

        



