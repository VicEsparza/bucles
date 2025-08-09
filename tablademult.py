#
#

n=int(input(f"De que numero quieres saber su tabla de multiplicar: "))

for j in range (n):
    print(f"La tabla de multiplicar del {j+1} es: ")
    for i in range(10):
        mul=(j+1)*(i+1)
        print(f"{j+1} x {i+1} = {mul}")