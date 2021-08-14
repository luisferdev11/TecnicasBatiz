import gestion_facturas

hacer_facturas = True

# Rodríguez Domínguez Luis Fernando ha hecho este bello código xd

print("Bienvenido a mi sistema de administración de facturas :)")
while hacer_facturas == True:
    gestion_facturas.seleccionar_accion()
    if input("Desea continuar usando el sistema?? ") in ("No", "no", "N", "n"):
        hacer_facturas = False