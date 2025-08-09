#
#

#iniciar contadores de genero
hombres=0
mujeres=0
usuarios_validos=0
usuarios_no_validos=0
promedioH=0
promedioM=0
edad=0
suma_edades_h=0
suma_edades_m=0
numeromayorh=0
numeromenorh=0
numeromayorm=0
numeromenorm=0

print("ingrese el genero de 5 usuarios ('H' para hombre, 'M' para mujer o 'Q' para salir): ")

#usar un bucle while para solicitar el genero de 5 usuarios validos
while usuarios_validos < 5:
    genero=input(f"Ingrese el genero del usuario {usuarios_validos + 1}:").upper()
    if genero=='Q':
        break

    if genero== 'H':
        edad= int(input(f"Ingresa tu edad: "))

        if edad>numeromayorh:
            numeromayorh=edad
        elif numeromenorh==0 or edad<numeromenorh:
            numeromenorh=edad
            
        suma_edades_h += edad
        hombres+= 1
        promedioH=suma_edades_h/hombres
        usuarios_validos+= 1

    elif genero == 'M':
        edad= int(input(f"Ingresa tu edad: "))
        
        if edad>numeromayorm:
            numeromayorm=edad
        elif numeromenorm==0 or edad<numeromenorm:
            numeromenorm=edad
            
        suma_edades_m+=edad
        mujeres += 1
        promedioM=edad/mujeres
        usuarios_validos+= 1

    elif genero!='H' and genero!='M':
        print(f"Ingrese un genero valido entre hombre(H) o mujer(M)")
        usuarios_no_validos+=1

#imprimir los resultados
promediogral= promedioH+promedioM/2
print("\nResultados: ")

print(f"\nHombres: {hombres}")
print(f"El promedio de edades en hombres fue: {promedioH: .2f}")
print(f"La edad mayor en hombres fue: {numeromayorh}")
print(f"La edad menor en hombres fue: {numeromenorh}")

print(f"\nMujeres {mujeres}")
print(f"El promedio de edades en mujeres fue: {promedioM: .2f}")

print(f"\nEntradas invalidas: {usuarios_no_validos}")