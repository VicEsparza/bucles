#Víctor Andree Esparza Martínez - 250183
#Programa 35: Calcular e imprimir el cuadrado de los numeros del 20 al 50

print(f"Los cuadrados de los numeros del 20 al 50 son: ")

#El programa no nos pide que el usuario defina variables por lo que solamente fijamos el rango de numeros del cual queremos sacar al cuadrado 
for i in range (19 , 50):

    #Sumamos a nuestra "i" 1 y usamos **2 para elevar al cuadrado. Con el +1 en cada iteracion nuestro numero base se incrementara en uno.
    #Una ves "i" alcance 50, lo elevara al cuadrado y dara por finalizado el programa
    if i<50:
        cuadrado=(i+1)**2
        print(f"{i+1} = {cuadrado}")