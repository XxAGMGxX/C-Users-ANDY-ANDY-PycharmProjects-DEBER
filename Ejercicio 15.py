#14.	Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela.
class SP:
    def __init__(self):
        pass
    def EstCi(self):
        suma=0
        prod=1
        nume= int(input("Ingrese un número: "))
        while num!=-1:
            suma= suma+nume
            prod= prod*nume
            print("La suma es: {}".format(suma))
            print("El producto es: {}".format(prod))
            nume = int(input("Ingrese un número: "))


SP= SP()
SP.EstCi()