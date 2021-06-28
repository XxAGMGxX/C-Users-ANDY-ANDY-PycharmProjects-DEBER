class ActS:
    def __init__(self):
        pass
    def calculoSueldo(self):
        Sueldo = float(input("Sueldo base:"))
        if Sueldo <= 600:
            AuSuel = Sueldo + (Sueldo * 0.1)
            print("Su nuevo sueldo es {}".format(AuSuel))
        else:
            AuSuel = Sueldo
        print("Su sueldo se mantiene por: $ {}".format(AuSuel))
ActS = ActS()
ActS.calculoSueldo()
