#Víctor Andree Esparza Martínez - 250183
#Programa 34: Ingresar un 4 numeros y sumarlos

#Definimos el valor de la variable suma
suma=0

#Sumaremos 4 numeros por lo que le pedimos al programa que repita la accion 4 veces con range(4)
for i in range(4):
    #Ingresamos nuestro numero y lo sumamos
    num=float(input(f"Ingrese el numero {i+1}: "))
    suma+=num
#Imprimimos nuestro resultado
print(f"La suma total de tus numeros es: {suma: .2f}")