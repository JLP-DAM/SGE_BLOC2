import ReadRegister

for Data in ReadRegister.ReadRegister():
    print("\n")
    print("Nom: " + Data[1])
    print("Adreça: " + Data[2])
    print("Telèfon: " + Data[3])
    print("Email: " + Data[4])
    print("Naixement: " + Data[5])