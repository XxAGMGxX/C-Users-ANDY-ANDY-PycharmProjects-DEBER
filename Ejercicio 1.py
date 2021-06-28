#1.	En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
class descuento:
    totcompra=float(input("Ingrese el total de la compra:"))
    desc= totcompra*0.15
    totpagar= totcompra-desc
    print("El total a pagar es: $",totpagar)
    print("El descuento aplicado es de: $",desc)