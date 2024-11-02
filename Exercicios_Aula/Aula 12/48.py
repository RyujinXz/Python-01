user = []
for i in range(3):
    nome = input('Digite seu nome: ')
    bairro = input('Digite seu bairro: ')
    user.append({'Nome': nome,'Bairro': bairro})
    
userNovo = sorted(user, key=lambda d: d['Nome'])

print(userNovo)