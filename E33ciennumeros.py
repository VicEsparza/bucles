#Víctor Andree Esparza Martínez - 250183
#Programa 33: Ingresar un numero, elevar al cuadrado y sumar los 100 siguientes

#Definimos nuestras variables, nuestra suma comienza en 0 y el valor de "n" sera ingresado por el usuario
print("Haremos el calculo de la suma de los cuadrados de 100 números naturales despues del que ingreses")
suma = 0
n= int(input(f"¿Desde que numero quieres comenzar?: "))

#Elevamos al cuadrado nuestro numero y sumamos, repetimos el ciclo hasta llegar a los 100 numeros
for i in range(n, n+100):
    #Con el += sumaremos nuestro resultado y a su vez se lo asignaremos como nuevo valor a nuestra variable, esto nos permitira hacer la suma de nuestros 100 numeros
    suma += i**2

#Imprimimos el resultado
print(f"La suma de los cuadrados de los primeros 100 números naturales es: {suma}")