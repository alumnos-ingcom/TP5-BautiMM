################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que determine si un numero entero positivo es capicúa.


import math
def prueba():
    numero = int(input("Ingrese un numero: "))
    numerodedigitos = int(math.log10(numero))+1
    numero1 = numero
    digito = 0
    numerocapicua = 0
    for i in range(numerodedigitos):
        digito = numero % 10
        numero = numero //10 
        numerocapicua = numerocapicua*10+digito
    if numero1 == numerocapicua:
        print("El numero es capicua")
    else:
        print("El numero no es capicua")
    
if __name__ == "__main__":
    prueba()
