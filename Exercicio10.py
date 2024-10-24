print("-------------------------------------------------------")
print(" VALOR DO DESCONTO DO VALE-TRANSPORTE E PLANO DE SAÚDE ")
print("-------------------------------------------------------")
print('')

#Variáveis
salario= int(input("Me diga o valor do seu salário: "))
descontoVale= (salario*0.06)
descontoPlano= (salario*0.03)
novoSalario = (salario - (descontoVale + descontoPlano))
#Resultado
print(f"Seu novo salário será de: {novoSalario} reais. ")
print (f"O desconto do vale-transporte foi de: {descontoVale}.")
print(f"O desconto do plano de saúde foi de: {descontoPlano}.")
