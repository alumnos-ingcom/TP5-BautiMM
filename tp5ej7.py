################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Escriba una funcion que determine la distancia entre dos números.

def prueba():
    numero = int(input("Ingrese el valor: "))
    numerodos = int(input("Ingrese un segundo valor: "))
    def distancia(numero):
        if numero >= 0:
            return numero
        else:
            return - numero
    def distancia(numerodos):
        if numerodos >= 0:
            return numerodos
        else:
            return - numerodos

    if numero == numerodos:
        print()
    if numero > 0 and numerodos < 0:
        print("La distancia es: ", numero + -numerodos)
    if numero < 0 and numerodos > 0:
        print("La distancia es: ", -numero + numerodos)
    if numero > 0 and numerodos > 0:
        if numero < numerodos:
            print("La distancia es: ", -numero + numerodos)
        else:
            print("La distancia es: ", numero - numerodos)
    if numero < 0 and numerodos < 0:
        if numero < numerodos:
            print("La distancia es: ", -numero + numerodos)
        else:
            print("La distancia es: ", numero - numerodos)
    print(prueba())
    pass


if __name__ == "__main__":
    prueba()
