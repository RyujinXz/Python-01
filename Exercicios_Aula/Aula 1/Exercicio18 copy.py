import random
lista = [1, 2, 3]
mao2 = random.choice(lista)
print("Você está jogando pedra, papel e tesoura.")
print("[1] para Pedra.")
print("[2] para Papel.")
print("[3] para Tesoura.")
mao1 = int (input("Declare a escolha do primeiro jogador: "))

resultado = mao1 + mao2


if (resultado == 3):
    print(f"Papel ganha de pedra.")
elif (resultado == 4):
    print(f"Pedra ganha tesoura.")
else:
    print(f"Tesoura ganha de papel.")