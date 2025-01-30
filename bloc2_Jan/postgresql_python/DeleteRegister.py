import Connect

def DeleteRegister():
    Connection = Connect.ConnectToDatabase()
    Cursor = Connection.cursor()

    SQLDelete = '''
    DELETE FROM Clientes
    WHERE Id_Cliente = 3;
    '''

    Cursor.execute(SQLDelete)
    Connection.commit()

    Cursor.close()
    Connection.close()

    print("Delete successful")

DeleteRegister()