n= int(input("definisci un numero"))
primo= True
if n<2:
    primo=False
else: 
    for i in range(2,n):
        if n%i==0:
         primo=False
if primo: 
    print("il numero è rpimo")
else:
    print("il numero non è rpimo")
