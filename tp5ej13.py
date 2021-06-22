################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que dado un texto y una palabra, retorne la ubicación de la palabra en el texto o una excepción si la palabra no forma parte del texto.

def prueba():
        import re

        frase = str(input("Ingrese una palabra o texto: "))
        palabra = str(input("ingrese la palabra a buscar: "))

        try:
            resultado = re.search(palabra, frase)

            inicio = resultado.start()
            final = resultado.end()

            print ("La primera letra de la palabra {} se encontró en el caracter {} y la ultima letra de la palabra se encontro en el caracter {}: ".format(palabra, inicio, final))
        except:
            print("La palabra no estaba en el texto: ")
        pass


if __name__ == "__main__":
    prueba()