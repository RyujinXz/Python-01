numeros = []
pares = []
impares = []
contador = 1

for i in range(7):
    numeros.append(int (input(f"Declare o {contador}° número: ")))
    contador += 1
    if (numeros[i]%2 ==0):
        pares.append(numeros[i])
    else:
        impares.append(numeros[i]) 
        
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
