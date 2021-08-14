"""
Una tienda ofrece un descuento del 15 % sobre el total de la compra durante el mes de octubre.
Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar al cliente.
"""
volver_a_realizar_pagos = True


def calculo_precio_final(importe, mes):
    if mes in ("Octubre", "octubre", "Oct", "oct", "10"):
        return importe - ((importe/100) * 15)
    else:
        return importe


while volver_a_realizar_pagos == True:
    importe_pago = float(input("Escribe el importe del gasto realizado: "))
    mes_pago = str(input("Escriba el mes en el que se realizó la compra (En número): "))

    print(f"El importe a pagar será de: {calculo_precio_final(importe_pago, mes_pago)}")
    realizar_otro_pago = str(input("Desea realizar otro pago?? "))

    while realizar_otro_pago != "Detenerse":
        if realizar_otro_pago in ("S", "s", "Si", "si"):
            realizar_otro_pago = "Detenerse"
        elif realizar_otro_pago in ("N", "n", "No", "no"):
            print("Gracias por usar esta cosa")
            volver_a_realizar_pagos = False
            break
        else:
            print("Deja de trollear")
            realizar_otro_pago = str(input("Desea realizar otro pago?? "))