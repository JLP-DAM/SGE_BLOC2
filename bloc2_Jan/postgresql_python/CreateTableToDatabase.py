import Connect

def CreateTables():
    Connection = Connect.ConnectToDatabase()

    Cursor = Connection.cursor()

    SQLClients = '''
       CREATE TABLE Clientes (
       Nombre_Cliente VARCHAR(100),
       Dirección_Cliente VARCHAR(200),
       Teléfono_Cliente VARCHAR(100),
       Correo_Electrónico_Cliente VARCHAR(100),
       Fecha_Cumpleaños VARCHAR(50));'''

    Cursor.execute(SQLClients)

    Connection.commit()

    Connection.close()
    Cursor.close()

    print("Tables created succesfully")

CreateTables()