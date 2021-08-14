import mysql.connector
from mysql.connector import errorcode


def Con(DB_USER, DB_PASS, DB_NAME, PORT) :
    global conexion, cursor

    DB_HOST = 'localhost'
    conexion = mysql.connector.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, database=DB_NAME, port=PORT)
    query = f"USE {DB_NAME}"
    cursor = conexion.cursor()
    cursor.execute(query)

def Regist():
    try:
        q1 = "SELECT * FROM munidadaprendizaje"
        print("Unidades de Aprendizaje")
        cursor.execute(q1)
        data1 = cursor.fetchall()
        print(data1)

        print("")
        q2 = "SELECT * FROM cespecialidad"
        print("Especialidades")
        cursor.execute(q2)
        data2 = cursor.fetchall()
        print(data2)

        print("")
        q3 = "SELECT * FROM cnivel"
        print("Niveles")
        cursor.execute(q3)
        data3 = cursor.fetchall()
        print(data3)

        print("")
        print("Ingresa las claves para el nuevo mapa curricular")

        id = input("Identificador de mapa curricular: ")
        idUA = input("Clave Unidad de aprendizaje: ")
        idE = input("Clave Especialidad: ")
        idN = input("Clave nivel: ")
        query = "INSERT into mmapacurricular (id_mc, cla_ua, id_esp, id_niv) " \
                "values (%s, %s, %s, %s )"
        valores = (id, idUA, idE, idN)
        try:
            cursor.execute(query, valores)
            # Efectuamos los cambios en la base de datos
            conexion.commit()
            print(cursor.rowcount, "Registro Agregado Satisfactoriamente")
        except:
            # Si se genero algun error revertimos la operación
            conexion.rollback()
            print("La transacción no fue llevada a cabo")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error con el usuario o password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

def Modif():
    try:
        print("Mapas curriculares registrados")
        q1 = "SELECT * FROM mmapacurricular"
        cursor.execute(q1)
        data1 = cursor.fetchall()
        print(data1)
        print("")
        q2 = "SELECT * FROM cespecialidad"
        print("Especialidades")
        cursor.execute(q2)
        data2 = cursor.fetchall()
        print(data2)
        print("")
        id = input("Identificador de mapa curricular: ")
        idE = input("Clave nueva de la Especialidad: ")
        query = "UPDATE mmapacurricular SET  id_esp = %s WHERE id_mc = %s"
        valores = (idE, id)
        try:
            cursor.execute(query, valores)
            # Efectuamos los cambios en la base de datos
            conexion.commit()
            print(cursor.rowcount, "Registro actualizado Satisfactoriamente")
        except:
            # Si se genero algun error revertimos la operación
            conexion.rollback()
            print("La transacción no fue llevada a cabo")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error con el usuario o password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

def Consu():
    try:
        nombre = input("Nombre(s) Alumno: ")
        app = input("Apellido Paterno alumno: ")
        apm = input("Apellido Materno Alumno: ")
        query = "SELECT * FROM malumno where nom_alu = %s and app_alu = %s and apm_alu = %s"
        print("Datos del alumno")
        valores = nombre, app, apm
        cursor.execute(query, valores)
        data = cursor.fetchall()
        print(data)
        print("")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error con el usuario o password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

def Borrar():
    try:
        q2 = "SELECT * FROM cespecialidad"
        print("Especialidades")
        cursor.execute(q2)
        data2 = cursor.fetchall()
        print(data2)
        print("")
        boleta = input("id de carrera a eliminar: ")
        query = "DELETE FROM cespecialidad WHERE id_esp = %s"
        valor = (boleta,)
        try:
            cursor.execute(query, valor)
            conexion.commit()

            print(cursor.rowcount, "Registro Eliminado")
        except:
            conexion.rollback()
            print("La acción no fue llevada a cabo")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error con el usuario o password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

def desconectar():
    print("Se cerró la conexión a la base de datos")
    cursor.close()
    conexion.close()