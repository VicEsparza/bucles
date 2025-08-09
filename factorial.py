#
#

n=int(input(f"De que numero quieres saber su factorial: "))
acumulador=1
#leer 5 numeros usando un ciclo for
for i in range(n):
    #factorial
    acumulador=acumulador*(i+1)

#imprimir factorial
print(f"El factorial de {n} es: {acumulador}")