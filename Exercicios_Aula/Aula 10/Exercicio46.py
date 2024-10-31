nomes = []
idades = []
junto = []
contador = 1

for i in range(3):
    nomes.append(input(f"Declare o nome da {contador}° pessoa: "))
    idades.append(int (input(f"Declare a idade de(a) {nomes[i]}: ")))
    junto.append( 
        {
            'Nome': nomes[i],
            'Idade': idades[i] 
        })
    contador += 1
junto_ordenado = sorted(junto, key=lambda x: x ['Idade'])

print(junto_ordenado[0])
       
        