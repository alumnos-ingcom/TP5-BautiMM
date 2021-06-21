################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una funcion que permita obtener el n-esimo termino de la suceción Tribonacci, siendo este termino un numero entero positivo mayor a 3.

def prueba():
    def printTribRec(n) :
        if (n == 0 or n == 1 or n == 2) :
            return 0
        elif (n == 3) :
            return 1
        else :
            return (printTribRec(n - 1) +
                    printTribRec(n - 2) +
                    printTribRec(n - 3))
    def printTrib(n) :
        for i in range(1, n) :
            print( printTribRec(i) , " ", end = "")
    n = 12
    printTrib(n)
    pass

if __name__ == "__main__":
    prueba()
