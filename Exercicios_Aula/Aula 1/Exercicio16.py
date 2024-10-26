peso = float (input("Declare sua massa corporal: "))
altura = float (input("Declare sua altura: "))
IMC = (peso/(altura*altura))

if (IMC > 25): 
    print(f"Acima do Peso Ideal. Seu IMC é: {IMC}.")
else: 
    print(f"Peso OK. Seu IMC é: {IMC}.")