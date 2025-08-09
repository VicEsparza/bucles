
#Programa: Practica de ejemplo

mayor=float('-inf')
contador=0
acumulador=0

#leer 5 numeros usando un bucle for
for i in range(5):
    num=float(input(f"Ingrese el numero {i+1}: "))
    acumulador=acumulador+num
    if num>mayor:
        mayor=num
        contador=contador+1
#imprimir el numero mayor
print(f"El numero mayor es {mayor}")
print(f"El numero de veces que cambio el numero mayor: {contador}")
print(f"La suma de los numeros es {acumulador}")