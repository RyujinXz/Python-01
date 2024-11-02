user = []
campo = []
for i in range(10):
    nome = input("Digite seu nome: ")
    telefone = int(input("Digite seu telefone: "))
    cidade = input("Digite sua cidade: ")
    user.append({'Nome': nome,'Telefone': telefone,'Cidade': cidade})
    if cidade == 'Campo Grande':
        campo.append(user[i])
    
print(campo['Nome'],campo['Telefone'])