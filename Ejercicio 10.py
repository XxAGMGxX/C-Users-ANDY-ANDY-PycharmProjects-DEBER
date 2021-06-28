# 9. Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función
class Resultado:
    def __init__(self):
        pass
    def calcuResult(self):
        var1 = int(input("Ingrese el primer valor: "))
        var2 = int(input("Ingrese el segundo valor: "))
        if var1 == 1:
            Resul = 100 * var2
        elif var1 == 2:
            Resul = 100 * var2
        elif var1 == 3:
            Resul = 100 / var2
        else:
            Resul = 0
        print("El resultado del número {} y el valor {} es de: {} ".format(var1, var2, Resul))

Resultado = Resultado()
Resultado.calcuResult()
