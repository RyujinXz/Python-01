def Somar(N1, N2):
    soma = N1 + N2
    return f'A soma dos dois números é: {soma}'
    
n1 = float (input(f"Digite o primeiro valor da soma: "))
n2 = float (input(f"Digite o segundo valor da soma: "))

print(Somar(n1, n2))
