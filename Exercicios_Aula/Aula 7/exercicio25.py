num = int (input("Digite um número para mostrar sua tabuada: "))
contagem = 1

while (contagem <= 10):
    print(f"{num} x {contagem} = {num*contagem}")
    contagem += 1
else: 
    print("FIM WHILE!!!")
    
print()
print()

for (i) in range(1, 11, 1):
    print(f"{num} x {i} = {num*i}")
