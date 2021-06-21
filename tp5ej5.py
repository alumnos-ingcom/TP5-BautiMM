################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Implementar una funcion que dada un texto, deje en minuscula lo que esté en mayuscula y en mayuscula lo que esté en minuscula.

def prueba():
    texto = str(input('Escriba algo: '))
    texto_swaped = texto.swapcase()
    print(texto_swaped)
    pass
if __name__ == "__main__":
    prueba()