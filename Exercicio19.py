a = int (input("Digite o primeiro número: "))
b = int (input("Digite o segundo número: "))
c = int (input("Digite o terceiro número: "))
valores = [a,b,c]
valores.sort()
valores.reverse()
print(f"O valor {valores[0]} é o maior.")