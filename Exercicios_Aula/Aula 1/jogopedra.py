player1 = input("Escolha sua opção entre pedra, papel e tesoura: ")
player2 = input("Escolha sua opção entre pedra, papel e tesoura: ")
if (player1==player2):
    print("Empate!")
elif ((player1 == "pedra" and player2 == "tesoura") or (player1 == "papel" and player2 == "pedra") or (player1 == "tesoura" and player2 == "papel")):
    print("O primeiro jogador venceu!!")
else:
    print("O segundo jogador venceu!!") 