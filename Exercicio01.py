# Senac Sabores 
total = 0
pizza = 0
while(pizza != 5):

    print("------------Senacarias Pizza's-----------------")
    print()
    print("Escolha um sabor de Pizza: ")
    print("[1] Calabresa com Cebola -> R$ 30.00")
    print("[2] Camarão com Catupiry -> R$ 50.00")
    print("[3] Frango com Requeijão -> R$ 45.00")
    print("[4] Banana com Chocolate -> R$ 89.00")
    print("[5] Finalizar Pedido.")
    print("-----------------------------------------------")

# String
    pizza = int(input("Digite a pizza escolhido (apenas números): "))


    match pizza:
        case 1: 
            print("Estamos preprando sua pizza de Calabresa com Cebola - R$ 39.90")
            total += 39.9
        case 2:
            print("Estamos preprando sua pizza de Camarão com Catupiry - R$ 49.90")
            total += 49.9
        case 3: 
            print("Estamos preprando sua pizza Frango com Requeijão - R$ 45.00")
            total += 45
        case 4:
            print("Estamos preprando sua pizza de Banana com Chocolate - R$ 62.00")
            total += 62
        case 5:
            print(f"Total do pedido: R$ {total}")
        case _:
            print("Escolha uma opção válida.")