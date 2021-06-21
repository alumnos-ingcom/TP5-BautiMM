################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo.(%)

def prueba():
    valor = int(input("Ingrese el valor: "))
    valor = valor+1
    def is_even(valor):
        return (valor // 2) * 2 == valor
    def is_odd(valor):
        return not(is_even(valor))
    for valor in range(valor):
        print(f"{valor} {'True' if is_even(valor) else 'False'}")
        pass

if __name__ == "__main__":
    prueba()

