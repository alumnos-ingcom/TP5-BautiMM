################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una funcion que dado un numero entero positivo, retorne una cadena de texto con su representación binaria.
# Implementar una funcion que haga el proceso inverso; dada una cadena de texto, retorne el numero entero.

def prueba():
    def binarizar(decimal):
        binario = ''
        while decimal // 2 != 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return str(decimal) + binario

    numero = int(input('Introduce el número a convertir a binario: '))
    print(binarizar(numero))

    def binario_a_decimal(numero_binario):
        numero_decimal = 0 
        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
        return numero_decimal

    print(binario_a_decimal(str(input('Introduce el número a convertir a decimal: '))))
    
    pass

if __name__ == "__main__":
    prueba()