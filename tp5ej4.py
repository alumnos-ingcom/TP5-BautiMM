################
# Juan Bautista Mangold Moro - @BautiMM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#E scribir una función que determine si un numero entero positivo es un número perfecto.

def prueba():
    def NumeroPerfecto(num):
      suma = 0
      for i in range(1,num):
        if (num % i == 0):
          suma += i
     
      if num == suma:
        return True
      else:
        return False
     
    num = int(input("introduzca un numero:"))
     
    if NumeroPerfecto(num):
      print("%s es un numero perfecto" % num)
    else:
      print("%s NO es un numero perfecto" % num)
      pass

if __name__ == "__main__":
    prueba()