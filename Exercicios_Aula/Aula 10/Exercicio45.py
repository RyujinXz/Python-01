alunos = []
medias = []
alunosUp6 = []

for i in range(10):
    alunos.append(input(f"Declare o nome do {i+1}º aluno(a): "))
    medias.append(float (input(f"Declare a nota de(a) {alunos[i]}: ")))
    if medias[i] > 6:
        alunosUp6.append(alunos[i])
        
print(alunosUp6)
