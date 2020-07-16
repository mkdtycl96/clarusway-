count = False
sonuc = []
for i in range(2,100):
    for ii in range(2,i):
        if(i%ii == 0):
            count = True
            break
    else:
        sonuc.append(i)
sonuc        
