alunos = []
medias = []
alunosUp6 = []
contador = 1

for i in range(10):
    alunos.append(input(f"Declare o nome do {contador}° aluno(a): "))
    medias.append(float (input(f"Declare a nota de(a) {alunos[i]}: ")))
    contador += 1
    if medias[i] > 6:
        alunosUp6.append(alunos[i])
        
print(alunosUp6)
