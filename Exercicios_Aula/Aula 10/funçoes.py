contador = 1
def Media(N1, N2, N3, N4,):
    media = (N1+N2+N3+N4)/4
    if(media>=7):
        return "APROVADO!"
    elif(media<7 and media>4):
        return "EM RECUPERAÇÃO!"
    else:
        return "REPROVADO!"


notas = []
for i in range(4):
    notas.append(float (input(f"Declare a {contador}º nota: ")))
    contador += 1
    
print(f"O aluno está: {Media(notas[0],notas[1],notas[2],notas[3])}")