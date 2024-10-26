numeros = []
contador = 1
que10 = []

for i in range(10):
    numeros.append(int (input(f"Declare o {contador}° número: "))) 
    print(numeros[i])
    contador += 1
    if numeros[i] > 10:
       que10.append(numeros[i])

print(que10) 
    
    
    
    