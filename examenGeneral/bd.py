import mysql.connector
from mysql.connector import errorcode


def con(DB_USER, DB_PASS, PORT, DB_NAME="mydb"):
    global conexion, cursor

    DB_HOST = 'localhost'
    conexion = mysql.connector.connect(
        user=DB_USER, password=DB_PASS, host=DB_HOST, database=DB_NAME, port=PORT)
    query = f"USE {DB_NAME}"
    cursor = conexion.cursor()
    cursor.execute(query)


def insert(figura, area, perimetro):
    query = f"INSERT into {figura} (area, perimetro) " \
        "values (%s, %s)"
    valores = (area, perimetro)
    try:
        cursor.execute(query, valores)
        # Efectuamos los cambios en la base de datos
        conexion.commit()
        print(cursor.rowcount, "Registro Agregado Satisfactoriamente")
    except Exception as e:
        print(e)
        # Si se genero algun error revertimos la operación
        conexion.rollback()
        print("La transacción no fue llevada a cabo")


def select(figura):
    query = f"SELECT * FROM {figura}"
    cursor.execute(query)
    output = []
    for row in cursor:
        output.append((float(row[1]), float(row[2])))
    return output


def selectArea(figura):
    query = f"SELECT area FROM {figura}"
    cursor.execute(query)
    output = []
    for row in cursor:
        output.append(float(row[0]))
    return output


def desconectar():
    print("Se cerró la conexión a la base de datos")
    cursor.close()
    conexion.close()
