'''

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
    
    
'''    

import math

areaPintada = float (input("Informe o tamanho da área a ser pintada (em m²): "))
litros = areaPintada / 6
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)
precoLatas = (latas * 80)
precoGaloes = (galoes * 25)
latasResto = (litros % 18)
galoesResto = math.ceil(latasResto / 3.6)
litrosgaloesResto = galoesResto*3.6
latanova = math.ceil(litros-litrosgaloesResto)/18
litroslataNova = latanova*18
precogaloesResto = galoesResto * 25
precomenor = (latas*80) + (galoesResto*3.6)
print("-"*30)
print(" "*10,"STATUS"," "*10)
print("-"*30)
print(f"LITROS: {litros:.2f}L.")
print(f"APENAS LATAS: {latas} // VALOR: R$ {precoLatas:.2f}")
print(f"APENAS GALÕES: {galoes} // VALOR: R$ {precoGaloes:.2f}")
print("-"*30)
print(" "*10,"MENOR DESPERDÍCIO"," "*10)
print("-"*30)
print(f"LATAS: {latas-1} VALOR: R$ {(latas-1)*80}")
print(f"GALÕES: {galoesResto} VALOR: R$ {galoesResto*25}")
print(f"VALOR: R$ {precomenor-80} e {precomenor}")
