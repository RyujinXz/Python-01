nota = float (input("Declare sua nota escolar: "))
while (nota < 0) or (nota > 10):
    print("Nota inválida.")
    nota = float (input("Declare uma nota válida: "))
else:
    print("Nota válida.")