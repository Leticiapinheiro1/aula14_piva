def valorPrimo(n):
    contador = 0
    for i in range(1,n+1):
        if (n%i==0):
            contador += 1
    if contador==2:
        return True
    else:
        return False
    
a=int(input("Digite os dois ultimos numeros do seu RA:"))    

print(f"O numero é primo : {valorPrimo(a)}")

z=a*2+5 ##ra 
print(z)

cont=0
numer=0

for i in range(z):
    numer+=1
    if valorPrimo(numer)==True:
        print(numer, end="-")   
        cont+=1    

primos = []
soma = 0

for i in range(z):
    if valorPrimo(i):
        primos.append(i)
        soma += i
        
print("Soma dos números primos:", soma)        





