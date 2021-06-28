#2	Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas.
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres
# ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
class comisión:
    SalarioB=float(input("El salario base es de:"))
    Va1=float(input("Valor de la primera venta:"))
    Va2=float(input("Valor de la segunda venta:"))
    Va3=float(input("Valor de la tercera venta:"))
    TotVentas= Va1 + Va2 + Va3
    Com= TotVentas*0.1
    TotRecibir= SalarioB + Com
    print("Su comision por concepto de ventas es de: $",Com)
    print("Sueldo a recibir:$",TotRecibir)