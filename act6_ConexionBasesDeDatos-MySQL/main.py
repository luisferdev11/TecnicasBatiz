from Acciones import  *

DB_USER = str(input("Escriba el nombre del usuario del la BD (root u otro): "))
DB_PASS = str(input("Escriba la contrasena del usuario a usar: "))
DB_NAME = str(input("Escriba el nombre de la base de datos: "))
PORT = int(input("Escriba el puerto a usar: "))

Con(DB_USER, DB_PASS, DB_NAME, PORT)

stop = "continuar"
while True:
    print("")
    print("Bienvenido")
    print("Selccione una de la siguientes opciones:")
    print("1. Para registrar en la BD")
    print("2. Para modificar algun registro en la BD")
    print("3. Para consultar en la BD")
    print("4. Para borrar algun registro en la BD")
    print("")
    case = int(input("Opcion: "))
    if case in (1,2,3,4):    
        if case == 1:
            Regist()
        elif case == 2:
            Modif()
        elif case == 3:
            Consu()
        elif case == 4:
            Borrar()
    else:
        print("Lo sentimos pero la opción no es válida")
    print("¿Desea realizar algo más?, sino escriba n")
    stop = input()
    if stop in ("N", "n", "No", "no"):
        desconectar()
        print("Gracias por usar este programa")
        break