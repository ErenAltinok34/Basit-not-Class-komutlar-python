import statistics

notlar=[60,89,90,70,40,50,80,90]
eskiNotlar = [60, 50]
print(len(notlar))
notlar.append(30)
print("burada",len(notlar),"adet not var.")
x = notlar.count(90)
print(x,"adet var.")
notlar.extend(eskiNotlar)
print(notlar)
yetmis = notlar.index(70)
print("70 notu listede ilk kez",yetmis+1,", sırada")
notlar.remove(70)
print(notlar)
notlar.sort()
print(notlar)
avg =sum(notlar) / len(notlar)
print("ortalama not",avg)
avg = statistics.mean(notlar)
print(avg)
