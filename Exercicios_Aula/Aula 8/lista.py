frutas = ["maça", "banana", "cereja"]
frutas.append("melão")
frutas.append("abacaxi")
frutas.sort()
frutas.reverse()
print(frutas)
for i in range(len(frutas)):
    if(frutas[i]=="maça"):
        frutas.pop(i)
        break
print(frutas)


#  frutas.append(input("Diga uma fruta: "))
# print(len(frutas))
