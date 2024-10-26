nota1= int (input("Diga a sua primeira nota escolar: "))
nota2= int (input("Diga a sua segunda nota escolar: "))
nota3= int (input("Diga a sua terceira nota escolar: "))
nota4= int (input("Diga a sua quarta nota escolar: "))
media= (nota1 + nota2 + nota3 + nota4)/4
if (((nota1 + nota2 + nota3 + nota4)/4) <= 6):
    print(f"Aprovado! Com sua média sendo: {media}.")
else:
    print(f"Reprovado! Com sua média sendo: {media}.")
     