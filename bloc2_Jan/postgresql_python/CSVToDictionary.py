import DictionaryToDatabase
import pandas as Pandas


def ConvertCSVToDictionary():
  CSV = Pandas.read_csv("../SendToDatabase/Clientes.csv")
  Dictionary = CSV.to_dict(orient='list')
  return Dictionary


Data = ConvertCSVToDictionary()

for Index in range(30):
  DictionaryToDatabase.SendDataToDatabase(Index, Data)