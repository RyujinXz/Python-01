user = []

for i in range(5):
    nome = input ('Digite seu nome: ')
    media = float(input('Digite sua média: '))
    user.append({'Nome': nome, 'Media': media})
    while (media<0 or media>10):
        media = float(input('Digite uma média válida: '))
        
print(user)