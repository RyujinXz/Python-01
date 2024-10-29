def ProgramasInfantis():
    listaProgramas=["Peppa Pig", "Chaves", "Pantera Cor de Rosa", "Tom e Jerry"]
    print(listaProgramas)
    return
def Carros():
    carro=[
    {
        "Modelo": "Jeep Renegade",
        "Preço": 120000    
    },
    {
        "Modelo":"Amarok",
        "Preço":"350000"
    },
    {
        "Modelo": "Hb20",
        "Preço": 100000
    },
    {
        "Modelo": "Mobi",
        "Preço": 70000
    }
    ]
    for c in carro:
        print(f'{c["Modelo"]} \n {c["Preço"]}')
idade = int (input("Declare sua idade: "))
if (idade>=18):
    Carros()
else:
    ProgramasInfantis()
       