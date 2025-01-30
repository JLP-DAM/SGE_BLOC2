import Connect

def UpdateRegister():
    Connection = Connect.ConnectToDatabase()
    Cursor = Connection.cursor()

    SQLUpdate = '''
    UPDATE Clientes
    SET Teléfono_Cliente = 000000003
    WHERE Id_Cliente = 3;
    '''

    Cursor.execute(SQLUpdate)
    Connection.commit()

    Cursor.close()
    Connection.close()

    print("Update successful")

UpdateRegister()