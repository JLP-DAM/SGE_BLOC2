import Connect

def ReadRegister():
    Connection = Connect.ConnectToDatabase()
    Cursor = Connection.cursor()

    SQLRead = "SELECT * FROM Clientes"

    Cursor.execute(SQLRead)
    Connection.commit()

    Results = Cursor.fetchall()

    return Results