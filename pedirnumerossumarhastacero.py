#
#

print("pedir numeros al usuario y sumarlos, hasta que el usuario ingrese cero")
suma=0
contar=0
n=int(input(f"ingrese un numero o un 0 para terminar: "))

while n !=0:
    suma+=n
    contar+=1
    n=int()