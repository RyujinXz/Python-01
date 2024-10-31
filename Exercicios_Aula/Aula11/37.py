def WelcomeCity(name, city):
    if city == 'Rio de Janeiro':
        return f'{name}, seja bem-vindo à Cidade Maravilhosa.'
    else:
        return f'{name}, seja bem-vindo a(o) {city}'

nome = input(f'Diga seu nome: ')
cidade = input(f'{nome}, diga a cidade que você mora: ')

print(WelcomeCity(nome, cidade))
