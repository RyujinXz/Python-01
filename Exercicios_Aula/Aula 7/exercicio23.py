numero = int (input("Diga um nome para contar até 100: "))

for i in range(numero, 101, 1):
    print(i)
    if(i%2 == 0):
        print(i)
else:
    print("Fim do For!")
    
while (numero<= 100):
    if (numero%2 == 0):
        print(numero)
numero+= 1