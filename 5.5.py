notlar=[60,70,50,90,50,80,60]
n=len(notlar)
print(notlar)
notlar.sort()
print(notlar[n-1])
print(notlar[n-2])
max=notlar[0]
for i in range(1,n):
    if(notlar[i]>max): max=notlar[i]

print("maximumnot :",max)