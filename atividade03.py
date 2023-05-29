
def somamulti(numero):
    soma= 0
    multi=1
    for i in numero:
        ra = int(i)
        soma += ra
        multi *= ra
    return soma, multi

numero=input("Digite um numero inteiro positivo:")
#numero do RA : 3011392313036
resultado= somamulti(numero)
print(resultado)


