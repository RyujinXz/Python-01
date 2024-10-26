contador = 1
soma = 0
lista = []
for i in range(10):
    lista.append (int(input(f"Declare o {contador}° para calcular a média: ")))
    soma+=lista[i]
    contador+= 1

print(f"Soma: {soma}")
media = (soma / len(lista))
print(f"A média dos 10 números foi: {media}.")