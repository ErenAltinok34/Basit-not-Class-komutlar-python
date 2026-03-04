notlar=[]
n = int(input("Kaç adet not girilecek? "))
for i in range(1,n+1):
    yeniNot=int(input("yeni bir not giriniz"))
    notlar.append(yeniNot)

print(notlar)

print(notlar[3])