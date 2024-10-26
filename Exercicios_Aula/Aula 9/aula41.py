lista = []
contador = 1
for i in range(8):
    lista.append(int (input(f"Declare o {contador}° número")))
    contador+= 1
    
lista.sort()
print(f"Menor Número: {lista[0]}")
print(f"Maior Número: {lista[len(lista)-1]}")