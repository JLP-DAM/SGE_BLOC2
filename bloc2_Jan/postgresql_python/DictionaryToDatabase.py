import Connect

def SendDataToDatabase(Index, Data):
   Connection = Connect.ConnectToDatabase()

   Cursor = Connection.cursor()
   SQLInstruction = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"

   Values = (Data["Nombre_Cliente"][Index], Data["Dirección_Cliente"][Index], Data["Teléfono_Cliente"][Index], Data["Correo_Electrónico_Cliente"][Index], Data["Fecha_Cumpleaños"][Index])

   Cursor.execute(SQLInstruction, Values)
   Connection.commit()

   Cursor.close()
   Connection.close()