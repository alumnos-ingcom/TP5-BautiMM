################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una funcion que permita obtener el n-esimo termino de la sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.

def prueba():
    num_uno, num_dos = 0, 1
    while num_dos <= 213:
        print(num_uno, num_dos, end=" ")
        num_uno = num_uno + num_dos
        num_dos = num_uno + num_dos
        pass
if __name__ == "__main__":
    prueba()