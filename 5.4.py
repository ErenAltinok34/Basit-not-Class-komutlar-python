notlar = [60,80,70,90,70,80,60]

sin = True
n = len(notlar)

for i in range(0, n):
    if notlar[i] != notlar[n-1-i]:
        sin = False
        break

if sin:
    print("notlar simetrik.")
else:
    print("notlar simetrik degil")