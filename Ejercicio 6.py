#6.	Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo 
# exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se 
# pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple.
class HoraExtras:
    def __init__(self):
        pass
    def calculoPago(self):
        hot, hoe, het= 0, 0, 0
        ph, phe, pt = 0, 0, 0
        hot = int(input("Ingrese horas trabajadas:"))
        ph = float(input("Ingrese valor por hora:"))
        if hot > 40:
            hoe = hot - 40
            if hoe > 8:
                het = hoe - 8
                hoe = 8
                phe = ph * 2 * hoe + ph * 3 * het
            else:
                phe = ph * 2 * hoe
            pt = ph * 40 + phe
        else:
            pt = ph * hot
        print("Horas extras: {} El pago de horas extras es de: {} El Salario total por horas trabajadas es de: {}".format(hoe,phe, pt))



HoraExtras = HoraExtras()
HoraExtras.calculoPago()
