nota1 = float (input("Declare sua primeira nota escolar: "))
nota2 = float (input("Declare sua segunda nota escolar: "))
media = (nota1+nota2)/2

if (media<4):
    print(f"Aluno Reprovado! Sua média foi: {media}.")
elif (media >= 4) and (media < 7):
    print(f"Aluno em Recuperação. Sua média foi: {media}.")
    recuperar = float (input("Declare sua nota de recuperação: "))
    if (recuperar < 5):
        print(f"Reprovado na Recuperação.")
    else:
        print(f"Aprovado na Recuperação.")
else:
    print(f"Aluno aprovado. Sua média foi: {media}.")
    