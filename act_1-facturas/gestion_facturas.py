facturas = {1: 23.5, 23: 88.88}     #Puede vaciar las facturas si gusta
pagos = {}


def seleccionar_accion():
    menu()
    seleccion_accion = str(input("Seleccione la acción que quiere llevar acabo, tecla 4 para consultar el manual: "))
    while seleccion_accion != "detener_la_accion":
        if seleccion_accion in ("1", "Uno", "uno"):
            add_factura()
            print(f"La deuda hasta el momento es de: {contar_deuda()}")
            print(f"El total pagada hasta el momento es de: {contar_pago()}")
            seleccion_accion = str(input("Seleccione la acción que quiere llevar acabo, tecla 4 para consultar el manual: "))
        elif seleccion_accion in ("2", "Dos", "dos"):
            pagar_deuda()
            print(f"La DEUDA hasta el momento es de: {contar_deuda()}")
            print(f"El total PAGADO hasta el momento es de: {contar_pago()}")
            seleccion_accion = str(input("Seleccione la acción que quiere llevar acabo, tecla 4 para consultar el manual: "))
        elif seleccion_accion in ("3", "Tres", "tres"):
            print(f"Tu deuda ha sido perdonada camarada, el monto perdonado fue de {contar_deuda()}")
            seleccion_accion = "detener_la_accion"
        elif seleccion_accion in ("4", "Cuatro", "cuatro"):
            menu()
            seleccion_accion = str(input("Seleccione la acción que quiere llevar acabo, tecla 4 para consultar el manual: "))
        else:
            print("Por favor, no esté trolleando")
            seleccion_accion = str(input("Seleccione la acción que quiere llevar a acabo: "))


def add_factura():
    clave = int(input("Escriba el NÚMERO de factura: "))
    facturas[clave] = float(input("Escriba el MONTO de la factura: "))
    registrar_factura = str(input("Quiere registrar otra factura?: "))
    while registrar_factura not in ("No", "no", "N", "n"):
        if registrar_factura in ("Si", "si", "S", "s"):
            clave = int(input("Escriba el NÚMERO de factura: "))
            facturas[clave] = float(input("Escriba el MONTO de la factura: "))
            registrar_factura = str(input("Quiere registrar otra factura?: "))
        else:
            print("Lo siento, este comando no es válido")
            registrar_factura = str(input("Quiere registrar otra factura?: "))


def pagar_deuda():
    clave = int(input("Escriba el número de factura a pagar: "))
    pago_factura = 0
    if clave in facturas:
        print(f"se eliminó el registro: {clave}")
        pago_factura += facturas[clave]
        pagos[clave] = facturas[clave]
        facturas.pop(clave)
    else:
        print("Esto no salió como debía, vuelva a digitar por favor")
    print(f"Has pagado: {pago_factura}")


def contar_deuda(contador_deuda=0):
    for i in facturas:
        contador_deuda += facturas[i]
    return contador_deuda


def contar_pago(contador_pagos=0):
    for i in pagos:
        contador_pagos += pagos[i]
    return contador_pagos


def menu():
    print("TECLA 1. Para REGISTRAR facturas")
    print("TECLA 2. Para PAGAR facturas")
    print("TECLA 3. TERMINAR PROCESO")
