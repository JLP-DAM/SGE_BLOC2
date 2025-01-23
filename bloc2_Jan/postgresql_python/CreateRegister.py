import Connect

def CreateRegister():
    Connection = Connect.ConnectToDatabase()

    Cursor = Connection.cursor()

    SQLCreate = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"

    Values = ('Roger', 'carrer el que sigui', '678113452', 'correu@correu.com', '12_09_1999')

    Cursor.execute(SQLCreate, Values)

    Connection.commit()

    Connection.close()
    Cursor.close()